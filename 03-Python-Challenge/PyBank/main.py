#Beginning of PyBank Data Project
# Create a function to import data
import os
import csv
import sys

#set up a directory to join the financial data to be able to read it
csvpath=os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print csv header information
    csv_header=next(csvreader)

#Declare variables
    month=[]
    revenue=[]
    revenue_change=[]
    monthly_change = []
    #print variable data
    #print(f"Header: {csv_header}")

#Transfer data into variables for each row in csv.reader to determine # of months
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    #print (len(month))

#Calculate total revenue in the time period
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    #print(total_revenue)

#Calculate average monthly change in revenue
    i=0
    for i in range(len(revenue)-1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
    #append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print revenue_change
    monthly_change = Total/len(revenue_change)
    #print (monthly change)
    #print(total)

#Calculate greatest increase in profits
    profit_increase = max(revenue_change)
    #print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]

#Calculate greatest decrease in profits
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month [j+1]

#Print output variables to Terminal
print(f'Financial Analysis')
print("-----------------------------------------")
print("Total number of month: " + str(len("month")))
print("Total revenue in period): $ " + str(total_revenue))
print("Average monthly change in revenue: $" + str(round(monthly_change,2)))
print(f"Greatest increase in profits: {month_increase} (${profit_increase})")
print(f"Greatest decrease in profits: {month_decrease} (${profit_decrease})")

#Print output variables to text file
sys.stdout = open("pybank.txt","w")
print(f'Financial Analysis')
print("-----------------------------------------")
print("Total number of months: " + str(len("month")))
print("Total revenue in period: $" + str(total_revenue))
print("Average monthly change in revenue: $" + str(round(monthly_change,2)))
print(f"Greatest increase in profits: {month_increase} (${profit_increase})")
print(f"Greatest decrease in profits: {month_decrease}, (${profit_decrease}")

sys.stdout.close()

