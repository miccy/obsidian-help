---
aliases:
  - Obsidian Flavored Markdown
  - Editing and formatting/Obsidian Flavored Markdown
description: Přečtěte si, jak Obsidian zachází se syntaxí Markdownu.
permalink: editing-and-formatting/obsidian-flavored-markdown
mobile: true
publish: true
---

Obsidian používá variantu Markdownu, která je založena na [CommonMark](https://commonmark.org/). Přidali jsme některá rozšíření pro podporu funkcí, jako jsou [[Basic formatting syntax#Interní odkazy|wikilinky]], [[Advanced formatting syntax#Matematika|matematika]] a [[Callouts|callouty]].

## Striktní zalomení řádků

Ve výchozím nastavení Obsidian dodržuje specifikaci CommonMark pro zalomení řádků. To znamená, že jednoduchá zalomení řádků v editoru jsou v náhledu považována za mezery. Pro vytvoření zalomení řádku musíte řádek ukončit dvěma mezerami nebo použít zpětné lomítko `\`.

Toto chování však můžete změnit v **Settings** (Nastavení) -> **Editor** -> **Strict line breaks** (Striktní zalomení řádků). Pokud toto nastavení vypnete, jednoduchá zalomení řádků v editoru se budou v náhledu vykreslovat jako zalomení řádků.

## Podpora HTML

Obsidian podporuje HTML tagy ve vašich poznámkách. To vám umožňuje přidávat prvky, které nejsou podporovány Markdownem, jako `<iframe>`, `<details>` nebo `<summary>`.

Z bezpečnostních důvodů však HTML čistíme, abychom zabránili spuštění škodlivých skriptů. To znamená, že tagy `<script>` a obslužné rutiny událostí (jako `onclick`) jsou zakázány.

## Rozdíly oproti standardnímu Markdownu

I když se snažíme co nejvíce držet CommonMark, existuje několik rozdílů:

- **Wikilinky**: Používáme `[[ ]]` pro interní odkazy, což není součástí specifikace CommonMark.
- **Embeds** (Vložení): Používáme `![[ ]]` pro vkládání poznámek a médií, což je také rozšíření.
- **Callouts**: Používáme vlastní syntaxi pro callouty (`> [!type]`), která je inspirována Microsoft Docs, ale není součástí CommonMark.
- **Math** (Matematika): Používáme `$` a `$$` pro matematiku, což je běžné v akademickém Markdownu, ale není to standardní CommonMark.
