# Adwait for Steam with Background Image
This is a personalization custom.css let **[Adwaita for Steam]** skin have a background image.

## Preview (Rubii💕)
![Library]

![Game]

## Install
### Linux
1. Recommend using [AdwSteamGtk]
2. Copy the [custom.css] to the Preferences/Custom CSS in AdwSteamGtk
3. Change \<imgage-file-name\> your image filename like `--image-path: url("background.png");`
4. Copy the image you want to `~/.steam/steam/steamui/adwaita/custom`
### Windows
1. Install [Python] (Remember to check "Add python.exe to PATH")
2. Download the [Source code (zip)] and unzip
3. Copy [install_windows.exe] to the folder and run it
4. Replace the [custom.css] to the `C:\Program Files (x86)\steam\steamui\adwaita\custom\custom.css`
5. Change \<imgage-file-name\> your image filename like `--image-path: url("background.png");`
6. Copy the image you want to `C:\Program Files (x86)\steam\steamui\adwaita\custom`

## Tweaks
For Top bar opacity by `--top-bar-opacity` and the Library content opacity by `--library-opacity`
You can also set the opacity using gradient, the preview image is using
```css
/* Library */
body.DesktopUI div._3xRRJfD2xy95i9NhJxLTp0 {
	background: linear-gradient(
		to right,
		rgba(0, 0, 0, 0.6),
		25%,
		rgba(0, 0, 0, 0.2)
	) !important;
}
```

## Thanks
**[Adwaita for Steam]**: The Adwait skin

**[AdwSteamGtk]**: The skin installer for linux

**[steam-GBC]**: Change background image


[Library]: screenshots/Library.png
[Game]: screenshots/Game.png

[custom.css]: custom.css
[install_windows.exe]: https://github.com/?/?/releases/latest/download/install_windows.exe

[Python]: https://www.python.org/downloads/
[Adwaita for Steam]: https://github.com/tkashkin/Adwaita-for-Steam?tab=readme-ov-file
[Source code (zip)]: https://github.com/tkashkin/Adwaita-for-Steam/releases/latest
[instructions]: https://github.com/tkashkin/Adwaita-for-Steam?tab=readme-ov-file##windows-install
[AdwSteamGtk]: https://github.com/Foldex/AdwSteamGtk
[steam-GBC]: https://github.com/YCZ01111/steam-GBC
