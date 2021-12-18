import enum
import os
import glob
import csv
from xlsxwriter.workbook import Workbook

workbook = Workbook('processed_data.xlsx')

for file in glob.glob(os.path.join('data', '*.csv')):
    worksheet = workbook.add_worksheet(file[5:-4])
    with open(file, 'rt') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)

workbook.close()
