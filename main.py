import csv
import os
import pandas as pd

datardir = "./data"
output = "./data.csv"

# open the output file
with open(output, "w") as output_file:
    header = ["sales", "date", "region"]
    csv.writer(output_file).writerow(header)
    for file_name in os.listdir(datardir):
        with open(f"{datardir}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            row_index = 0
            for input_row in reader:
                if row_index > 0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    date = input_row[3]
                    region = input_row[4]

                    if product == "pink morsel":
                        sale = float(raw_price[1:]) * int(quantity)
                        output_row = [sale, date, region]
                        csv.writer(output_file).writerow(output_row)
                row_index += 1

df = pd.read_csv(output)
df.dropna()
df.to_csv('pmsales.csv')
os.remove(output)