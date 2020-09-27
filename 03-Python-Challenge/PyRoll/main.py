#import polling data to begin analysis
import os
import cvs
import sys

#set up directory to the polling data
csv.path=os.path.join('Resources', 'election_data.csv')
with open (csvpath, newline='') as cvsfile:
    csvreader = csv.reader(csvfile, delimiter ',')

#print (csv_reader)
csv_header = next(csvreader)

#declare variables
votes = []
county = []
candidates = []
khan = []
correy = []
otooley = []

#Transfer data into variables for each row
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

#Calculate number of votes per person
    for candidate in candidates:
        if candidate = "Khan":
        khan.append(candidates)
        khan_votes = len(khan)
    elif candidate == "Correy":
        correy.append(candidates)
        correy_votes = len(correy)
    elif candidate == "Li":
        li.append(candidates)
        li_votes = len(i)
    else:
        otooley.append(candidates)
        otooley_votes = len(otooley)

#print out candidates
#print (khan_votes)
#print (correy_votes)
#print (li_votes)
#print (ooley_votes)

#Calculate the percentage of votes per person:
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100),2)
    li_percent = round(((li_votes / total_votes)* 100), 2)
    otooley_percent = round(((otooley_votes / total_votes)*100),2)

#print (khan_percent)
#print (correy_percent)
#print (li_percent)
#print (otooley_percent)

#Calculate the winner of the votes
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

#Print out to Terminal
print ("Election Results")
print ("-------------------------------------------")
print ("Total Votes: " + str(total_votes))
print ("-------------------------------------------")
print ("Khan: " + str(khan_percent) + "%" + " (" + str(khan_votes) + ")")
print ("Correy: " + str(correy_percent) + "%" + " (" + str(correy_votes) + ")")
print ("Li: " + str(li_percent) + "%" + " (" + str(li_votes) + ")")
print ("O'Tooley: " + str(otooley_percent) + "%" + " (" + str(otooley_votes) + ")")
print ("-------------------------------------------")
print ("Winner: " + str(winner))
print ("-------------------------------------------")

#Print results into text file
sys.stdout = open ("pypoll.txt", "w")
print ("Election Results")
print ("----------------------------------------")
print ("Total Votes: " + str(total_votes))
print ("----------------------------------------")
print ("Khan: " + str(khan_percent) + "%" + "(" + str(khan_votes) + ")")
print ("Correy: " + str(correy_percent) + "%" + " (" + str(correy_votes) + ")")
print ("Li: " + str(li_percent) + "%" + " (" + str(li_votes) + ")")
print ("O'Tooley: " + str(otooley_percent) + "%" + " (" + str(otooley_votes) + ")")
print ("-------------------------------------------")
print ("Winner: " + str(winner))
print ("-------------------------------------------")
sys.stdout.close()