import xlrd
def du_qu():
        a=[]
        f=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\pycharm-dome\web自动化\data\zm.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            a.append(sheet.row_values(i))
        print(a)
        return a
if __name__=='__main__':
    du_qu()
