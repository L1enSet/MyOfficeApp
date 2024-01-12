import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame
from PyQt5.QtCore import Qt, QPoint


class GameWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)

		self.setGeometry(250, 200, 400, 400)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	root = GameWindow()
	root.show()
	sys.exit(app.exec_())