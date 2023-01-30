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
        if float(current_day[1]) < float(previous_day[1]):
            day_number = current_day[0]
            difference = float(previous_day[1]) - float(current_day[1])
            days.append(day_number)
            deficits.append(difference)
        previous_day = current_day
    if len(deficits) == 0:
        fp = Path.cwd()/"summary_report.txt"
        with fp.open(mode = "a", encoding = "UTF-8") as file:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    else:
        report = []
        for index in range(len(deficits)):
            report.append(f"[CASH DEFICIT] DAY: {days[index]}, AMOUNT: USD{deficits[index]}\n")
        fp = Path.cwd()/"summary_report.txt"
        with fp.open(mode = "a", encoding = "UTF-8") as file:
            file.writelines(report)
