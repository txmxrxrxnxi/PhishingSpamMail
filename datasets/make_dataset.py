import csv

input_file = 'spam.csv'
output_file = 'spam_changed.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
        open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = ['No', 'Email Text', 'Email Type']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
    
    writer.writeheader()
    
    for idx, row in enumerate(reader, start=1):
        email_type = 'Safe Email' if row['Category'] == 'ham' else 'Spam Email'
        writer.writerow({'No': idx, 'Email Text': row['Message'], 'Email Type': email_type})
        

        