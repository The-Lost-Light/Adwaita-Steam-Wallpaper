import os

bat_file = 'install_windows.bat'
py_file = 'install.py'

with open(bat_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines[148] = lines[148][:17] + ' --custom-css' + lines[148][17:]

with open(bat_file, 'w', encoding='utf-8') as file:
    file.writelines(lines)

with open(py_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines[203] = '\twith target_css.open(encoding="utf-8") as css_file:\n'

with open(py_file, 'w', encoding='utf-8') as file:
    file.writelines(lines)

os.system(bat_file)
