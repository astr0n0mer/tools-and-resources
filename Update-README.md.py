import json

def getHeaderRow(columns):
    # | Sr. | Site | Description |
    header = "| Sr. |"
    # |---|---|---|
    lines = "|---|"
    for column in columns:
        if column.lower()=="hyperlink":
            continue
        header += " " + column.capitalize() + " |"
        lines += "---|"

    header = header + "\n" + lines + "\n"
    return header

def createTable(obj, depth):
    if(type(obj)==dict):
        for key in obj.keys():
            output.write("#"*depth + " " + key + "\n\n")
            createTable(obj[key], depth+1)
    elif(type(obj)==list):
        output.write(getHeaderRow(obj[0].keys()))
        for i in range(len(obj)):
            site = list(obj[i].values())[0]
            hyperlink = list(obj[i].values())[1]
            description = list(obj[i].values())[2]
            output.write("| " + str(i+1) + ". | [" + site + "](" + hyperlink + ") | " + description + " |\n")
        output.write("\n")

# -------------------main-------------------
rawFile = open("raw.json")
rawData = json.load(rawFile)
output = open("README.md", "w")

depth = 1
createTable(rawData, depth)

rawFile.close()
output.close()
print("Successfully updated README.md")
