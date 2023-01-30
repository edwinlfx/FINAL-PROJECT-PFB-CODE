#import Path from pathliub and csv module
from pathlib import Path
import csv

#create a function called overhead_function
#define an overhead function because function will be used in main.py
def overhead_function():
    #create a file path to the csv file
    fp =Path.cwd()/"csv_reports"/"overheads-day-90.csv"
    #read csv file using with syntax and .open() to apphend overhead category and percentage
    #set mode to "r" in order to read the csv file
    with fp.open(mode="r", encoding="UTF-8", newline ="") as file:
        reader = csv.reader(file)
        #skip header
        next(reader)
        #create overheads variable as an empty list to store the category and percentage in the list
        overheads = []
        #use for loop to apphend overhead category and percentage into the overhead empty list
        for column in reader:
            #column[0] is the overhead category and column[1] is the corresponding percentage of that overhead's category
            overheads.append([column[0], column[1]])
    
    #create "highest_overhead" variable as a list variable with an empty string and 0 in it
    highest_overhead = ["", 0]
    for item in overheads:
        if float(item[1]) > float(highest_overhead[1]):
            highest_overhead = item

    fp=Path.cwd()/"summary_report.txt"
    with fp.open(mode = "w", encoding = "UTF-8") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest_overhead[0].upper()}: {highest_overhead[1]}%\n")
