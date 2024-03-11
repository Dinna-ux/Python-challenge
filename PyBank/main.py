#provides a function to interact with the operating system
import os

#location of the file
csvpath = os.path.join('Resources","budget_data.csv")
                       
#Open a file path
import csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    months = []
    total_profit_losses = []
    changes = []

    for row in csvreader:
        months.append(row[0])
        total_profit_losses.append(int(row[1]))

