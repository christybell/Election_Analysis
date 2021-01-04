# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        # total_votes +=1
        total_votes = total_votes + 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the candidate list.
            candidate_options.append(candidate_name)

# Print the candidate list
print(candidate_options)

# # Print the total votes.
# print(total_votes)

    # for total_votes in election_data:
    #     total_votes = total_votes + 1

    #     print(total_votes)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    # for vote in election_data:
    #     votecounter = votecounter + 1
       
    #print(election_data)

# # Close the file.
# election_data.close()

# print(votecounter)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base don popular vote.

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #Write three counties to the file.
#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
