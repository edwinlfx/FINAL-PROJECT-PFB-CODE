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
    