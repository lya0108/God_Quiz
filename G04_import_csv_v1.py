import csv

file = open("gods.csv", "r")
all_gods = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_gods.pop(0)

# get the first 50 rows
print(all_gods[:50])

print(f"Length: {len(all_gods)}")