import csv
import os

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base don popular vote.

# Assign a variable fo the file to load and the path.
file_to_load = 'Resources/election_results.csv'

votecounter = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    columnnames = next(election_data)

    # To do: perform analysis.
    for vote in election_data:
        votecounter = votecounter + 1
       
    #print(election_data)

# Close the file.
election_data.close()

print(votecounter)


# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#     print(election_data)
