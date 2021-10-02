# Your task is to create a Python script that analyzes the records to calculate:
# Total number of months in data set
# The net total amount of Profit/Losses over entire period
# Calculate the changes in Profit/Losses and find avg of changes
# The greatest increase in profits(date and amount) over period
# The greatest decrease in profits(d and a) over period

#Steps: Start with calculating total number of months and net profit loss.

# Modules
import os
import csv

# Set Lists and Define Variables
# pl short for profit/loss
date = []
monthly_pl_changes = []
count_date = 0
net_total_pl = 0
prior_month_pl = 0
current_month_pl = 0
profit_loss_change = 0



# Set path for file
csvpath = r'C:\Users\cchic\DataViz\budget_data.csv'




# Open the CSV
with open(csvpath) as csvfile:




    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvfile)


    # Loop through dataset
    #next(csvreader)
    for row in csvreader:
        # Count the number of months:
        count_date += 1

        #Calculate Net Total Profit/Loss
        current_month_pl = int(row[1])
        net_total_pl += current_month_pl

        if(count_date == 1):
            # Set value of current to prior for computations
            prior_month_pl = current_month_pl
            #break 
        
        else:

            # PL Change calculation
            profit_loss_change = current_month_pl - prior_month_pl

            # append to date list
            date.append(row[0])

            # append pl to monthly pl changes list
            monthly_pl_changes.append(profit_loss_change)

            # set for next loop
            prior_month_pl = current_month_pl

    # sum profits/losses
    sum_pl_changes = sum(monthly_pl_changes)

    # average monthly profits/lossess
    average_pl = sum(monthly_pl_changes)/ len(monthly_pl_changes)

    # greatest increase/decrease calculations
    greatest_increase = max(monthly_pl_changes)
    greatest_decrease = min(monthly_pl_changes)

    greatest_increase_date_index = monthly_pl_changes.index(greatest_increase)
    greatest_decrease_date_index = monthly_pl_changes.index(greatest_decrease)

    top_profit_date = date[greatest_increase_date_index]
    worst_loss_date = date[greatest_decrease_date_index]

print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(count_date))
print("Total PL: " + "$" + str(net_total_pl))
print("Average Change: " + "$" + str(int(average_pl)))
print("Greatest Increase in Profits: " + str(top_profit_date)+ " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_loss_date)+ " ($" + str(greatest_decrease) + ")")

# Export results to text file
with open('pybankresults.txt', 'w') as text:
    text.write(" Financial Analysis"+ "\n")
    text.write("------------------------\n")
    text.write(" Total Months: " + str(count_date) + "\n")
    text.write(" Total PL:" + "$" + str(net_total_pl) + "\n")
    text.write(" Average Change: " + "$" + str(int(average_pl)) + "\n")
    text.write(" Greatest Increase in Profits: " + str(top_profit_date)+ " ($" + str(greatest_increase) + ")\n")
    text.write(" Greatest Decrease in Profits: " + str(worst_loss_date)+ " ($" + str(greatest_decrease) + ")\n")
    