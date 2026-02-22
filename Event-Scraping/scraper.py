import csv

with open('event_links.csv',newline='') as csvf:
    reader = csv.reader(csvf)
    for row in reader:
        print(', '.join(row))

