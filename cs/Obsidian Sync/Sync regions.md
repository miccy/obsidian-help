---
aliases:
  - Sync regions
  - Data center
  - Server location
  - Obsidian Sync/Regions
cssclasses:
  - soft-embed
description: Tento průvodce vysvětluje, jak vybrat region pro vaše data Obsidian Sync a jak přesunout data mezi regiony.
mobile: true
permalink: sync/regions
publish: true
---
Když vytvoříte nový vzdálený trezor pomocí Obsidian Sync, můžete si vybrat region, kde budou vaše data uložena.

## Dostupné regiony

Aktuálně máme servery v následujících regionech:

- **Severní Amerika**: Oregon, USA (AWS `us-west-2`)
- **Evropa**: Frankfurt, Německo (AWS `eu-central-1`)
- **Asie**: Tokio, Japonsko (AWS `ap-northeast-1`)
- **Oceánie**: Sydney, Austrálie (AWS `ap-southeast-2`)

Výběr regionu, který je k vám blíže, může vést k rychlejší synchronizaci, ale Obsidian Sync funguje dobře bez ohledu na to, který region zvolíte.

## Výběr regionu

Region si můžete vybrat při vytváření nového vzdáleného trezoru.

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Sync**.
3. Vedle **Remote vault** klikněte na **Choose** (Vybrat).
4. Vedle **Create new vault** klikněte na **Create** (Vytvořit).
5. Vyberte požadovaný **Region** z rozbalovací nabídky.

![[sync-regional-sync-servers.png#interface|300]]

## Přesun dat mezi regiony

Není možné přesunout existující vzdálený trezor do jiného regionu přímo. Místo toho musíte vytvořit nový vzdálený trezor v požadovaném regionu a synchronizovat svá data do něj.

1. **Odpojte se od aktuálního vzdáleného trezoru**:
   - Přejděte do **[[Settings|Nastavení]]** -> **Sync**.
   - Klikněte na **Disconnect** (Odpojit).
2. **Vytvořte nový vzdálený trezor v novém regionu**:
   - Postupujte podle výše uvedených kroků pro vytvoření nového vzdáleného trezoru a vyberte nový region.
3. **Připojte se a synchronizujte**:
   - Připojte svůj lokální trezor k novému vzdálenému trezoru.
   - Obsidian nahraje vaše data na nový server.
4. **Smažte starý vzdálený trezor** (volitelné):
   - Jakmile jsou vaše data bezpečně synchronizována do nového regionu, můžete starý vzdálený trezor smazat, abyste uvolnili slot.

> [!Warning]
> Když přejdete na nový vzdálený trezor, [[Version history|Historie verzí]] ze starého vzdáleného trezoru se nepřenese. V novém regionu začnete s čistou historií.
