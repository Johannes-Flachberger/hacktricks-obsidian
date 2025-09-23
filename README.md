# Hacktricks-Obsidian

This repo fetches contents of [HackTricks](https://github.com/HackTricks-wiki/hacktricks) and [HackTricks Cloud](https://github.com/HackTricks-wiki/hacktricks-cloud) and presents them as an [obsidian](https://obsidian.md/) vault. The contents are not edited - only the formatting is transformed to obsidian-flavoured markdown.

For me, this has several advantages over hosting browsing hacktricks online or hosting it locally:
- more lightweight: no need for running a docker container, building the html sites and a webserver 
- better browsing experience: I think obsidian offers a cleaner browsing experience and search features compared to mdbook.
- known environment: I build my personal knowledge base in obsidian - its cool to have the hacktricks content available in the same environment.

## Usage

1. Clone the repo
2. Checkout the main branch
3. With obsidian, open the /hacktricks-all subfolder as a vault

Alternatively, you can open the repo using vscode - most of the obsidian specific syntax is rendered correctly when using the [Foam extension](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode) for vscode.

## How it works

The master branches of the "upstream" repos are fetched daily. The source files are transformed to obsidian-flavoured markdown and pushed into a unified directory on the main branch using github actions.

## License and Attribution

This repository uses contents of [HackTricks](https://github.com/carlospolop/hacktricks) and [HackTricks Cloud](https://github.com/HackTricks-wiki/hacktricks-cloud) by Carlos Polop.  
The original work © Carlos Polop 2021 is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  

My contributions and modifications are shared under the same license.