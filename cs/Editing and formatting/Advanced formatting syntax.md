---
aliases:
  - Advanced formatting syntax
  - Editing and formatting/Advanced formatting syntax
  - Math
  - Diagram
  - Mermaid
description: Naučte se o pokročilých funkcích formátování, jako je matematika, diagramy a callouty.
permalink: editing-and-formatting/advanced-formatting-syntax
mobile: true
publish: true
---

Obsidian podporuje několik pokročilých funkcí formátování nad rámec standardního Markdownu.

## Matematika

Obsidian používá [MathJax](https://www.mathjax.org/) pro vykreslování matematických výrazů. Můžete použít standardní syntaxi LaTeX.

### Inline matematika

Pro přidání matematiky do řádku uzavřete svůj výraz do jednoduchých znaků dolaru `$`.

```markdown
Řešením rovnice $x^2 + 5 = 14$ je $x = 3$.
```

Řešením rovnice $x^2 + 5 = 14$ je $x = 3$.

### Matematický blok

Pro vytvoření matematického bloku uzavřete svůj výraz do dvojitých znaků dolaru `$$`.

```markdown
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

## Diagramy

Obsidian používá [Mermaid](https://mermaid-js.github.io/) pro vykreslování diagramů a grafů.

```markdown
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
```

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

## Callouty (výzvy)

Callouty vám umožňují zvýraznit konkrétní části vašich poznámek. Viz [[Callouts|Callouty]] pro více podrobností.

```markdown
> [!info]
> Zde je blok calloutu.
> Podporuje **Markdown** a [[Basic formatting syntax|wikilinky]].
```

> [!info]
> Zde je blok calloutu.
> Podporuje **Markdown** a [[Basic formatting syntax|wikilinky]].

## Poznámky pod čarou

Viz [[Basic formatting syntax#Footnotes|Poznámky pod čarou]].

## Komentáře

Viz [[Basic formatting syntax#Comments|Komentáře]].
