---
aliases:
  - Troubleshoot Obsidian Publish
  - Publish/Troubleshooting
description: Tento průvodce popisuje běžné problémy s Obsidian Publish a jak je vyřešit.
permalink: publish/troubleshoot
mobile: true
publish: true
---

Tento průvodce popisuje běžné problémy s Obsidian Publish a jak je vyřešit.

Pro problémy související s Obsidian Sync, viz [[Troubleshoot Obsidian Sync|Řešení problémů s Obsidian Sync]].

## Změny se nezobrazují

Pokud jste publikovali změny, ale na vašem webu se nezobrazují:

1. **Vymažte mezipaměť prohlížeče**: Váš prohlížeč může mít v mezipaměti starší verzi vašeho webu. Zkuste vymazat mezipaměť nebo otevřít web v anonymním okně.
2. **Zkontrolujte chyby**: Zkontrolujte dialog **Publish changes** pro případné chybové zprávy.
3. **Počkejte několik minut**: Někdy může trvat několik minut, než se změny rozšíří na všechny servery.

## Obrázky se nenačítají

Pokud se obrázky na vašem webu nenačítají:

1. **Zkontrolujte velikost souboru**: Ujistěte se, že vaše obrázky splňují [[Publish limitations#File size|limit velikosti souboru]].
2. **Zkontrolujte cestu k souboru**: Ujistěte se, že cesta k obrázku ve vaší poznámce odpovídá umístění obrázku ve vašem trezoru.
3. **Zkontrolujte speciální znaky**: Vyhněte se používání speciálních znaků v názvech souborů obrázků.

## Problémy s vlastní doménou

Pokud vaše vlastní doména nefunguje:

1. **Zkontrolujte DNS záznamy**: Ověřte, že jsou vaše DNS záznamy nakonfigurovány správně. Viz [[Custom domains|Vlastní domény]].
2. **Počkejte na propagaci**: Změny DNS mohou trvat až 48 hodin, než se globálně rozšíří.
3. **Zkontrolujte SSL certifikát**: Pokud vidíte bezpečnostní varování, počkejte na vygenerování SSL certifikátu (až 1 hodinu).

## "Page not found" (404)

Pokud vidíte chybu "Page not found" (Stránka nenalezena):

1. **Zkontrolujte trvalý odkaz**: Ujistěte se, že URL, kterou se snažíte navštívit, odpovídá [[Permalinks|trvalému odkazu]] poznámky.
2. **Zkontrolujte stav publikování**: Ujistěte se, že poznámka byla publikována.
3. **Zkontrolujte velikost písmen**: URL rozlišují velká a malá písmena (case-sensitive). Ujistěte se, že velikost písmen odpovídá názvu souboru nebo trvalému odkazu.

## Stále máte potíže?

Pokud stále máte problémy s Obsidian Publish, kontaktujte prosím náš tým podpory.

1. Otevřete **Publish changes**.
2. Klikněte na tlačítko **Change site options** (ikona ozubeného kola).
3. Sjeďte dolů na **Contact support** (Kontaktovat podporu).
4. Klikněte na **Email support** (E-mailová podpora).
