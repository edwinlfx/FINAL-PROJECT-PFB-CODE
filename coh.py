#import Path from pathlib and csv module
from pathlib import Path
import csv
#define a cash-on-hand (coh) function() which will be used in main.py 
def coh_function():
    #create a file path to the csv file
    fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    #read csv file using with syntax and .open() to append day number and deficit
    #set mode to "r" in order to read the csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        #skip header
        next(reader)
        #create "data" variable as an empty list to store the day number and amount of cash-on-hand of that day itself in the list
        data = []
        #use for loop to append day number and cash-on-hand of that day itself into the data empty list 
        #column[0] is the day number and column[1] is the corresponding amount of cash-on-hand of that day itself
        for column in reader:
            data.append([column[0]], [column[1]])
    #create "deficits" variable as an empty list to store deficit amount
    deficits = []
    #create "days" variable as an empty list to store the day numbers
    days = []
    #create "previous_day" list variable with 0 as the day number and 0 as the cash-on-hand amount
    previous_day = [0, 0]
    #use for loop to iterate over the number of data
    for current_day in data:
        #use if statement to find out if the cash-on-hand of the current day is lower than the cash-on-hand of the previous day
        #use float() to convert from string to float when comparing because the net profit would still be a string if not converted 
        if float(current_day[1]) < float(previous_day[1]):
            #if true, create "day_number" variable to store "current_day" number
            day_number = current_day[0]
            #create "difference" variable to calculate the cash deficit
            #use float() to convert strings into floats
            #"difference" is found by taking previous day cash-on-hand minus current day cash-on-hand
            difference = float(previous_day[1]) - float(current_day[1])
            #append "day_number" to "days" list using .append()
            days.append(day_number)
            #append "difference" to "deficits" list using .append()
            deficits.append(difference)
        #once an iteration is completed, the previous day values will be the current day values
        previous_day = current_day
    
    #use if else statement to determine if there is no deficit
    #if length of deficit is 0 (no items in the deficit list),
    #cash-on-hand portion on the summary report will display "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    if len(deficits) == 0:
        #create a file to txt file and name it as "summary_report.txt"
        fp = Path.cwd()/"summary_report.txt"
        #cash-on-hand portion of the summary report will be appended into the txt file using append mode and .write()
        with fp.open(mode = "a", encoding = "UTF-8") as file:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    
    #else, cash-on-hand portion of report will display the day of the cash deficit and the amount of deficit of that day itself
    else:
        #create "report" variable as an empty list to store the cash-on-hand report portion of the summary report
        report = []
        #use for loop to iterate over the range in the length of the deficit list
        for index in range(len(deficits)):
            #use .append() to append an f-string of the cash-on-hand report portion into the report list 
            #use f-string and \n to make the cash-on-hand portion in the summary report neater and so that it follows format in the assignment brief
            report.append(f"[CASH DEFICIT] DAY: {days[index]}, AMOUNT: USD{deficits[index]}\n")
        #create a file to txt file and name it as "summary_report.txt"
        fp = Path.cwd()/"summary_report.txt"
        #cash-on-hand portion of the summary report will be appended into the txt file using append mode and .writelines()
        #.writelines() only works for lists and report is a list
        with fp.open(mode = "a", encoding = "UTF-8") as file:
            file.writelines(report)
