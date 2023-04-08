import os
import csv

#Create pathway to budget_data.csv
csv_path = "C:/Users/13217/Desktop/BootCamp_Coursework/Git_Repositories/python-challenge/PyBank/Resource/budget_data.csv"

#Eventually the new file name will be "budget_output.txt"

new_file = "C:/Users/13217/Desktop/BootCamp_Coursework/Git_Repositories/python-challenge/PyBank/Analysis/budget_output.txt"

#Global Variables
month_total = 0
PL_total = 0
PL = []
PL_change = 0
PL_previous = 0
PL_change_list = []
PL_month_change = []
PL_greatest_increase = ["", 0]
PL_greatest_decrease = ["", 9999999]
PL_change_average = 0

#Opens the csv file
with open(csv_path) as csvfile:
    csvreader = csv.DictReader(csvfile)
#Begins looping code
    for row in csvreader:
        #For each line in "Date" column and starting at 0, add 1 to the previous count
        month_total += 1
        #starting at 0, for each row, add previous PL_total value to this row's PL_total value
        PL_total = PL_total +int(row["Profit/Losses"])
        #Obtain variable values needed to calculate PL_change_average per month
        #Each PL_change value equals the current PL value minus the previous PL value
        PL_change = int(row["Profit/Losses"]) - PL_previous
        PL_previous = int(row["Profit/Losses"])
        #PL_change_list takes all PL change values and consolidates it
        PL_change_list = PL_change_list + [PL_change]
        #PL_month_change does the same but with the dates
        PL_month_change = [PL_month_change] + [row["Date"]]

        #Conditional if statements to find the greatest increase and greatest decrease
        #If PL_change is greater than the greatest current increase then add the date and value
        if PL_change>PL_greatest_increase[1]:
            PL_greatest_increase[0] = row["Date"]
            PL_greatest_increase[1] = PL_change
        #If PL_change is greater than the greatest current decrease then add the date and value
        if PL_change<PL_greatest_decrease[1]:
            PL_greatest_decrease[0] = row["Date"]
            PL_greatest_decrease[1] = PL_change
    #Calculates the PL average change per month over the entire time period
    #Sum adds up all the values in the PL_change_list
    #len adds up the number of values in the PL_change_list
    PL_change_average = PL_change/month_total

    #Prints the analysis to the terminal
    print("Financial Analysis\n")
    print("----------------------\n")
    print("Total Months: %d\n" % month_total)
    print("Total: $%d\n" % PL_total)
    print("Average Change: $%d\n" % PL_change_average)
    print("Greatest Increase in Profits: %s ($%s)\n" % (PL_greatest_increase[0], PL_greatest_increase[1]))
    print("Greatest Decrease in Profits: %s ($%s)\n" % (PL_greatest_decrease[0], PL_greatest_decrease[1]))

#Creating a new file named "budget_output.txt" and writing the outcomes in it
# \n is equivalent to pressing enter on the keyboard
# %d is a placeholder for a number while %s is a placeholder for a string
# [] indicate what values should be placed where
with open(new_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------\n")
    file.write("Total Months: %d\n" % month_total)
    file.write("Total: $%d\n" % PL_total)
    file.write("Average Change: $%d\n" % PL_change_average)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (PL_greatest_increase[0], PL_greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (PL_greatest_decrease[0], PL_greatest_decrease[1]))