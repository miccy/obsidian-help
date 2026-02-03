---
aliases:
  - Obsidian Publish/Publish and unpublish notes
description: Naučte se, jak publikovat svůj obsah pomocí Obsidian Publish
permalink: publish/publish
mobile: true
publish: true
---

Tato stránka vysvětluje, jak spravovat váš publikovaný obsah. Chcete-li se dozvědět, jak přizpůsobit styl vašeho webu, viz [[Customize your site|Přizpůsobení webu]].

## Předpoklady

- Účet Obsidian. Pokud žádný nemáte, [zaregistrujte se nyní](https://obsidian.md/auth?returnto=%2Faccount%2Fpublish#signup).
- Aktivní předplatné Obsidian Publish. Pokud žádné nemáte, předplaťte si ho na [panelu vašeho účtu](https://obsidian.md/account/publish).
- Základní plugin **Publish** je [[Set up Obsidian Publish#Enable Obsidian Publish|povolen]].
- Je vytvořen [[Manage sites#Create a new site|Web Publish]].

## Publikování poznámek

1. V **Pásu karet (Ribbon)** vyberte **Publish changes** (![[lucide-send.svg#icon]]).
2. V dialogu **Publish changes** vyberte **NEW** pro zobrazení všech nepublikovaných poznámek.
3. Vyberte poznámky, které chcete publikovat.
4. Zvolte **Publish**.

## Zrušení publikování poznámek (Unpublish)

Poznámky zůstávají ve vašem lokálním trezoru i poté, co zrušíte jejich publikování.

1. V **Pásu karet (Ribbon)** vyberte **Publish changes** (![[lucide-send.svg#icon]]).
2. V dialogu **Publish changes** vyberte **UNCHANGED** pro zobrazení všech publikovaných poznámek.
3. Vyberte poznámky, jejichž publikování chcete zrušit.
4. Zvolte **Publish**.

## Aktualizace publikované poznámky

1. V **Pásu karet (Ribbon)** vyberte **Publish changes** (![[lucide-send.svg#icon]]).
2. V dialogu **Publish changes** vyberte **CHANGED** pro zobrazení všech upravených poznámek od posledního publikování.
3. Vyberte poznámky, které chcete aktualizovat.
4. Zvolte **Publish**.

> [!hint] Tip
> Mazání přejmenovaných nebo odstraněných poznámek a obrázků z Publish probíhá v tomto kroku. Pro smazání těchto dat musíte ručně zaškrtnout políčko, protože z bezpečnostních důvodů není vybráno automaticky.

## Publikování propojených dat

Při publikování poznámek obsahujících odkazy na jiné poznámky nebo vložené obrázky může dojít k nefunkčním odkazům, pokud nejsou publikovány i odkazované poznámky. **Obsidian Publish** tomu pomáhá předcházet automatickým výběrem médií propojených z poznámek, které jste již vybrali.

Chcete-li zahrnout všechny propojené poznámky, vyberte **Add linked** (Přidat propojené) v dialogu **Publish changes**.

Před publikováním zkontrolujte aktualizovaný výběr, abyste se ujistili, že neobsahuje žádná data, která ještě nejste připraveni publikovat.

> [!tip] Funkce **Add linked** respektuje všechna vyloučení definovaná v [[#Ignore data|Ignorování dat]].

## Automatický výběr dat k publikování

Nastavte `publish: true` ve [[Properties|Vlastnostech]] poznámky, aby se automaticky zahrnula k publikování jako nová nebo změněná poznámka.

Můžete také automaticky vybírat poznámky a propojené obrázky v konkrétních složkách jejich přidáním jako **Included** (Zahrnuté) složky:

1. V **Pásu karet (Ribbon)** vyberte **Publish changes** (![[lucide-send.svg#icon]]) nebo otevřete [[Command palette|Paletu příkazů]] a napište **Publish: Publish changes...**.
2. Vyberte ikonu **Manage publish filters** (![[lucide-filter.svg#icon]]).
3. V sekci **Included folders** vyberte **Manage**.
4. Vyberte složky, které chcete zahrnout.
5. Složka je přidána do seznamu zahrnutých.
6. Po dokončení zvolte **Done**.

### Ignorování dat

Chcete-li ignorovat poznámku v Obsidian Publish, nastavte `publish: false` ve [[Properties|Vlastnostech]] poznámky. Poznámka se již nebude zobrazovat v seznamu poznámek k publikování.

Můžete také automaticky ignorovat poznámky a obrázky v konkrétních složkách jejich přidáním jako **Excluded** (Vyloučené) složky:

1. V **Pásu karet (Ribbon)** vyberte **Publish changes** (![[lucide-send.svg#icon]]) nebo otevřete [[Command palette|Paletu příkazů]] a napište **Publish: Publish changes...**.
2. Vyberte ikonu **Manage publish filters** (![[lucide-filter.svg#icon]]).
3. V sekci **Excluded folders** vyberte **Manage**.
4. Vyberte složky, které chcete vyloučit.
5. Složka je přidána do seznamu vyloučených.
6. Po dokončení zvolte **Done**.

> [!note] `publish: true` přepisuje vyloučené složky
> Pokud má soubor `publish: true`, bude publikován i v případě, že je ve složce nebo filtru, který je vyloučen. Je to proto, že `publish: true` poskytuje specifičtější kontrolu.
