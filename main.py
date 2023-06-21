from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QInputDialog, QTextEdit, QLineEdit, QListWidget, QWidget, QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
app = QApplication([])
window1 = QWidget()
window2 = QWidget()
notes = []
window1.setWindowTitle('Умные заметки')
window2.setWindowTitle('Руководство')
list_tags = QListWidget()
text1 = QLabel('Для создания заметки нажмите на кнопку "Создать" и в окне напашите заметку')
text2 = QLabel('Для удаления заметки нажмите на неё в панеле "Сохраненные заметки" и нажмите на нее')
text3 = QLabel('Сохраненные заметки')
button1 = QPushButton('Создать')
button2 = QPushButton('Удалить')
button3 = QPushButton('Руководство')
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QVBoxLayout()
line6 = QVBoxLayout()
window1.setLayout(line3)
window2.setLayout(line4)
line4.addLayout(line5)
line5.addWidget(text1)
line5.addWidget(text2)
line3.addLayout(line1)
line3.addLayout(line2)
line1.addWidget(text3)
line2.addWidget(button3)
line2.addWidget(button2)
line2.addWidget(button1)
line1.addWidget(list_tags)
window1.show()
notes = []

def show_note():
    key = list_tags.selectedItems()[0].text()
    for note in notes:
        if note[0] == key:
            list_tags.addItems(note[2])

def add_note():
    note_name, ok = QInputDialog.getText(window1, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_tags.addItem(note[0])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')

def del_note():
    if list_tags.selectedItems():
        key = list_tags.selectedItems()[0].text()
        del notes[key]
        list_tags.clear()
        list_tags.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для удаления не выбрана!")


list_tags.itemClicked.connect(show_note)
button1.clicked.connect(add_note)
button2.clicked.connect(del_note)
button3.clicked.connect(window2.show)



app.exec_()