---
aliases:
  - Troubleshoot Obsidian Sync
  - Sync/Troubleshooting
cssclasses:
  - soft-embed
description: Tento průvodce popisuje běžné problémy s Obsidian Sync a jak je vyřešit.
mobile: true
permalink: sync/troubleshoot
publish: true
---
Tento průvodce popisuje běžné problémy s Obsidian Sync a jak je vyřešit.

Pro problémy související s Obsidian Publish, viz [[Troubleshoot Obsidian Publish|Řešení problémů s Obsidian Publish]].

## Řešení konfliktů

Když upravíte stejnou poznámku na dvou různých zařízeních současně, Obsidian Sync vytvoří "sloučenou" verzi poznámky, která obsahuje změny z obou zařízení.

Pokud Obsidian Sync nemůže sloučit změny automaticky, zachová verzi, která byla upravena naposledy.

V obou případech Obsidian Sync uchovává kopii obou verzí v [[Version history|Historii verzí]]. Můžete použít historii verzí k obnovení verze, kterou si chcete ponechat.

## Synchronizace se zasekla

Pokud se proces synchronizace zdá zaseknutý nebo trvá dlouho, zkontrolujte protokol **Sync activity** (Aktivita synchronizace).

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Sync**.
3. Pod **Sync activity**, klikněte na **View** (Zobrazit).
4. Protokol vám ukáže, které soubory se právě synchronizují, a případné chyby, které se vyskytly.

Běžné důvody pro pomalou synchronizaci:

- **Velké soubory**: Synchronizace velkých souborů (jako jsou videa nebo obrázky ve vysokém rozlišení) může trvat dlouho, zejména na pomalých internetových připojeních.
- **Mnoho malých souborů**: Synchronizace tisíců malých souborů může být také pomalá, protože každý soubor musí být zpracován individuálně.
- **Nestabilní připojení k internetu**: Pokud je vaše připojení nestabilní, Obsidian Sync možná bude muset opakovat nahrávání nebo stahování souborů.

## Soubory se nesynchronizují

Pokud se některé soubory nesynchronizují mezi vašimi zařízeními:

1. **Zkontrolujte nastavení Selektivní synchronizace**: Ujistěte se, že jste povolili synchronizaci pro typy souborů, které chcete synchronizovat. Viz [[Sync settings and selective syncing|Nastavení synchronizace a selektivní synchronizace]].
2. **Zkontrolujte vyloučené složky**: Ujistěte se, že soubory nejsou ve složce, kterou jste vyloučili ze synchronizace.
3. **Zkontrolujte názvy souborů**: Některé operační systémy mají omezení na názvy souborů. Vyhněte se používání speciálních znaků jako `*`, `"`, `<`, `>`, `|`, `?` nebo `:`.

## Chyba "Vault not found"

Pokud vidíte chybu "Vault not found" (Trezor nenalezen) při pokusu o připojení ke vzdálenému trezoru:

- Ujistěte se, že jste přihlášeni ke správnému účtu Obsidian.
- Zkontrolujte, zda nebyl vzdálený trezor smazán.
- Pokud jde o sdílený trezor, ujistěte se, že k němu stále máte přístup.

## Problémy se šifrovacím heslem

Pokud vás Obsidian vyzve k zadání šifrovacího hesla, ale nepamatujete si, že byste nějaké nastavovali:

- Možná jste při vytváření vzdáleného trezoru vybrali **End-to-end encryption** (Koncové šifrování) a nastavili vlastní heslo.
- Pokud si své heslo nemůžete zapamatovat, nebudete moci dešifrovat svá data. Viz [[Security and privacy#What happens if I lose my encryption password?|Co se stane, když ztratím své šifrovací heslo?]] pro více informací.

## Stále máte potíže?

Pokud stále máte problémy s Obsidian Sync, kontaktujte prosím náš tým podpory.

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Sync**.
3. Sjeďte dolů na **Contact support** (Kontaktovat podporu).
4. Klikněte na **Email support** (E-mailová podpora).
5. Tím se vytvoří nový e-mail s připojenými ladicími informacemi. Popište prosím svůj problém v těle e-mailu.
