import csv
with open('python.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The Column names are as follows {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Name"]} works in the {row["Department"]} department, and was born in {row["Birth month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

