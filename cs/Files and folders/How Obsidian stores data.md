---
aliases:
  - How Obsidian stores data
  - Files and folders/How Obsidian stores data
description: Přečtěte si, jak Obsidian ukládá vaše poznámky a nastavení.
permalink: files-and-folders/how-obsidian-stores-data
mobile: true
publish: true
---

Obsidian je postaven na principu, že vaše data patří vám. Na rozdíl od mnoha jiných aplikací pro psaní poznámek Obsidian neukládá vaše poznámky do proprietární databáze. Místo toho je ukládá jako soubory Markdown v prostém textu do složky na vašem počítači.

## Trezor (The Vault)

Složku, která obsahuje vaše poznámky, nazýváme **Trezor** (Vault). Můžete mít tolik trezorů, kolik chcete, a každý trezor může obsahovat tolik poznámek, kolik chcete.

Protože trezor je jen složka, můžete ke svým poznámkám přistupovat pomocí jakékoli jiné aplikace, která dokáže číst textové soubory. To znamená, že nejste nikdy uzamčeni v Obsidianu.

## Struktura souborů

Uvnitř vašeho trezoru Obsidian odráží strukturu vašeho souborového systému.

- **Složky**: Složky v Obsidianu odpovídají přímo složkám na vašem počítači.
- **Poznámky**: Poznámky odpovídají souborům `.md`.
- **Přílohy**: Obrázky a další přílohy odpovídají jejich příslušným souborům (např. `.png`, `.pdf`).

## Globální nastavení

Obsidian také ukládá některá globální nastavení, která se vztahují na všechny vaše trezory. Ta jsou uložena v umístění specifickém pro systém.

- **Windows**: `%APPDATA%\Obsidian\`
- **macOS**: `~/Library/Application Support/obsidian/`
- **Linux**: `~/.config/obsidian/` (nebo podobně v závislosti na distribuci)

## Složka `.obsidian`

Každý trezor má skrytou složku s názvem `.obsidian`, která obsahuje nastavení specifická pro tento trezor. Viz [[Configuration folder|Konfigurační složka]] pro více podrobností.
