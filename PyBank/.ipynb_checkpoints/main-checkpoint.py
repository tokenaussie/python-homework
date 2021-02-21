# Import Libraries
import pandas as pd
from pathlib import Path

# Read in CSV file
csv_path = Path("C:\Users\ooika\Google Drive\Fintech Monash course I created this folder\Week2Homework\python-homework\PyBank\budget_data.csv")
budget_data = pd.read_csv(csv_path, parse_dates=True, index_col="Date", infer_datetime_format=True)
budget_data.head()

Assess and clean data
# Check for nulls
budget_data.isnull().mean() * 100
# Drop nulls
budget_data = budget_data.dropna().copy()
# Drop duplicates
budget_data = budget_data.drop_duplicates().copy()
# Validate no more missing values
budget_data.isnull().sum()

# Create empty lists to iterate through specific rows
total_months = []
total_profit = []
average_changes_profit = []


# Determine the net total amount of Profit/Losses over the entire period.

# Determine the average of the changes in Profit/Losses over the entire period.

# Determine the greatest increase in profits (date and amount) over the entire period.

# Determine the greatest decrease in profits (date and amount) over the entire period.


# Determine average price across two years
crypto_data_avg = crypto_data.groupby("cryptocurrency")["data_price"].mean()
crypto_data_avg


Your task is to create a Python script that analyzes the records to calculate each of the following:
The total number of months included in the dataset.
The net total amount of Profit/Losses over the entire period.
The average of the changes in Profit/Losses over the entire period.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in profits (date and amount) over the entire period.
Your resulting analysis should look similar to the following:
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
Your final script should print the analysis to the terminal and export a text file with the results.