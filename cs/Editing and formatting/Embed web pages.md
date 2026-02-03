---
aliases:
  - Embed web pages
  - Iframe
  - Editing and formatting/Embed web pages
description: Naučte se vkládat webové stránky do svých poznámek pomocí iframes.
permalink: editing-and-formatting/embed-web-pages
mobile: true
publish: true
---

Webové stránky můžete vkládat do svých poznámek pomocí HTML tagů `<iframe>`.

## Základní použití

Pro vložení webové stránky použijte následující syntaxi:

```html
<iframe src="https://example.com" width="100%" height="500"></iframe>
```

Nahraďte `https://example.com` URL adresou stránky, kterou chcete vložit.

## Vkládání videí

Můžete vkládat videa ze stránek jako YouTube nebo Vimeo pomocí jejich kódů pro vložení (embed codes).

### YouTube

1. Přejděte na video YouTube, které chcete vložit.
2. Klikněte na **Sdílet**.
3. Klikněte na **Vložit**.
4. Zkopírujte HTML kód a vložte jej do své poznámky.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Bezpečnost

Z bezpečnostních důvodů Obsidian omezuje některé funkce v rámci iframes, jako je přístup k vašemu lokálnímu souborovému systému nebo spouštění skriptů, které by mohly interagovat s aplikací Obsidian.
