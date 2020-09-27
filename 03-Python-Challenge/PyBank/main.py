#Beginning of PyBank Data Project
# Create a function to import financial data
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
month=[]
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
print(len(month))

#Calculate total revenue in the time period
revenue_int=map(int, revenue)
total_revenue=(sum(revenue_int))
print(total_revenue)

#Calculate average monthly change in revenue
i=0
for i in range(len(revenue)-1): profit_loss= int(revenue[i+1]) - int(revenue[i])
revenue_change.append(profit_loss)
total=sum(revenue_change)
#print(revenue_change)
monthly_change = total/len(revenue_change)
#print(monthly_change)
print(total)

#Calculate greatest increase in profits
profit_increase =max(revenue_change)
print(profit_increase)
k=revenue_change.index(profit_increase)
month_increase = month[k+1]

#Calculate greatest decrease in profits

#Print output variables to Terminal


