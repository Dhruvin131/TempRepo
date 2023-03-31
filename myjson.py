import json

# with open("mydata.json") as f:
#     filedata = json.load(f)
# print(filedata)

with open("mydata.json") as file:
    data = json.load(file)

print(list(data["cal"]["run"].keys())[-1])

d1 = {"z":1,"d":2}
d1["a"] = 3
print(type(d1.keys()))

x = '''{
    "a":"1",
    "b":2,
    "c":3
}'''

x = {
    "a":"1",
    "b":2,
    "c":3
}
data = json.loads(x)
print(data)
