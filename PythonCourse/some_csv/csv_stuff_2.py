import csv
import random

lines = 30
random_range = 1000
# writing cv
# with open('some_random_values.csv', mode='w') as random_val_file:
#     random_writer = csv.writer(random_val_file, delimiter=',')
#
#     random_writer.writerow(['index', 'range', 'value'])

# data lines
with open('some_random_values.csv', mode='a') as random_val_file:
    random_writer = csv.writer(random_val_file,  delimeter=',')

    for i in range(lines):
        u = random.randint(0, random_range)
        random_writer.writerow([i, random_range, u])

