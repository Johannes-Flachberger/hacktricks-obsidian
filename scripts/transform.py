import os
import re
from html_to_markdown import convert_to_markdown

# Root of your repo
BASE_DIR = "./src"


external_link_pattern = r"\[([^$]+)\$\$([^$]+)\$\$\]\(\)"
def transform_external_links(match):
    print(f"Updating external link: {match.group(0)}")
    label = match.group(1)      # Link text
    path = match.group(2)        # URL
    path = path.replace("external:https://cloud.hacktricks.wiki/en", "hacktricks-cloud")
    path = path.replace("external:external:https://book.hacktricks.wiki/en", "hacktricks")
    path = path.replace("index.html", "README.md")
    path = path.replace(".html", ".md")
    return f"[[{path}|{label}]]"

link_pattern = r"\[([^\]]+?)\]\(([\w\-\/]*)index\.html(#([^\)]*))?\)"
def transform_links(match):
    print(f"Updating link: {match.group(0)}")
    label = match.group(1)      # Link text
    label = label.replace("**", "")  # Remove bold markdown
    label = label.replace("_", "")  # Remove italic markdown
    folder = match.group(2)     # Path before index.html
    anchor = match.group(3)     # Optional anchor
    
    if anchor:
        # Prettify anchor: "system-information" -> "System Information
        anchor_text = anchor.replace("-", " ").title()
        return f"[[{folder}README.md{anchor_text}|{label}]]"
    else:
        return f"[[{folder}README.md|{label}]]"

ref_pattern = r"{{[\s]*#ref[\s]*}}(?:\n)?[\s>]*([^\n]*)(?:\n)?[\s>]*{{#endref}}"
def transform_refs(match):
    return f"[[{match.group(1)}]]"

file_pattern = r"{{[\s]*#file[\s]*}}(?:\n)?([^\\\n#]*(?:#(.*))?)(?:\n)?{{[\s]*#endfile[\s]*}}"
def transform_files(match):
    return f"[[files/{match.group(1)}]]"

include_pattern = r"{{[\s]*#include[\s]*([^\}]+)}}"
def tranfsform_includes(match):
    # remove banners
    if "banner" in match.group(1):
        return ""
    else:
        return f"![[{match.group(1)}]]"

tab_pattern = r'{{#tab name="(.+)"}}'
def transform_tabs(match):
    return f"**{match.group(1)}**"

img_pattern = r"<img src=(?:\"|')([^\"']*)(?:\"|')(?:.*)\/?>"
def transform_img(match):
    return f"![[{match.group(1)}]]"

html_pattern = r"<([a-zA-Z][^>\s]*)\b[^>]*>.*?<\/\1>|<[a-zA-Z][^>]*\/>"
def transform_html(match):
    return convert_to_markdown(match.group(0))

img_link_pattern = r"\[\]\(<(.*)>\)"
def transform_img_links(match):
        return f"[[{match.group(1)}]]"


fenced_code_pattern = r'((`{3,})[\s\S]*?^\2)|(`.+?`)'

def split_content(content):
    parts = []
    last_end = 0

    for match in re.finditer(fenced_code_pattern, content, flags=re.MULTILINE):
        start, end = match.start(), match.end()

        # Add everything before this code block
        if last_end < start:
            parts.append(content[last_end:start])

        # Add the code block itself
        parts.append(match.group(0))

        last_end = end

    # Add remaining text after last code block
    if last_end < len(content):
        parts.append(content[last_end:])

    return parts


for subdir, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)
            print(f"Updating file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            parts = split_content(content)
            result = []
            for i, part in enumerate(parts):
                if not part:
                    continue
                if part.startswith(r"```") or part.startswith("`"):
                    # Code section -> skip or keep as-is
                    result.append(part)
                else:
                    # Non-code section -> run your link-rewriting regex
                    # Remove single backticks
                    part = re.sub(r"(?<!`)`(?!`|[^`\n]*`)", "", part)
                    # Transform and cleanup HTML
                    part = re.sub(html_pattern, transform_html, part)
                    part = re.sub(img_pattern, transform_img, part)
                    # Transform mdbook patterns
                    part = re.sub(external_link_pattern, transform_external_links, part)
                    part = re.sub(link_pattern, transform_links, part)
                    part = re.sub(ref_pattern, transform_refs, part)
                    part = re.sub(file_pattern, transform_files, part)
                    part = re.sub(include_pattern, tranfsform_includes, part)
                    part = re.sub(r"{{#tabs}}", "", part)
                    part = re.sub(r"{{#endtab}}|{{#endtabs}}", "", part)
                    part = re.sub(tab_pattern, transform_tabs, part)
                    part = re.sub(r"{{#note}}|{{#endnote}}", "", part)
                    # Transform weird image links
                    part = re.sub(img_link_pattern, transform_img_links, part)
                    part = re.sub(r"[\n]{3,}", "\n\n", part)
                    result.append(part)
            new_content = "".join(result)

            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)