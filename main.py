import os
import csv
#import the csv file
budgetfilepath = os.path.join('budget_data.csv')

#read the csv file. 
with open(budgetfilepath) as budget_info:


    budget_reader = csv.reader(budget_info)

    budget_header = next(budget_reader)
    budget =[]
    date =[]
    budget_change =[]

    for row in budget_reader:
            budget.append(float(row[1]))
            date.append(row[0])
    for i in range(1, len(budget)):
                budget_change.append(budget[i] - budget[i-1])
    average_budget_change = sum(budget_change)/len(budget_change)


max_budget_change = max(budget_change)
min_budget_change = min(budget_change)

max_budget_change_date = str(date[budget_change.index(max(budget_change))])
min_budget_change_date = str(date[budget_change.index(min(budget_change))])

print("Financial Analysis")
print ("-----------------")
print("Total Months:", len(date))
print ("Total Budget Revenue:", sum(budget))
print("Average Revenue Change: $", round(average_budget_change))
print("Greatest Increase in Budget:  "+ max_budget_change_date + "  $" + str(max_budget_change))
print("Greatest Decrease in Budget:  "+ min_budget_change_date + "  $" + str(min_budget_change))

