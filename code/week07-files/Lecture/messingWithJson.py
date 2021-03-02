# messing with json
import json

electricBill = {
    'name' : 'andrew',
    'amount' : '999'
}

#with open("storeData.json", "wt") as f:
#    json.dump(electricBill, f)

with open("storeData.json", "rt") as f:
    readDict = json.load(f)
    print (readDict["name"])