param(
    [string]$theme_name = "dark"
)

$command = "C:\Windows\Resources\Themes\" + $theme_name + ".theme"
Invoke-Expression $command
# Invoke-Expression $command opens the settings app by default
# Script sleeps for 2 seconds to allow the settings app to open and then "SystemSettings" process is stopped
Start-Sleep -Seconds 2
Stop-Process -Name SystemSettings