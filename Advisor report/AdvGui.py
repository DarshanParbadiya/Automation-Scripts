
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QPushButton, QFileDialog
from PyQt6 import uic#importing the ui file

class MainWindow(QMainWindow):
    zip_file = None
    sales_file = None
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advisor Report 9AM")
        uic.loadUi('Advgui.ui',self)
        self.zipButton.clicked.connect(self.clickHandlerZip)
        self.salesButton.clicked.connect(self.clickHandlerSales)
        self.resultButton.clicked.connect(self.clickHandlerResult)
    def dothis():
        pass

    def makeReport(self,zip_file,sales,save_location):
        sales_sheet = sales
        import pandas as pd
        from zipfile import ZipFile 
        # file_name  = input("please enter the Zip file name with extension:")
        file_name = zip_file
        ivra_file =  None
        try:
            with ZipFile(file_name, "r") as zip:
                zip.extractall(path="", pwd="ptlwk001".encode("utf-8"))
        except Exception as e:
            print('Can no uncomporess the Archive',e)

        from datetime import datetime
        # Get today's date in YYYY-MM-DD format
        formatted_date = datetime.today().strftime('%Y%m%d')

        print(f"Today's date: {formatted_date}")
        import re
        import os
        list_files = os.listdir()
        for file in list_files:
            #find IVRA
            text = file
            match = re.search(fr'\b{formatted_date}\b',text)
            if match:
                print("Match found:", match.group())
                print("Extracted the IVRA file into current folder with the:", match.group())
                message = "Extracted the IVRA file into current folder with the:" +  match.group()
                self.logs.setText(message)
                ivra_file = text
                
            else:
                print("No match found.",text)


        IRVA_sheet = ivra_file
        # sales_sheet = input("Enter the file name of sales support sheet:")

        # IRVA_sheet = "IVRAUM003-BO-20240509-0900am.xls"



        irva = pd.read_excel(IRVA_sheet)
        sales = pd.read_excel(sales_sheet)

        
        FundName = sales["FUND NAME"]
        MarketValue = sales["MARKET VALUE"]
        BookValue = sales["BOOK VALUE"]
        RepFullName = sales["REP FULL NAME"]

        FundNameIRVA = irva["FUND NAME"]
        MarketValueIRVA = irva["MARKET VALUE"]
        BookValueIRVA = irva["BOOK VALUE"]

        #Create full name for IRVA file
        FirstName = irva['REP FIRST NAME']
        LastName = irva['REP LAST NAME']
        # RepFullNameIRVA = irva["REP FULL NAME"]
        irva['full_name'] = FirstName + ' ' + LastName
        RepFullNameIRVA = irva['full_name']


        FUNDNAME = pd.concat([FundNameIRVA, FundName], ignore_index=True)
        MARKETVALUE = pd.concat([MarketValueIRVA, MarketValue], ignore_index=True)
        BOOKVALUE = pd.concat([BookValueIRVA, BookValue], ignore_index=True)
        REPFULLNAME = pd.concat([RepFullNameIRVA, RepFullName], ignore_index=True)


        from datetime import date

        today = date.today()
        formatted_date = today.strftime('%B %d, %Y')
        print(formatted_date)  # Output: "September 13, 2023"

        output_file_raw = f'Advisor Daily Holdings as {formatted_date}.xlsx'
        output_file = f'Advisor Daily Holdings as {formatted_date}.xlsx'


        # Create a DataFrame from the concatenated Series
        combined_df = pd.DataFrame({
            'FUND NAME': FUNDNAME,
            'MARKET VALUE': MARKETVALUE,
            'BOOK VALUE': BOOKVALUE,
            'REP FULL NAME': REPFULLNAME
        })

        try:
        # Export the DataFrame to an Excel file
            combined_df.to_excel(output_file_raw, index=False)
        except Exception as e:
            print('error creating the Excel sheet ,{e}')

        print(f"Data exported to {output_file_raw}")


        import os
        current_directory = os.getcwd()
        print(f"The current directory is: {current_directory}")

        import win32com.client as win32
        try:
            xlApp = win32.Dispatch('Excel.Application')
            xlApp.Visible= False
            # wb = xlApp.Workbooks.Open(r"C:\Users\dparbadiya\OneDrive - AIC Global Holdings\Desktop\python code"+f"\{output_file_raw}")
            wb = xlApp.Workbooks.Open(f"{current_directory}\{output_file_raw}")
            # wb.SaveAs(r"C:\Users\dparbadiya\OneDrive - AIC Global Holdings\Desktop\python code"+f"\{output_file}")
            # wb.Close(SaveChanges=1)
            # wb = xlApp.Workbooks.Open(r"C:\Users\dparbadiya\OneDrive - AIC Global Holdings\Desktop\python code"+f"\{output_file_raw}")
            #get worksheet
            ws_data = wb.Worksheets('Sheet1')
            
            sheet2 = wb.Sheets.Add()
            sheet2.Name = "Sheet2"  # Set the desired sheet name
            ws_table = wb.Worksheets('Sheet2')


            # # function to clear the pivot table
            # def clear_pts(ws):
            #     for pt in ws.PivotTables():
            #         pt.TableRange2.Clear()
            # clear_pts(ws_table)

            #create pt cache connection - pivot table cache.
            pt_cache = wb.PivotCaches().Create(1,ws_data.Range("A1").CurrentRegion)

            #create pivot table
            pt = pt_cache.CreatePivotTable(ws_table.Range("A1"),"Advisor_Report")


            pt.ColumnGrand = True


            #change report layout
            pt.RowAxisLayout(2)  
            #compact - 00
            #tabular - 01
            #Outline - 2


            #change pivot table style
            pt.TableStyle2 = "PivotStyleLight16"


            #insert pivot table fields
            #insert pivot table fields
            def insert_pt_field_set1(pt):
                field_rows = {}
                field_rows['REP FULL NAME'] = pt.PivotFields("REP FULL NAME")
                field_rows['FUND NAME'] = pt.PivotFields("FUND NAME")

                field_values = {}
                field_values['BOOK VALUE'] = pt.PivotFields('BOOK VALUE')
                field_values['MARKET VALUE'] = pt.PivotFields('MARKET VALUE')

                #insert row fields to pivot table design

                field_rows['REP FULL NAME'].Orientation = 1
                field_rows['REP FULL NAME'].Position = 1
                
                field_rows['FUND NAME'].Orientation = 1
                field_rows['FUND NAME'].Position = 2



                #insert Value fields

                field_values['BOOK VALUE'].Orientation = 4
                field_values['BOOK VALUE'].NumberFormat = "$ #,##0.00"

                field_values['MARKET VALUE'].Orientation = 4
                field_values['MARKET VALUE'].NumberFormat = "$ #,##0.00"




            #create report
            insert_pt_field_set1(pt)

            #save the workbook
            wb.SaveAs(f"{save_location}"+f"\{output_file}")
            self.logs.setText("file Saved to the location")
            wb.Close(True)
            print('Created the pivot table and saved the sheet.')
            self.logs.setText("Created the pivot table and saved the sheet.")
        except Exception as e:
            print('Exception',e)
            self.logs.setText('Exception',e)
        finally:
            xlApp.Quit()
            print("Resources released")
            self.logs.setText("Resources released")

    def clickHandlerZip(self):
        dialog = QFileDialog()
        dialogSuccessful= dialog.exec()
        selectedFiles = dialog.selectedFiles()
        print(selectedFiles)
        if dialogSuccessful:
            self.zipEdit.setText(selectedFiles[0])
             
        else:
            print("User Cancelled the dialog")
        

    def clickHandlerSales(self):
        pass
        # dialog = QFileDialog()
        # dialogSuccessful= dialog.exec()
        # selectedFiles = dialog.selectedFiles()
        # print(selectedFiles)
        # if dialogSuccessful:
        #     self.salesEdit.setText(selectedFiles[0])
             
        # else:
        #     print("User Cancelled the dialog")
        

    def clickHandlerResult(self):
        # sales_box = self.salesEdit.text()
        if(self.zipEdit.text() == ""):
            self.logs.setText("Please Choose zip File")
            print('empty zip edit')
        # if(self.salesEdit.text() == ""):
        #     print('empty sales path')
        #     self.logs.setText("Please Choose sales File")
        else:
            self.logs.setText("Files are provided: Now Doing the Report")

        
            passwd = self.passwordEdit.text()
            if(passwd==""):
                passwd = 'password'
            print('password is:',passwd)

            report_location = self.reportEdit.text()
            if(report_location==""):
                report_location = 'K:\Advisor Holdings Daily Report'
            print('report location is:',report_location)

            print("do the report using the variables defined on the top")

            zip = self.zipEdit.text()
            sale = self.salesEdit.text()
            print(self.salesEdit.text())
            self.makeReport(zip, sale,report_location)

    
    
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

# Use this code to load the UI file directly without converting it to python file
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow
# from PyQt6 import uic#importing the ui file
# #Say Hello app done
# class MainUI(QMainWindow):
#     def __init__(self):
#         super(MainUI,self).__init__()
#         uic.loadUi('gui.ui',self)
        

# app = QApplication(sys.argv)
# ui = MainUI()
# ui.show()
# app.exec()
