import requests
import json
import csv
import schedule
import time


connect_API=requests.get('https://random-data-api.com/api/v2/users.json')
data=json.loads(connect_API.text)
fields =[]
for x in data:
    val = data[x]
    
    if isinstance(val,str):
        fields.append(x)
    elif isinstance(val,dict):
        for y in val:
            fields.append(y)
            if y=="coordinates":
                for z in val["coordinates"]:
                    fields.append(z)                  
    
fields.remove("coordinates")
filename = "users.csv"


with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    
def Fetch_user_data():
    connect_API=requests.get('https://random-data-api.com/api/v2/users.json')
    data=json.loads(connect_API.text)
    Fvalues =[]

    for x in data:
        val = data[x]
        
        if isinstance(val,str):
            Fvalues.append(val)
        elif isinstance(val,dict):
            for y in val:
                if y=="coordinates":
                    for z in val["coordinates"]:
                        Fvalues.append(val["coordinates"][z])
                else:
                    Fvalues.append(val[y])               
    rows=[]
    rows.append(Fvalues)
 

    with open('users.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
   
schedule.every(1).seconds.do(Fetch_user_data)




while True:
    schedule.run_pending()
    time.sleep(1)