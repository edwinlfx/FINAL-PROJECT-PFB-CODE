#import Path from pathliub and csv module
from pathlib import Path
import csv
def overhead_function():
fp =Path.cwd()/"csv_reports"/"overheads-day-90.csv"
with fp.open(mode="r", encoding="UTF-8", newline ="") as file:
    reader = csv.reader(file)
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
    file.write(f"[HIGHEST OVERHEAS] {highest_overhead[0].upper()}: {highest_overhead[1]}%\n")