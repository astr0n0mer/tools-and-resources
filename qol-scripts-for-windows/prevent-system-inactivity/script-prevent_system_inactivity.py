import json
import pyautogui as pgui
import random

def moveMouse(numberOfMoves, secondsPerMove, runInfiniteFlag):
    width = pgui.size().width
    height = pgui.size().height
    print("NOTE: Move mouse to the TOP-LEFT corner of the screen to exit")
    while(True):
        try:
            if(not(runInfiniteFlag or numberOfMoves)):
                raise Exception()
            pgui.moveTo(random.randint(1, width), random.randint(1, height), secondsPerMove-pgui.PAUSE)
            pgui.press("ctrl")
            numberOfMoves -= 1
        except:
            print("Exiting script")
            break

# --------------------main--------------------
with open("./settings.json", 'r') as jsonFile:
    rawData = json.load(jsonFile)
hours = rawData["hours"]
minutes = rawData["minutes"]
seconds = rawData["seconds"]
durationOfScript = (hours*60 + minutes)*60 + seconds
secondsPerMove = rawData["secondsPerMove"]
numberOfMoves = int(durationOfScript/secondsPerMove)

if(numberOfMoves < 0):
    print("Script run duration needs to be greater than or equal to " + str(secondsPerMove) + " second(s)")
elif(numberOfMoves > 0):
    print("Running \"prevent_system_inactivity\" script for ", end="")
    if(hours > 0):
        print(str(hours) + " hour(s)", end=" ")
    if(minutes > 0):
        print(str(minutes) + " minute(s)", end=" ")
    if(seconds > 0):
        print(str(seconds) + " second(s)", end=" ")
    print()
    moveMouse(numberOfMoves, secondsPerMove, False)
else:
    print("Running \"prevent_system_inactivity\" script indefinitely")
    moveMouse(numberOfMoves, secondsPerMove, True)
