---
aliases:
  - Social media link previews
  - Obsidian Publish/Open Graph
  - Obsidian Publish/Social cards
description: Naučte se, jak přizpůsobit zobrazení vašeho webu Obsidian Publish na sociálních sítích.
permalink: publish/social-media
mobile: true
publish: true
---

Když sdílíte odkaz na svůj web Obsidian Publish na sociálních sítích (jako Twitter, Facebook nebo LinkedIn) nebo v aplikacích pro zasílání zpráv (jako Discord, Slack nebo WhatsApp), často se zobrazí karta náhledu. Toto se nazývá **náhled odkazu na sociálních sítích** (social media link preview) nebo značka **Open Graph**.

Obsidian Publish automaticky generuje tyto značky pro váš web.

## Přizpůsobení náhledů odkazů

Informace zobrazené v náhledu odkazu můžete přizpůsobit pomocí hlavičky (frontmatter) vašich poznámek.

### Titulek (Title)

Titulek náhledu odkazu se bere z názvu poznámky nebo z vlastnosti `title` v hlavičce.

```yaml
---
title: Můj vlastní titulek
---
```

### Popis (Description)

Popis se bere z vlastnosti `description` v hlavičce. Pokud není nastaven, Obsidian Publish se pokusí vygenerovat popis z obsahu poznámky.

```yaml
---
description: Toto je krátký popis obsahu stránky.
---
```

### Obrázek (Image)

Můžete nastavit vlastní obrázek pro náhled odkazu pomocí vlastnosti `image`. Hodnota by měla být cesta k obrázku ve vašem trezoru (např. `Attachments/muj-obrazek.png`).

```yaml
---
image: Attachments/muj-obrazek.png
---
```

Ideálně by obrázek měl mít alespoň **1200 x 630 pixelů** pro nejlepší zobrazení na většině platforem.

## Nastavení pro celý web

Můžete také nastavit výchozí hodnoty pro celý váš web v **Site options** (Možnosti webu).

1. Otevřete **Publish changes**.
2. Klikněte na tlačítko **Change site options** (ikona ozubeného kola).
3. Pod **Social media link previews** můžete nastavit výchozí **Site description** (Popis webu) a **Site image** (Obrázek webu).

Tato výchozí nastavení budou použita, pokud poznámka nemá vlastní popis nebo obrázek definovaný v hlavičce.
