import csv

def generateDeck():
    s = ['H', 'S', 'D', 'C']
    with open('cardN.csv', 'w', newline='') as csvfile:
        fieldnames = ['card value', 'suit']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
        for i in s:
            for j in range(1, 14):
                if j == 1:
                    writer.writerow({'card value': "A", 'suit': i})
                elif j == 11:
                    writer.writerow({'card value': "J", 'suit': i})
                elif j == 12:
                    writer.writerow({'card value': "Q", 'suit': i})
                elif j == 13:
                    writer.writerow({'card value': "K", 'suit': i})
                else:
                    writer.writerow({'card value': j, 'suit': i})
            