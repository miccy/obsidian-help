---
aliases:
  - Switch to Obsidian Sync
  - Migrate to Obsidian Sync
  - Obsidian Sync/Migration
cssclasses:
  - soft-embed
description: Tento průvodce vysvětluje, jak migrovat vaše existující poznámky na Obsidian Sync.
mobile: true
permalink: sync/switch-to-sync
publish: true
---
Pokud již používáte jinou službu pro synchronizaci poznámek (jako iCloud, Dropbox nebo OneDrive), můžete přejít na Obsidian Sync a užít si lepší soukromí a spolehlivost.

> [!Warning]
> Nepoužívejte Obsidian Sync a jinou synchronizační službu na stejném trezoru současně. To může vést k poškození dat a konfliktům synchronizace.

## Příprava trezoru

Než povolíte Obsidian Sync, měli byste zakázat svou současnou synchronizační službu pro váš trezor.

### Pokud je váš trezor v iCloud Drive

1. Přesuňte složku svého trezoru z iCloud Drive do lokální složky na svém zařízení (např. `Dokumenty` nebo `Plocha`).
2. Před přesunem počkejte, až iCloud stáhne všechny vaše soubory.

### Pokud je váš trezor v Dropboxu, OneDrivu nebo Google Drive

1. Pozastavte nebo zakažte synchronizaci pro složku vašeho trezoru v nastavení aplikace vašeho cloudového poskytovatele.
2. Alternativně přesuňte složku svého trezoru ze synchronizované složky do lokální složky na svém zařízení.

## Nastavení Obsidian Sync

Jakmile váš trezor již není synchronizován jinou službou:

1. Otevřete svůj trezor v Obsidianu.
2. Postupujte podle pokynů v [[Set up Obsidian Sync|Nastavení Obsidian Sync]] pro vytvoření vzdáleného trezoru a připojení vašeho lokálního trezoru.
3. Počkejte na dokončení počáteční synchronizace.

## Nastavení dalších zařízení

Na vašich dalších zařízeních:

1. Otevřete Obsidian.
2. Zvolte **Open vault from Obsidian Sync** (Otevřít trezor z Obsidian Sync).
3. Připojte se ke svému vzdálenému trezoru.
4. Zvolte lokální složku, kam chcete trezor uložit.
   - **Důležité**: Ujistěte se, že tato složka *není* synchronizována jinou cloudovou službou.

Obsidian stáhne vaše poznámky ze vzdáleného trezoru do vašeho zařízení.
