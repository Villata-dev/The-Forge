# PyInstaller Build Script
import subprocess
subprocess.run(["pyinstaller", "--onefile", "--noconsole", "main.py"])
