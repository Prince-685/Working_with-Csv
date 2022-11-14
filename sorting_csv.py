import pandas as pandasForSortingCSV
import csv
  

csvData = pandasForSortingCSV.read_csv("users.csv")
                                         
csvData.sort_values(["first_name"], 
                    axis=0,
                    ascending=[True],
                    inplace=True)
fields=list(csvData.keys())
values=csvData.values.tolist()

filename="users-sorted.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(values)


   
  
