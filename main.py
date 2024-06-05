import csv

phones = {}

with open('big_data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        phones[f"1{row[2]}"] = row[1]

with open('rtb_bids.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] not in phones:
            with open('output.csv', 'a') as fw:
                writer = csv.writer(fw)
                writer.writerow([row[0][1:10]])