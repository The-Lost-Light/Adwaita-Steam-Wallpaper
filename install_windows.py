import os
import winreg
from tkinter import filedialog
import shutil
import requests

custom_css_url = "https://raw.githubusercontent.com/The-Lost-Light/Adwaita-Steam-Wallpaper/refs/heads/main/custom.css"

color_themes = ["adwaita", "breeze", "catppuccin-frappe", "catppuccin-macchiato", "catppuccin-mocha", "dracula", "gruvbox", "kate", "metro", "nord", "one-pro", "pop", "tokyo-night", "tomorrow-night", "vapor", "vgui2", "yaru"]

file_types = [
	("All supported image formats", "*.apng *.bmp *.gif *.ico *.cur *.jpg *.jpeg *.jfif *.pjpeg *.pjp *.png *.svg *.tif *.tiff *.webp"),
	("APNG", "*.apng"),
	("BMP", "*.bmp"),
	("GIF", "*.gif"),
	("ICO", "*.ico;*.cur"),
	("JPG", "*.jpg;*.jpeg;*.jfif;*.pjpeg;*.pjp"),
	("PNG", "*.png"),
	("SVG", "*.svg"),
	("TIFF", "*.tif;*.tiff"),
	("WebP", "*.webp")
]


def fix_install(py_file):
	with open(py_file, "r", encoding="utf-8") as file:
		lines = file.readlines()
	lines[203] = '\twith target_css.open(encoding="utf-8") as css_file:\n'
	with open(py_file, "w", encoding="utf-8") as file:
		file.writelines(lines)


def get_choose(prompt, options=None):
	if options:
		for index, choice in enumerate(options, start=1):
			print(f"{index}). {choice}")
	return input(prompt).strip()


def install_adwaita():
	chosen_colortheme = color_themes[int(get_choose("Choose a color theme:", color_themes)) - 1]

	no_rounded_corners = ""
	if get_choose("Disable Rounded Corners? (y/n): ").lower() == "y":
		no_rounded_corners = " -e general/no_rounded_corners"

	hide_whats_new = ""
	if get_choose("Hide the Library What's New Shelf? (y/n): ").lower() == "y":
		hide_whats_new = " -e library/hide_whats_new"

	sidebar_hover_only = ""
	if get_choose("Show Library Sidebar only on mouse over? (y/n): ").lower() == "y":
		sidebar_hover_only = " -e library/sidebar_hover"

	login_qr = ""
	login_qr_choice = get_choose("Login Dialog Mobile QR Code:", ["Show", "Show only on mouse over", "Hide"])
	if login_qr_choice == "2":
		login_qr = " -e login/hover_qr"
	elif login_qr_choice == "3":
		login_qr = " -e login/hide_qr"

	try:
		os.system("python install.py --custom-css -c " + chosen_colortheme + no_rounded_corners + hide_whats_new + sidebar_hover_only + login_qr)
	except:
		exit()
	copy_image()


def get_steam_path():
	try:
		registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Valve\\Steam")
		install_path, _ = winreg.QueryValueEx(registry_key, "SteamPath")
		winreg.CloseKey(registry_key)
		return install_path
	except FileNotFoundError:
		print("Can't find steam path.")
		exit()


def copy_image():
	file_path = filedialog.askopenfilename(title="Select image", filetypes=file_types)
	if not file_path:
		print("No file selected")
		return
	custom_folder_path = get_steam_path()+"/steamui/adwaita/custom"
	try:
		shutil.copy(file_path, os.path.join(custom_folder_path, os.path.basename(file_path)))
		print(f"Copied image to {custom_folder_path}")
		tweak_css(os.path.join(custom_folder_path, "custom.css"), os.path.basename(file_path))
	except Exception as e:
		print(f"Copy failed: {e}")


def tweak_css(css_path, image_filename):
	response = requests.get(custom_css_url)
	if response.status_code == 200:
		lines = response.text.splitlines()
		lines[2] = f'\t--image-path: url("{image_filename}");'
		css_file = "\n".join(lines)
		with open(css_path, "w", encoding="utf-8") as file:
			file.write(css_file)
		print(f"custom.css is installed to {css_path}")
	else:
		print(f"Download css failed，Error code: {response.status_code}")


def uninstall():
	os.system("python install.py -u")


if __name__ == "__main__":
	operate =  get_choose("Choose an operate:", ["Install", "Uninstall"])
	if operate == "1":
		fix_install("install.py")
		install_adwaita()
	elif operate == "2":
		uninstall()
