import os
import csv
#import the csv file
budgetfilepath = os.path.join('budget_data.csv')

#open the csv file
with open(budgetfilepath) as budget_info:

#read the csv file
    budget_reader = csv.reader(budget_info)
#skip the header
    budget_header = next(budget_reader)

    #declare budget, date and budget change 
    budget =[]
    date =[]
    budget_change =[]
#for the total rows of data in the file, count the columns 1 and columns 0
    for row in budget_reader:
            budget.append(float(row[1]))
            date.append(row[0])
    #loop to find the total difference of all the revenue column and calculating the average change
    for i in range(1, len(budget)):
                budget_change.append(budget[i] - budget[i-1])
    average_budget_change = sum(budget_change)/len(budget_change)

#minimum and maximum revenue changes.
max_budget_change = max(budget_change)
min_budget_change = min(budget_change)

#converting the budget changes in the year into date format
max_budget_change_date = str(date[budget_change.index(max(budget_change))])
min_budget_change_date = str(date[budget_change.index(min(budget_change))])

print("Financial Analysis")
print ("-----------------")
print("Total Months:", len(date))
print ("Total Budget Revenue:", sum(budget))
print("Average Revenue Change: $", round(average_budget_change))
print("Greatest Increase in Budget:  "+ max_budget_change_date + "  $" + str(max_budget_change))
print("Greatest Decrease in Budget:  "+ min_budget_change_date + "  $" + str(min_budget_change))

#saving teh analysis to an output text file, naming the file.
output_file =os.path.join('financial_analysis.txt')
#write the analysis to output_file.
with open(output_file, "w") as txt_file:

    financial_analysis =(f"Financial Analysis"
        f"-----------------------" 
        f"Total Months:", len(date), " "
        f"Total Budget Revenue:", sum(budget), " "
        f"Average Revenue Change:  $", round(average_budget_change) , " "
        f"Greatest Increase in Budget:  "+ max_budget_change_date + "  $"+ str(max_budget_change) , " "
        f"Greatest Decrease in Budget:  "+ min_budget_change_date + "  $" + str(min_budget_change), " ")

    print(financial_analysis)

    txt_file.write(str(financial_analysis))

