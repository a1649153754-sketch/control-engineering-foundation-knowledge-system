@echo off
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0UPLOAD_TO_GITHUB.ps1"
pause
