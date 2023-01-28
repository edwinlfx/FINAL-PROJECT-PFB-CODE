from pathlib import path
import csv
fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    