import csv
import random


csv.field_size_limit(500 * 1024 * 1024)

file1 = 'Phishing_Email.csv'
file2 = 'spam_changed.csv'
output_file = 'PhishingSpamMail.csv'

rows = []


with open(file1, 'r', newline='', encoding='utf-8') as f1, \
        open(file2, 'r', newline='', encoding='utf-8') as f2:
    
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    
    headers = next(reader1)
    next(reader2)

    rows.extend(list(reader1))
    rows.extend(list(reader2))

random.shuffle(rows)

for i, row in enumerate(rows, start=1):
    row[0] = i

with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)  # Write the headers
    writer.writerows(rows)    # Write the shuffled rows

