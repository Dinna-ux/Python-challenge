#Interacting with the operating system
import os

#connecting to the csv data
csvpath = os.path.join(".","Resources","election_data.csv")

csvpath

# provide various classes for reading and writing data to CSV files
import csv
#Opening the CSV file, and declaring variables 
with open(csvpath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    data = list(csvreader)
    count_row = len(data)
    candidates = list()
    results = list()
    for i in range (0,count_row):
        candidate = data[i][2]
        results.append(candidate)
        if candidate not in candidates: 
            candidates.append(candidate)
    candidate_count = len(candidates)

#Creating a complete list of candidates who received votes, adding candidate votes and  percentage of votes each candidate won
candidate_vote = list()
percentage_votes = list()
for j in range (0,candidate_count):
        candidate_name = candidates[j]
        candidate_vote.append(tally.count(candidate_name))
        percentage_count = candidate_vote[j]/count_row
        percentage_votes.append(percentage_count)

#Winner based on popular votes
winner = votes.index(max(candidate_vote))  

#printing the total number of votes each candidate won including the winner of the election based on the popular vote and formating the analysis.
print("Election Results")
print()
print("-------------------------")
print()
print(f"Total Votes: {count_row:}" )
print()
print("-------------------------" )
for k in range (0,candidate_count):
    print(f"{candidates[k]}: {percentage_votes[k]:.3%} ({candidate_vote[k]:})\n")
print("-------------------------")
print()
print(f"Winner: {candidates[winner]}")
print()
print("--------------------------")

#The text file contains for Pypoll:Total Votes, each candidate’s total votes and percent of votes, and the winner 
print("Election Results", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
print(f"Total Votes: {row_count:}", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
for k in range (0,candidate_count): 
        print(f"{candidates[k]}: {percentage_votes[k]:.3%} ({candidate_vote[k]:})", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
print(f"Winner: {candidates[winner]}", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
