import os
import csv

from pathlib import Path

inputfile = 'budget_data.csv'


csvfile = 'budget_data.csv'

text_path = "Financial_Analysis.txt"
      
outfile = ("Financial_Analysis.txt")

totalmonths = []
profits = []
pc = []


with open(inputfile) as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ',')
     csv_header = next(csvreader)

     for row in csvreader:
          totalmonths.append(row[0])
          profits.append(int(row[1]))

for i in range(len(profits) - 1):
         pc.append(profits[i+1] - profits[i])



total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = (sum(pc) / len(pc))

greatest_increase = ((totalmonths[pc.index(max(pc))+1]))
greatest_decrease = ((totalmonths[pc.index(min(pc))+1]))
g_increase = max(pc)
g_decrease = min(pc)

print("Financial Analysis")
print(f".................................")
print(f'Total Months: {total_months}\n')
print(f'Total Profits: {sum_profits}\n')
print(f'Average Revenue Change: {avg_change}\n')
print(f'Greatest Increase in profits: {greatest_increase} (${g_increase}\n)')
print(f'Greatest Decrease in profits: {greatest_decrease} (${g_decrease}\n)')


with open(outfile, "w") as file:
      
      file.write("Fianacial Analysis")
      file.write("\n")
      file.write("...............................................")
      file.write("\n")
      file.write(f"Total Months: {(total_months)}")
      file.write("\n")
      file.write(f"Total Profits: ${sum_profits}")
      file.write("\n")
      file.write(f"Average Revenue Change: {round(avg_change)}")
      file.write("\n")
      file.write(f"Greatest Increase in profits: {greatest_increase} (${g_increase})")
      file.write("\n")
      file.write(f"Greatest Decrease in profits: {greatest_decrease} (${g_decrease})")


