from openpyxl import load_workbook

wb = load_workbook('MakingPythonMecro\\study.xlsx',
                   read_only=False,  # 읽기 전용(읽기 전용에 최적화되어 파일을 불러온다)
                   # False면 셀안 공식을 가져오고 True면 공식 적용된 값만을 불러온다.
                   data_only=False,
                   )
sheet1 = wb['Sheet1']  # Sheet1 시트를 가져오기.

sheet1['E2'].value = 'one' #E2의 값을 "one"으로 변경
wb.save(filename='study.xlsx') #파일 study.xlsx로 덮어쓰기.

#프로그램 실행 시에는 엑셀 파일을 꼭 꺼주세요.