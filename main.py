from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QInputDialog, QTextEdit, QLineEdit, QListWidget, QWidget, QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
app = QApplication([])
window = QWidget()
notes = []
window.setWindowTitle('Умные заметки')
texted = QTextEdit()
list_tags = QListWidget()
text1 = QLabel('Текстовое поле')
text2 = QLabel('Сохраненные заметки')
button1 = QPushButton('Создать')
button2 = QPushButton('Удалить')
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
window.setLayout(line3)
line3.addLayout(line1)
line3.addLayout(line2)
line1.addWidget(text1)
line1.addWidget(texted)
line1.addWidget(button1)
line2.addWidget(text2)
line2.addWidget(list_tags)
line2.addWidget(button2)
window.show()
app.exec_()



def show_note():
    key = list_tags_left.selectedItems()[0].text()
    for note in notes:
        if note[0] == key:
            texted.setText(note[1])
            list_tags_right.clear()
            list_tags_right.addItems(note[2])


def add_note():
    note_name, ok = QInputDialog.getText(window, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_tags_left.addItem(note[0])
        list_tags_right.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')


def save_note():
    if list_tags_left.selectedItems():
        key = list_tags_left.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = texted.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
        
    else:
        print("Заметка для сохранения не выбрана!")
def del_note():
    if list_tags_left.selectedItems():
        key = list_tags_left.selectedItems()[0].text()
        del notes[key]
        list_tags_left.clear()
        list_tags_right.clear()
        lineed.clear()
        list_tags_left.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для удаления не выбрана!")

list_tags_left.itemClicked.connect(show_note)
button1.clicked.connect(save_note)