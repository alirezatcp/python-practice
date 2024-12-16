import csv

# write in csv file
with open(file='examp.csv', mode='w', newline='') as csv_file:
    write = csv.writer(csv_file) # if we want to write in csv file we should use this
    write.writerow(['name', 'age', 'weight']) # write a row

    data = [
        ['ali', 30, 90],
        ['reza', 20, 70],
        ['alireza', 22, 80]
    ]
    write.writerows(data) # write multi rows in csv file

# read from csv file
with open('examp.csv', 'r') as csv_file:
    data = csv.reader(csv_file)
    print(next(data))
    csv_file.seek(0)
    content_in_list = list(csv.DictReader(csv_file))
    print(content_in_list)