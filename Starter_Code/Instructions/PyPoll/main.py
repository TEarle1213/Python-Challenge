#import dependencies
import os
import csv
#find file
file=os.path.join("resources/election_data.csv")
#set up variables
candidates= []
candidate_name=[]
vote_per_candidate=[]
percent_per_candidate=[]
counter=0
#open file
with open(file, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
     #skip header
    csv_header=next(csvreader)
    #loop
    for row in csvreader:
        counter = counter+1
        candidates.append(row[2])
    for i in set(candidates):
        candidate_name.append(i)
        vote=candidates.count(i)
        vote_per_candidate.append(vote)
        percentage=round((vote/counter)*100,2)
        percent_per_candidate.append(percentage)    
total_votes=sum(vote_per_candidate)
highest_percent=percent_per_candidate.index(max(percent_per_candidate))
winner=candidate_name[highest_percent]    
    #create text block
text=(
    "Election Results" +'\n'
    "----------------------" +'\n'
    f'Total Votes: {total_votes}' + "\n"
    "----------------------" +'\n' 
    f'{candidate_name[0]} : {percent_per_candidate[0]}% ({vote_per_candidate[0]})' + "\n"
    f'{candidate_name[1]} : {percent_per_candidate[1]}% ({vote_per_candidate[1]})' + "\n"
    f'{candidate_name[2]} : {percent_per_candidate[2]}% ({vote_per_candidate[2]})' + "\n"
    "----------------------" +'\n'
    f'Winner: {winner}'+ "\n"
    "----------------------" +'\n') 
#print to terminal
print(text)
#create text file and write to it
textfile=os.path.join("Analysis/electext.txt")
with open(textfile, 'w') as electext:
   electext.write(text)