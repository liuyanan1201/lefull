import xlrd
from config import config
#打开一个excel 并获取指定的工作表
def get_sheet(file,name):
    excel=xlrd.open_workbook(file)
    sheet=excel.sheet_by_name(name)
    return sheet

#从一个工作表中找到执行用例名的数据
def get_case(sheet,case_name):
    for i in range(1,sheet.nrows):
        if sheet.cell(i,0).value==case_name:
            return sheet.row_values(i)
        return None


if __name__ == "__main__":
    sh=get_sheet(config.data_file, "TestLandLord")
    # print(sh)
    case_data= get_case(sh,"test_1_landlord_new")
    print(case_data)