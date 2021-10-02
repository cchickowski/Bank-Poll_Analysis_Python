# Your task is to create a script that analyzes votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# Total number of votes each candidate won
# The winner of the election based on popular vote
# Use Dictionaries!!
# Start with total vote count then figure out percentages for individuals one by one
# Test often!

import os
import csv

# Candidate dictionary
candidates_dict = {}


# Set path for file
csvpath = r'C:\Users\cchic\DataViz\election_data.csv'


# Open the CSV
with open(csvpath) as csvfile:



    # Read the file
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvfile)

    # Set votes = to 0 before loop
    votes = 0
   # Use for loop to calculate total votes
    for row in csvreader:
        votes += 1
        candidate_name = row[2]
        if candidate_name in candidates_dict:
            candidates_dict[candidate_name] += 1
        else:
            candidates_dict[candidate_name] = 1

# Start percentage calculations
# Khan Percent of Vote
candidates_dict["Khan Percent of Vote"] = round((candidates_dict["Khan"]/votes) * 100)
# Correy Percent of Vote
candidates_dict["Correy Percent of Vote"] = round((candidates_dict["Correy"]/votes) * 100)
# Li Percent of Vote
candidates_dict["Li Percent of Vote"] = round((candidates_dict["Li"]/votes) * 100)
# O'Tooley Percent of Vote
candidates_dict["O'Tooley Percent of Vote"] = round((candidates_dict["O'Tooley"]/votes) * 100)

# Winner calculation. Thank you Kite.com
winner = max(candidates_dict, key= candidates_dict.get)

# Print Results
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(votes))
print("----------------------------")
print("Khan: " + str(candidates_dict["Khan Percent of Vote"]) + "% " + "(" + str(candidates_dict["Khan"]) +" votes)")
print("Correy: " + str(candidates_dict["Correy Percent of Vote"]) + "% " + "(" + str(candidates_dict["Correy"]) +" votes)")
print("Li: " + str(candidates_dict["Li Percent of Vote"]) + "% " + "(" + str(candidates_dict["Li"]) +" votes)")
print("O'Tooley: " + str(candidates_dict["O'Tooley Percent of Vote"]) + "% " + "(" + str(candidates_dict["O'Tooley"]) +" votes)")
print("-----------------------------")
print("Winner: " + str(winner))

# Export Results as Text file
with open('pypollresults.txt', 'w') as text:
    text.write(" Election Results"+ "\n")
    text.write("------------------------\n")
    text.write(" Total Votes: " + str(votes) + "\n")
    text.write("------------------------\n") 
    text.write("Khan: " + str(candidates_dict["Khan Percent of Vote"]) + "% " + "(" + str(candidates_dict["Khan"]) +" votes)"  + "\n")
    text.write("Correy: " + str(candidates_dict["Correy Percent of Vote"]) + "% " + "(" + str(candidates_dict["Correy"]) +" votes)"  + "\n")
    text.write("Li: " + str(candidates_dict["Li Percent of Vote"]) + "% " + "(" + str(candidates_dict["Li"]) +" votes)"  + "\n")
    text.write("O'Tooley: " + str(candidates_dict["O'Tooley Percent of Vote"]) + "% " + "(" + str(candidates_dict["O'Tooley"]) +" votes)"  + "\n")
    text.write("------------------------\n")
    text.write("Winner: " + str(winner)+ "\n")




