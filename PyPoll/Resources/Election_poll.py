import os
import csv

from pathlib import Path

election_data = "election_data.csv"

text_path = "Election_poll.txt"
outfile = os.path.join('elections', text_path)

Charles_Casper_Stockham = "Charles Casper Stockham"
Diana_DeGette = "Diane DeGette"
Raymon_Anthony_Doane = "Raymon Anthony Doane"


total_votes = 0
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

with open(election_data, newline="", encoding="utf-8") as datafile:
    csvreader = csv.reader(datafile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:

        ballot = row

        total_votes +=1

        if row[2] == "Charles Casper Stockham":
                Charles_Casper_Stockham_votes +=1

        elif row[2] == "Diana DeGette":
                Diana_DeGette_votes +=1

        elif row[2] == "Raymon Anthony Doane":
                Raymon_Anthony_Doane_votes +=1
            

candidates = ["Charles_Casper_Stockham", "Diana_DeGette", "Raymon_Anthony_Doane"]       
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes, Raymon_Anthony_Doane_votes]


dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)


Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_votes) * 100
Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_votes) * 100


print(f"Election Results")
print(f"....................................................")
print(f"Total Votes: {total_votes}")
print(f"....................................................")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diane DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"....................................................")
print(f"winner: {key}")
print(f".....................................................")


Output_file = Path("Election_Results.txt")

with open(Output_file, "w") as file:
     file.write(f"Election Results")
     file.write("\n")
     file.write(f"...................................................")
     file.write("\n")
     file.write(f" Total Votes: {total_votes}")
     file.write("\n")
     file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
     file.write("\n")
     file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
     file.write("\n")
     file.write(f"Raymon Anthony Doane: { Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
     file.write("\n")
     file.write(f"......................................................")
     file.write("\n")
     file.write(f"Winner: {key}")
     file.write("\n")
     file.write(f"...........................................................")