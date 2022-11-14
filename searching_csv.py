import pandas as pandasForSortingCSV
import csv

csvData = pandasForSortingCSV.read_csv("users.csv")
                                        
values=csvData.values.tolist()

username=input("enter username:\n")
for row in values:
    if (row[4]==username):
        print(row)
        break
    else:
        print("no user found with this credentials")