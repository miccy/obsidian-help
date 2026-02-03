---
aliases:
  - Search
  - Core plugins/Search
  - Find
description: Hledejte text ve vašich poznámkách.
permalink: plugins/search
mobile: true
publish: true
---

Plugin **Search** (Vyhledávání) vám umožňuje vyhledávat text ve všech vašich poznámkách.

## Použití

1. Otevřete levý postranní panel.
2. Klikněte na ikonu **Search** (lupa).
3. Napište svůj vyhledávací dotaz.

## Operátory vyhledávání

Obsidian podporuje mocné vyhledávací operátory.

- **path:** (cesta): Hledat v cestě souboru. `path:denní`
- **file:** (soubor): Hledat v názvu souboru. `file:schůzka`
- **tag:** (štítek): Hledat štítky. `tag:#kniha`
- **line:** (řádek): Hledat text na stejném řádku. `line:(foo bar)`
- **section:** (sekce): Hledat text ve stejné sekci. `section:(nadpis obsah)`
- **content:** (obsah): Hledat v obsahu souboru (výchozí).

## Booleovské operátory

- **OR** (NEBO): `foo OR bar` (najde poznámky s "foo" nebo "bar")
- **-**: `-foo` (vyloučit poznámky s "foo")
- **""**: `"foo bar"` (hledání přesné fráze)
- **( )**: `(foo OR bar) AND baz` (seskupování)
