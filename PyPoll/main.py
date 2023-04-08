import os
import csv

#Create pathway to election_data.csv
csv_path= "C:/Users/13217/Desktop/BootCamp_Coursework/Git_Repositories/python-challenge/PyPoll/Resource/election_data.csv"

#Eventually the new file name will be "PyPoll_Output.txt"
new_file = "C:/Users/13217/Desktop/BootCamp_Coursework/Git_Repositories/python-challenge\PyPoll/Analysis/PyPoll_Output.txt"

#Global Variables
candidate_list = list()
vote_tally = list()
candidate_votes = list()
candidate_percentage = list()

#Opens the csv file and skips header line
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    #Counts the total number of votes
    votes = list(csvreader)
    total_votes = len(votes)

    #Creates a list of all candidates that were voted for. If a new candidate appears, adds to list
    for i in range(0,total_votes):
        candidate = votes[i][2]
        vote_tally.append(candidate)
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    candidate_list_new = len(candidate_list)

    #Calculates the total number of votes per candidate and the percentage of the vote they received
    for j in range(0,candidate_list_new):
        candidate_name = candidate_list[j]
        candidate_votes.append(vote_tally.count(candidate_name))
        vote_percent = candidate_votes[j]/total_votes
        candidate_percentage.append(vote_percent)

    #Calculates the winner based off of the highest number of votes
    candidate_winner = candidate_votes.index(max(candidate_votes))

    #Prints the analysis to the terminal
    print('Election Results')
    print('-------------------------------')
    print('Total Votes: ',  total_votes)
    print('-------------------------------')
    for a in range (0,candidate_list_new):
        print(f'{candidate_list[a]}: {candidate_percentage[a]:.3%} ({candidate_votes[a]:,})')
    print('-------------------------------')
    print('Winner: ', candidate_list[candidate_winner])
    print('-------------------------------')

    #Creates "PyPoll_Output.txt" file and writes what we printed in the terminal
    # \n is equivalent to pressing enter on the keyboard
    # %d is a placeholder for a number while %s is a placeholder for a string
    # [] indicate what values should be placed where
    
    print("Election Results", file=open(new_file, "a"))
    print("----------------------", file=open(new_file, "a"))
    print("Total Votes: %d" % total_votes, file=open(new_file, "a"))
    print("----------------------", file=open(new_file, "a"))
    for a in range(0,candidate_list_new):
        print(f'{candidate_list[a]}: {candidate_percentage[a]:.3%} ({candidate_votes[a]:,})', file = open(new_file, "a"))
    print("----------------------", file=open(new_file, "a"))
    print("Winner: %s" % candidate_list[candidate_winner], file=open(new_file, "a"))
    print("----------------------", file=open(new_file, "a"))