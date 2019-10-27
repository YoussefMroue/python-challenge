import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath, newline ='') as file:

    csvreader = csv.reader(file, delimiter =',')
    csvreader2 = next(csvreader)

    months = 0
    total = 0
    difference = 0
    profit_list = []
    month_list = []
    profit_list_differences = []
    

    for row in csvreader:
        months = months + 1
        profit = int(row[1])
        total = total + profit
        month_list.append(row[0])
        profit_list.append(row[1])

        
    

    for i in range(len(profit_list)-1):
        a = profit_list[i+1]
        b = int(profit_list[i])
        difference = int(profit_list[i+1]) - int(profit_list[i])
        profit_list_differences.append(difference)

    maxindex = profit_list_differences.index((max(profit_list_differences)))+1
    minindex = profit_list_differences.index((min(profit_list_differences)))+1

    average_difference = (sum(profit_list_differences)/len(profit_list_differences))

    print("Financial Analysis \n----------------------------")
    print("Total Months: " + str(months))
    print("Total: " + str(total))
    print("Average Change: " + str(round(average_difference,2)))
    print("Greatest Increase in Profits: " + month_list[maxindex] +" " + str(max(profit_list_differences)))
    print("Greatest Decrease in Profits: " + month_list[minindex] +" " + str(min(profit_list_differences)))



    f = open("FinancialAnalysis.txt","w")
    f.write(
        "Financial Analysis \n----------------------------\nTotal Months: " + str(months) +
         "\nTotal: " + str(total)+ "\nAverage Change: " + str(round(average_difference,2))
         +"\nGreatest Increase in Profits: " + month_list[maxindex] +" " + str(max(profit_list_differences))
         +"\nGreatest Decrease in Profits: " + month_list[minindex] +" " + str(min(profit_list_differences)))
    f.close()