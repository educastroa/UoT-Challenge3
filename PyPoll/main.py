import csv

path = 'resources/election_data.csv'

with open(path, 'r', newline='') as file:

    csv_reader = csv.reader(file)

    csvArray = list(csv_reader)
    
    row_count = len(csvArray)

    totalVotes = len(csvArray) - 1
    
    votes = {}

    votesArray = []

    for i in range(1, row_count):

        votes[csvArray[i][2]] = votes.get(csvArray[i][2], 0) + 1 

    for key, value in votes.items():
        votesArray.append({"candidate": key, "votes": value})

    sorted_data = sorted(votesArray, key=lambda x: x['votes'], reverse=True)

    content = f"Election Results\n\n-------------------------\n\nTotal Votes: {totalVotes}\n\n-------------------------\n\nCharles Casper Stockham: {round((votes['Charles Casper Stockham']/totalVotes)*100,3)}% ({votes['Charles Casper Stockham']})\n\nDiana DeGette: {round((votes['Diana DeGette']/totalVotes)*100,3)}% ({votes['Diana DeGette']})\n\nRaymon Anthony Doane: {round((votes['Raymon Anthony Doane']/totalVotes)*100,3)}% ({votes['Raymon Anthony Doane']})\n\n-------------------------\n\nWinner: {sorted_data[0]['candidate']}\n\n-------------------------"
    
    print(content)

    txt_path = "PyPoll.txt"

    with open(txt_path, "w") as file:
        file.write(content)