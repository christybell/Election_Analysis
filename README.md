# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.52.1, Git Bash 2.29.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Challenge Overview
The election commission requested some additional data to complete the election audit:

1. Calculate the voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total vote count.
3. Determine the county with the largest turnout.

## Challenge Results

To calculate the voter turnout and percentage of votes by county, I sequentially added code to:

  - Rows 21-22 to initialize a list called `county_list`to hold the names of the counties and initialize a dictionary called `county_votes` to hold the county as the key and votes cast for each county as the values.
  
  - Rows 30-31 to initialize an empty string called `largest_county` to hold the county name for the county with the largest turnout and initialize a variable called `largest_turnout` to hold the number of votes of the county that had the largest turnout.
  
  - While inside the `for` loop beginning on Row 41, I added a script to Row 50 to get the county name from each row.
  
  - Rows 67-73, I added a decision statement to check if the `county_name` does not match any existing county already in the list. If true, I added the `county_name` to the `county_list`. Finally, I wrote a script to initialize the vote count to 0 and track the number of `county_votes`.
  
  - Row 76, I added a script to add votes to the `county_votes` while looping through all the rows.
  
  - Rows 94-98, I wrote a `for` loop to get the county from the `county_votes` dictionary. Next, I initialized the variable `county_vote_count ` to hold the county's votes. Then, I wrote a script to calculate the county's percentage of votes using variable `county_vote_percentage`.
  
  - Row 99, I intialized a string called `county_results` to capture the current county, its percentage of the total votes and its total voter turnout. On Row 102, I wrote a print statment to print `county_results` to the command line.
  
  - Rows 106-108, I wrote a decision statement to determine the county with the largest turnout, and in Rows 111-155 I printed the results to the command line.

After I added my code determining the additional requests for data, I ran my code in Git Bash and confirmed that my output matched the image shown in the challenge assignment, as my screenshot shows below:

<img src="images/Command Line Output.PNG">

I was also instructed to save the additional election results to a text file on Rows 104 and 118. I confirmed that the output was written to the text file correctly, as my screenshot shows below:

<img src="images/Text File Output.PNG">

## Challenge Summary
In summary, the additional analysis shows that:
- Denver County had the largest turnout of voters in the election.
- The county results were:
  - Jefferson County had 38,855 votes, representing 10.5% of the total vote count.
  - Denver County had 306,055 votes, representing 82.8% of the total vote count.
  - Arapahoe County had 24,801 votes, representing 6.7% of the total vote count.
