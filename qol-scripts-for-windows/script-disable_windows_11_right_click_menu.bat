@echo off
rem Source #1: https://techdows.com/2021/10/disable-or-enable-windows-11-new-context-menu.html
rem Source #2: https://www.anoopcnair.com/windows-11-context-menu-how-to-disable-enable#:~:text=want%20to%20disable

@reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
pause
