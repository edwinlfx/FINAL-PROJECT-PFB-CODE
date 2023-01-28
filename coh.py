from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    data = []
    for column in reader:
        data.append([column[0]], [column[1]])
deficits = []
days = []
previous_day = [0, 0]
for current_day in data:
    if float(current_day[1]) < float(previous_day[1]):
        day_number = current_day[0]
        difference = float(previous_day[1]) - float(current_day[1])
        days.append(day_number)
        deficits.append(difference)