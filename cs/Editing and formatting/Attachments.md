---
aliases:
  - Attachments
  - Editing and formatting/Attachments
  - Files and folders/Attachments
description: Naučte se přidávat přílohy (obrázky, PDF, zvuk, video) do svých poznámek.
permalink: editing-and-formatting/attachments
mobile: true
publish: true
---

Přílohy jsou soubory, které nejsou poznámkami Markdown, jako jsou obrázky, PDF, zvukové soubory a videa. Přílohy můžete přidat do svého trezoru a vložit je do svých poznámek.

## Podporované formáty souborů

Obsidian podporuje různé formáty souborů. Viz [[Accepted file formats|Přijímané formáty souborů]] pro kompletní seznam.

## Přidávání příloh

Přílohy můžete do svého trezoru přidat několika způsoby:

- **Přetáhni a pusť** (Drag and drop): Přetáhněte soubor z průzkumníka souborů vašeho počítače do Obsidianu.
- **Kopírovat a vložit**: Zkopírujte soubor nebo obrázek do schránky a vložte jej do poznámky.
- **Systémový průzkumník souborů**: Přesuňte soubory do složky vašeho trezoru pomocí průzkumníka souborů vašeho operačního systému.

## Vkládání příloh

Pro vložení přílohy do poznámky použijte následující syntaxi:

```markdown
![[nazev-souboru.png]]
```

Nebo pro PDF:

```markdown
![[dokument.pdf]]
```

## Správa příloh

Ve výchozím nastavení se nové přílohy ukládají do kořenového adresáře vašeho trezoru. Toto chování můžete změnit v **Settings** (Nastavení) -> **Files and links** (Soubory a odkazy) -> **Default location for new attachments** (Výchozí umístění pro nové přílohy).

Můžete si vybrat ukládání příloh:

- Do kořenové složky.
- Do stejné složky jako aktuální poznámka.
- Do konkrétní složky (např. `Přílohy`).
- Do podsložek v konkrétní složce.
