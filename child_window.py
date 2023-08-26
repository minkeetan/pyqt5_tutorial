from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

child_windows = []  # List to hold references to child windows

class ChildWindow(QWidget):
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.setWindowTitle("Child Window")
        self.setGeometry(200, 200, 200, 100)

def create_child(label):
    child = ChildWindow(label)
    child.show()
    child_windows.append(child)  # Keep a reference to prevent garbage-collection

def show_label(label):
    label.setText("Child window is shown.")

def main():
    app = QApplication([])
    app.setStyle('Fusion')

    window = QWidget()
    main_layout = QHBoxLayout()

    # Left panel
    left_layout = QVBoxLayout()
    left_button1 = QPushButton("Create Child 1")
    left_button2 = QPushButton("Create Child 2")
    left_button3 = QPushButton("Create Child 3")

    left_button1.clicked.connect(lambda: create_child(middle_label1))
    left_button2.clicked.connect(lambda: create_child(middle_label2))
    left_button3.clicked.connect(lambda: create_child(middle_label3))

    left_layout.addWidget(left_button1)
    left_layout.addWidget(left_button2)
    left_layout.addWidget(left_button3)

    # Middle panel
    middle_layout = QVBoxLayout()
    middle_label1 = QLabel("Middle Label 1")
    middle_label2 = QLabel("Middle Label 2")
    middle_label3 = QLabel("Middle Label 3")
    middle_layout.addWidget(middle_label1)
    middle_layout.addWidget(middle_label2)
    middle_layout.addWidget(middle_label3)

    # Right panel
    right_layout = QVBoxLayout()
    right_button1 = QPushButton("Check Child 1")
    right_button1.clicked.connect(lambda: show_label(middle_label1))
    right_button2 = QPushButton("Check Child 2")
    right_button2.clicked.connect(lambda: show_label(middle_label2))
    right_button3 = QPushButton("Check Child 3")
    right_button3.clicked.connect(lambda: show_label(middle_label3))
    right_layout.addWidget(right_button1)
    right_layout.addWidget(right_button2)
    right_layout.addWidget(right_button3)

    # Add layouts to main layout
    main_layout.addLayout(left_layout)
    main_layout.addLayout(middle_layout)
    main_layout.addLayout(right_layout)

    window.setLayout(main_layout)
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()
