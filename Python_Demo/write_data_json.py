import json

with open('order.json','r') as json_file:
    json_object=json.load(json_file)

for order in json_object["orders"]:
    del order["client"]

with open('new_order.json','w') as new_file:
    json.dump(json_object,new_file,indent=4)