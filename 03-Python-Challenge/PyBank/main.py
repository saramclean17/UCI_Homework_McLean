#Beginning of PyBank Data Project
# Create a function to import data
import os
import csv
import sys

#set up a directory to join the financial data to be able to read it
csvpath=os.path.join('Resources', 'budget_data.csv')

With open(csvpath,new line = ' ') as csvfile:
    csvreader=csv.reader(csvfile, delimiter ',')
    #print csv header information
    csv_header=next(csvreader)

#Declare variables
month=list[]
revenue=[]
revenue_change=[]
greatest_increase_in_profits=[]
greatest_decrease_in_profits=[]

#print variable data
print(f"Header": {csv_header})

#Transfer data into variables for each row in csv.reader
month.append(row[0])
revenue.append(row[1])

#Print data to calculate number of months
total_months=len(months)
print(len(month))

#Calculate total revenue in the time period
    total_revenue=sum(profit_loss)

#Calculate average monthly change in revenue
   average_change=round(sum(profit_loss_date)/(total_months -1)),2)


#Calculate greatest increase in profits
    greatest_increase = max(profit_loss_date)
    greatest_increase_date = profit_loss_date.get(greatest_increase,0)

#Calculate greatest decrease in profits
   greatest_decrease = min(profit_loss_date)
   greatest_decrease_date = profit_loss_date.get(greatest_decrease,0)

#Print output variables to Terminal
print(f'Financial Analysis')
print("-----------------------------------------")
print("Total number of month: " + str(len("month")))
print("Total revenue in period): $" + str(total_revenue))
print("Average monthly change in revenue: $" + str(round(monthly_change,2)))
print(f"Greatest increase in profits: {greatest_increase[0]}, (${greatest_increase[1]})")
print(f"Greatest decrease in profits: {greatest_decrease[0]}, (${greatest_decrease[1]})")

sys.stdout.close()

