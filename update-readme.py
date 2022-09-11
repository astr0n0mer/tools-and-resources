import json

def getHeaderRow(columns):
    # | Sr. | Site | Description |
    header = "| Sr. |"
    # |---|---|---|
    lines = "|---|"
    for column in columns:
        if "link" in column.lower():
            continue
        header += " " + column.strip().capitalize() + " |"
        lines += "---|"

    header = header + "\n" + lines + "\n"
    return header

def createTable(obj, depth):
    if(type(obj)==dict):
        for key in obj.keys():
            output.write("#"*depth + " " + key.strip() + "\n\n")
            createTable(obj[key], depth+1)
    elif(type(obj)==list):
        output.write(getHeaderRow(obj[0].keys()))
        for i in range(len(obj)):
            site = list(obj[i].values())[0].strip()
            hyperlink = list(obj[i].values())[1].strip()
            description = list(obj[i].values())[2].strip()
            output.write("| " + str(i+1) + ". | [" + site + "](" + hyperlink + ") | " + description + " |\n")
        output.write("\n")

# -------------------main-------------------
with open("raw.json", 'r') as jsonFile:
    rawData = json.load(jsonFile)
output = open("README.md", "w")

depth = 1
createTable(rawData, depth)

output.close()
print("Successfully updated README.md")
