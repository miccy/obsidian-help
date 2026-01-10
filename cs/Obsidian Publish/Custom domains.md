---
aliases:
  - Custom domains
  - Obsidian Publish/Custom domain
description: Naučte se, jak nastavit vlastní doménu pro váš web Obsidian Publish.
permalink: publish/custom-domains
mobile: true
publish: true
---

Obsidian Publish vám umožňuje používat pro váš web vlastní doménové jméno (např. `www.example.com`) nebo subdoménu (např. `poznamky.example.com`).

## Konfigurace vaší domény

Chcete-li použít vlastní doménu, musíte nejprve nakonfigurovat záznamy DNS pro vaši doménu u vašeho registrátora (např. GoDaddy, Namecheap, Google Domains, Wedos).

### Subdoména (např. poznamky.example.com)

Pokud chcete používat subdoménu, musíte vytvořit **záznam CNAME** (CNAME record).

- **Typ**: CNAME
- **Jméno/Hostitel**: `poznamky` (nebo jakákoli subdoména, kterou chcete)
- **Hodnota/Cíl**: `publish.obsidian.md`
- **TTL**: Automaticky (nebo 1 hodina)

### Kořenová doména (např. example.com)

Pokud chcete používat svou kořenovou doménu (známou také jako "apex domain"), musíte vytvořit **záznam A** (A record).

- **Typ**: A
- **Jméno/Hostitel**: `@` (nebo nechte prázdné)
- **Hodnota/Cíl**: `147.182.204.144`
- **TTL**: Automaticky (nebo 1 hodina)

> [!Warning]
> Proxyování přes Cloudflare není podporováno. Pokud používáte Cloudflare, ujistěte se, že stav proxy je nastaven na **DNS Only** (ikona šedého mraku).

## Konfigurace Obsidian Publish

Jakmile jste nakonfigurovali své záznamy DNS, musíte říct Obsidian Publish, aby používal vaši vlastní doménu.

1. Otevřete **Publish changes**.
2. Klikněte na tlačítko **Change site options** (ikona ozubeného kola).
3. Pod **Site URL** (URL webu) vyberte **Custom URL** (Vlastní URL).
4. Zadejte svou vlastní doménu (např. `poznamky.example.com`).
5. Klikněte na **Save site settings** (Uložit nastavení webu).

## SSL certifikáty

Obsidian Publish automaticky generuje SSL certifikáty pro vaši vlastní doménu pomocí Let's Encrypt. Tím je zajištěno, že váš web je bezpečně dostupný přes HTTPS.

Vygenerování SSL certifikátu může trvat až hodinu poté, co nakonfigurujete svou doménu.

## Přesměrování

Pokud změníte svou vlastní doménu nebo přejdete z výchozí URL na vlastní doménu, existující odkazy na váš web mohou přestat fungovat.

Můžete nastavit přesměrování pro přeposílání návštěvníků ze starých URL na nové. Obsidian Publish však v současné době nepodporuje konfiguraci vlastních přesměrování.
