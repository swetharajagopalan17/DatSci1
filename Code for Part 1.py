import pandas as pd

"""
data_dict = {}
list_driver_ids = []

f1 = open("driver_ids.csv", "r")
heading = f1.readline()
data1 = f1.readlines()
f1.close()

for line in data1:
    pieces = line.split(",")
    if pieces[0].strip() not in data_dict.keys():
        data_dict[pieces[0].strip()] = pieces[1].strip()

f2 = open("ride_timestamps.csv", "r")
data2 = f2.readlines()
f2.close()


for line in data2:
    pieces = line.split(",") #makes a list
    for i in range(len(pieces)):
        if i % 3 == 0:
            data_dict[pieces[i].append(pieces[])]
"""
data_dict= {}

df = pd.read_csv("driver_ids.csv")

#driver ids and onboarding dates
for i in range(len(df)):
    if df.loc[i][0] not in data_dict:
        print(df.iloc[i])
        #data_dict[df.loc[i][0]] = [df.loc[i][1]]
#print(data_dict)

"""
df = pd.read_csv("ride_ids.csv")
for key, values in data_dict.items():
    for x in range(3):
        data_dict[key].append(0)
        print(data_dict)

counter = 0
for i in range(len(df)):
    x = df.loc[i][2]
    y = df.loc[i][3]
    z = df.loc[i][4]

    for key,list_items in data_dict.items():
        print(data_dict[key])
        data_dict[key][1] += x
        data_dict[key][2] += y
        data_dict[key][3] += z
"""  







