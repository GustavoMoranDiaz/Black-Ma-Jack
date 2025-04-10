import csv
s = ['H', 'S', 'D', 'C']
with open('cardN.csv', 'w', newline='') as csvfile:
    fieldnames = ['card value', 'suit']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
    for i in s:
        for j in range(1, 14):
            writer.writerow({'card value': j, 'suit': i})
            