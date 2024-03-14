#provides a function to interact with the operating system
import os

#open the csv file
csvpath = os.path.join(".","Resources","budget_data.csv")
csvpath 

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
        
#Calculating the total number of months included in the dataset
months_included = len(months)

#Calculating net total amount of "Profit/Losses" over the entire period
net_total_amount = sum(total_profit_losses)

#Calculating changes in "Profit/Losses" over the entire period
for i in range(1, months_included):
    change_profit_losses = total_profit_losses[i]-total_profit_losses[i-1]
    changes.append(change_profit_losses)

#Calculating the average of the changes above
average_change = sum(changes) / len(changes)

#greatest increase and deacrease in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_profit = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_profit = months[changes.index(greatest_decrease) +1]

#Analysing and printing the results
print("Financial Analysis")
print()
print("-------------------------")
print()
print(f"Total Months: {months_included}\n")
print(f"Total: ${net_total_amount}\n")
print(f"Average Change: ${average_change:.2f}\n")
print(f"Greatest Increase in Profits: {greatest_increase_profit} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_profit} (${greatest_decrease})\n")

##The text file contains for PyBank:Total Months, Total, Average change,Greatest Increase, and Greatest Decrease
print("Financial Analysis", file=open("PyBank.txt", "a"))
print("-------------------------", file=open("PyBank.txt", "a"))
print(f"Total Months: {months_included}", file=open("PyBank.txt", "a"))
print(f"Total: ${net_total_amount}", file=open("PyBank.txt", "a"))
print(f"Average Change: ${average_change:.2f}", file=open("PyBank.txt", "a"))
print(f"Greatest Increase in Profits: {greatest_increase_profit} (${greatest_increase})", file=open("PyBank.txt", "a"))
print(f"Greatest Decrease in Profits: {greatest_decrease_profit} (${greatest_decrease})", file=open("PyBank.txt", "a"))

