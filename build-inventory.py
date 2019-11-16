import requests

print("Getting inventory for sets...")

infile = open("sets.csv", "r")
infilelines = infile.readlines()

outfile = open("inventory.csv", "w+")

for l in infilelines:
    details = l.split(",")
    setRef = details[0].strip("\"")

    URL = "https://brickset.com/exportscripts/inventory/" + setRef

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    if len(r.text) > 100:
        print("Writing inventory for set " + setRef + "...")
        outfile.write(r.text)
    else:
        print(setRef + ": no such set / no inventory")

infile.close()
outfile.close()
