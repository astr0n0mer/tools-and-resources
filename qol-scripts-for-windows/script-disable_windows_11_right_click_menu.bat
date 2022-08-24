@echo off
rem Source: https://techdows.com/2021/10/disable-or-enable-windows-11-new-context-menu.html

@reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
pause