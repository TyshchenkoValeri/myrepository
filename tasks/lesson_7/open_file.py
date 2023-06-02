import csv

exchange_course = 37.7
result = []
with open('test_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        d = {}
        for key, value in row.items():
            if key:
                d[key] = round(float(value) * exchange_course, 2)
            else:
                d[key] = value
        result.append(d)

with open('salaries_uah.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, result[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(result)
