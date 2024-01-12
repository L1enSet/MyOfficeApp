# -*- coding: utf-8 -*-

#developer L1enSet
#27/03/2023 - start
#01/04/2023 - alfa ready
#07/04/2023 - beta is ready

import sys
import webbrowser
from os import startfile
from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget, QApplication, QPushButton, QLabel, QFrame, QListWidget, QListWidgetItem, QCheckBox, QComboBox, QTextEdit
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
        self.setGeometry(100,100,300,420)
        self.setWindowTitle("App2.0")
        self.main_frame = WidgetTabs(self)

        #labels
        self.lbl_title = QLabel("MyOfficeApp(Lite)_v1.0", self)
        self.lbl_title.setGeometry(5, 402, 300, 15)
        #buttons
        self.btn_exit = QPushButton("Exit", self)
        self.btn_exit.setGeometry(250, 402, 40, 15)
        self.btn_exit.clicked.connect(app.quit)

        self.btn_minimalize = QPushButton("---", self)
        self.btn_minimalize.setGeometry(205, 402, 40, 15)
        self.btn_minimalize.clicked.connect(self.showMinimized)
        
        self.setAutoFillBackground(False)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


class WidgetTabs(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.setGeometry(0,0,300,400)
        
        self.tab3 = RolesWidget()
        self.tab4 = ShortAnswersWidget()
        self.tab6 = SettingsWidget()
        
        self.addTab(self.tab3, 'Роли')
        self.addTab(self.tab4, 'Быстрые ответы')
        self.addTab(self.tab6, 'Настройки')
        
        self.setAutoFillBackground(False)
        
        
class RolesWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,300,230)
        self.setAutoFillBackground(True)
        self.setStyleSheet("""QFrame {background-color: rgb(16, 34, 36);}""")

        #elementsUI
        #list widget
        bg_container = """QFrame {background-color: rgb(16, 34, 36);}"""
        self.container = Container(self, 280, 360, 10, 7, bg_container)
        self.lst_widget = QListWidget(self.container)
        self.lst_widget.setGeometry(0, 0, 280, 360)
        self.add_roles()
        self.lst_widget.itemClicked.connect(self.copy_role)

    def add_roles(self):
        with open("content_docs/roles.txt", "r", encoding="utf-8") as file:
            for i in file.readlines():
                self.lst_widget.addItem(i)
        return 0
    
    def copy_role(self):
        index = self.lst_widget.currentRow()
        item = self.lst_widget.item(index)
        c_board.setText(item.text()[4:-1])
        
        return 0


class ShortAnswersWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,300,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-color: rgb(16, 34, 36);}""")

        #elementsUI
        #container
        bg_container = """QFrame {background-color: rgb(16, 34, 36);}"""
        self.container = Container(self, 280, 360, 10, 7, bg_container)
        #list_widget
        self.lst_answers = QListWidget(self.container)
        self.lst_answers.setGeometry(0,0,280,320)
        try:
            self.open_file()
            self.add_items()
            self.lst_answers.itemClicked.connect(self.get_answer)
        except FileNotFoundError:
            pass

        self.txt_answer = QTextEdit(self.container)
        self.txt_answer.setGeometry(0, 320, 280, 40)
        self.txt_answer.setPlaceholderText("View answer...")
        self.txt_answer.setStyleSheet("""QTextEdit {background-position: bottom;}""")

    def open_file(self):
        self.short_answers = {}
        with open('content_docs/short_answers.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                seek_phrase = list(line.split('::'))
                self.short_answers[seek_phrase[0]]=seek_phrase[1]

        return 0

    def add_items(self):
        for key in self.short_answers.keys():
            self.lst_answers.addItem(key)

        return 0

    def get_answer(self):
        index = self.lst_answers.currentRow()
        item = self.lst_answers.item(index)
        c_board.setText(self.short_answers[item.text()])
        self.txt_answer.setText(self.short_answers[item.text()])

        return 0
        
                 
class SettingsWidget(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0,0,300,230)
        self.setAutoFillBackground(False)
        self.setStyleSheet("""QFrame {background-color: rgb(16, 34, 36);}""")

        #elementsUI
        #container
        qss_container = """QFrame {background-color: rgb(16, 34, 36);}"""
        self.container = Container(self, 280, 190, 10, 7, qss_container)

        #check box
        self.app_upped = QCheckBox("Окно всегда сверху", self.container)
        self.app_upped.setGeometry(5, 5, 200, 20)
        self.app_upped.stateChanged.connect(self.window_up)

        #buttons
        self.btn_open_roles = QPushButton("Редактировать роли", self.container)
        self.btn_open_roles.setGeometry(5, 55, 125, 20)
        self.btn_open_roles.clicked.connect(lambda: self.start_file('roles.txt'))

        self.btn_open_answers = QPushButton("Редактировать ответы", self.container)
        self.btn_open_answers.setGeometry(5, 80, 125, 20)
        self.btn_open_answers.clicked.connect(lambda: self.start_file('short_answers.txt'))

        #urls
        self.btn_url_portal = QPushButton("URL Portal ics", self.container)
        self.btn_url_portal.setGeometry(135, 30, 80, 20)
        self.btn_url_portal.clicked.connect(lambda: self.open_url("https://portal24.itsperm.ru/"))

        self.btn_url_google_file = QPushButton("URL Google file", self.container)
        self.btn_url_google_file.setGeometry(135, 55, 80, 20)
        self.btn_url_google_file.clicked.connect(lambda: self.open_url("https://docs.google.com/spreadsheets/d/1IIEX6grQZHUpVGw1Qzi0xB2wqrLbEAHX9wEJ_TXgS44/edit#gid=84736261"))

        self.btn_url_sui = QPushButton("URL СУИ", self.container)
        self.btn_url_sui.setGeometry(135, 80, 80, 20)
        self.btn_url_sui.clicked.connect(lambda: self.open_url("https://sm.permkrai.ru/otrs/index.pl?Action=AgentDashboard"))

        self.btn_url_ats = QPushButton("URL ATS", self.container)
        self.btn_url_ats.setGeometry(135, 105, 80, 20)
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
