---
aliases:
  - Local and remote vaults
  - Local vault
  - Remote vault
  - Obsidian Sync/Vaults
cssclasses:
  - soft-embed
description: Tato stránka vysvětluje rozdíl mezi lokálními a vzdálenými trezory v Obsidian Sync.
mobile: true
permalink: sync/local-and-remote-vaults
publish: true
---
Obsidian Sync používá koncept **lokálních trezorů** (local vaults) a **vzdálených trezorů** (remote vaults). Pochopení rozdílu mezi nimi je klíčové pro pochopení toho, jak Sync funguje.

## Lokální trezor (Local vault)

**Lokální trezor** je složka na vašem zařízení, která obsahuje vaše poznámky. Toto je trezor, se kterým pracujete, když používáte Obsidian.

- Je uložen na pevném disku nebo úložišti vašeho zařízení.
- Můžete k němu přistupovat, i když jste offline.
- Změny, které provedete, se okamžitě uloží do vašeho lokálního trezoru.

## Vzdálený trezor (Remote vault)

**Vzdálený trezor** je trezor uložený na serverech Obsidian Sync. Slouží jako centrální uzel pro synchronizaci vašich dat.

- Je uložen v cloudu.
- Soubory ve vzdáleném trezoru nemůžete upravovat přímo.
- Obsahuje historii vašich změn ([[Version history|Historie verzí]]).

## Jak fungují společně

Když nastavíte Obsidian Sync, připojíte **lokální trezor** ke **vzdálenému trezoru**.

1. Když provedete změny ve svém lokálním trezoru, Obsidian nahraje tyto změny do vzdáleného trezoru.
2. Vzdálený trezor poté uloží tyto změny a historii verzí.
3. Ostatní zařízení připojená ke stejnému vzdálenému trezoru si tyto změny stáhnou a aktualizují své vlastní lokální trezory.

![[obsidian-sync-diagram.png]]

Tato architektura zajišťuje, že:

- Vždy máte lokální kopii svých dat.
- Můžete pracovat offline a synchronizovat své změny později.
- Vaše data jsou zálohována ve vzdáleném trezoru.

## Správa trezorů

Své vzdálené trezory můžete spravovat v nastavení Sync.

- Pro vytvoření nového vzdáleného trezoru viz [[Set up Obsidian Sync#Create a new remote vault|Vytvoření nového vzdáleného trezoru]].
- Pro smazání vzdáleného trezoru viz [[Set up Obsidian Sync#Delete a remote vault|Smazání vzdáleného trezoru]].
- Pro kontrolu využití úložiště viz [[Plans and storage limits#Check storage usage|Kontrola využití úložiště]].
