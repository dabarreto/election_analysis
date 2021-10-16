# ELECTION ANALYSIS
# ----------------------------------------------------------
# The Election Audit analysis for The Colorado Board of Elections include the following activities:
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

# 1: Create a county list and county votes dictionary.


# Winning Candidate and Winning Count Tracker
# Declare a variable that hols an empty value for the winning candidate
winning_candidate = ""

# Declare a variable for the "winning count" equal to zero.
winning_count = 0

# Declare a variable for the "winning percentage" equal to zero.
winning_percentage = 0

# 2: Track the largest county and county voter turnout.

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

        # 3: Extract the county name from each row.

        # If the candidate does not match any existing candidate add it to the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Set each candidate vote to zero to track their vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.


        # 5: Add a vote to that county's vote count.


# Save the results to a text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Resutls\n"
        f"---------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name, vote count and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write (candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        # If the vote count is greater than the winning_count and the percentage is greater than the winning_percentage
        # Set the winning_count equal to the votes and set the winning_percentage equal to the vote_percentage
        # Set the winning_count equal to the variable, candidate_name, in the forr loop

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count and percentage 
    winning_candidate_summary = (
        f"---------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

