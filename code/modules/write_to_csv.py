import csv

def write_to_csv(data, filename):
    print('write_to_csv() ...')
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)