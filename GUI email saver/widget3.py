from PySide6.QtCore import Qt,QObject, QThread, Signal
import sys
from PySide6.QtWidgets import QWidget,QMainWindow,QApplication
from emailapp import Ui_MainWindow
import win32com.client
import datetime
import os
import re
from msg import ConvertMessage
from PySide6 import QtCore
from time import sleep
import configparser

class Worker(QObject):
    def __init__(self,option,start,end,url,path,self1):
        super().__init__()
        self.selected_option = option
        self.startDate = start
        self.endDate = end
        self.url = url
        self.path = path

    def changeStatus(self,msg):
        self.progress.emit(msg)


    finished = Signal()
    progress = Signal(str)

    def run(self):
        """Long-running task."""
        try:

            self.save_emails()
        except Exception as e:
            print(f'Error : {e}')
            self.finished.emit()
        else:
            self.finished.emit()

    def save_emails(self):
        self.msgs = []
        # self.i = 0
        # self.n = len(self.msgs)
        print('saving emails')
        self.message = f'saving the emails for {self.selected_option}'
        self.msgs.append(self.message)
        self.changeStatus(self.message)

        # self.show_message()
        try:
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        except Exception as e:
            self.changeStatus(f'can not open outlook application {e}')

        # # Connect to the Inbox folder (6 corresponds to the Inbox folder)
        inbox = outlook.GetDefaultFolder(6)

        today_date = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        try:
            if (self.selected_option == 'Today'):
                print('today')
                self.filtered_emails = [email for email in inbox.Items if email.ReceivedTime.date() == today_date]
            if (self.selected_option == 'Yesterday'):
                print('Yesterday')
                self.filtered_emails = [email for email in inbox.Items if email.ReceivedTime.date() == yesterday]
            if (self.selected_option == 'Date Range'):
                print('range')
                self.filtered_emails = [email for email in inbox.Items if
                                        email.ReceivedTime.date() >= self.startDate and email.ReceivedTime.date() <= self.endDate]
        except Exception as e:
            self.changeStatus(f"Can not filter the email for {self.selected_option}")

        else:
            self.changeStatus(f'Filtered The email for {self.selected_option}')
            # self.show_message() 
            self.save_into_folder(self.filtered_emails)

    def save_into_folder(self, filtered_emails):
        count = 0
        skips = []
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            skips = config['DEFAULT']['skip'].split(',')
            # print(f"skipping this words{skips}")
        except:
            print('config file not found')
            skips = ['[Test]', 'FW', 'RE']
        for email in filtered_emails:
            url_pattern = self.url
            extra_matching = config['EXTRA MATCH']['match'].split(',')
            all = []
            all.append(url_pattern)
            all.extend(extra_matching)
            print(f'matching all of this strings mentioned here: {all}')
            try:
                email_body = email.body.encode('utf-8', errors='ignore').decode('utf-8')
                email_Subject = email.Subject.encode('utf-8', errors='ignore').decode('utf-8')
            except UnicodeDecodeError:
                email_body = email.body.encode('latin-1', errors='ignore').decode('latin-1')
                email_Subject = email.Subject.encode('utf-8', errors='ignore').decode('latin-1')
            # print(email_body)

            try:
                for url_pattern in all:
                    urls = re.findall(url_pattern, email_body)
                    if urls:
                        is_skip = False
                        # if "[Test]" in email_Subject:
                        #     print(f"Skipping {email_Subject} as it's a test email.")
                        #     continue
                        #
                        # if "FW" in email.Subject:
                        #     print(f"Skipping FW MESSAGES {email_Subject} as it's a forwarded email.")
                        #     continue
                        #
                        # if "RE" in email.subject:
                        #     print(f"skipping RE Messages {email_Subject}")
                        #     continue
                        for skip in skips:
                            if skip in email_Subject:
                                print(f"Skipping {email_Subject} as it's a {skip} in config.")
                                is_skip = True

                        if is_skip:
                            continue

                        date_of_email = str(email.ReceivedTime).split(" ")[0]

                        specific_date = datetime.datetime.strptime(date_of_email, "%Y-%m-%d").date()
                        path = f'{self.path}\\{specific_date}'
                        # path = f'O:\Sales\Bulletins\mailchimp bulletin\{specific_date}'
                        try:
                            os.mkdir(path)
                            # print('Folder Created')
                        except:
                            # print('already Exists')
                            pass
                        # print(email)

                        # if ':' or '<' or '"' or "/" or "\\" or "|" or "?" or "*" or "." in email.subject:
                        #     modified_string = modified_string.replace(':', '-')
                        modified_string = self.sanitize_subject(email_Subject)
                        final_string = str(path) + f"/{modified_string}.msg"
                        final_string_html = str(path) + f"/{modified_string}.html"
                        final_string_txt = str(path) + "/errors.txt"
                        print(final_string)

                        # Saving the email
                        try:
                            print(email_Subject)
                            email.SaveAs(final_string)
                            ConvertMessage(final_string, final_string_html).save_to_html(final_string, final_string_html)
                            # # email.SaveAs(final_string)
                            # with open(final_string_txt, 'a') as f:
                            #     f.write(f'{email.Subject} \n {email.body}')

                            count += 1
                            print(count)

                        except Exception as e:
                            # print(email.subject)
                            print(f'Not able to save {email.subject} because of {e}')
                            file_path = os.path.join(path, date_of_email)
                            # Create a new text file called "example.txt" and write some text into it
                            with open(final_string_txt, 'a', encoding="utf8") as f:
                                f.write(
                                    f'not able to create file for the email : {email_Subject}\n error : {e}\n possible file name:{final_string}\n')
                        else:
                            print('no Exception')
                            if count == 0:
                                self.changeStatus(f"No Emails {self.selected_option}")
                            else:

                                self.changeStatus(f"Successfully saved {email.Subject}")

                    if count == 0:
                        self.changeStatus(f"No Emails {self.selected_option}")
                    else:
                        self.changeStatus(f"Successfully saved All emails for {self.selected_option}")

            except Exception as e:
                print('Not able to filter the emails from the content because of : ',e)



    def sanitize_subject(self,subject):
        # Define the characters not allowed in Windows file names
        invalid_chars = r'[<>:"/\\|?*\.]'

        # Replace invalid characters with an empty string
        sanitized_subject = re.sub(invalid_chars, '_', subject)

        return sanitized_subject



class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        config = configparser.ConfigParser()
        config.read('config.ini')


        # save the messages when clicked on the button
        # self.save_button.clicked.connect(self.save_emails)
        self.thread = {}
        self.startDate = self.dateEdit.date().toPython()
        self.endDate = self.dateEdit_2.date().toPython()
        self.current_option = self.selected_option.currentText()
        total = self
        self.save_button.clicked.connect(self.runLongTask)

        self.selected_option.currentIndexChanged.connect(self.show_date_widget)
        # By default hide date picker
        self.date_column.hide()
        self.default_path = config['PATH']['path']
        self.path.setText(self.default_path)
        self.default_url = config['MATCH']['match']
        self.matchingUrl = self.default_url
        self.url.setText(self.default_url)
        self.statusbar.messageChanged.connect(self.reportProgress)
        print(f"configuration path : {self.default_path} \nmatch:{self.matchingUrl}")


    def reportProgress(self, msg):
        self.statusbar.showMessage(f"{msg}")


    def runLongTask(self):
        # Step 2: Create a QThread object
        option = self.selected_option.currentText()
        startDate = self.dateEdit.date().toPython()
        endDate = self.dateEdit_2.date().toPython()
        url = self.url.text()
        path = self.path.text()
        print(self.selected_option.currentText())
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(option,startDate,endDate,url,path,self)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.processing_button()

        self.thread.finished.connect(
             self.enable_Button
        )
        # self.thread.finished.connect(
        #     lambda: self.reportProgress("Long-Running Step: 0")
        # )

    def processing_button(self):
        self.save_button.setText('Wait...')
        self.save_button.setChecked(True)
        self.save_button.setEnabled(False)
    def enable_Button(self):
        self.save_button.setChecked(False)
        self.save_button.setEnabled(True)
        self.save_button.setText('Save')


    def save_emails(self,option,start,end):

        self.msgs = []
        # self.i = 0
        # self.n = len(self.msgs)
        print('saving emails')
        self.message = f'saving the emails for {self.selected_option.currentText()}'
        self.msgs.append(self.message)
        self.statusbar.showMessage(self.message,200)

        # self.show_message()

        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

        # # Connect to the Inbox folder (6 corresponds to the Inbox folder)
        inbox = outlook.GetDefaultFolder(6)

        today_date = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)


        if(self.selected_option.currentText() == 'Today'):
            print('today')
            self.filtered_emails = [email for email in inbox.Items if email.ReceivedTime.date() == today_date]
        if(self.selected_option.currentText() == 'Yesterday'):
            print('Yesterday')
            self.filtered_emails = [email for email in inbox.Items if email.ReceivedTime.date() == yesterday]
        if(self.selected_option.currentText() == 'Date Range'):
            print('range')
            self.startDate = self.dateEdit.date().toPython()
            self.endDate = self.dateEdit_2.date().toPython()
            self.filtered_emails = [email for email in inbox.Items if email.ReceivedTime.date()>= self.startDate and email.ReceivedTime.date()<=self.endDate]

        print(self.url.text())


        self.message = 'using the path: ' + self.path.text()
        self.msgs.append(self.message)
        print(self.message)
        self.statusbar.clearMessage()
        self.statusbar.showMessage(self.message,200)
        # self.show_message()
        self.save_into_folder(self.filtered_emails)
        outlook = None



    def save_into_folder(self,filtered_emails):
        count = 0
        for email in filtered_emails:
            url_pattern = self.url.text()
            urls = re.findall(url_pattern, email.body)
            if urls:
                if "[Test]" in email.Subject:
                    print(f"Skipping {email.Subject} as it's a test email.")
                    continue

                if "FW" in email.Subject:
                    print(f"Skipping FW MESSAGES {email.Subject} as it's a forwarded email.")
                    continue

                date_of_email = str(email.ReceivedTime).split(" ")[0]

                specific_date = datetime.datetime.strptime(date_of_email, "%Y-%m-%d").date()
                path = f'{self.path.text()}\\{specific_date}'
                # path = f'O:\Sales\Bulletins\mailchimp bulletin\{specific_date}'
                try:
                    os.mkdir(path)
                    # print('Folder Created')
                except:
                    # print('already Exists')
                    pass
                # print(email)
                modified_string = email.Subject
                if ':' or '<' or '"' or "/" or "\\" or "|" or "?" or "*" in email.subject:
                    modified_string = modified_string.replace(':', '-')
                final_string = str(path) + f"/{modified_string}.msg"
                final_string_html = str(path) + f"/{modified_string}.html"
                print(final_string)

                #Saving the email
                try:
                    email.SaveAs(final_string)
                    ConvertMessage(final_string,final_string_html).save_to_html(final_string,final_string_html)
                    # # email.SaveAs(final_string)
                    # with open(final_string_txt, 'a') as f:
                    #     f.write(f'{email.Subject} \n {email.body}')

                    count+=1
                    print(count)

                except:
                    file_path = os.path.join(path, date_of_email)
                    # Create a new text file called "example.txt" and write some text into it
                    with open('UIbackup/file_path', 'a') as f:
                        f.write(f'not able to create file for the email : {email.Subject} \n {email.body}')
                else:
                    print('no Exception')
                    if count == 0:
                        self.statusbar.clearMessage()
                        self.statusbar.showMessage("No Emails today",200)
                    else:
                        self.statusbar.clearMessage()
                        self.statusbar.showMessage(f"Successfully saved {email.Subject}",200)
        if count == 0:
            self.statusbar.clearMessage()
            self.statusbar.showMessage("No Emails today")
        else:
            self.statusbar.clearMessage()
            self.statusbar.showMessage(f"Successfully saved All emails for {self.selected_option.currentText()}")





    def show_date_widget(self):
        if self.selected_option.currentText() == 'Date Range':
            self.date_column.show()
            self.today_date = datetime.date.today()
            self.dateEdit.setDisplayFormat('MM/dd/yyyy')
            self.dateEdit.setDate(self.today_date)
            self.yesterday = self.today_date - datetime.timedelta(days=1)
            self.dateEdit_2.setDisplayFormat('MM/dd/yyyy')
            self.dateEdit_2.setDate(self.yesterday)
        else:
            self.date_column.hide()

    # def show_message(self):
    #     self.statusBar.showMessage(self.msgs[self.i])
    #     self.i += 1
    #     if self.i == self.n:
    #         self.timer.stop()
    #         self.i = 0