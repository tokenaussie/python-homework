#Pseudocode
#Provided an excel spreadsheet with 2 columns (Date and profit/losses)
#Task is to create a python script
#The total number of months included in the dataset.
#The net total amount of Profit/Losses over the entire period.
#The average of the changes in Profit/Losses over the entire period.
#The greatest increase in profits (date and amount) over the entire period.
#The greatest decrease in profits (date and amount) over the entire period.

# Import the pathlib and csv
from pathlib import Path
import csv

# Set the path
budget_csv = Path("budget_data.csv")

# Initialise variables
months = []
profit = []

# Open the csv file as an object
# We use the next function to read each row of data after the header 
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

# Run the loops to extract information
    for row in csvreader:
        
        # Months and profit are variables defined above, as a list.
        # Row represents the value returned from each iteration of csvreader.
        # 0 means that I am taking the first column of csvreader (date), and adding that to the months list.
        # 1 means that I am taking the second column of csvreader (profit/losses), and adding that to the profit list.
        months.append(row[0])
        profit.append(row[1])
        
        # Total number of months included in data set
        # Use len because you are counting the number of rows
        total_months = len(months)

# Define variables again for next step
total_profit = 0
change_profit = 0
series_profit = []
y=0
z=1
            
# The net total amount of Profit/Losses over the entire period.
# Remember profit is a list. You are saying that for x in the profit list, the total profit keeps adding onto itself.
# Int is used to make x an integer.
# change profit is taking each integer value of z minus integer value of y.
# Series_profit is a list I defined. I am adding the change profit to the list to create a series profit.
for x in profit:
    total_profit = total_profit +int(x)
    if z < total_months:
        change_profit = int(profit[z]) - int(profit[y])
        series_profit.append(change_profit)
        y = y + 1
        z = z + 1
        
# The average of the changes in Profit/Losses over the entire period.
# We are taking the sum of the series profit list, divided by the number of rows inside the list, rounded to 2 decimal places.
average_change = round(sum(series_profit) / len(series_profit), 2)
        
# The greatest increase in profits (date and amount) over the entire period.
# We are finding out what the max profit is, then using that to find out where in the index the date that occured.
# Followed by +1 to get the month when that occurred.
max_profit = max(series_profit)
date_max_index = series_profit.index(max_profit)
date_max = months[(date_max_index+1)]

# The greatest decrease in profits (date and amount) over the entire period.
# Exactly like the previous example.
min_profit = min(series_profit)
date_min_index = series_profit.index(min_profit)
date_min = months[(date_min_index+1)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_max} ${max_profit}")
print(f"Greatest Decrease in Profits: {date_min} ${min_profit}")

# Exporting text file with resutls
with open ('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Total: ${total_profit}" + "\n")
    text.write(f"Average Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Profits: {date_max} ${max_profit}" + "\n")
    text.write(f"Greatest Decrease in Profits: {date_min} ${min_profit}")