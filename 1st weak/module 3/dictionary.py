""" 
dictionary is key value pair
spcially looping dictionary 
"""
parson = {'name':'sada chan','address':'kalapakhi','job':'youtbuer'}

print(parson)
print(parson['name'])
print(parson.keys())
print(parson.values())

parson['langage'] = 'python'
parson['name'] = 'kala chan'
del parson['job']
sorted(parson)
print(parson)

print("-------------->")

for item in parson.items():
    print(item)


for k ,item in enumerate(parson):
    print(k,item)