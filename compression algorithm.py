# importing the pandas library
import csv
import pandas as pd

df = pd.read_csv("deep_sea_coral1.csv")

# updating the column value/data


for i in range(len(df["latitude"])):
    df.loc[i, 'latitude'] = round(df.loc[i, 'latitude'])
    print(i)

for i in range(len(df["longitude"])):
    df.loc[i, 'longitude'] = round(df.loc[i, 'longitude'])
    print(i)

# writing into the file
df.to_csv("rounded deep_sea_coral.csv", index=False)

with open('rounded deep_sea_coral.csv', 'r') as in_file, open('new_coral.csv', 'w') as out_file:
    seen = set()  # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue  # skip duplicate
        seen.add(line)
        out_file.write(line)

        print("working")

print("Done!")