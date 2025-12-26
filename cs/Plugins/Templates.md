---
aliases:
  - Templates
  - Core plugins/Templates
  - Snippets
description: Vkládejte úryvky textu do svých poznámek.
permalink: plugins/templates
mobile: true
publish: true
---

Plugin **Templates** (Šablony) vám umožňuje vkládat úryvky textu do vašich poznámek. To je užitečné pro vytváření konzistentních struktur poznámek, jako jsou denní záznamy, poznámky ze schůzek nebo šablony projektů.

## Vytvoření šablony

1. Vytvořte ve svém trezoru složku pro ukládání šablon (např. `Šablony`).
2. Vytvořte novou poznámku uvnitř této složky.
3. Přidejte obsah, který chcete použít jako šablonu.

Ve svých šablonách můžete používat proměnné:

- `{{date}}`: Vloží aktuální datum.
- `{{time}}`: Vloží aktuální čas.
- `{{title}}`: Vloží název aktuální poznámky.

## Konfigurace pluginu

1. Přejděte do **Settings** (Nastavení) -> **Templates** (Šablony).
2. Nastavte **Template folder location** (Umístění složky šablon) na složku, kterou jste vytvořili.
3. (Volitelné) Nastavte **Date format** (Formát data) a **Time format** (Formát času).

## Vložení šablony

1. Otevřete poznámku, kam chcete vložit šablonu.
2. Klikněte na ikonu **Insert template** (Vložit šablonu) na pásu karet (ikona stránky s textem).
3. Vyberte šablonu, kterou chcete vložit.

Alternativně použijte paletu příkazů: "Templates: Insert template" (Šablony: Vložit šablonu).
