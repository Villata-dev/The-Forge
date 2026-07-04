#!/bin/bash
echo "[*] Ejecutando analisis estatico de codigo con Flake8..."
flake8 core/ engine/ systems/ entities/ vfx/
echo "[+] Analisis completado."
