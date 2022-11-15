import json
data = '''
[
{ "id" : "001",
"x" : "2",
"name" : "Chuck"
} ,
{ "id" : "009",
"x" : "7",
"name" : "Brent"
}
]'''

# looping a list
info = json.loads(data)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

#  dictionary

data2 = '''
{
"name" : "Chuck",
"phone" : {
"type" : "intl",
"number" : "+1 734 303 4456"
},
"email" : {
"hide" : "yes"
}
}
'''

info2 = json.loads(data2)
name=info2['name']
phone_number=info2['phone']['number']
print(f'name:{name} {phone_number}  {info2["phone"]["type"]}')