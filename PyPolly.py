#Instructions:
    #Total number of votes cast
    #A complete list of candidates who received votes
    #Total number of votes each candidate received
    #Percentage of votes each candidate won
    #The winner of the election based on popular vote

#Pseudocode:
    #1. Count the total votes casted
    #2. Generate a candidate list with votes
    #3. Generate the number of votes for each candidate
    #4. Calculate the percentage of votes for each candidate
    #5. Determine the candidate with the highest number of votes received as winner
    #Total number of votes cast
    #A complete list of candidates who received votes
    #Total number of votes each candidate received
    #Percentage of votes each candidate won
    #The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)


