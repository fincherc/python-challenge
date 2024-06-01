#Your task is to create a Python script that analyzes the records to calculate each of the following values:

    # The total number of months included in the dataset

    # The net total amount of "Profit/Losses" over the entire period

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in profits (date and amount) over the entire period

#Open the file
#Read in the header
#Proceed with a loop to get the counter for the months
#Net the total amount for profit/losses over the period

import os
import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #counter to hold the number of months
    counter = 0
    #total_net to hold profit/losses
    total_net = 0
    #average_change to hold profit/losses
    average_change = 0

    #Greatest Increase/Decrease in Profits
    greatest_increase = 0
    greatest_increase_date = 0
    greatest_decrease = 0
    greatest_decrease_date = 0

    #Hold Previous entry to get difference to add
    previous_entry = 0

    for row in csvreader:
        total_net = total_net + row[1]

        if(counter == 0):
            previous_entry = row[1]
        else:
            change = row[1] - previous_entry

            #determine if the change is actually needing to be adjusted to either variable
            if(change > 0):
                if(greatest_increase < change):
                    greatest_increase = change
                    greatest_increase_date = row[0]
            else:
                if(greatest_decrease > change):
                    greatest_decrease = change
                    greatest_decrease_date = row[0]

            #average_change and prep work to proceed
            average_change = average_change + (change)
            previous_entry = row[1]
        
        counter = counter + 1

    average_change = average_change / (counter - 1)


#Final Results:

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: ${counter}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")    