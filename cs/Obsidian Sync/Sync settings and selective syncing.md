---
aliases:
  - Sync settings
  - Selective syncing
  - Obsidian Sync/Select files and settings to sync
  - Settings profile
description: Tato stránka vysvětluje nastavení synchronizace a vede vás při výběru souborů k synchronizaci.
mobile: true
permalink: sync/settings
publish: true
---

Když [[Plans and storage limits#Create a new remote vault|vytvoříte vzdálený trezor]] a [[Set up Obsidian Sync#Connect to a remote vault|připojíte se k němu]], základní plugin Sync se stane místem pro správu vašeho vzdáleného trezoru.

## Nastavení Sync

**Vzdálený trezor (Remote vault)**
Tato sekce zobrazuje váš aktuálně připojený vzdálený trezor. Obsahuje tlačítko **Disconnect** (Odpojit) pro odpojení od vzdáleného trezoru a tlačítko **Manage** (Spravovat) pro zobrazení všech vzdálených trezorů, ke kterým má váš účet přístup (včetně sdílených trezorů prostřednictvím [[Collaborate on a shared vault|spolupráce]]).

> [!todo] Pokud se váš vzdálený trezor nachází u synchronizační služby třetí strany, uvidíte červenou chybovou zprávu. Pro vyřešení postupujte podle kroků v [[Switch to Obsidian Sync]].

**Stav synchronizace (Sync status)**
Zobrazuje aktuální stav synchronizace vzdáleného trezoru. Tato sekce obsahuje tlačítko **Pause** (Pozastavit) nebo **Resume** (Obnovit) v závislosti na stavu.

**Název zařízení (Device name)**
Přiřaďte unikátní název aktuálně synchronizovanému zařízení. To pomáhá sledovat aktivitu v [[Status icon and messages#Sync activity log|protokolu synchronizace]]. Toto nastavení je specifické pro zařízení, stejně jako [[#Selective syncing|Selektivní synchronizace]].

**[[#Řešení konfliktů]]**
Zvolte, jak se řeší konflikty, když je poznámka nezávisle upravena na více zařízeních. Toto nastavení je specifické pro zařízení, stejně jako [[#Selective syncing|Selektivní synchronizace]].

**Smazané soubory (Deleted files)**
Obsahuje tlačítko **View** (Zobrazit) nebo **Restore** (Obnovit) pro smazané soubory. Další podrobnosti naleznete v [[Version history|Historii verzí]].

**Využití úložiště (Storage usage)**
Zobrazuje ukazatel průběhu, kolik z vašeho synchronizačního úložiště je využito.

> [!tip] Může trvat až 30 minut, než se aktuální využití aktualizuje kvůli zpracování na straně serveru.

**Kontaktovat podporu (Contact support)**
Poskytuje pokyny, jak [[Help and support#Contact Obsidian support|kontaktovat podporu Obsidianu]], včetně možností **Copy debug info** (Kopírovat ladicí informace) a **Email support** (E-mailová podpora).

### Řešení konfliktů

Obsidian Sync obsahuje základní [[Troubleshoot Obsidian Sync#Conflict resolution|řešení konfliktů]] pro zpracování změn provedených z různých zařízení. Od verze Obsidian 1.9.7 si můžete vybrat, jak se konflikty řeší na každém zařízení:
- **Automaticky sloučit (Automatically merge)** (výchozí): Obsidian Sync kombinuje všechny změny z různých zařízení do jednoho souboru. Ačkoli to zachová všechny úpravy, může to občas vytvořit duplicitní text nebo problémy s formátováním, které budete muset ručně vyčistit.
- **Vytvořit soubor konfliktu (Create conflict file)**: Když jsou detekovány konfliktní změny, Obsidian vytvoří samostatný soubor konfliktu místo automatického sloučení. Můžete si pak prohlédnout obě verze a sloučit je sami, což vám dává plnou kontrolu nad konečným výsledkem.

> [!note] Možnost souboru konfliktu v současné době nepodporuje nástroje pro slučování v aplikaci. Můžete použít komunitní pluginy s funkcemi "diff" nebo "merge", které vám s tímto procesem v Obsidianu pomohou.

---

V nastavení základního pluginu Sync si můžete také vybrat, co chcete synchronizovat. Tato sekce pokrývá **selektivní synchronizaci** a **synchronizaci konfigurace trezoru** spolu s jejich úskalími.

## Selektivní synchronizace

Soubory synchronizované do vašeho [[Local and remote vaults|vzdáleného trezoru]] se započítávají do vašeho [[Frequently asked questions#How large can each remote vault be|limitu úložiště]]. Ve výchozím nastavení Obsidian Sync aktivuje **selektivní synchronizaci** pro následující typy souborů:
- Obrázky
- Zvuk
- Videa
- PDF

Chcete-li synchronizovat další typy souborů, přepněte možnost `Sync all other types`.

Výchozí nastavení **synchronizace konfigurace trezoru** zahrnuje:
- Ostatní typy souborů
- Hlavní nastavení
- Vzhled
- Motivy a úryvky (snippets)
- Klávesové zkratky
- Seznam aktivních základních pluginů
- Nastavení základních pluginů

Chcete-li synchronizovat komunitní pluginy, musíte ručně povolit **Active community plugin list** (Seznam aktivních komunitních pluginů) a **Installed community plugin list** (Seznam nainstalovaných komunitních pluginů).

### Změna typů souborů, které chcete synchronizovat

1. Otevřete **[[Settings|Nastavení]] → Sync**.
2. Pod **Selective sync**, povolte typy souborů, které chcete synchronizovat.
3. Restartujte aplikaci pro použití nových nastavení. Na mobilu nebo tabletu to může vyžadovat vynucené ukončení.

Vezměte na vědomí, že váš [[Plans and storage limits|plán Sync]] definuje maximální velikost souboru, který můžete synchronizovat. Plán Standard umožňuje synchronizaci souborů až do 5 MB, zatímco plán Plus podporuje soubory až do 200 MB.

> [!info] Přidání souboru do seznamu **Excluded files** (Vyloučené soubory) jej neodstraní ze vzdáleného trezoru, pokud již byl synchronizován. Nakonfigurujte nastavení synchronizace *před* synchronizací, abyste se vyhnuli zbytečnému využití úložiště.

### Vyloučení složky ze synchronizace

Ve výchozím nastavení Obsidian synchronizuje všechny soubory a složky ve vašem trezoru. Chcete-li vyloučit konkrétní složku ze synchronizace:
1. Otevřete **[[Settings|Nastavení]] → Sync**.
2. Vedle **Excluded folders** (Vyloučené složky) vyberte **Manage** (Spravovat).
3. Vyberte složku, kterou chcete vyloučit ze seznamu.
4. Vyberte **Done** (Hotovo).

Pro odstranění složky ze seznamu vyloučení vyberte tlačítko ![[lucide-x.svg#icon]] vedle názvu složky.

#### Vždy vyloučeno ze synchronizace

##### Snímky obnovy souborů (File recovery snapshots)

Snímky v pluginu [[File recovery|Obnova souborů]] nejsou synchronizovány přes Obsidian Sync, protože snímky jsou uloženy v [[How Obsidian stores data#Global settings|Globálním nastavení]].

##### Skryté soubory a složky

Soubory a složky začínající tečkou `.` jsou považovány za skryté a vyloučené ze synchronizace. Jedinou výjimkou je [[Configuration folder|konfigurační složka]] trezoru (`.obsidian`), která se synchronizuje.

Běžné příklady skrytých souborů a složek, které nejsou synchronizovány:
- `.vscode`
- `.git`
- `.idea`
- `.gitignore`

##### Nastavení Sync

Nastavení Sync se nesynchronizují mezi zařízeními. Musíte je nakonfigurovat zvlášť na každém zařízení podle potřeby.

## Aktualizace nastavení synchronizovaného trezoru

Chcete-li upravit nastavení synchronizace na více zařízeních, postupujte podle těchto kroků:

> [!tip] Pojmy "primární" a "sekundární" zařízení jsou pouze pro přehlednost; Sync mezi nimi nerozlišuje.

### Primární zařízení

Primární zařízení funguje jako zdroj pravdy. Změny zde provedené se synchronizují na všechna ostatní zařízení.

1. Přejděte do **[[Settings|Nastavení]] → Sync**.
2. Aktivujte požadovaná nastavení pod **Vault configuration sync** (Synchronizace konfigurace trezoru).
3. Znovu načtěte nebo restartujte Obsidian. Na mobilu nebo tabletu může být vyžadováno vynucené ukončení.
4. Dejte nastavení čas na synchronizaci s vaším vzdáleným trezorem.

### Sekundární zařízení

Sekundární zařízení (například váš telefon) přijímají aktualizace z primárního zařízení.

1. Přejděte do **[[Settings|Nastavení]] → Sync**.
2. Povolte nezbytná nastavení pod **Vault configuration sync**.
3. Počkejte na stažení změn ze vzdáleného trezoru.
4. Znovu načtěte nebo restartujte aplikaci pro použití synchronizovaných nastavení. Na mobilu nebo tabletu může být vyžadováno vynucené ukončení.

### Opětovné načítání nastavení

Některá nastavení lze znovu načíst za běhu (hot reload), zatímco jiná vyžadují restart:

- **Hot-reloadable**: Většina konfigurací Obsidianu, včetně klávesových zkratek a vlastností, nastavení vzhledu a konfigurací pro již povolené základní pluginy.
- **Vyžaduje restart**: Změny CSS (např. [[CSS snippets]], [[Themes|Motivy]]), konfigurace zobrazení grafu a stavy základních pluginů (např. povolení/zakázání Denních poznámek).

Komunitní pluginy obvykle nepodporují opětovné načítání za běhu a vyžadují restart, když jsou použita nová nastavení.

> [!todo] Vývojáři pluginů: Naučte se, jak [integrovat funkci hot-reload s Obsidian Sync](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/onExternalSettingsChange).

## Profily nastavení

Obsidian Sync může synchronizovat více [[Configuration folder|konfiguračních složek]] do stejného vzdáleného trezoru, což vám umožní vytvořit oddělené profily (např. jeden pro mobil, jiný pro váš notebook).

### Vytvoření profilu nastavení

Pro vytvoření nového profilu nastavení:

1. Otevřete **[[Settings|Nastavení]] → Files and links** (Soubory a odkazy).
2. Pod **Override config folder** (Přepsat konfigurační složku) zadejte název pro váš profil, začínající tečkou (`.`), např. `.obsidian-mobile`.
3. Restartujte Obsidian pro použití změn.

> [!note]
> Změna profilu nastavení bude vyžadovat novou konfiguraci nastavení synchronizace. Abyste se vyhnuli opětovnému stahování pluginů a motivů, zkopírujte svou existující složku `.obsidian` a přejmenujte ji tak, aby odpovídala vašemu novému profilu (např. `.obsidian-mobile`), než provedete změny.
