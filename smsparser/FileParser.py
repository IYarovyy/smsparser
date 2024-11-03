import csv
import os
from os.path import basename
from os.path import join
from os.path import splitext

import openpyxl
import traceback
import sys

from smsparser.RowParser import RowParser


class FileParser:
    def __init__(self, out_folder, err_folder):
        self.out_folder = out_folder
        self.err_folder = err_folder

    def parse(self, file):
        wb = openpyxl.load_workbook(file, data_only=True)
        for sheet in wb.worksheets:
            csv_file_name = splitext(basename(file))[0] + "_" + sheet.title + ".csv"
            os.makedirs(self.out_folder, exist_ok=True)
            os.makedirs(self.err_folder, exist_ok=True)

            try:
                with open(join(self.out_folder, csv_file_name), "wt") as csv_file:
                    writer = csv.writer(csv_file, delimiter=',')
                    header_row = []
                    for cell in sheet[1]:
                        header_row.append(str(cell.value).strip().lower())
                    # Skip sheet
                    if header_row[0] == "Данных нет":
                        continue
                    header = {k: v for v, k in enumerate(header_row)}

                    for row in sheet.iter_rows(min_row=2):
                        parser = RowParser(header, row)
                        sender = parser.get_sender()
                        recipient = parser.get_recipient()

                        # Skip row
                        if sender is None \
                                or recipient is None \
                                or sender == 'None' \
                                or recipient == 'None':
                            continue

                        writer.writerow([parser.get_time(),
                                         parser.get_sender(),
                                         parser.get_recipient(),
                                         parser.get_text(),
                                         parser.get_lac(),
                                         parser.get_cell(),
                                         parser.get_address()])
            except Exception as inst:
                print(str(file), file=sys.stderr)
                print(traceback.format_exc(), file=sys.stderr)
                # os.rename(file, os.path.join(self.err_folder, basename(file)))
