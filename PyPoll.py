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

# Create a county list and county votes dictionary.
# Empty list to hold the names of the counties
county_list = []
# Empty dictionary to hold the county as the key and the votes cast for each county as the values
county_votes = {}

# Winning Candidate and Winning Count Tracker
# Declare a variable that hols an empty value for the winning candidate
winning_candidate = ""
# Declare a variable for the "winning count" equal to zero.
winning_count = 0
# Declare a variable for the "winning percentage" equal to zero.
winning_percentage = 0

# Track the largest county and county voter turnout.
# Empty string to hold the county name with the largest turnout
county_turnout = ""
# Initialize a variable (equal to zero) to hold the number of votes of the county that had the largest turnout
county_count = 0


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

        # While reading the election results from each row inside the for loop, extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Set each candidate vote to zero to track their vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
            # Add the existing county to the list of counties.
            county_list.append(county_name)
            # Set each county vote to zero to track their vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

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

    # Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # Retrieve the county vote count.
        votes_county = county_votes.get(county_name)
        # Calculate the percentage of votes for the county.
        county_percentage = float(votes_county) / float(total_votes) * 100
        # Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({votes_county:,})\n")
        print(county_results)
        # Save the county votes to a text file.
        txt_file.write(county_results)
         
        # Write an if statement to determine the winning county and get its vote count.
        if votes_county > county_count:
            county_count = votes_county
            county_turnout = county_name

    # Print the county with the largest turnout to the terminal.
    county_turnout_summary = (
        f"---------------------------------------------\n"
        f"Largest County Turnout: {county_turnout}\n"
        f"---------------------------------------------\n")
    print(county_turnout_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(county_turnout_summary)

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

