---
aliases:
  - Upgrade Sync encryption
  - Update encryption
  - Encrypt remote vault
  - Obsidian Sync/Encryption
cssclasses:
  - soft-embed
description: Tento průvodce vysvětluje, jak povolit koncové šifrování pro existující trezor Obsidian Sync.
mobile: true
permalink: sync/upgrade-encryption
publish: true
---
Když jste poprvé vytvořili svůj vzdálený trezor, měli jste možnost vybrat si mezi **Spravovaným šifrováním** (Managed encryption) a **Koncovým šifrováním** (End-to-end encryption).

Pokud jste zvolili **Spravované šifrování**, můžete kdykoli přejít na **Koncové šifrování**.

> [!Warning]
> Pro upgrade šifrování musíte odpojit a znovu připojit svůj vzdálený trezor. To zahrnuje opětovné nahrání všech vašich dat. Tento proces může chvíli trvat v závislosti na velikosti vašeho trezoru.

## Upgrade šifrování

Pro upgrade šifrování musíte vytvořit nový vzdálený trezor s povoleným koncovým šifrováním a poté do něj synchronizovat svá data.

1. **Odpojte se od aktuálního vzdáleného trezoru**:
   - Přejděte do **[[Settings|Nastavení]]** -> **Sync**.
   - Klikněte na **Disconnect** (Odpojit).
2. **Vytvořte nový vzdálený trezor**:
   - Vedle **Remote vault** klikněte na **Choose** (Vybrat).
   - Vedle **Create new vault** klikněte na **Create** (Vytvořit).
   - Povolte **End-to-end encryption** (Koncové šifrování).
   - Zadejte silné heslo. **Důležité**: Uschovejte toto heslo v bezpečí. Pokud ho ztratíte, přijdete o svá data.
   - Klikněte na **Create** (Vytvořit).
3. **Připojte se a synchronizujte**:
   - Připojte svůj lokální trezor k novému vzdálenému trezoru.
   - Obsidian nahraje vaše data a před odesláním na server je zašifruje vaším novým heslem.
4. **Smažte starý vzdálený trezor** (volitelné):
   - Jakmile jsou vaše data bezpečně synchronizována do nového vzdáleného trezoru, můžete starý smazat, abyste uvolnili slot.

## Ověření stavu šifrování

Můžete si ověřit, že je pro váš vzdálený trezor povoleno koncové šifrování.

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Sync**.
3. Vedle **Remote vault** klikněte na **Manage** (Spravovat).
4. Hledejte ikonu zámku ( ![[lucide-lock.svg#icon]] ) vedle vašeho vzdáleného trezoru.
   - Pokud je zámek přítomen, koncové šifrování je povoleno.
   - Pokud zámek chybí, používáte spravované šifrování.
