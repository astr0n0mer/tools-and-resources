# Read raw.json
# Store the name of each mainSection i.e. Cheat Sheets, Courses, Dev Tools, etc in mainSectionList
# Store subSectionList in mainSection i.e. General, CSS Tools, Fonts, etc in subSectionList
    # for each subSection in subSectionList, invoke createTable(mainSection, subSection)

import json

def createTable(mainSection, subSection):
    columns = list(rawData[mainSection][0][subSection][0].keys())
    line = "Introduction text"
    output.write(line)

    # | # | Site Name | Hyperlink | Description |
    line = "\n\n| # | "
    for column in columns:
        line += column + " | "
    # |---|---|---|---|
    line += "\n| --- |"
    for column in columns:
        line += " --- |"
    output.write(line)

    newLine()
    for row in range(len(rawData[mainSection][0][subSection])):
        output.write("| " + str(row+1) + ". | ")
        for col in columns:
            output.write(rawData[mainSection][0][subSection][row][col] + " |")
        newLine()

    newLine()

def newLine():
    output.write("\n")

rawFile = open("raw.json")
rawData = json.load(rawFile)
output = open("README.md", "w")

mainSectionList = list(rawData.keys())
for mainSection in mainSectionList:
    subSectionList = list(rawData[mainSection][0].keys())
    for subSection in subSectionList:
        createTable(mainSection, subSection)

rawFile.close()
output.close()
