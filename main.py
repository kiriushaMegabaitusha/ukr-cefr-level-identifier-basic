import cefr_check_utils, data_utils, readability_utils

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout
import sys

app = QApplication(sys.argv)

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Аналізатор рівня УМІ')

        self.open_button = QPushButton(self)
        self.open_button.setText('Відкрити txt файл')

        self.open_label = QLabel(self)
        self.open_label.setText('Для початку роботи відкрийте файл із текстом, що аналізуватиметься.')

        layout = QVBoxLayout()
        layout.addWidget(self.open_label)
        layout.addWidget(self.open_button)


        container = QWidget(self)
        container.setLayout(layout)

        self.setCentralWidget(container)

window = window()

window.show()

app.exec()