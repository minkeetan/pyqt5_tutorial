from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,200,300,300) # sets the windows x, y, width, height
    win.setWindowTitle("My first window!") # setting the window title

    label = QLabel(win)
    label.setText("my first label")
    label.move(50, 50)  # x, y from top left hand corner.
    
    win.show()
    sys.exit(app.exec_())

main()