---
aliases:
  - File recovery
  - Core plugins/File recovery
  - Backup
  - Restore
description: Automaticky zálohujte své poznámky a obnovujte předchozí verze.
permalink: plugins/file-recovery
mobile: true
publish: true
---

Plugin **File recovery** (Obnova souborů) automaticky pořizuje snímky (snapshots) vašich poznámek v pravidelných intervalech. To poskytuje záchrannou síť proti náhodné ztrátě dat.

## Jak to funguje

- Obsidian uloží snímek vaší poznámky každých X minut (nastavitelné).
- Snímky jsou uloženy lokálně ve vašem zařízení v konfigurační složce `.obsidian`.
- Snímky se uchovávají po určitý počet dní (nastavitelné).

## Obnova poznámky

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **File recovery** (Obnova souborů).
3. Klikněte na **View** (Zobrazit) vedle **Snapshots** (Snímky).
4. Vyhledejte poznámku, kterou chcete obnovit.
5. Vyberte snímek ze seznamu pro jeho náhled.
6. Klikněte na **Copy to clipboard** (Kopírovat do schránky) pro obnovení obsahu, nebo zkopírujte/vložte ručně.

## Konfigurace

Interval snímků a délku historie můžete nakonfigurovat v **Settings** (Nastavení) -> **File recovery** (Obnova souborů).

> [!Note]
> Obnova souborů není náhradou za řádné řešení zálohování. Chrání pouze proti náhodným úpravám nebo smazání v rámci Obsidianu. Nechrání proti selhání pevného disku nebo poškození souborového systému.
