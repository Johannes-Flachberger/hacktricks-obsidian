# Hacktricks-Obsidian

This is a fork of [HackTricks](https://github.com/HackTricks-wiki/hacktricks) that presents the original hacktricks contents as an [obsidian](https://obsidian.md/) vault.

For me, this has several advantages over hosting browsing hacktricks online or hosting it locally:
- simpler: no need for running a docker container, a webserver or building the html sites...
- better browsing experience: I think obsidian offers a cleaner browsing experience and search features compared to mdbook
- known environment: I build my personal knowledge base in obsidian - its cool to have the hacktricks content available in the same environment.
- available offline

## How it works

The "mdbook" branch represents the current state of the upstream repo and is updated daily. The source files are transformed to markdown format (with obsidian specifics) and pushed to the main branch using github actions.

## Usage

1. Clone the repo
2. Checkout the main branch
3. With obsidian, open the /hacktricks subfolder as a vault

## License and Attribution

This repository is a fork of [HackTricks](https://github.com/carlospolop/hacktricks) by Carlos Polop.  
The original work © Carlos Polop 2021 is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  

My contributions and modifications are shared under the same license.  