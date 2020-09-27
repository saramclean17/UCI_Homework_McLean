#Beginning of PyBank Data Project
# Create a function to import financial data
import os
import csv
import sys

#set up a directory to join the financial data to be able to read it
csvpath=os.path.join('Resources', 'budget_data.csv')

With open(csvpath,new line = ' ') as csvfile:
    csvreader=csv.reader(csvfile, delimiter ',')
    csv_header=next(csvreader)

#Declare variables
month=[]
revenue=[]
average_change=[]
greatest_increase_in_profits=[]
greatest_decrease_in_profits=[]

#Transfer data into variables for each row in csv.reader
month.append(row[0])
revenue.append(row[1])

#Print data to calculate number of months
print(len(month))

#Calculate total revenue in the time period


