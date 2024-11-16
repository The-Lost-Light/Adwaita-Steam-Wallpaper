# 帶有背景的 Adwait Steam 美化
這是一個帶有背景圖片客製化的 custom.css **[Adwaita for Steam]** 美化。

## 預覽 (露比好可愛💕)
![Library]

![Game]

## 安裝
### Linux
1. 推薦透過 [AdwSteamGtk] 安裝
2. 在終端中執行
``` sh
curl -LsSf https://raw.githubusercontent.com/The-Lost-Light/Adwaita-Steam-Wallpaper/refs/heads/main/install.sh | sh -s /path/to/image
```
### Windows
1. 安裝 [Python] (記得勾選 "Add python.exe to PATH")
2. 下載 [Source code (zip)] 並解壓縮
3. 將 [installer-windows.exe] 複製到第2步解壓縮後的資料夾並執行

## 調整
你可以在以下位置修改 [custom.css]
- Linux: `~/.steam/steam/steamui/adwaita/custom/custom.css`
- Windows: `C:\Program Files (x86)\steam\steamui\adwaita\custom\custom.css`

透過修改 `--top-bar-opacity` 改變頂欄不透明度和修改 `--library-opacity` 改變收藏庫不透明度。

你也可以是用顏色漸變, 例如預覽圖是透過以下修改
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

## 感謝
**[Adwaita for Steam]**: Steam Adwaita Steam 框架

**[AdwSteamGtk]**: Adwait for Steam 的 Linux 安裝程式

**[steam-GBC]**: 另一種透過 [Millennium] 框架加入背景圖片的方法


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
