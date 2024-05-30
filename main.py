import cefr_check_utils
import data_utils
import readability_utils
import pandas as pd

from datetime import date

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QFileDialog
import sys

import readability_utils


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
        self.analyze_button.clicked.connect(self.analyze_text)

        self.analysis_label = QLabel(self)

        self.save_report_button = QPushButton(self)
        self.save_report_button.setText('Зберегти звіт')
        self.save_report_button.setHidden(True)
        self.save_report_button.clicked.connect(self.save_report_dialog)

        self.save_label = QLabel(self)
        self.save_label.setHidden(True)

        self.save_word_table_button = QPushButton(self)
        self.save_word_table_button.setText('Зберегти корпус слів')
        self.save_word_table_button.setHidden(True)
        self.save_word_table_button.clicked.connect(self.save_word_table_dialog)

        self.save_sentences_table_button = QPushButton(self)
        self.save_sentences_table_button.setText('Зберегти корпус речень')
        self.save_sentences_table_button.setHidden(True)
        self.save_sentences_table_button.clicked.connect(self.save_sentence_table_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.open_label)
        layout.addWidget(self.open_button)
        layout.addWidget(self.filename_label)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.analysis_label)
        layout.addWidget(self.save_report_button)
        layout.addWidget(self.save_label)
        layout.addWidget(self.save_word_table_button)

        container = QWidget(self)
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(
            self,
            "Оберіть текстовий файл",
            "",
            "Text files (*.txt)"
        )
        if filename[0]:
            global analyzed_text
            with open(filename[0], 'r', encoding='utf-8') as f:
                analyzed_text = f.read()
            self.filename_label.setText(filename[0])
            self.analyze_button.setEnabled(True)

    def save_report_dialog(self):
        global report
        filename = QFileDialog.getSaveFileName(
            self,
            "Оберіть місце збереження звіту",
            "",
            "Text files (*.txt)"
        )
        if filename[0]:
            with open(filename[0], 'w', encoding='utf-8') as f:
                f.write(report)
            self.save_label.setText(filename[0])
            self.save_label.setHidden(False)

    def save_word_table_dialog(self):
        filename = QFileDialog.getSaveFileName(
            self,
            "Оберіть місце збереження корпусу слів",
            "",
            "Table files (*.csv)"
        )
        if filename[0]:
            word_table.to_csv(filename[0])
            self.save_label.setText(filename[0])
            self.save_label.setHidden(False)

    def save_sentence_table_dialog(self):
        global sent_table
        filename = QFileDialog.getSaveFileName(
            self,
            "Оберіть місце збереження корпусу речень",
            "",
            "Table files (*.csv)"
        )
        if filename[0]:
            sent_table.to_csv(filename[0])
            self.save_label.setText(filename[0])
            self.save_label.setHidden(False)

    def analyze_text(self):
        global analyzed_text, \
            word_table, \
            sent_table, \
            ARI, \
            Flesch_Kincaid, \
            grammeme_level_interpretation, \
            report
        word_table = data_utils.create_word_table(analyzed_text)
        sent_table = data_utils.create_sentence_table(analyzed_text)
        ARI = readability_utils.interpret_ARI(readability_utils.ARI_index(
            len(sent_table),
            len(word_table),
            word_table['word_len'].sum()
        ))
        Flesch_Kincaid = readability_utils.interpret_Flesh_Kincaid_grade(readability_utils.Flesh_Kincaid_grade_level(
            len(sent_table),
            len(word_table),
            word_table['syllable_count'].sum()
        ))

        word_table = cefr_check_utils.check_grammemes_level(word_table)
        grammeme_level_interpretation = cefr_check_utils.interpret_cefr_list(word_table['cefr_level'])

        report = f'''
        ЗВІТ ПРО АНАЛІЗ
        РІВНЯ CEFR ТЕКСТУ
        Дата: {date.today().strftime('%Y-%m-%d')}
        Текст: {self.filename_label.text()}
        
        К-сть речень у тексті: {len(sent_table)}
        К-сть токенів у тексті: {len(word_table)}
        
        Рівень мови за ARI: {ARI}
        Рівень Flesch-Kincaid: {Flesch_Kincaid}
        Рівень за індексом грамем:
        - max: {grammeme_level_interpretation['max']}
        - avg: {grammeme_level_interpretation['avg']}
        - mode: {grammeme_level_interpretation['mode']}
        '''

        self.analysis_label.setText(report)

        self.save_report_button.setHidden(False)
        self.save_word_table_button.setHidden(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = window()

    window.show()

    app.exec()
