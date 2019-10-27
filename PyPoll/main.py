import os
import csv



votes  = 0
candidate_raw = []
candidates  = []
tally = {}
results = []

csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, newline ='') as file:
    csvreader = csv.reader(file, delimiter =',')
    csvreader2 = next(csvreader)



    for row in csvreader:
        votes = votes + 1
        candidate_raw.append(row[2])
    

    for cand in candidate_raw:
        if cand not in candidates:
                candidates.append(cand)

    for cand in candidate_raw:
        if cand not in tally:
            tally[cand] = 1
        elif cand in tally:
            tally[cand] += 1

    winner_votes = max(tally.values())

    for x, vote in tally.items():
        if vote == winner_votes:
            winner = x


    percents = {}
    for k in tally:
        percents[k] = (tally[k]/votes)*100
    
    print(
        "Election Results\n-------------------------\nTotal Votes: "+ str(votes)+
        "\n-------------------------")
    for q,v in percents.items():
        o = tally[q]
        results.append(q + ": "+str(round(v,2))+"% " + "("+str(o)+")")
    print(*results, sep = "\n")
    print("-------------------------\nWinner: "+winner+"\n-------------------------")
    f = open("PollAnalysis.txt","w")
    f.write("Election Results\n-------------------------\nTotal Votes: "+ str(votes)+
        "\n-------------------------" + str(results) + "\n" +"-------------------------\nWinner: "+winner+"\n-------------------------")


    
