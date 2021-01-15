import csv
import random

lines = 30
random_range = 1000
# writing a csv file
with open('random_values.csv', mode='w') as rand_val_file:
    random_writer = csv.writer(rand_val_file, delimiter=',')
# first we write the header line
    random_writer.writerow(['index', 'range', 'value'])
# then data lines
with open('random_values.csv', mode='a') as rand_val_file:
    random_writer = csv.writer(rand_val_file, delimiter=',')

    for i in range(lines):
        u = random.randint(0, random_range)
        random_writer.writerow([i, random_range, u])

# reading csv file
with open('random_values.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        print(f"\t index {row['index']} range {row['range']} value {row['value']}")
        line_count += 1
    print(f'Processed {line_count} lines')
# then data lines
