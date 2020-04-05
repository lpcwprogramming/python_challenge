# Python Challenge - PyBank

# Introduction
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
# The dataset is composed of two columns: `Date` and `Profit/Losses`.

###Create a Python script that analyzes and calculates the following###
# Total number of months included in the dataset
# Net total amount of 'Profit/Losses' over the entire period
# Average of the changes in 'Profit/Losses' over the entire period
# Greatest increase in profits (date and amount) over the entire period
# Greatest decrease in losses (date and amount) over the entire period

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Open and read csv file

import os
import csv
import operator

csv_location = '/Users/Leishla/Desktop/Bootcamp/nu-chi-data-pt-03-2020-u-c/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'

with open(csv_location) as csvfile:

    # Specify delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read each row of data
    for row in csvreader:

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
        #Total number of months included in the dataset#

        months = [row[0] for row in csvreader]

        total_months = (len(months))

        csvfile.seek(0)
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Net total amount of 'Profit/Losses' over the entire period#

        csv_header = next(csvreader)

        profit_losses = []

        profit_losses = [(int(row[1])) for row in csvreader]

        total_profit = sum(profit_losses)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Average of the changes in 'Profit/Losses' over the entire period#

    diff_list = [profit_losses[i + 1] - profit_losses[i]
        for i in range(len(profit_losses)-1)]
    
    total_diff = sum(diff_list)

    average_change = total_diff/(total_months-1)

    average_round = str(round(average_change, 2))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Greatest increase in profits (date and amount) over the entire period#

    missing = profit_losses[0]

    [diff_list.insert(0, missing)]
    
    tuples = zip(months, diff_list)

    tup_list = list(tuples)

    profit_increase = max(tup_list, key=operator.itemgetter(1))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Greatest decrease in losses (date and amount) over the entire period#

    profit_decrease = min(tup_list, key=operator.itemgetter(1))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Final Analysis terminal output#

    print("Final Analysis")
    print("-----------------------------")
    print(f"Total months: {total_months}")
    print(f"Total profits: ${total_profit}")
    print(f"Average change: ${average_round}")
    print(f"Greatest increase in profits: {profit_increase}")
    print(f"Greatest decrease in profits: {profit_decrease}")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Write final analysis to text file#

#Open file in write mode#
file_location = '/Users/Leishla/Desktop/Bootcamp/Homework working folder/python_challenge/PyBank/pybank_output.txt'

with open(file_location, 'w') as textfile:

#Write to file#
    
    textfile.write("Final Analysis")
    textfile.write("-----------------------------")
    textfile.write("Total months: {0}".format(total_months))
    textfile.write("Total profits: {0}".format(total_profit))
    textfile.write("Average change: ${0}".format(average_round))
    textfile.write("Greatest increase in profits: {0}".format(profit_increase))
    textfile.write("Greatest decrease in profits: {0}".format(profit_decrease))
