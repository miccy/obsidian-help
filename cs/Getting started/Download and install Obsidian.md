---
permalink: install
---
Obsidian je dostupný pro všechny hlavní desktopové a mobilní platformy. Zde jsou všechny podporované způsoby stažení a instalace Obsidianu.

## Instalace Obsidianu na Windows

1. Otevřete prohlížeč a přejděte na stránku [Stažení Obsidianu](https://obsidian.md/download).
2. Pod **Windows** klikněte na **Universal** pro stažení instalačního souboru.
3. Otevřete instalační soubor a postupujte podle pokynů.
4. Otevřete Obsidian stejně, jako byste otevřeli jakoukoli jinou aplikaci.

## Instalace Obsidianu na macOS

1. Otevřete prohlížeč a přejděte na stránku [Stažení Obsidianu](https://obsidian.md/download).
2. Pod **macOS** klikněte na **Universal** pro stažení instalačního souboru.
3. Otevřete instalační soubor.
4. V okně, které se otevře, přetáhněte Obsidian do složky Aplikace (Applications).
5. Otevřete Obsidian stejně, jako byste otevřeli jakoukoli jinou aplikaci.

## Instalace Obsidianu na Linux

Pokud používáte Linux, můžete si Obsidian nainstalovat několika způsoby. Postupujte podle pokynů pro systém balíčků, který používáte.

### Instalace Obsidianu pomocí Snap

1. Otevřete prohlížeč a přejděte na stránku [Stažení Obsidianu](https://obsidian.md/download).
2. Pod **Linux** klikněte na **Snap** pro stažení instalačního souboru.
3. Otevřete terminál a přejděte do složky, kam jste stáhli instalační soubor.
4. V terminálu spusťte následující příkaz pro instalaci balíčku Snap: (příznak `--dangerous` je vyžadován, protože Canonical, společnost stojící za Snapem, náš balíček nekontrolovala; příznak `--classic` umožňuje Obsidianu přistupovat mimo sandbox, kde jsou uloženy vaše poznámky)

   ```bash
   snap install obsidian_<verze>_<arch>.snap --dangerous --classic
   ```

5. Otevřete Obsidian stejně, jako byste otevřeli jakoukoli jinou aplikaci.

### Instalace Obsidianu pomocí AppImage

1. Otevřete prohlížeč a přejděte na stránku [Stažení Obsidianu](https://obsidian.md/download).
2. Pod **Linux** klikněte na **AppImage** pro stažení instalačního souboru.
3. Otevřete terminál a přejděte do složky, kam jste stáhli instalační soubor.
4. V terminálu spusťte následující příkaz pro otevření Obsidianu:

   ```bash
   chmod u+x Obsidian-<verze>.AppImage
   ./Obsidian-<verze>.AppImage --no-sandbox
   ```
Poznámka: Na Chromeboocích musí být nainstalován balíček `libnss3-dev`, jinak můžete obdržet chybu `error while loading shared libraries: libnss3.so: cannot open shared object file: No such file or directory`.

### Instalace Obsidianu pomocí Flatpak

1. V terminálu spusťte následující příkaz pro instalaci Obsidianu:

   ```bash
   flatpak install flathub md.obsidian.Obsidian
   ```

2. Otevřete Obsidian spuštěním následujícího příkazu:

   ```bash
   flatpak run md.obsidian.Obsidian
   ```

## Instalace Obsidianu na Android

1. Najděte Obsidian v [Obchodě Play](https://play.google.com/store/apps/details?id=md.obsidian).
2. Klepněte na **Instalovat** pro stažení aplikace.
3. Otevřete Obsidian stejně, jako byste otevřeli jakoukoli jinou aplikaci.

Volitelně si můžete stáhnout APK pro Android ze stránky [Stažení Obsidianu](https://obsidian.md/download).

## Instalace Obsidianu na iPhone a iPad

1. Najděte Obsidian v [App Store](https://apps.apple.com/us/app/obsidian-connected-notes/id1557175442).
2. Klepněte na **Získat** pro stažení aplikace.
3. Otevřete Obsidian stejně, jako byste otevřeli jakoukoli jinou aplikaci.
