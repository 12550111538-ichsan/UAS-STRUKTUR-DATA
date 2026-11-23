@echo off
cd /d "%~dp0"
python main.py
if errorlevel 1 (
  echo.
  echo Program gagal dijalankan. Pastikan Python sudah terpasang dan dikenali PowerShell.
  pause
)
