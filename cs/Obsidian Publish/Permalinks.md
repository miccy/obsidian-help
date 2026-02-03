---
aliases:
  - Permalinks
  - Obsidian Publish/Permalink
description: Naučte se, jak nastavit trvalé URL adresy pro stránky vašeho webu Obsidian Publish.
permalink: publish/permalinks
mobile: true
publish: true
---

Obsidian Publish vám umožňuje nastavit **trvalé odkazy** (permalinks) pro vaše poznámky. To je užitečné, pokud chcete sdílet odkaz na poznámku a chcete mít jistotu, že odkaz přestane fungovat, i když poznámku později přejmenujete.

## Nastavení trvalého odkazu

Chcete-li nastavit trvalý odkaz pro poznámku, musíte použít vlastnost `permalink` v hlavičce (frontmatter) poznámky.

1. Otevřete poznámku, pro kterou chcete nastavit trvalý odkaz.
2. Přidejte vlastnost `permalink` do hlavičky.
3. Nastavte hodnotu na cestu, kterou chcete pro poznámku (např. `/moje-poznamka`).

```yaml
---
permalink: /moje-poznamka
---
```

Jakmile poznámku publikujete, bude dostupná na `publish.obsidian.md/vas-web/moje-poznamka`.

## Výchozí trvalé odkazy

Ve výchozím nastavení je URL poznámky odvozena z její cesty k souboru.

- Poznámka s názvem `Moje Poznámka.md` v kořenovém adresáři vašeho trezoru bude mít URL `/Moje+Poznámka`.
- Poznámka s názvem `Moje Poznámka.md` ve složce s názvem `Moje Složka` bude mít URL `/Moje+Složka/Moje+Poznámka`.

Pokud poznámku přejmenujete nebo přesunete, její výchozí URL se změní, což může narušit existující odkazy. Nastavení vlastního trvalého odkazu tomu zabrání.

## Úvodní stránka (Index page)

Můžete nastavit konkrétní poznámku jako úvodní stránku (domovskou stránku) vašeho webu.

1. Otevřete **Publish changes**.
2. Klikněte na tlačítko **Change site options** (ikona ozubeného kola).
3. Pod **Home page file** (Domovská stránka) vyberte poznámku, kterou chcete použít jako domovskou stránku.
4. Klikněte na **Save site settings** (Uložit nastavení webu).

Alternativně můžete nastavit trvalý odkaz poznámky na `/`, aby se stala domovskou stránkou.

```yaml
---
permalink: /
---
```
