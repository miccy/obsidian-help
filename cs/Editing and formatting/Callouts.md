---
aliases:
  - Callouts
  - Editing and formatting/Callouts
  - Admonitions
  - Alerts
description: Používejte callouty ke zvýraznění informací, jako jsou varování, tipy a citace.
permalink: editing-and-formatting/callouts
mobile: true
publish: true
---

Callouty (výzvy) jsou speciálním typem blokové citace, která vám umožňuje zvýraznit konkrétní části vašich poznámek. Často se používají pro varování, tipy nebo jiné důležité informace.

## Syntaxe

Pro vytvoření calloutu použijte následující syntaxi:

```markdown
> [!typ] Titulek
> Obsah
```

- `typ`: Typ calloutu (např. `info`, `warning`, `tip`).
- `Titulek`: Volitelný titulek pro callout. Pokud je vynechán, použije se název typu (s velkým počátečním písmenem).
- `Obsah`: Obsah calloutu. Může obsahovat Markdown.

Příklad:

```markdown
> [!info] Toto je informační callout
> Zde jsou nějaké informace.
```

> [!info] Toto je informační callout
> Zde jsou nějaké informace.

## Podporované typy

Obsidian podporuje několik vestavěných typů calloutů. Každý typ má jinou ikonu a barvu.

| Typ | Aliasy | Ikona | Barva |
| :--- | :--- | :--- | :--- |
| `note` | | Tužka | Modrá |
| `abstract` | `summary`, `tldr` | Schránka | Azurová |
| `info` | | Info | Modrá |
| `todo` | | Zaškrtávátko | Modrá |
| `tip` | `hint`, `important` | Plamen | Azurová |
| `success` | `check`, `done` | Zaškrtávátko | Zelená |
| `question` | `help`, `faq` | Otazník | Oranžová |
| `warning` | `caution`, `attention` | Výstražný trojúhelník | Oranžová |
| `failure` | `fail`, `missing` | Křížek | Červená |
| `danger` | `error` | Blesk | Červená |
| `bug` | | Brouk | Červená |
| `example` | | Seznam | Fialová |
| `quote` | `cite` | Citace | Šedá |

## Skládací callouty

Callouty můžete učinit skládacími (foldable) přidáním `+` nebo `-` za typ.

- `+`: Callout je ve výchozím nastavení rozbalený.
- `-`: Callout je ve výchozím nastavení sbalený.

```markdown
> [!faq]- Jsou callouty skládací?
> Ano! Ve skládacím calloutu je obsah skrytý, dokud nekliknete na šipku pro jeho rozbalení.
```

> [!faq]- Jsou callouty skládací?
> Ano! Ve skládacím calloutu je obsah skrytý, dokud nekliknete na šipku pro jeho rozbalení.

## Vlastní callouty

Vzhled calloutů můžete přizpůsobit pomocí CSS snippetů. Příklady a návody naleznete na [Fóru Obsidianu](https://forum.obsidian.md/).
