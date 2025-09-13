import os
import re
from html_to_markdown import convert_to_markdown

# Root of your repo
BASE_DIR = "./src"

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

md_link_pattern = r"\[([^\]]*?)\]\((.+)>?\)"
def transform_md_links(match):
    path = match.group(2)
    if path.startswith("<") and path.endswith(">"):
        path = path[1:-1]
    return f"[[{match.group(2)}|{match.group(1)}]]"

fenced_code_pattern = r'(\n^(`{3,})[\s\S]*?^\2\n|`.+?`)'
for subdir, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)
            print(f"Updating file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            parts = re.split(fenced_code_pattern, content, flags=re.MULTILINE)
            result = []
            for i, part in enumerate(parts):
                if not part:
                    continue
                if part.startswith(r"\n```") or part.startswith("`"):
                    # Code section -> skip or keep as-is
                    result.append(part)
                else:
                    # Non-code section -> run your link-rewriting regex
                    # Remove single backticks
                    part = re.sub(r"(?<!`)`(?!`|[^`\n]*`)", "", part)
                    # Transform and cleanup HTML
                    part = re.sub(html_pattern, transform_html, part)
                    part = re.sub(img_pattern, transform_img, part)
                    part = re.sub(r"<details[^>]*>|<\/details>", "", part)
                    part = re.sub(r"<summary[^>]*>|<\/summary>", "**", part)
                    part = re.sub(r"<strong[^>]*>|<\/strong>", "", part)
                    part = re.sub(r"<pre[^>]*><code[^>]*>", "_", part)
                    part = re.sub(r"<\/code><\/pre>", "```", part)
                    part = re.sub(r"<code[^>]*>|<\/code>", "`", part)
                    # Transform mdbook patterns
                    part = re.sub(link_pattern,transform_links, part)
                    part = re.sub(ref_pattern, transform_refs, part)
                    part = re.sub(file_pattern, transform_files, part)
                    part = re.sub(include_pattern, tranfsform_includes, part)
                    part = re.sub(r"{{#tabs}}", "", part)
                    part = re.sub(r"{{#endtab}}|{{#endtabs}}", "", part)
                    part = re.sub(tab_pattern, transform_tabs, part)
                    part = re.sub(r"{{#note}}|{{#endnote}}", "", part)
                    # Transform markdown to obsidian links
                    part = re.sub(md_link_pattern, transform_md_links, part)
                    part = re.sub(r"\n\n\n", "\n\n", part)
                    result.append(part)
            new_content = "".join(result)

            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)