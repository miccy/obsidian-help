---
aliases:
  - Set up Obsidian Sync
  - Obsidian Sync/Quick Start
  - Obsidian Sync/Setup
cssclasses:
  - soft-embed
description: Tento průvodce vysvětluje, jak nastavit Obsidian Sync na vašich zařízeních.
mobile: true
permalink: sync/set-up
publish: true
---
Obsidian Sync je integrován přímo do aplikace Obsidian, takže nemusíte instalovat žádné další pluginy ani software.

Abyste mohli používat Obsidian Sync, musíte si nejprve vytvořit účet a předplatit si Obsidian Sync.

## Vytvoření účtu

1. Otevřete stránku [účet Obsidian](https://obsidian.md/account).
2. Pokud ještě nemáte účet, zvolte **Sign up** (Registrovat) a postupujte podle pokynů.
3. Po přihlášení přejděte do sekce **Sync** a předplaťte si Obsidian Sync.

## Nastavení Sync

Po zakoupení Obsidian Sync můžete v Obsidianu povolit základní plugin Sync.

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Core plugins** (Základní pluginy).
3. Zapněte **Sync**.
4. V postranním panelu se objeví nová karta **Sync**. Vyberte ji pro otevření nastavení Sync.
5. Přihlaste se ke svému účtu Obsidian.

## Připojení ke vzdálenému trezoru

Po přihlášení musíte připojit svůj lokální trezor ke [[Local and remote vaults|vzdálenému trezoru]].

> [!Info] Co je vzdálený trezor?
> Vzdálený trezor je online verze vašeho trezoru uložená na serverech Obsidian Sync. Slouží jako centrální uzel pro synchronizaci vašich dat mezi zařízeními.

### Vytvoření nového vzdáleného trezoru

Pokud jste ještě nevytvořili vzdálený trezor, můžete jej vytvořit přímo z aplikace.

1. V nastavení Sync vedle **Remote vault** zvolte **Choose** (Vybrat).
2. Vedle **Create new vault** zvolte **Create** (Vytvořit).
3. Pojmenujte svůj vzdálený trezor.
4. Vyberte [[#Regionální synchronizační servery|region]] pro svůj vzdálený trezor.
5. Zvolte **Create**.
6. Zvolte **Connect** (Připojit) pro propojení vašeho lokálního trezoru s novým vzdáleným trezorem.
7. Zvolte **Start syncing** (Spustit synchronizaci) pro zahájení procesu synchronizace.

### Připojení k existujícímu vzdálenému trezoru

Pokud již máte vzdálený trezor (například vytvořený na jiném zařízení), můžete se k němu připojit.

1. V nastavení Sync vedle **Remote vault** zvolte **Choose**.
2. Zvolte **Connect** vedle vzdáleného trezoru, se kterým chcete synchronizovat.
3. Zvolte **Start syncing** pro zahájení stahování vašich poznámek.

> [!Tip]
> Pokud nastavujete nové zařízení a chcete stáhnout existující trezor, můžete nejprve vytvořit nový lokální trezor, nebo použít možnost **Open vault from Obsidian Sync** (Otevřít trezor z Obsidian Sync) v přepínači trezorů.

## Konfigurace nastavení Sync

Po připojení můžete nakonfigurovat, které soubory a nastavení chcete synchronizovat.

- Ve výchozím nastavení Obsidian Sync synchronizuje obrázky, zvuk, video a soubory PDF.
- Synchronizaci pro další typy souborů, nastavení a pluginy můžete povolit v sekci **Selective sync** (Selektivní synchronizace).
- Další podrobnosti naleznete v části [[Sync settings and selective syncing|Nastavení synchronizace a selektivní synchronizace]].

## Synchronizace na mobilních zařízeních

Nastavení Sync na mobilu je podobné jako na desktopu.

1. Otevřete aplikaci Obsidian na svém mobilním zařízení.
2. Otevřete paletu příkazů (tažením dolů z horní části) a vyhledejte **Sync: Open Sync settings**.
3. Nebo přejděte do **Settings** -> **Sync**.
4. Přihlaste se a připojte se ke svému vzdálenému trezoru podle výše uvedeného popisu.

## Smazání vzdáleného trezoru

> [!tip] Smazání vzdáleného trezoru neodstraní vaše lokální data ve vašem zařízení.

1. Otevřete **[[Settings|Nastavení]]**.
2. V postranním panelu vyberte **Sync**.
3. Vyberte **Manage** (Spravovat) vedle Remote vaults. Otevře se okno se seznamem vašich vzdálených trezorů.
4. Vyberte ikonu koše ( ![[lucide-trash-2.svg#icon]] ) vedle vzdáleného trezoru, který chcete smazat.
5. Potvrďte smazání výběrem červeného tlačítka **Delete** (Smazat).
6. Váš vzdálený trezor byl smazán.

> [!info] Pokud ikona koše není viditelná, možná se budete muset nejprve odpojit od vzdáleného trezoru. Po odpojení vyberte tlačítko **Choose** pro otevření seznamu vzdálených trezorů.

### Regionální synchronizační servery

Obsidian Sync vám umožňuje vybrat umístění hostingu pro váš vzdálený trezor. Pokud používáte verzi Obsidianu `1.4.16` nebo starší, umístění bude vybráno automaticky za vás.

Pokud si nejste jisti, v jakém regionu se váš aktuální trezor nachází, podívejte se na návod [[Security and privacy#Where can I find my current Sync server and where is it hosted?|Kde najdu svůj aktuální Sync server a kde je hostován?]].

![[sync-regional-sync-servers.png#interface|300]]

Po výběru umístění **nelze** vaše datové centrum přesunout na jiný server bez opětovného nahrání vašich dat. Pro změnu regionu postupujte podle [[Sync regions|průvodce regiony trezoru Sync]].

![[Security and privacy#^sync-geo-regions]]

## Další kroky

Zde jsou některé doporučené dokumenty k přečtení.

- Prozkoumejte více o [[Sync settings and selective syncing|výběru souborů a nastavení k synchronizaci]].
- Zjistěte, co se stane, pokud se váš vzdálený trezor [[Version history|zaplní]].
- [[Collaborate on a shared vault|Spolupracujte na sdíleném trezoru]] s jiným uživatelem Obsidian Sync.
- Podívejte se na [[Frequently asked questions|Sync FAQ]] pro odpovědi na běžné otázky.
