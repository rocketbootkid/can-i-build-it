outpage = open("html/index.html", "w+")
inpage = open("sets.csv", "r")

lines = inpage.readlines()

outpage.write("<html>\n<head>\n<title>Lego Technic Set - Inventory Viewer</title>\n</head>\n\n<body>\n<table cellspacing=1 cellpadding=3 border=1>\n<tr><td>Set<td>Description</tr>\n")

for l in lines:
    details = l.split(",")
    setRef = details[0].strip("\"")
    outpage.write("<tr><td><a href='" + setRef + ".html'>" + details[0] + "</a><td><h2>" + details[1].strip("\"") + "</h2><td><img src='https://images.brickset.com/sets/images/" + setRef + ".jpg' width=200></tr>\n")

outpage.write("\n</table>\n</body>\n</html>")

outpage.close()
inpage.close()

