import PyInstaller.main

PyInstaller.main.run([
'main.py',
'--onefile',
'--windowed',
'--name=TheForge',
'--add-data=assets:assets',
'--noconfirm',
])
