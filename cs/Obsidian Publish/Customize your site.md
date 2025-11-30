---
aliases:
  - Customize your site
  - Obsidian Publish/Customization
  - Obsidian Publish/Theme
  - Obsidian Publish/Logo
description: Naučte se, jak přizpůsobit vzhled a chování vašeho webu Obsidian Publish.
permalink: publish/customize
mobile: true
publish: true
---

Vzhled a chování vašeho webu Obsidian Publish si můžete přizpůsobit tak, aby odpovídal vašemu stylu.

## Změna možností webu

Pro přístup k možnostem přizpůsobení:

1. Otevřete **Publish changes**.
2. Klikněte na tlačítko **Change site options** (ikona ozubeného kola).

### Obecná nastavení

- **Site name** (Název webu): Název vašeho webu. Ten se zobrazuje na kartě prohlížeče a ve výsledcích vyhledávání.
- **Home page file** (Domovská stránka): Poznámka, kterou návštěvníci uvidí, když navštíví kořenovou URL vašeho webu.
- **Logo**: Nahrajte logo pro váš web. Logo se zobrazuje v navigační liště.

### Motiv (Theme)

- **Light/Dark mode** (Světlý/Tmavý režim): Zvolte, zda váš web používá světlý režim, tmavý režim, nebo zda se řídí systémovou preferencí uživatele.
- **Accent color** (Barva zvýraznění): Zvolte vlastní barvu zvýraznění pro odkazy a tlačítka.

### Komponenty

Na svém webu můžete povolit nebo zakázat různé komponenty uživatelského rozhraní:

- **Graph view** (Zobrazení grafu): Zobrazuje interaktivní graf vašich poznámek.
- **Table of contents** (Obsah): Zobrazuje obsah aktuální poznámky.
- **Backlinks** (Zpětné odkazy): Zobrazuje seznam poznámek, které odkazují na aktuální poznámku.
- **Hover preview** (Náhled při najetí): Zobrazí náhled poznámky při najetí myší na odkaz.
- **Search** (Vyhledávání): Povolí vyhledávací panel pro váš web.

## Vlastní CSS

Pro pokročilé přizpůsobení můžete použít vlastní CSS (Kaskádové styly).

1. Vytvořte soubor s názvem `publish.css` v kořenovém adresáři vašeho trezoru.
2. Přidejte svá pravidla CSS do tohoto souboru.
3. Publikujte soubor `publish.css` pomocí **Publish changes**.

Obsidian Publish automaticky aplikuje styly z `publish.css` na váš web.

> [!Tip]
> HTML svého webu Publish můžete prozkoumat pomocí vývojářských nástrojů prohlížeče, abyste našli třídy CSS, na které chcete cílit.

## Vlastní JavaScript

Obsidian Publish také podporuje vlastní JavaScript.

1. Vytvořte soubor s názvem `publish.js` v kořenovém adresáři vašeho trezoru.
2. Přidejte svůj kód JavaScript do tohoto souboru.
3. Publikujte soubor `publish.js` pomocí **Publish changes**.

> [!Warning]
> Buďte opatrní při přidávání vlastního JavaScriptu. Nesprávný kód může narušit funkčnost vašeho webu.
