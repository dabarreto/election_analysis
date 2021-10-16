# Election Analysis

## Project Overview

The purpose of this analysis is to determine the results of a recent local congressional election and submit the results to The Colorado Board of Elections.

The summary results include:
- The total local number of votes cast.
- The total votes by County.
- The County with the highest turnout.
- The list of candidates who received votes.
- The total number of votes each candidate received.
- The percentage of votes each candidate won.
- The winner of the election based on popular vote.

### Resources

- Data source: [election_results.csv](https://github.com/dabarreto/election_analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.38.1
------------------------------------------

## Election-Audit Results:

The Python code [PyPoll.py](https://github.com/dabarreto/election_analysis/blob/main/PyPoll.py) includes the step by step to analyze the elections by county.

The election outcomes are in [election_analysis.tx](https://github.com/dabarreto/election_analysis/blob/main/Analysis/election_analysis.txt) and include a breakdown by county and candidate:
![Vote_Results](https://github.com/dabarreto/election_analysis/blob/main/Analysis/results_image.PNG)


## Election-Audit Summary:
The Python code [PyPoll.py](https://github.com/dabarreto/election_analysis/blob/main/PyPoll.py) can be used in other elections:
- By keeping the same structure in the input file (Ballot ID,County,Candidate).
- The code can be adapted to only get results by candidate if needed.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Important: Keep in mind that you have to have the same folder structure. I had problems with my Anaconda and Python installation and the paths in my system moved, so make sure to remove/addapt the relative paths to your working directory.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Created by: Ana Daniela Barreto Rodriguez.\
Data Analytics Bootcamp - Tecnologico de Monterrey.\
© 2020 - 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.\
October 16, 2021.
