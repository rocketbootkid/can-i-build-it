inpage = open("sets.csv", "r")
lines = inpage.readlines()
inventory = open("inventory.csv", "r")
inventorylines = inventory.readlines()

for l in lines:
    details = l.split(",")
    setRef = details[0].strip("\"")
    setName = details[1].strip("\"")

    outpage = open("html/" + setRef + ".html", "w")
    outpage.write("<html>\n<head>\n<title>" + setRef + " " + setName + " Inventory</title>\n</head>\n\n<body><h2>" + setRef + " " + setName + "</h2>\n<table cellspcing=1 cellpadding=3 border=1>\n")

    for i in inventorylines:
        inventoryDetails = i.split(",")
        if inventoryDetails[0].strip("\"") == setRef:
            outpage.write("<tr><td>" + inventoryDetails[1] + "<td>" + inventoryDetails[2] + " x " + inventoryDetails[3].strip("\"") + " " + inventoryDetails[6].strip("\"") + "<td><img src=" + inventoryDetails[7] + " width=96></tr>\n")

    outpage.write("\n</table>\n</body>\n</html>")

    outpage.close()

inpage.close()
inventory.close()