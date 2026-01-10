---
aliases:
  - Status icon and messages
  - Obsidian Sync/Status
cssclasses:
  - soft-embed
description: Tato stránka vysvětluje různé stavové ikony a zprávy, které můžete vidět při používání Obsidian Sync.
mobile: true
permalink: sync/status
publish: true
---
Když je povolen Obsidian Sync, uvidíte v pravém dolním rohu aplikace (nebo v pravém postranním panelu na mobilu) stavovou ikonu. Tato ikona vám sděluje aktuální stav procesu synchronizace.

## Stavové ikony

- ![[obsidian-icon-sync-check.svg#icon]] **Fully synced** (Plně synchronizováno): Všechny vaše změny byly nahrány a všechny vzdálené změny byly staženy.
- ![[obsidian-icon-sync.svg#icon]] **Syncing** (Synchronizace): Obsidian právě nahrává nebo stahuje soubory.
- ![[obsidian-icon-sync-disconnected.svg#icon]] **Disconnected** (Odpojeno): Obsidian Sync není připojen k serveru. To může být způsobeno tím, že jste offline, nebo problémem na serveru.
- ![[obsidian-icon-sync-pause.svg#icon]] **Paused** (Pozastaveno): Synchronizace byla ručně pozastavena.

## Protokol aktivity synchronizace

Detailní protokol veškeré aktivity synchronizace si můžete prohlédnout najetím myší na stavovou ikonu (na desktopu) nebo přechodem do **Settings** (Nastavení) -> **Sync** -> **Sync activity** (Aktivita synchronizace) -> **View** (Zobrazit).

Protokol zobrazuje:

- **Uploaded** (Nahráno): Soubory, které byly úspěšně nahrány do vzdáleného trezoru.
- **Downloaded** (Staženo): Soubory, které byly úspěšně staženy ze vzdáleného trezoru.
- **Deleted** (Smazáno): Soubory, které byly smazány (buď lokálně nebo vzdáleně).
- **Accepted** (Přijato): Změny, které byly úspěšně sloučeny.
- **Errors** (Chyby): Jakékoli chyby, které se vyskytly během procesu synchronizace.

## Běžné zprávy

### "Waiting for server" (Čekání na server)

Tato zpráva znamená, že se Obsidian snaží připojit k serveru Sync. Pokud tato zpráva přetrvává, zkontrolujte své připojení k internetu.

### "Storage limit reached" (Limit úložiště dosažen)

Tato zpráva znamená, že váš vzdálený trezor je plný. Budete muset smazat některé soubory nebo [[Plans and storage limits#Upgrade your plan|upgradovat svůj plán]], abyste mohli pokračovat v synchronizaci.

### "File too large" (Soubor je příliš velký)

Tato zpráva znamená, že se snažíte synchronizovat soubor, který je větší než [[Plans and storage limits#Maximum file size|maximální velikost souboru]] povolená vaším plánem. Tento soubor bude přeskočen.
