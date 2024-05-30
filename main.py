import cefr_check_utils, data_utils, readability_utils

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QFileDialog
import sys

analyzed_text = ''

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Аналізатор рівня УМІ')

        self.open_button = QPushButton(self)
        self.open_button.setText('Відкрити txt файл')
        self.open_button.clicked.connect(self.open_file_dialog)

        self.open_label = QLabel(self)
        self.open_label.setText('Для початку роботи відкрийте файл із текстом, що аналізуватиметься.')

        self.filename_label = QLabel(self)

        self.analyze_button = QPushButton(self)
        self.analyze_button.setText('Аналізувати')
        self.analyze_button.setEnabled(False)

        self.analysis_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.open_label)
        layout.addWidget(self.open_button)
        layout.addWidget(self.filename_label)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.analysis_label)


        container = QWidget(self)
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(
            self,
            "Оберіть текстовий файл",
            '',
            "Text files (*.txt)"
        )
        if filename[0]:
            global analyzed_text
            with open(filename[0], 'r', encoding='utf-8') as f:
                analyzed_text = f.read()
            self.filename_label.setText(filename[0])
            self.analyze_button.setEnabled(True)







if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = window()

    window.show()

    app.exec()