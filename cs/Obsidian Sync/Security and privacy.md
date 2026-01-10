---
aliases:
  - Security and privacy
  - Obsidian Sync/Privacy
  - Obsidian Sync/Security
cssclasses:
  - soft-embed
description: Tato stránka vysvětluje, jak Obsidian Sync chrání vaše data pomocí koncového šifrování.
mobile: true
permalink: sync/security-and-privacy
publish: true
---
Soukromí je jedním z hlavních principů Obsidianu. Věříme, že vaše data patří vám a že nikdo jiný by k nim neměl mít přístup.

Když používáte Obsidian Sync, vaše data jsou zašifrována ve vašem zařízení pomocí vašeho **šifrovacího hesla** předtím, než jsou odeslána na naše servery. Toto se nazývá **koncové šifrování** (end-to-end encryption).

Protože neznáme vaše šifrovací heslo, nemůžeme číst vaše poznámky. To také znamená, že pokud ztratíte své heslo, **nemůžeme pro vás data obnovit**.

> [!Important]
> Pokud při nastavování Sync zvolíte **Spravované šifrování** (Managed encryption), Obsidian vygeneruje a spravuje šifrovací klíč za vás. To je pohodlné, ale znamená to, že náš tým podpory by *teoreticky* mohl přistupovat k vašim datům, pokud by k tomu byl nucen orgány činnými v trestním řízení, nebo pokud by byly naše systémy kompromitovány.
>
> Pro maximální soukromí doporučujeme zvolit **Koncové šifrování** (End-to-end encryption) a vytvořit si vlastní silné heslo.

## Často kladené otázky k šifrování

### Jaký šifrovací algoritmus Obsidian Sync používá?

Obsidian Sync používá pro šifrování **AES-256-GCM**. Jedná se o průmyslový standard, který je široce považován za bezpečný.

### Kde jsou má data uložena?

Vaše šifrovaná data jsou uložena na našich serverech. K hostování naší infrastruktury využíváme hlavní poskytovatele cloudu.

### Mohou zaměstnanci Obsidianu číst mé poznámky?

Ne. Pokud používáte **Koncové šifrování**, vaše poznámky jsou šifrovány klíčem odvozeným z vašeho vlastního hesla. Vaše heslo neukládáme, takže nemůžeme dešifrovat vaše data.

### Co se stane, když ztratím své šifrovací heslo?

Pokud ztratíte své šifrovací heslo, nebudete moci nastavit Sync na žádném novém zařízení. Vaše data jsou však stále v bezpečí na zařízeních, kde jste již Sync nastavili.

Pro zotavení ze ztráty hesla:

1. Zálohujte svá data na jednom ze synchronizovaných zařízení (např. zkopírováním složky trezoru na bezpečné místo).
2. Vytvořte nový vzdálený trezor s novým heslem.
3. Připojte svůj lokální trezor k novému vzdálenému trezoru.

### Kde najdu svůj aktuální Sync server a kde je hostován?

V nastavení Sync můžete zkontrolovat, na kterém serveru je hostován váš vzdálený trezor.

1. Otevřete **[[Settings|Nastavení]]**.
2. Vyberte **Sync**.
3. Vedle **Remote vault**, vyberte **Manage** (Spravovat).
4. Region vašeho vzdáleného trezoru je zobrazen vedle názvu trezoru.

^sync-geo-regions

Aktuálně máme servery v následujících regionech:

- **Severní Amerika**: Oregon, USA (AWS `us-west-2`)
- **Evropa**: Frankfurt, Německo (AWS `eu-central-1`)
- **Asie**: Tokio, Japonsko (AWS `ap-northeast-1`)
- **Oceánie**: Sydney, Austrálie (AWS `ap-southeast-2`)

### Je Obsidian Sync v souladu s GDPR?

Ano. Jsme odhodláni chránit vaše soukromí a dodržovat všechny platné zákony o ochraně osobních údajů, včetně GDPR.

Další informace naleznete v našich [Zásadách ochrany osobních údajů](https://obsidian.md/privacy) a [Podmínkách služby](https://obsidian.md/terms).
