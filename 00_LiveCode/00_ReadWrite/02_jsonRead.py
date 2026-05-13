import json

filePath = "00_LiveCode/00_ReadWrite/assets/text.txtdata2.json"

class Vehicle:
    def __init__(self,wheals,stearing):
        self.wheals = wheals
        self.stearing = stearing
        
with open(filePath, 'r') as f:
    value = json.load(f)

v1 = Vehicle(**value)

print(type(v1))
print(v1.stearing,v1.wheals)