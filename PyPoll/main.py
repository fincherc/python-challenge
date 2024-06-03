import os
import csv

csvpath = os.path.join('', 'Resources', 'election_data.csv')
output_path = os.path.join("..", "analysis", "analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #counter to hold the number of votes
    counter = 0

    #Dictionary to hold the votes
    candidate = {
        "Charles Casper Stockham" : 0,
        "Diana DeGette" : 0,
        "Raymon Anthony Doane" : 0
    }

    for row in csvreader:
        counter = counter + 1

        if (row[2] in candidate):
            candidate[row[2]] = candidate[row[2]] + 1
    
    winner_name = ""
    winner_votes = 0

    for key in candidate:
        if(candidate[key] > winner_votes):
            winner_votes = candidate[key]
            winner_name = key

#Election Results:

print("Election Results")
print("------------------------------")
print(f"Total Votes: {counter}")
print("------------------------------")

for key in candidate:
    print(f"{key}: {round((candidate[key]/counter) * 100, 3)}% ({candidate[key]})")

print("------------------------------")
print(f"Winner: {winner_name}")

#Write to .txt file:
txtName = os.path.join("", "analysis", "analysis.txt")
txtwriter = open(txtName, "w")
txtwriter.write("Election Results\n")
txtwriter.write("------------------------------\n")
txtwriter.write(f"Total Votes: {counter}\n")

for key in candidate:
    txtwriter.write(f"{key}: {round((candidate[key]/counter) * 100, 3)}% ({candidate[key]})\n")

txtwriter.write("------------------------------\n")
txtwriter.write(f"Winner: {winner_name}\n")
txtwriter.close()

#Remaining focus: Write to .txt file
#Source to "check if key exists": https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
# write file: https://www.w3schools.com/python/python_file_write.asp
# string file write new line: https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time