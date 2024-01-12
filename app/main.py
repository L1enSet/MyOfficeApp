# -*- coding: utf-8 -*-

#developer L1enSet
#27/03/2023 - start
#01/04/2023 - alfa ready
#07/04/2023 - beta is ready

import sys
import webbrowser
from weather import Weather
from database_manage import DriveDB
from os import startfile
from datetime import datetime
from os import getcwd
from PyQt5.QtWidgets import QMainWindow, QWidget, QToolBox, QTabWidget, QApplication, QPushButton, QLabel, QFrame, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QCheckBox, QFileDialog, QComboBox
from PyQt5.QtCore import Qt, QPoint


class Styles():

    def qss_sakura():
        with open("style/sakura_qss.txt", "r") as file:
            qss = file.read()

        return qss

    def qss_orange():
        with open("style/orange_qss.txt", "r") as file:
            qss = file.read()

        return qss

    qss_now = None #отображает текущий qss настраивается в settings
    
    qss_copy_All = """#CopyAllButton { color: rgba(102, 255, 102, 0.6); }"""
    

class Root(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setGeometry(100,100,405,295)
        self.setWindowTitle("App2.0")
        self.database = DriveDB("database.db")
        self.main_frame = ToolBox(self)

        #labels
        self.lbl_title = QLabel("MyOfficeApp_v2.1_(beta) L1enSet", self)
        self.lbl_title.setGeometry(5, 277, 300, 15)
        #buttons
        self.btn_exit = QPushButton("Exit", self)
        self.btn_exit.setGeometry(360, 277, 40, 15)
        self.btn_exit.clicked.connect(app.quit)

        self.btn_minimalize = QPushButton("---", self)
        self.btn_minimalize.setGeometry(320, 277, 40, 15)
        self.btn_minimalize.clicked.connect(self.showMinimized)

        #self.btn_update_weather = QPushButton('Update', self)
        #self.btn_update_weather.setGeometry(250, 402, 60, 15)
        #self.btn_update_weather.clicked.connect(self.weather_now)

        #container
        #self.weather_frame = Container(self, 250, 150, 2, 252)
        #self.webdriver_frame = Container(self, 150, 150, 253, 252)

        #self.lbl_weather = QLabel("", self.weather_frame)
        #self.lbl_weather.setGeometry(5, 0, 250, 150)
        #self.weather_now()
        
        self.setAutoFillBackground(False)

    def weather_now(self):
        weather = Weather()
        now = weather.weather_now()
        forecast = weather.weather_fc()

        text = f"""
Сейчас:
В небе:   {now['weather_main']}
Температура:   {now['temp_now']}°C
По ощущениям:   {now['temp_feels']}°C
Ветер:   {now['wind_speed']}М/С   {now['wind_vect']}

В ближайшем будущем   {forecast['datetime']}:
Ожидается:   {forecast['weather_main']}
Температура:   {forecast['temp_now']}°C
Будет ощущаться как:   {forecast['temp_feels']}°C
"""
        self.lbl_weather.setText(text)
        return 0

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


class ToolBox(QToolBox):
    def __init__(self, parent=None):
        QToolBox.__init__(self, parent)
        self.setGeometry(0,0,409,275)
        self.layout().setSpacing(0)

        self.box1 = WidgetTabsMain(self)
        self.box2 = WidgetTabsOther(self)

        self.addItem(self.box1, "MainFrame")
        self.addItem(self.box2, "OtherFrame")

        self.setAutoFillBackground(False)
        

class WidgetTabsMain(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.setGeometry(0,0,409,250)
        
        self.tab1 = FormWidget()
        self.tab2 = TextWidget()
        self.tab3 = RolesWidget()
        self.tab4 = ShortAnswersWidget()
        self.tab5 = TicketsWidget()
        self.tab6 = SettingsWidget()
        
        self.addTab(self.tab1, 'Form')
        self.addTab(self.tab2, 'Book')
        self.addTab(self.tab3, 'Roles')
        self.addTab(self.tab4, 'Answers')
        self.addTab(self.tab5, 'Ticket')
        self.addTab(self.tab6, 'Settings')
        
        self.setAutoFillBackground(False)


class WidgetTabsOther(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.setGeometry(0,0,409,250)

        self.tab1 = CallsLogWidget()
        
        
        self.addTab(self.tab1, 'Calls')
        
        self.setAutoFillBackground(False)
        
        
class FormWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-image: url("images/bg_form.jpg");}""")
        self.database = DriveDB("database.db")
        
        self.last_data = None

        #ElementsUI
        #container
        qss_container = """QFrame {background-image: url("images/bg_form_frame.jpg");}"""
        self.container = Container(self, 310, 130, 90, 65, qss_container)
        #labels
        #line_edits
        #EDIT NAME
        self.edit_name = QLineEdit(self.container)
        self.edit_name.setPlaceholderText("Name")
        self.edit_name.setGeometry(5, 5, 150, 20)
        #EDIT TROUBLE
        self.edit_trouble = QLineEdit(self.container)
        self.edit_trouble.setPlaceholderText("Trouble/ticket")
        self.edit_trouble.setGeometry(5, 30, 150, 20)
        #EDIT COMPANY
        self.edit_company = QLineEdit(self.container)
        self.edit_company.setPlaceholderText("Organization")
        self.edit_company.setGeometry(5, 55, 150, 20)
        #EDIT PHONE
        self.edit_phone = QLineEdit(self.container)
        self.edit_phone.setPlaceholderText("Phone")
        self.edit_phone.setGeometry(5, 80, 150, 20)
        
        #events line edit
        self.edit_name.returnPressed.connect(self.edit_trouble.setFocus)
        self.edit_trouble.returnPressed.connect(self.edit_company.setFocus)
        self.edit_company.returnPressed.connect(self.edit_phone.setFocus)
        self.edit_phone.returnPressed.connect(self.edit_name.setFocus)

        #buttons
        #BTN COPY NAME
        self.btn_copy_name = QPushButton("Copy", self.container)
        self.btn_copy_name.setGeometry(160, 5, 70, 20)
        self.btn_copy_name.clicked.connect(lambda: self.copy_value(self.edit_name))
        
        #BTN COPY TROUBLE
        self.btn_copy_trouble = QPushButton("Copy", self.container)
        self.btn_copy_trouble.setGeometry(160, 30, 34, 20)
        self.btn_copy_trouble.clicked.connect(lambda: self.copy_value(self.edit_trouble))
        
        #BTN OPEN TICKET
        self.btn_open_ticket = QPushButton("Open", self.container)
        self.btn_open_ticket.setGeometry(196, 30, 34, 20)
        self.btn_open_ticket.clicked.connect(lambda: self.open_ticket(self.edit_trouble))
        
        #BTN COPY COMPANY
        self.btn_copy_company = QPushButton("Copy", self.container)
        self.btn_copy_company.setGeometry(160, 55, 70, 20)
        self.btn_copy_company.clicked.connect(lambda: self.copy_value(self.edit_company))
        
        #BTN COPY PHONE
        self.btn_copy_phone = QPushButton("Copy", self.container)
        self.btn_copy_phone.setGeometry(160, 80, 70, 20)
        self.btn_copy_phone.clicked.connect(lambda: self.copy_value(self.edit_phone))
        
        #BTN CLEAR
        self.btn_clear = QPushButton("Clear", self.container)
        self.btn_clear.setGeometry(160, 105, 70, 20)
        self.btn_clear.clicked.connect(self.clear_form)
        
        #BTN COPY ALL
        self.btn_copy_all = QPushButton("Copy All", self.container)
        self.btn_copy_all.setObjectName('CopyAllButton')
        self.btn_copy_all.setGeometry(5, 105, 150, 20)
        self.btn_copy_all.clicked.connect(self.copy_all_data)
        
    def copy_value(self, element):
        #element это поле откуда брать значение
        c_board.setText(element.text().capitalize())
        
        return 0
    
    def open_ticket(self, element):
        url = "https://sm.permkrai.ru/otrs/index.pl?Action=AgentTicketSearch;Subaction=Search;TicketNumber={}".format(element.text())
        webbrowser.open(url, new=2, autoraise=True)
        
        return 0
    
    def copy_all_data(self):
        name = self.edit_name.text().capitalize()
        trouble = self.edit_trouble.text().capitalize()
        company = self.edit_company.text().capitalize()
        phone = self.edit_phone.text().capitalize()
        date = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
        
        file_data = """date - {}
name - {}
trouble - {}
company - {}
phone - {}

""".format(date, name, trouble, company, phone)
        
        clipboard_data = """Имя: {}
Проблема: {}
Организация: {}
""".format(name, trouble, company)
        
        if (name, trouble, company, phone) == self.last_data:
            c_board.setText(clipboard_data)
        
        else:
            c_board.setText(clipboard_data)
            self.database.add_call((name, trouble, company, phone, date))
            
            self.last_data = (name, trouble, company, phone)
            self.btn_copy_all.setStyleSheet(Styles.qss_copy_All)
        
        return 0
    
    def clear_form(self):
        self.last_data = None
        self.edit_name.setText("")
        self.edit_trouble.setText("")
        self.edit_company.setText("")
        self.edit_phone.setText("")
        
        self.btn_copy_all.setStyleSheet(Styles.qss_now)
        

class TextWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-image: url("images/bg_notebook.jpg");}""")

        #elementsUI
        #text area
        bg_container = """QFrame {background-image: url("images/bg_text_edit.jpg");}"""
        self.container = Container(self, 250, 140, 150, 10, bg_container)
        self.text_area = QTextEdit(self.container)
        self.text_area.setPlaceholderText('Somthing text...')
        self.text_area.setGeometry(0, 0, 250, 140)
         
        #buttons
        #BTN COPY
        self.btn_copy = QPushButton('Copy', self)
        self.btn_copy.setGeometry(275, 155, 117, 20)
        self.btn_copy.clicked.connect(self.copy_text)

        #BTN CLEAR
        self.btn_clear = QPushButton('Clear', self)
        self.btn_clear.setGeometry(155, 155, 117, 20)
        self.btn_clear.clicked.connect(self.text_area.clear)
    
    def copy_text(self):
        self.text_area.selectAll()
        self.text_area.copy()
    
    def clear_text(self):
        self.text_area.setText('')
        

class RolesWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(True)
        self.setStyleSheet("""QFrame {background-image: url("images/bg_roles.jpg");}""")
        self.database = DriveDB("database.db")

        #elementsUI
        #list widget
        bg_container = """QFrame {background-image: url("images/bg_list_roles.jpg");}"""
        self.container = Container(self, 250, 190, 145, 7, bg_container)
        self.lst_widget = QListWidget(self.container)
        self.lst_widget.setGeometry(0, 0, 250, 190)    
        self.show_roles()
        self.lst_widget.itemClicked.connect(self.copy_role)
        

    def show_roles(self):
        """with open("content_docs/roles.txt", "r", encoding="utf-8") as file:
            for i in file.readlines():
                self.lst_widget.addItem(i[:-1])"""
        
        for i in self.database.sql_request(request_text="select * from roles"):
            self.lst_widget.addItem(i[1])

        return 0
    
    def copy_role(self):
        index = self.lst_widget.currentRow()
        item = self.lst_widget.item(index)
        c_board.setText(item.text())
        
        return 0
        
        
class TicketsWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-image: url("images/bg_tickets.jpg");}""")

        self.data_tickets = {} #основной словарь заполняется методом open_file
        
        self.ticket_value = 1 #текущее значение ключа для data_tickets методы open nex и rear будут двигать метку
        self.chek_position = None #для проверки смещения в методах next_ticket и break_ticket позволяет понять куда листали последний раз
        
        #elementsUI
        #container
        bg_container = """QFrame {background-image: url("images/bg_tickets_frame.jpg");}"""
        self.container = Container(self, 300, 190, 100, 7, bg_container)
        
        #line edit
        self.route_file = QLineEdit(self.container)
        self.route_file.setPlaceholderText("Route to file")
        self.route_file.setGeometry(5, 5, 200, 20)

        self.ticket_num = QLineEdit(self.container)
        self.ticket_num.setPlaceholderText("TicketNum")
        self.ticket_num.setGeometry(5, 65, 200, 20)
        
        #buttons
        self.btn_open_file= QPushButton("Open file", self.container)
        self.btn_open_file.setGeometry(5, 30, 98, 20)
        self.btn_open_file.clicked.connect(self.open_file)

        self.btn_close_file = QPushButton("Close file", self.container)
        self.btn_close_file.setEnabled(False)
        self.btn_close_file.setGeometry(107, 30, 98, 20)
        self.btn_close_file.clicked.connect(self.close_file)

        self.btn_copy_ticket = QPushButton("Copy", self.container)
        self.btn_copy_ticket.setEnabled(False)
        self.btn_copy_ticket.setGeometry(5, 90, 37, 20)
        self.btn_copy_ticket.clicked.connect(self.copy_data)

        self.btn_next_ticket = QPushButton(">>>", self.container)
        self.btn_next_ticket.setEnabled(False)
        self.btn_next_ticket.setGeometry(87, 90, 37, 20)
        self.btn_next_ticket.clicked.connect(self.next_ticket)

        self.btn_rear_ticket = QPushButton("<<<", self.container)
        self.btn_rear_ticket.setEnabled(False)
        self.btn_rear_ticket.setGeometry(46, 90, 37, 20)
        self.btn_rear_ticket.clicked.connect(self.rear_ticket)

        self.btn_open_ticket = QPushButton("Open ticket", self.container)
        self.btn_open_ticket.setEnabled(False)
        self.btn_open_ticket.setGeometry(129, 90, 76, 20)
        self.btn_open_ticket.clicked.connect(self.open_ticket)
        
        #labels
        self.lbl_last_ticket = QLabel("Last ticket - {}".format(None), self.container)
        self.lbl_last_ticket.setGeometry(5, 115, 150, 20)

        self.lbl_ticket_num = QLabel("Ticket num - {}".format(None), self.container)
        self.lbl_ticket_num.setGeometry(5, 140, 100, 20)
        
        self.lbl_tickets_all = QLabel("Tickets all - {}".format(None), self.container)
        self.lbl_tickets_all.setGeometry(5, 165, 100, 20)

    def open_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(self, 'Open document', getcwd())[0]
            self.route_file.setText(file_name)
            data = open(file_name, 'r')
            num = 1
            for line in data.readlines():
                self.data_tickets[num]=line[:len(line)-1] #срез для удаления переноса сроки
                num += 1
            data.close()
            
            #Включаем кнопки
            self.btn_close_file.setEnabled(True)
            self.btn_copy_ticket.setEnabled(True)
            self.btn_open_ticket.setEnabled(True)
            self.btn_next_ticket.setEnabled(True)
            #Настраиваем UI для первых значений
            self.lbl_ticket_num.setText("Ticket num - {}".format(self.ticket_value))
            self.lbl_last_ticket.setText("Last ticket - {}".format(self.data_tickets[self.ticket_value]))
            self.lbl_tickets_all.setText("Tickets all - {}".format(str(len(self.data_tickets.keys()))))
            
            self.ticket_num.setText(self.data_tickets[self.ticket_value])
            
            return 0

        except FileNotFoundError:
            self.ticket_num.setText("FILE NOT FOUND")

    def open_ticket(self):
        try:
            url = "https://sm.permkrai.ru/otrs/index.pl?Action=AgentTicketSearch;Subaction=Search;TicketNumber={}".format(self.data_tickets[self.ticket_value])
            webbrowser.open(url, new=2, autoraise=True)
            
            self.btn_rear_ticket.setEnabled(True) 
            self.data_tickets[self.ticket_value] += '+'
            self.ticket_num.setText(self.data_tickets[self.ticket_value])
            self.lbl_ticket_num.setText("Ticket num - {}".format(str(self.ticket_value)))
            
            try:
                self.lbl_last_ticket.setText("Last ticket - {}".format(self.data_tickets[self.ticket_value -1]))
            except KeyError:
                pass
            
            self.ticket_value += 1
            self.chek_position = True
            
        except KeyError:
            self.ticket_num.setText("ERROR no tickets")
        
        return 0

    def copy_data(self):
        c_board.setText(self.ticket_num.text())
        return 0

    def next_ticket(self): #листать слвоарь вперед для просмотра
        try:
            #проверка для того что бы понять на сколько листать словарь
            if self.chek_position == True:
                pass
            elif self.chek_position == None:
                self.ticket_value += 1
            elif self.chek_position == False:
                self.ticket_value += 2
            
            self.ticket_num.setText(self.data_tickets[self.ticket_value])
            self.lbl_ticket_num.setText("Ticket num - {}".format(str(self.ticket_value)))
            self.btn_rear_ticket.setEnabled(True)
            self.ticket_value += 1
            
            self.chek_position = True
            
        except KeyError:
            self.ticket_num.setText("ERROR bad tickt number")

        return 0

    def rear_ticket(self): #листать назад
        try: 
            #проверка для того что бы понять на сколько листать словарь
            if self.chek_position == True:
                self.ticket_value -= 2
            elif self.chek_position == None:
                self.ticket_value -= 1
            elif self.chek_position == False:
                pass
                
            self.ticket_num.setText(self.data_tickets[self.ticket_value])
            self.lbl_ticket_num.setText("Ticket num - {}".format(str(self.ticket_value)))
            self.btn_rear_ticket.setEnabled(True)
            self.ticket_value -= 1
            
            self.chek_position = False
            
        except KeyError:
            self.ticket_num.setText("ERROR bad tickt number")
    
    def close_file(self):
        #возврат всех переменных в исходные значения (до открытия файла)
        self.data_tickets = {}
        self.ticket_value = 1 
        self.chek_position = None
        self.lbl_last_ticket.setText("Last ticket - {}".format(None))
        self.lbl_ticket_num.setText("Ticket num - {}".format(None))
        self.lbl_tickets_all.setText("Tickets all - {}".format(None))
        self.route_file.setText(None)
        self.ticket_num.setText(None)
        
        self.btn_copy_ticket.setEnabled(False)
        self.btn_next_ticket.setEnabled(False)
        self.btn_rear_ticket.setEnabled(False)
        self.btn_open_ticket.setEnabled(False)
        
        return 0


class ShortAnswersWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-image: url("images/bg_answers.jpg");}""")
        self.database = DriveDB("database.db")
        self.list_items = {}

        #elementsUI
        #container
        bg_container = """QFrame {background-image: url("images/bg_answers_frame.jpg");}"""
        self.container = Container(self, 285, 193, 115, 7, bg_container)
        #list_widget
        self.lst_answers = QListWidget(self.container)
        self.lst_answers.setGeometry(0,0,285,153)
        try:
            self.show_items()
            self.lst_answers.itemClicked.connect(self.get_answer)
        except FileNotFoundError:
            pass

        self.txt_answer = QTextEdit(self.container)
        self.txt_answer.setGeometry(0, 153, 285, 40)
        self.txt_answer.setPlaceholderText("View answer...")
        self.txt_answer.setStyleSheet("""QTextEdit {background-position: bottom;}""")

    def show_items(self):
        for i in self.database.sql_request(request_text="select * from answers"):
            self.lst_answers.addItem(i[1])
            

        return 0

    def get_answer(self):
        index = self.lst_answers.currentRow()
        item = self.lst_answers.item(index)
        text = self.database.sql_request(request_text="select answer from answers where title = '{}'".format(item.text()))
        display_text = text.fetchone()[0]
        c_board.setText(display_text)
        self.txt_answer.setText(display_text)

        return 0
        
                 
class SettingsWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-image: url("images/bg_settings.jpg");}""")

        #elementsUI
        #container
        qss_container = """QFrame {background-image: url("images/bg_settings_frame.jpg");}"""
        self.container = Container(self, 280, 190, 120, 7, qss_container)

        #check box
        self.app_upped = QCheckBox("Window always UP", self.container)
        self.app_upped.setGeometry(5, 5, 200, 20)
        self.app_upped.stateChanged.connect(self.window_up)

        #buttons
        self.btn_open_log = QPushButton("Open log", self.container)
        self.btn_open_log.setGeometry(5, 30, 100, 20)
        self.btn_open_log.clicked.connect(lambda: self.start_file('log.txt'))

        self.btn_open_roles = QPushButton("Open roles", self.container)
        self.btn_open_roles.setGeometry(5, 55, 100, 20)
        self.btn_open_roles.clicked.connect(lambda: self.start_file('roles.txt'))

        self.btn_open_answers = QPushButton("Open answers", self.container)
        self.btn_open_answers.setGeometry(5, 80, 100, 20)
        self.btn_open_answers.clicked.connect(lambda: self.start_file('short_answers.txt'))

        #urls
        self.btn_url_portal = QPushButton("URL Portal ics", self.container)
        self.btn_url_portal.setGeometry(115, 30, 80, 20)
        self.btn_url_portal.clicked.connect(lambda: self.open_url("https://portal24.itsperm.ru/"))

        self.btn_url_google_file = QPushButton("URL Google file", self.container)
        self.btn_url_google_file.setGeometry(115, 55, 80, 20)
        self.btn_url_google_file.clicked.connect(lambda: self.open_url("https://docs.google.com/spreadsheets/d/1IIEX6grQZHUpVGw1Qzi0xB2wqrLbEAHX9wEJ_TXgS44/edit#gid=84736261"))

        self.btn_url_sui = QPushButton("URL СУИ", self.container)
        self.btn_url_sui.setGeometry(115, 80, 80, 20)
        self.btn_url_sui.clicked.connect(lambda: self.open_url("https://sm.permkrai.ru/otrs/index.pl?Action=AgentDashboard"))

        self.btn_url_ats = QPushButton("URL ATS", self.container)
        self.btn_url_ats.setGeometry(115, 105, 80, 20)
        self.btn_url_ats.clicked.connect(lambda: self.open_url("http://172.17.3.76:82/index.html#"))

        #combo box
        self.color_box = QComboBox(self.container)
        self.color_box.setGeometry(5, 105, 100, 20)
        self.color_box.addItems(['sakura_qss', 'orange_qss'])
        self.color_box.activated[str].connect(self.set_theme)

    def set_theme(self, text):
        theme = {
            'sakura_qss':Styles.qss_sakura,
            'orange_qss':Styles.qss_orange}
        Styles.qss_now = theme[text]()
        return Mainwindow.setStyleSheet(Styles.qss_now)

    def start_file(self, file_name):
        return startfile('content_docs\{}'.format(file_name)) #os.startfile

    def window_up(self, state):
        if state == Qt.Checked:
            Mainwindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            Mainwindow.show()
        else:
            Mainwindow.setWindowFlags(Qt.FramelessWindowHint)
            Mainwindow.show()

    def open_url(self, url):
        webbrowser.open(url, new=2, autoraise=True)

        return 0

class CallsLogWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,409,230)
        self.setAutoFillBackground(True)
        self.setStyleSheet("""QFrame {background-color: rgb(21, 23, 25);}""")
        self.database = DriveDB("database.db")

        #elementsUI
        #list widget
        #bg_container = """QFrame {background-image: url("images/bg_list_roles.jpg");}"""
        bg_container = """QFrame {background-image: none;}"""
        self.container = Container(self, 200, 190, 7, 7, bg_container)
        self.lst_widget = QListWidget(self.container)
        self.lst_widget.setGeometry(0, 0, 200, 190)

        self.container_descript = Container(self, 180, 190, 217, 7, bg_container)
        self.user_edit = QLineEdit(self.container_descript)
        self.user_edit.setGeometry(4, 4, 80, 17)
        self.organization_edit = QLineEdit(self.container_descript)
        self.organization_edit.setGeometry(4, 24, 80, 17)
        self.phone_edit = QLineEdit(self.container_descript)
        self.phone_edit.setGeometry(4, 44, 80, 17)
        self.date_edit = QLineEdit(self.container_descript)
        self.date_edit.setGeometry(4, 64, 80, 17)
        self.trouble_edit = QTextEdit(self.container_descript)
        self.trouble_edit.setGeometry(4, 84, 170, 80)


        self.show_calls()
        self.lst_widget.itemClicked.connect(self.about_call)

    def show_calls(self):
        for i in self.database.sql_request(request_text="select * from calls"):
            self.lst_widget.addItem("{} - {}::{}".format(i[4], i[5], i[0]))
    
    def about_call(self):
        index = self.lst_widget.currentRow()
        item = self.lst_widget.item(index)
        item_id = item.text().split("::")[1]
        querry = self.database.sql_request(request_text="select * from calls where id = {}".format(item_id))
        call = querry.fetchone()
        self.user_edit.setText(call[1])
        self.organization_edit.setText(call[3])
        self.phone_edit.setText(call[4])
        self.date_edit.setText(call[5])
        self.trouble_edit.setText(call[2])



class Container(QFrame):
    def __init__(self, parent=None, width=10, height=10, horizont=10, vertical=10, qss=None):
        QFrame.__init__(self, parent)
        self.width = width
        self.height = height
        self.horizont = horizont
        self.vertical = vertical
        self.qss = qss
        self.setGeometry(self.horizont,
                         self.vertical,
                         self.width,
                         self.height)
        self.setObjectName("Container")
        self.setStyleSheet(self.qss)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    c_board = QApplication.clipboard()
    Mainwindow = Root()
    Mainwindow.setWindowFlags(Qt.FramelessWindowHint)
    Mainwindow.setStyleSheet(Styles.qss_sakura())
    Mainwindow.show()
    sys.exit(app.exec_())
