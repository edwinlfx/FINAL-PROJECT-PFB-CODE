#import Path from pathlib and csv module 
from pathlib import Path
import csv
#define a profitloss_function() because function will be used in main.py
def profitloss_function():
    #create a file path to the csv file 
    fp = Path.cwd()/"csv_report"/"profit-and-loss-usd.csv"
    #read csv file using with syntax and .open() to append day number and deficit
    #set mode to "r" in order to read csv file
    with fp.open(mode="r", encoding="UTF-8", newline = "") as file:
        reader = csv.reader(file)
        #skip header
        next(reader)
        #create data variable as an empty list to store the day number and amount of net profit of that day itself in the list
        data = []
        #use for loop to append day number and net profit of that day itselfinto the data empty list
        #column[0] is the day number and column [4] is the corresponding amount of net profit of that day itself
        for column in reader:
            data.append([column[0], column[4]])
            
    #create "deficits" variable as an empty list to store deficit amount        
    deficits = []
    #create "days" variable as an empty list to store the day numbers
    days = []
    #create previous day list variable with 0 as the day number and 0 as the net profit amount
    previous_day = [0,0]
    #use for loop to iterate over the number of data
    for current_day in data:
        #use if statement to find out if the net profit of the current day is lower than the net profit of the previous day
        #use float() to convert from string to float when comparing because the net profit would still be a string if not converted
        if float(current_day[1]) < float(previous_day [1]):
            #if true, create day_number variable to store current_day number
            day_number = current_day[0]
            #create difference varirable to calculate the profit deficit
            #use float () to convert strings to floats
            #difference is found by taking previous day net profit minus current day net profit
            difference = float(previous_day[1]) - float(current_day[1])
            #append day_number to days list using .append ()
            days.append(day_number)
            deficits.append(difference)
        previous_day = current_day
        
    if len(deficits) == 0:
        fp = Path.cwd()/"summary_report.txt"
        with fp.open(mode="a", econding="UTF-8") as file:
            file.write("[NET PROFIT SURPLUS] NET PROFIT  ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    else:
        report =[]
        for index in range(len(deficits)):
            report.append(f"[PROFIT DEFICIT] DAY: {days[index]}, AMOMUNT: USD{deficits[index]}\n")
        fp = Path.cwd()/"summary_report.txt"
        with fp.open(mode="a", encoding="UTF-8") as file:
            file.writelines(report)
   
  
    
            
            
            
