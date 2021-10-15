# ELECTION ANALYSIS
# ----------------------------------------------------------
# This analysis include the results of the elections.
# ----------------------------------------------------------
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Import Dependencies
import csv
import os

# Import CSV File
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('election_analysis\Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect to the file.
file_to_save = os.path.join('election_analysis\Analysis', 'election_analysis.txt')

# Variable to count up all the votes
# Initialize a total vote counter
total_votes = 0

# Declare empty list to get Candidate Options
candidate_options = []

# Declare empty dictionary to count votes for each candidate
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Election Analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
    #    print(row)
        # Add to the total vote count
        total_votes +=1

# Print the total votes.
# print(total_votes)

        # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Set each candidate vote to zero to track their vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

# Print the candidate list
# print(candidate_options)

# Print the candidate vote dictionary
# print(candidate_votes)