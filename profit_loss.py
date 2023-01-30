#import Path from pathlib and csv module 
from pathlib import Path
import csv
#define a profitloss_function() because function will be used in main.py
def profitloss_function():
    #create a file path to the csv file 
    fp = Path.cwd()/"IGP CSV"/"profit-and-loss-usd.csv"
    #read csv file using with syntax and .open() to append day number and deficit
    #set mode to "r" in order to read csv file
