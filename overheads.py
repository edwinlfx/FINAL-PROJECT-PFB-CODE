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
        overheads = []
        for column in reader:
            overheads.append([column[0], column[1]])

    highest_overhead = ["", 0]
    for item in overheads:
        if float(item[1]) > float(highest_overhead[1]):
            highest_overhead = item

    fp=Path.cwd()/"summary_report.txt"
    with fp.open(mode = "w", encoding = "UTF-8") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest_overhead[0].upper()}: {highest_overhead[1]}%\n")
