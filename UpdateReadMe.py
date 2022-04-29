# Read raw.json
# Store the name of each mainSection i.e. Cheat Sheets, Courses, Dev Tools, etc in mainSectionList
# Store subSectionList in mainSection i.e. General, CSS Tools, Fonts, etc in subSectionList
    # for each subSection in subSectionList, invoke createTable(mainSection, subSection)

import json

def getHeaderRow(columns):
    header = ""
    # | Sr. | Site Name | Hyperlink | Description |
    header = "\n\n| Sr. | "
    for column in columns:
        header += column + " | "
    return header

def getTableLines(columns):
    # |---|---|---|---|
    lines = "\n| --- |"
    for column in columns:
        lines += " --- |"
    return lines

def newLine():
    output.write("\n")

def createTable(mainSection, subSection):
    columns = list(rawData[root][mainSection][subSection][0].keys())
    output.write("## " + subSection)
    output.write(getHeaderRow(columns))
    output.write(getTableLines(columns))

    newLine()
    for row in range(len(rawData[root][mainSection][subSection])):
        output.write("| " + str(row+1) + ". | ")
        for col in columns:
            output.write(rawData[root][mainSection][subSection][row][col] + " | ")
        newLine()

    # output.write(getTableLines(columns))
    newLine()

rawFile = open("raw.json")
rawData = json.load(rawFile)
root = "root"
output = open("README.md", "w")

mainSectionList = list(rawData[root].keys())
for mainSection in mainSectionList:
    subSectionList = list(rawData[root][mainSection].keys())
    subSectionCount = len(subSectionList)

    for subSection in subSectionList:
        createTable(mainSection, subSection)

rawFile.close()
output.close()
