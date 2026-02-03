---
aliases:
  - Version history
  - Obsidian Sync/Version history
  - Restore deleted files
  - Recover deleted files
  - Recover version
cssclasses:
  - soft-embed
description: Tento článek vysvětluje, jak zobrazit a obnovit předchozí verze vašich poznámek pomocí Obsidian Sync.
mobile: true
permalink: sync/version-history
publish: true
---
Když provedete změny v poznámce, Obsidian Sync uchovává historii těchto změn až po dobu jednoho roku (v závislosti na vašem [[Plans and storage limits|plánu]]). Tyto verze můžete kdykoli procházet a obnovovat.

> [!Note] Historie verzí vs. Obnova souborů
> Obsidian má vestavěný plugin [[File recovery|Obnova souborů]], který také ukládá snímky vašich poznámek.
>
> - **Historie verzí (Version history)** ukládá verze na vzdáleném trezoru, když synchronizujete změny.
> - **Obnova souborů (File recovery)** ukládá snímky lokálně ve vašem zařízení v pravidelných intervalech.
>
> Obě funkce jsou užitečné pro obnovu ztracených dat, ale fungují nezávisle na sobě.

## Zobrazení historie verzí

Chcete-li zobrazit historii verzí poznámky:

1. Klikněte pravým tlačítkem na poznámku v Průzkumníku souborů nebo klikněte na nabídku **More options** (tři tečky) v aktivní poznámce.
2. Vyberte **View version history** (Zobrazit historii verzí).
3. V levém postranním panelu se objeví seznam verzí.

Zobrazení historie verzí ukazuje:

- Datum a čas každé verze.
- Zařízení, které provedlo změnu.
- Velikost poznámky v dané verzi.

Vyberte libovolnou verzi pro zobrazení náhledu poznámky v daném okamžiku. Náhled ukazuje rozdíly (diff) mezi vybranou verzí a aktuální verzí poznámky.

- Přidaný text je zvýrazněn zeleně.
- Odstraněný text je zvýrazněn červeně.

## Obnova verze

Pokud chcete vrátit svou poznámku na předchozí verzi:

1. Postupujte podle výše uvedených kroků pro zobrazení historie verzí.
2. Vyberte verzi, kterou chcete obnovit.
3. Klikněte na **Restore this version** (Obnovit tuto verzi).

Tím se nahradí aktuální obsah poznámky vybranou verzí. Pro obnovení se vytvoří nová verze, takže neztratíte historii toho, co se stalo před obnovením.

## Obnova smazaných souborů

Obsidian Sync také uchovává historii smazaných souborů. Pro obnovení smazaného souboru:

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Sync**.
3. Vedle **Deleted files** (Smazané soubory) klikněte na **View** (Zobrazit).
4. Použijte vyhledávací panel nebo procházejte seznam pro nalezení souboru, který chcete obnovit.
5. Klikněte na **Restore** (Obnovit) vedle souboru.

Soubor bude obnoven do svého původního umístění ve vašem trezoru.

## Uchovávání verzí

Doba, po kterou je historie verzí uchovávána, závisí na vašem plánu Obsidian Sync:

- **Standard**: 1 měsíc
- **Plus**: 12 měsíců

Verze starší než doba uchování jsou automaticky smazány. To neovlivňuje vaše aktuální poznámky, pouze historii předchozích změn.

> [!Info]
> Historie verzí se nezapočítává do limitu úložiště vašeho vzdáleného trezoru.
