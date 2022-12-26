import csv

def output_formatted_line(filename):
 with open(filename) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=',')
     line_count = 0
     for row in csv_reader:
         if line_count == 0:
             print(f'Column names are {", ".join(row)}')
             line_count += 1
         else:
             print(f'\tThere has been {row[2]} sales on {row[3]} in the {row[4]} region .')
             line_count += 1

database = int(input('Please enter the databse you would like to  reach 0, 1 or 2: '))

if database == 0:
    output_formatted_line('data/daily_sales_data_0.csv')
elif database == 1:
    output_formatted_line('data/daily_sales_data_1.csv')
elif database == 2:
    output_formatted_line('data/daily_sales_data_2.csv')
else:
    print('That is not a valid database, please retry.')
