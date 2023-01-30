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
        
        next(reader)
        
        data = []
        
        
        for column in reader:
            data.append([column[0], column[4]])
    deficits = []
    days = []
    previous_day = [0,0]
    for current_day in data:
        if float(current_day[1]) < float(previous_day [1]):
            day_number = current_day[0]
            difference = float(previous_day[1]) - float(current_day[1])
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
        with fp.open(mde="a", encdoing="UTF-8") as file:
   
  
    
            
            
            
