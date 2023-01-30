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
            difference = float(previous_day[1]) - float(currrent_day[1])
            
   
  
    
            
            
            
