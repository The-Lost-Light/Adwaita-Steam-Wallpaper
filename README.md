English [正體中文]
---
# Adwait for Steam with Background Image
This is a personalization custom.css let **[Adwaita for Steam]** skin have a background image.

## Preview (Rubii💕)
![Library]

![Game]

## Install
### Linux
1. Recommend install using [AdwSteamGtk]
2. Run in terminal
``` sh
curl -LsSf https://raw.githubusercontent.com/The-Lost-Light/Adwaita-Steam-Wallpaper/refs/heads/main/install.sh | sh -s /path/to/image
```
### Windows
1. Install [Python] (Remember to check "Add python.exe to PATH")
2. Download the [Source code (zip)] and unzip
3. Copy [installer-windows.exe] to the folder decompressed in step 2 and execute

## Tweaks
You can tweak [custom.css] in
- Linux: `~/.steam/steam/steamui/adwaita/custom/custom.css`
- Windows: `C:\Program Files (x86)\steam\steamui\adwaita\custom\custom.css`

For Top bar opacity by `--top-bar-opacity` and the Library content opacity by `--library-opacity`.

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
**[Adwaita for Steam]**: The Steam Adwaita skin framework

**[AdwSteamGtk]**: The skin installer for Linux

**[steam-GBC]**: Another method to change background image with [Millennium] framework


[正體中文]: README_zh-tw.md

[Library]: screenshots/Library.png
[Game]: screenshots/Game.png

[Python]: https://www.python.org/downloads/
[Source code (zip)]: https://github.com/tkashkin/Adwaita-for-Steam/releases/latest
[installer-windows.exe]: https://github.com/The-Lost-Light/Adwaita-Steam-Wallpaper/releases/download/v1.1.1/installer-windows-v1.1.1.exe

[custom.css]: custom.css

[Adwaita for Steam]: https://github.com/tkashkin/Adwaita-for-Steam?tab=readme-ov-file
[AdwSteamGtk]: https://github.com/Foldex/AdwSteamGtk
[steam-GBC]: https://github.com/YCZ01111/steam-GBC
[Millennium]: https://github.com/SteamClientHomebrew/Millennium
