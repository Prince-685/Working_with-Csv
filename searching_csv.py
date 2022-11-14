import pandas as pandasForSortingCSV

csvData = pandasForSortingCSV.read_csv("users.csv")
                                        
values=csvData.values.tolist()

username=input("enter username:\n")
flag=0
for row in values:
    if (row[4]==username):
        flag=1
        print(row)
        break

if flag==0:
    print("no user found with this credentials")