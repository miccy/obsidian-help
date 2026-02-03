---
aliases:
  - Symbolic links and junctions
  - Symlinks
  - Files and folders/Symbolic links and junctions
description: Přečtěte si, jak Obsidian zachází se symbolickými odkazy a spojeními.
permalink: files-and-folders/symbolic-links-and-junctions
mobile: true
publish: true
---

Obsidian podporuje symbolické odkazy (symlinks) a spojení (junctions) na desktopových operačních systémech.

## Co jsou symbolické odkazy?

Symbolický odkaz je soubor, který ukazuje na jiný soubor nebo adresář. Funguje jako zkratka, ale většina aplikací s ním zachází, jako by to byl skutečný soubor nebo adresář.

## Použití symlinků v Obsidianu

Symlinky můžete použít k zahrnutí souborů nebo složek mimo váš trezor.

1. Vytvořte symlink uvnitř složky vašeho trezoru, který ukazuje na externí soubor nebo složku.
2. Obsidian detekuje symlink a zobrazí obsah, jako by byl uvnitř vašeho trezoru.

## Omezení

- **Mobil**: Symbolické odkazy nejsou podporovány na iOS ani Androidu.
- **Sync**: Obsidian Sync nesynchronizuje cíl symlinku. Může synchronizovat samotný symlink, ale na jiných zařízeních bude pravděpodobně nefunkční.
- **Sledování souborů**: Obsidian nemusí detekovat změny provedené v cílovém souboru, pokud je mimo trezor.
