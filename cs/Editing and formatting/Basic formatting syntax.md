---
aliases:
  - Basic formatting syntax
  - Markdown syntax
  - Formatting
  - Editing and formatting/Basic formatting syntax
description: Naučte se formátovat své poznámky pomocí Markdownu.
permalink: editing-and-formatting/basic-formatting-syntax
mobile: true
publish: true
---

Obsidian používá **Markdown** k formátování vašich poznámek. Markdown je odlehčený značkovací jazyk, který můžete použít k přidání formátovacích prvků do textových dokumentů v prostém textu.

Tento průvodce pokrývá základní syntaxi formátování. Pro pokročilejší funkce viz [[Advanced formatting syntax|Pokročilá syntaxe formátování]].

## Nadpisy

Pro vytvoření nadpisu přidejte před text nadpisu jeden až šest symbolů `#`. Počet použitých `#` určuje velikost nadpisu.

```markdown
# Nadpis 1
## Nadpis 2
### Nadpis 3
#### Nadpis 4
##### Nadpis 5
###### Nadpis 6
```

## Stylování textu

| Styl | Syntaxe | Příklad |
| :--- | :--- | :--- |
| **Tučné** | `**Tučné**` | **Tučné** |
| *Kurzíva* | `*Kurzíva*` | *Kurzíva* |
| **_Tučné a Kurzíva_** | `***Tučné a Kurzíva***` | ***Tučné a Kurzíva*** |
| ~~Přeškrtnuté~~ | `~~Přeškrtnuté~~` | ~~Přeškrtnuté~~ |
| ==Zvýraznění== | `==Zvýraznění==` | ==Zvýraznění== |

## Citace

Text můžete citovat pomocí `>`.

```markdown
> Lidské bytosti čelí stále složitějším a naléhavějším problémům a jejich efektivita při řešení těchto problémů je záležitostí, která je kritická pro stabilitu a pokračující pokrok společnosti.
>
> - Doug Engelbart, 1961
```

> Lidské bytosti čelí stále složitějším a naléhavějším problémům a jejich efektivita při řešení těchto problémů je záležitostí, která je kritická pro stabilitu a pokračující pokrok společnosti.
>
> \- Doug Engelbart, 1961

## Kód

Kód můžete formátovat jak v řádku (inline), tak v blocích kódu.

### Inline kód

Text uvnitř zpětných uvozovek (backticks) na řádku bude formátován jako kód.

```markdown
V aktuálním adresáři napište `ls -a` pro výpis všech souborů.
```

V aktuálním adresáři napište `ls -a` pro výpis všech souborů.

### Bloky kódu

Text uvnitř tří zpětných uvozovek bude formátován jako blok kódu.

````markdown
```js
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'});
  }
}
```
````

```js
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'});
  }
}
```

Můžete také specifikovat programovací jazyk pro zapnutí zvýraznění syntaxe.

## Odkazy

Můžete vytvářet odkazy na jiné poznámky nebo externí webové stránky.

### Interní odkazy

Pro odkaz na jinou poznámku ve vašem trezoru použijte dvojité hranaté závorky `[[ ]]`.

```markdown
Odkaz na [[Moje poznámka]]
```

### Externí odkazy

Pro odkaz na externí webovou stránku použijte standardní syntaxi Markdown odkazu `[ ]( )`.

```markdown
[Obsidian](https://obsidian.md)
```

[Obsidian](https://obsidian.md)

## Seznamy

Můžete vytvářet neuspořádané (s odrážkami) a uspořádané (číslované) seznamy.

### Neuspořádané seznamy

Použijte `-`, `*` nebo `+` pro vytvoření odrážek.

```markdown
- Položka 1
- Položka 2
  - Položka 2a
  - Položka 2b
```

- Položka 1
- Položka 2
  - Položka 2a
  - Položka 2b

### Uspořádané seznamy

Použijte čísla následovaná tečkou pro vytvoření číslovaných seznamů.

```markdown
1. První položka
2. Druhá položka
3. Třetí položka
```

1. První položka
2. Druhá položka
3. Třetí položka

### Seznamy úkolů

Seznamy úkolů (checklists) můžete vytvořit přidáním `[ ]` k položce seznamu.

```markdown
- [ ] Položka k udělání
- [x] Hotová položka
```

- [ ] Položka k udělání
- [x] Hotová položka

## Obrázky

Obrázky můžete do poznámek přidávat pomocí stejné syntaxe jako odkazy, ale s vykřičníkem `!` na začátku.

```markdown
![Můj obrázek](https://placekitten.com/200/300)
```

Můžete také vkládat obrázky z vašeho trezoru.

```markdown
![[muj-obrazek.png]]
```

Pro změnu velikosti obrázku přidejte `|velikost` do textu odkazu.

```markdown
![[muj-obrazek.png|100]]
```

## Tabulky

Tabulky můžete vytvářet pomocí svislítek `|` a pomlček `-`.

```markdown
| První záhlaví | Druhé záhlaví |
| ------------- | :-----------: |
| Buňka obsahu  | Buňka obsahu  |
| Buňka obsahu  | Buňka obsahu  |
```

| První záhlaví | Druhé záhlaví |
| ------------- | :-----------: |
| Buňka obsahu  | Buňka obsahu  |
| Buňka obsahu  | Buňka obsahu  |

## Horizontální oddělovače

Horizontální oddělovač (čáru) můžete vytvořit pomocí tří nebo více pomlček, hvězdiček nebo podtržítek.

```markdown
---
***
___
```

---

## Poznámky pod čarou

Do svých poznámek můžete přidávat poznámky pod čarou.

```markdown
Zde je jednoduchá poznámka pod čarou,[^1] a zde je delší.[^bignote]

[^1]: Toto je první poznámka pod čarou.
[^bignote]: Zde je jedna s více odstavci a kódem.

    Odsazujte odstavce, abyste je zahrnuli do poznámky pod čarou.

    `{ muj kod }`

    Přidejte tolik odstavců, kolik chcete.
```

Zde je jednoduchá poznámka pod čarou,[^1] a zde je delší.[^bignote]

[^1]: Toto je první poznámka pod čarou.
[^bignote]: Zde je jedna s více odstavci a kódem.

    Odsazujte odstavce, abyste je zahrnuli do poznámky pod čarou.

    `{ muj kod }`

    Přidejte tolik odstavců, kolik chcete.

## Komentáře

Můžete přidávat komentáře, které jsou viditelné pouze v režimu úprav (Editing view).

```markdown
%% Toto je komentář %%
```
