# 帶有背景的 Adwait Steam 美化
這是一個帶有背景圖片客製化的 custom.css **[Adwaita for Steam]** 美化。

## 預覽 (露比好可愛💕)
![Library]

![Game]

## 安裝
### Linux
1. 推薦使用 [AdwSteamGtk]
2. 在 AdwSteamGtk 中複製 [custom.css] 的內容到 Preferences/Custom CSS 選項中
3. 將 \<imgage-file-name\> 改成背景圖片的檔名, 例如 `--image-path: url("background.png");`
4. 將背景圖片複製到 `~/.steam/steam/steamui/adwaita/custom`
### Windows
1. 安裝 [Python] (記得勾選 "Add python.exe to PATH")
2. 下載 [Source code (zip)] 並解壓縮
3. 將 [installer-windows.exe] 複製到第2步解壓縮後的資料夾並執行

## 調整
你可以透過修改 `--top-bar-opacity` 改變頂欄不透明度和修改 `--library-opacity` 改變收藏庫不透明度.

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

**[steam-GBC]**: 另一種透過 [Millennium] 框架加入背景圖片的方法.

[Library]: screenshots/Library.png
[Game]: screenshots/Game.png

[custom.css]: custom.css
[installer-windows.exe]: https://github.com/The-Lost-Light/Adwaita-Steam-Wallpaper/releases/download/v1.1.0/installer-windows-v1.1.0.exe

[Python]: https://www.python.org/downloads/
[Adwaita for Steam]: https://github.com/tkashkin/Adwaita-for-Steam?tab=readme-ov-file
[Source code (zip)]: https://github.com/tkashkin/Adwaita-for-Steam/releases/latest
[instructions]: https://github.com/tkashkin/Adwaita-for-Steam?tab=readme-ov-file##windows-install
[AdwSteamGtk]: https://github.com/Foldex/AdwSteamGtk
[steam-GBC]: https://github.com/YCZ01111/steam-GBC
[Millennium]: https://github.com/SteamClientHomebrew/Millennium
