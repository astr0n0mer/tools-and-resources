# Prevent System Inactivity

## Steps:

1. Define the run duration using [settings.json](./settings.json)
1. Run [script-prevent_system_inactivity.exe](./script-prevent_system_inactivity.exe)

## Potential values for [settings.json](./settings.json)

| Duration = hours+minutes+seconds | Notes                                       |
| -------------------------------- | ------------------------------------------- |
| if _duration_ == 0               | The script runs indefinitely.               |
| if _duration_ > 0                | The script runs for the specified duration. |
| if _duration_ < 0                | The script does not run.                    |

_Note_: `secondsPerMove` is the time taken for moving the mouse pointer from one point to another.
