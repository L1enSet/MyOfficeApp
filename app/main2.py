#developer L1enSet 27/03/2023

from PyQt5.QtWidgets import QTabWidget

class MainWindow(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        self.setGeometry(100,100,400,200)
        self.setWindowTitle("MyOffice2.0")
        #self.setWindowFlags(

        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
