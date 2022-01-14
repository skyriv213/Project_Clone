import win32com.client
# Dispatch함수를 통해 인스턴스를 생성했을 때부터 엑셀은 이미 실행상태이다.
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
# # wb로 지정한 workbook을 추가시켜줌
wb1 = excel.Workbooks.Add()
# # worksheet를 추가시켜줌
ws1 = wb1.Worksheets("Sheet1")
# # worksheet의 1.1칸에 값을 지정 및 저장
ws1.cells(1,1).Value="python"
ws1.cells(1,2).Value = "is"
ws1.Range("C1").Value = "good"
ws1.Range("C1").Interior.ColorIndex = 10
wb1.SaveAs('c:\\Users\\skyriv\\Desktop\\Project_Clone\\Trading_algorithm\\Ex_Com\\test.xlsx')
# excel.Quit()
wb = excel.Workbooks.Open('c:\\Users\\skyriv\\Desktop\\Project_Clone\\Trading_algorithm\\Ex_Com\\test.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()