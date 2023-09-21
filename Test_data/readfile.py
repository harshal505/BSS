import openpyxl


class Read_test_data:
    @staticmethod
    def getData():
        fileName = r"H:\Harshal data\pythonProject\pythonProject2\Test_data\datafile.xlsx"
        book = openpyxl.load_workbook(fileName)
        sheet = book["User"]
        trows = sheet.max_row
        t_columns = sheet.max_column
        final_list = []

        for r in range(2, trows + 1):
            rlist = []
            for c in range(1, t_columns + 1):
                print(r, c)
                rlist.append(sheet.cell(row=r, column=c).value)
            final_list.append(rlist)
        return final_list

b = Read_test_data()
d = b.getData()
print(d)
