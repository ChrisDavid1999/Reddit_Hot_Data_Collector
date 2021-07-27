import xlsxwriter


class Writer:
    def __init__(self, file, name):
        self.excelFile = xlsxwriter.Workbook(file)
        self.worksheet = self.excelFile.add_worksheet(name)
        self.row = 0
        self.col = 0

    def close(self):
        self.excelFile.close()

    def write(self, identify, title, score):
        self.worksheet.write(self.row, self.col, identify)
        self.worksheet.write(self.row, self.col + 1, title)
        self.worksheet.write(self.row, self.col + 2, score)
        self.row += 1