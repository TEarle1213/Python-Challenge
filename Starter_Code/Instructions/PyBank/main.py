#Import Dependencies
import os 
import csv

#find file
file=os.path.join("resources/budget_data.csv")

#set up lists/variables
monthslist=[]
changes=[]
money=[]
previous =0
#open up file
with open(file, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #skip header
    csv_header=next(csvreader)
    #loop
    for row in csvreader:
        #add months to monthslist
        monthslist.append(row[0])
        #add money to moneylist
        money.append(int(row[1]))
    for i in range(1,len(money)):    
        #calculate change per month and add to list
        changes.append(money[i]-money[i-1])
        #get average
        average = round(sum(changes)/len(changes),2)
        #get best/worst numbers and associated months
        increase = (max(changes))
        decrease = (min(changes))
        best_month = str(monthslist[changes.index(increase)])
        worst_month= str(monthslist[changes.index(decrease)])
#get totals        
months=len(monthslist)
pnl=sum(money)
#create text block
text=(
    "Financial Analysis" +'\n'
    "----------------------" +'\n' 
    f'Total Months: {months}' + "\n"
    f'Total: ${pnl}' +"\n"
    f'Average Change: {average}' + "\n"
    f'Greatest Increase in Profits: {best_month}(${(str(increase))})'+'\n'
    f'Greatest Decrease in Profits: {worst_month} (${(str(decrease))})'+'\n')

#print to terminal
print(text)
#create text file and write to it
textfile=os.path.join("Analysis/fintext.txt")
with open(textfile, 'w') as fintext:
    fintext.write(text)








