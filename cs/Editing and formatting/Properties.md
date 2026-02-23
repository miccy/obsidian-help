---
aliases:
  - Properties
  - YAML frontmatter
  - Metadata
  - Editing and formatting/Properties
description: Naučte se, jak přidat metadata do svých poznámek pomocí vlastností.
permalink: editing-and-formatting/properties
mobile: true
publish: true
---

Vlastnosti (Properties), známé také jako YAML frontmatter, vám umožňují přidat metadata do vašich poznámek. Tato metadata mohou být využita pluginy, vyhledáváním a dalšími funkcemi.

## Přidání vlastností

Chcete-li přidat vlastnosti do poznámky, přidejte blok YAML na úplný začátek souboru. Blok YAML začíná a končí třemi pomlčkami `---`.

```yaml
---
author: Jan Novák
tags: [obsidian, markdown]
publish: true
---
```

## Typy vlastností

Obsidian podporuje několik typů vlastností:

- **Text**: Jeden řádek textu.
- **List** (Seznam): Seznam textových hodnot.
- **Number** (Číslo): Číselná hodnota.
- **Checkbox** (Zaškrtávací políčko): Logická hodnota (pravda/nepravda).
- **Date** (Datum): Hodnota data (RRRR-MM-DD).
- **Time** (Čas): Hodnota času (HH:MM).

## Zobrazení vlastností

Vlastnosti můžete zobrazit a upravit pomocí **Zobrazení vlastností** (Properties view).

1. Otevřete poznámku.
2. Vlastnosti se zobrazí v horní části poznámky.
3. Kliknutím na vlastnost ji upravíte.
4. Kliknutím na **Add property** (Přidat vlastnost) přidáte novou vlastnost.

## Vyhledávání vlastností

Můžete vyhledávat poznámky na základě jejich vlastností pomocí vyhledávacího operátoru `property:` (vlastnost).

```
["author":Jan Novák]
```

Toto najde všechny poznámky, kde je vlastnost `author` rovna `Jan Novák`.
