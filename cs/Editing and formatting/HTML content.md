---
aliases:
  - HTML content
  - HTML tags
  - Editing and formatting/HTML content
description: Naučte se používat HTML tagy ve svých poznámkách.
permalink: editing-and-formatting/html-content
mobile: true
publish: true
---

Obsidian podporuje HTML tagy ve vašich poznámkách. To vám umožňuje přidávat prvky, které nejsou podporovány standardním Markdownem.

## Podporované tagy

Obsidian podporuje většinu HTML tagů, včetně:

- `<div>`
- `<span>`
- `<br>`
- `<hr>`
- `<table>`
- `<details>` a `<summary>`
- `<iframe>` (viz [[Embed web pages|Vložení webových stránek]])

## Sanitizace

Z bezpečnostních důvodů Obsidian sanitizuje (čistí) HTML, aby zabránil spuštění škodlivého kódu.

- Tagy `<script>` jsou odstraněny.
- Obslužné rutiny událostí (např. `onclick`, `onload`) jsou odstraněny.
- Atributy `style` jsou povoleny, ale některé vlastnosti mohou být filtrovány.

## Příklady

### Details a Summary

Pomocí `<details>` a `<summary>` můžete vytvořit sbalitelné sekce.

```html
<details>
<summary>Klikněte pro rozbalení</summary>

Zde je nějaký skrytý obsah.
</details>
```

<details>
<summary>Klikněte pro rozbalení</summary>

Zde je nějaký skrytý obsah.
</details>

### Zarovnání textu na střed

Text můžete zarovnat na střed pomocí `<div>` s `style="text-align: center;"`.

```html
<div style="text-align: center;">
  Tento text je zarovnán na střed.
</div>
```

<div style="text-align: center;">
  Tento text je zarovnán na střed.
</div>
