@echo off
SET destinationFolder=windows-lockscreen-wallpapers

rem Create destinationFolder if not already exists
if not exist "%destinationFolder%" mkdir "%destinationFolder%"
rem Copy all the wallpaper files to destinationFolder
copy "%userprofile%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\*.*" "%destinationFolder%"

cd "%destinationFolder%"
rem Rename all files to .jpg
ren *.* *.jpg
rem Delete all duplicate files that have already been converted to .jpg
del *.
pause