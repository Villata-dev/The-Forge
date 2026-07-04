#!/bin/bash
VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Uso: ./release.sh [version]"
  exit 1
fi
echo "[*] Compilando binarios de la version $VERSION..."
python scripts/build_exe.py
echo "[*] Generando tag en Git..."
git tag -a "v$VERSION" -m "Release version $VERSION"
echo "[+] Proceso finalizado."
