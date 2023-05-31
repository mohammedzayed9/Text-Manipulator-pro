import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QInputDialog
import re


class TextManipulatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Manipulator App')
        self.resize(600, 400)

        self.input_label = QLabel('Input Text:')
        self.input_textedit = QTextEdit()
        self.manipulation_label = QLabel('Select Manipulation:')
        self.manipulation_combobox = QComboBox()
        self.manipulation_combobox.addItem('Uppercase Transformation')
        self.manipulation_combobox.addItem('Lowercase Transformation')
        self.manipulation_combobox.addItem('Remove Whitespace')
        self.manipulation_combobox.addItem('Capitalize First Letter')
        self.manipulation_combobox.addItem('Sort Lines Alphabetically')
        self.manipulation_combobox.addItem('Remove Duplicates')
        self.manipulation_combobox.addItem('Shuffle Lines Randomly')
        self.manipulation_combobox.addItem('Count Words')
        self.manipulation_combobox.addItem('Find and Replace Text')
        self.manipulation_combobox.addItem('Add Prefix to Lines')
        self.manipulation_combobox.addItem('Add Suffix to Lines')
        self.manipulation_combobox.addItem('Add Prefix and Suffix to All Lines')
        self.manipulation_combobox.addItem('Delimited Column Extractor')
        self.manipulation_combobox.addItem('Upper Case Converter')
        self.manipulation_combobox.addItem('Lower Case Converter')
        self.manipulation_combobox.addItem('Title Case Converter')
        self.manipulation_combobox.addItem('Sentence Case Converter')
        self.manipulation_combobox.addItem('Pascal Case Converter')
        self.manipulation_combobox.addItem('Camel Case Converter')
        self.manipulation_combobox.addItem('Remove Empty Lines')
        self.manipulation_combobox.addItem('Remove Leading/Trailing Spaces')
        self.manipulation_combobox.addItem('Remove Leading Spaces')
        self.manipulation_combobox.addItem('Remove Trailing Spaces')
        self.manipulation_combobox.addItem('Disemvowel Tool')
        self.manipulation_combobox.addItem('Reverse Text Generator')
        self.manipulation_combobox.addItem('Number Each Line')
        self.manipulation_combobox.addItem('Number Each Line (Zero-based)')
        self.manipulation_combobox.addItem('Add Line Breaks')
        self.manipulation_combobox.addItem('Word-Wrap')
        self.manipulation_combobox.addItem('Remove Line Breaks')
        self.manipulation_combobox.addItem('Convert Tabs to Spaces')
        self.manipulation_combobox.addItem('Convert Spaces to Tabs')
        self.manipulation_combobox.addItem('Concatenate Text')
        self.manipulation_combobox.addItem('Remove Smart Quotes')
        self.manipulation_combobox.addItem('Count Letters')
        self.manipulation_combobox.addItem('Count Rows')
        self.manipulation_combobox.addItem('Create/remove line breaks')
        self.manipulation_combobox.addItem('Insert prefix and/or suffix into each line/item')
        self.manipulation_combobox.addItem('Join text lines, side by side')
        self.manipulation_combobox.addItem('Remove blank lines')
        self.manipulation_combobox.addItem('Remove duplicate lines/items')
        self.manipulation_combobox.addItem('Remove lines/items containing...')
        self.manipulation_combobox.addItem('Remove unwanted line numbers')

        self.manipulate_button = QPushButton('Manipulate Text')
        self.output_label = QLabel('Manipulated Text:')
        self.output_textedit = QTextEdit()
        self.copy_button = QPushButton('Copy to Clipboard')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_textedit)

        manipulation_layout = QHBoxLayout()
        manipulation_layout.addWidget(self.manipulation_label)
        manipulation_layout.addWidget(self.manipulation_combobox)

        input_manipulation_layout = QVBoxLayout()
        input_manipulation_layout.addLayout(input_layout)
        input_manipulation_layout.addLayout(manipulation_layout)

        layout.addLayout(input_manipulation_layout)
        layout.addWidget(self.manipulate_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_textedit)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

        self.manipulate_button.clicked.connect(self.manipulate_text)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

    def manipulate_text(self):
        text = self.input_textedit.toPlainText()
        manipulation = self.manipulation_combobox.currentText()

        manipulated_text = self.process_manipulation(text, manipulation)
        self.output_textedit.setPlainText(manipulated_text)

    def process_manipulation(self, text, manipulation):
       try:
        if manipulation == 'Uppercase Transformation':
            return text.upper()
        elif manipulation == 'Lowercase Transformation':
            return text.lower()
        elif manipulation == 'Remove Whitespace':
            return re.sub(r'\s+', '', text)
        elif manipulation == 'Capitalize First Letter':
            return text.capitalize()
        elif manipulation == 'Sort Lines Alphabetically':
            lines = text.split('\n')
            sorted_lines = sorted(lines)
            return '\n'.join(sorted_lines)
        elif manipulation == 'Remove Duplicates':
            lines = text.split('\n')
            unique_lines = list(set(lines))
            return '\n'.join(unique_lines)
        elif manipulation == 'Shuffle Lines Randomly':
            lines = text.split('\n')
            import random
            random.shuffle(lines)
            return '\n'.join(lines)
        elif manipulation == 'Count Words':
            words = text.split()
            word_count = len(words)
            return f'Total words: {word_count}'
        elif manipulation == 'Find and Replace Text':
            find_text, ok1 = QInputDialog.getText(self, 'Find Text', 'Enter the text to find:')
            replace_text, ok2 = QInputDialog.getText(self, 'Replace Text', 'Enter the replacement text:')
            if ok1 and ok2:
                replaced_text = text.replace(find_text, replace_text)
                return replaced_text
            else:
                return text
        elif manipulation == 'Add Prefix to Lines':
            prefix, ok = QInputDialog.getText(self, 'Add Prefix', 'Enter the prefix:')
            if ok:
                lines = text.split('\n')
                prefixed_lines = [f'{prefix}{line}' for line in lines]
                return '\n'.join(prefixed_lines)
            else:
                return text
        elif manipulation == 'Add Suffix to Lines':
            suffix, ok = QInputDialog.getText(self, 'Add Suffix', 'Enter the suffix:')
            if ok:
                lines = text.split('\n')
                suffixed_lines = [f'{line}{suffix}' for line in lines]
                return '\n'.join(suffixed_lines)
            else:
                return text
        elif manipulation == 'Add Prefix and Suffix to All Lines':
            prefix, ok1 = QInputDialog.getText(self, 'Add Prefix', 'Enter the prefix:')
            suffix, ok2 = QInputDialog.getText(self, 'Add Suffix', 'Enter the suffix:')
            if ok1 and ok2:
                lines = text.split('\n')
                prefixed_suffixed_lines = [f'{prefix}{line}{suffix}' for line in lines]
                return '\n'.join(prefixed_suffixed_lines)
            else:
                return text
        elif manipulation == 'Delimited Column Extractor':
            delimiter, ok = QInputDialog.getText(self, 'Delimited Column Extractor', 'Enter the delimiter:')
            if ok:
                lines = text.split('\n')
                extracted_columns = []
                for line in lines:
                    columns = line.split(delimiter)
                    extracted_columns.append(columns)
                return '\n'.join([delimiter.join(columns) for columns in extracted_columns])
        elif manipulation == 'Upper Case Converter':
            return text.upper()
        elif manipulation == 'Lower Case Converter':
            return text.lower()
        elif manipulation == 'Title Case Converter':
            return text.title()
        elif manipulation == 'Sentence Case Converter':
            return '. '.join(sentence.capitalize() for sentence in re.split(r'(?<=[.!?])\s+', text))
        elif manipulation == 'Pascal Case Converter':
            words = re.findall(r'\b\w+\b', text)
            return ''.join(word.capitalize() for word in words)
        elif manipulation == 'Camel Case Converter':
            words = re.findall(r'\b\w+\b', text)
            return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        elif manipulation == 'Remove Empty Lines':
            lines = text.split('\n')
            non_empty_lines = [line for line in lines if line.strip()]
            return '\n'.join(non_empty_lines)
        elif manipulation == 'Remove Leading/Trailing Spaces':
            lines = text.split('\n')
            trimmed_lines = [line.strip() for line in lines]
            return '\n'.join(trimmed_lines)
        elif manipulation == 'Remove Leading Spaces':
            lines = text.split('\n')
            trimmed_lines = [re.sub(r'^\s+', '', line) for line in lines]
            return '\n'.join(trimmed_lines)
        elif manipulation == 'Remove Trailing Spaces':
            lines = text.split('\n')
            trimmed_lines = [re.sub(r'\s+$', '', line) for line in lines]
            return '\n'.join(trimmed_lines)
        elif manipulation == 'Disemvowel Tool':
            vowels = 'aeiouAEIOU'
            return ''.join(char for char in text if char not in vowels)
        elif manipulation == 'Reverse Text Generator':
            return text[::-1]
        elif manipulation == 'Number Each Line':
            lines = text.split('\n')
            numbered_lines = [f'{i + 1}. {line}' for i, line in enumerate(lines)]
            return '\n'.join(numbered_lines)
        elif manipulation == 'Number Each Line (Zero-based)':
            lines = text.split('\n')
            numbered_lines = [f'{i}. {line}' for i, line in enumerate(lines)]
            return '\n'.join(numbered_lines)
        elif manipulation == 'Add Line Breaks':
            search_string, ok = QInputDialog.getText(self, 'Add Line Breaks', 'Enter the search string:')
            if ok:
                add_before = QMessageBox.question(self, 'Add Line Breaks', 'Add line break before the search string?',
                                                   QMessageBox.Yes | QMessageBox.No)
                add_after = QMessageBox.question(self, 'Add Line Breaks', 'Add line break after the search string?',
                                                  QMessageBox.Yes | QMessageBox.No)
                new_line = QMessageBox.question(self, 'Add Line Breaks',
                                                 'Replace line breaks with a specific string?', QMessageBox.Yes | QMessageBox.No)

                if add_before == QMessageBox.Yes:
                    text = text.replace(search_string, f'\n{search_string}')
                if add_after == QMessageBox.Yes:
                    text = text.replace(search_string, f'{search_string}\n')
                if new_line == QMessageBox.Yes:
                    new_line_string, ok = QInputDialog.getText(self, 'Add Line Breaks',
                                                                 'Enter the string to replace line breaks with:')
                    if ok:
                        text = text.replace('\n', new_line_string)

                return text
            else:
                return text
        elif manipulation == 'Word-Wrap':
            column_width, ok = QInputDialog.getInt(self, 'Word-Wrap', 'Enter the column width:')
            if ok:
                words = text.split()
                lines = []
                current_line = ''
                for word in words:
                    if len(current_line) + len(word) <= column_width:
                        current_line += word + ' '
                    else:
                        lines.append(current_line.strip())
                        current_line = word + ' '
                lines.append(current_line.strip())
                return '\n'.join(lines)
            else:
                return text
        elif manipulation == 'Remove Line Breaks':
            return text.replace('\n', '')
        elif manipulation == 'Convert Tabs to Spaces':
            num_spaces, ok = QInputDialog.getInt(self, 'Convert Tabs to Spaces', 'Enter the number of spaces per tab:')
            if ok:
                return text.replace('\t', ' ' * num_spaces)
            else:
                return text
        elif manipulation == 'Convert Spaces to Tabs':
            num_spaces, ok = QInputDialog.getInt(self, 'Convert Spaces to Tabs', 'Enter the number of spaces per tab:')
            if ok:
                return text.replace(' ' * num_spaces, '\t')
            else:
                return text
        elif manipulation == 'Concatenate Text':
            delimiter, ok = QInputDialog.getText(self, 'Concatenate Text', 'Enter the delimiter:')
            if ok:
                lines = text.split('\n')
                concatenated_text = delimiter.join(lines)
                return concatenated_text
            else:
                return text
        elif manipulation == 'Remove Smart Quotes':
            smart_quotes = {
                '“': '"',
                '”': '"',
                '‘': "'",
                '’': "'"
            }
            for smart_quote, straight_quote in smart_quotes.items():
                text = text.replace(smart_quote, straight_quote)
            return text
        elif manipulation == 'Count Letters':
            return f'Total letters: {len(text)}'
        elif manipulation == 'Count Rows':
            lines = text.split('\n')
            row_count = len(lines)
            return f'Total rows: {row_count}'
        elif manipulation == 'Create/remove line breaks':
            search_string, ok = QInputDialog.getText(self, 'Create/Remove Line Breaks',
                                                     'Enter the search string:')
            if ok:
                create_line_breaks = QMessageBox.question(self, 'Create/Remove Line Breaks',
                                                           'Create new line breaks?', QMessageBox.Yes | QMessageBox.No)
                remove_line_breaks = QMessageBox.question(self, 'Create/Remove Line Breaks',
                                                           'Remove existing line breaks?', QMessageBox.Yes | QMessageBox.No)
                replace_line_breaks = QMessageBox.question(self, 'Create/Remove Line Breaks',
                                                            'Replace line breaks with a specific string?',
                                                            QMessageBox.Yes | QMessageBox.No)
                if create_line_breaks == QMessageBox.Yes:
                    text = text.replace(search_string, f'\n{search_string}')
                if remove_line_breaks == QMessageBox.Yes:
                    text = text.replace('\n', '')
                if replace_line_breaks == QMessageBox.Yes:
                    new_line_string, ok = QInputDialog.getText(self, 'Create/Remove Line Breaks',
                                                                 'Enter the string to replace line breaks with:')
                    if ok:
                        text = text.replace('\n', new_line_string)
                return text
            else:
                return text
        elif manipulation == 'Insert Prefix and/or Suffix into each line/item':
            prefix, ok1 = QInputDialog.getText(self, 'Insert Prefix and/or Suffix',
                                                'Enter the prefix (leave empty to skip):')
            suffix, ok2 = QInputDialog.getText(self, 'Insert Prefix and/or Suffix',
                                                'Enter the suffix (leave empty to skip):')
            if ok1 and ok2:
                lines = text.split('\n')
                modified_lines = [f'{prefix}{line}{suffix}' for line in lines]
                return '\n'.join(modified_lines)
            else:
                return text
        elif manipulation == 'Join Text Lines, Side by Side':
            delimiter, ok = QInputDialog.getText(self, 'Join Text Lines', 'Enter the delimiter:')
            if ok:
                lines = text.split('\n')
                joined_lines = [line.strip() for line in lines]
                return delimiter.join(joined_lines)
            else:
                return text
        elif manipulation == 'Number Each Line/Item':
            lines = text.split('\n')
            numbered_lines = [f'{i + 1}. {line}' for i, line in enumerate(lines)]
            return '\n'.join(numbered_lines)
        elif manipulation == 'Remove Blank Lines':
            lines = text.split('\n')
            non_blank_lines = [line for line in lines if line.strip()]
            return '\n'.join(non_blank_lines)
        elif manipulation == 'Remove Duplicate Lines/Items':
            lines = text.split('\n')
            unique_lines = list(set(lines))
            return '\n'.join(unique_lines)
        elif manipulation == 'Remove Lines/Items Containing...':
            search_string, ok = QInputDialog.getText(self, 'Remove Lines/Items Containing...',
                                                     'Enter the search string:')
            if ok:
                lines = text.split('\n')
                filtered_lines = [line for line in lines if search_string not in line]
                return '\n'.join(filtered_lines)
            else:
                return text
        elif manipulation == 'Remove Lines/Items Not Containing...':
            search_string, ok = QInputDialog.getText(self, 'Remove Lines/Items Not Containing...',
                                                     'Enter the search string:')
            if ok:
                lines = text.split('\n')
                filtered_lines = [line for line in lines if search_string in line]
                return '\n'.join(filtered_lines)
            else:
                return text
        elif manipulation == 'Remove Unwanted Line Numbers':
            lines = text.split('\n')
            modified_lines = [re.sub(r'^\d+\.\s', '', line) for line in lines]
            return '\n'.join(modified_lines)
        else:
            return text
       except Exception as e:
           QMessageBox.critical(self, str(e))
    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_textedit.toPlainText())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    text_manipulator = TextManipulatorApp()
    text_manipulator.show()
    sys.exit(app.exec_())
