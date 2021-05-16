from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
    
app = QApplication([])
window = QWidget()
text = QTextEdit()
zamet = QListWidget()
teg = QListWidget()
sozz = QPushButton("Создать заметку")
delz = QPushButton("Удалить заметку")
sohz = QPushButton("Сохранить заметку")
dobz = QPushButton("Добавить заметку")
otz = QPushButton("Открыть от заметки")
iskz = QPushButton("Искать заметки по тегу")

spisokz = QLabel("Список заметок")
spisokt = QLabel("Список тегов")
vodt = QLineEdit()

linii1 = QVBoxLayout()
linii2 = QVBoxLayout()
linii3 = QHBoxLayout()

linii1.addWidget(text)
linii2.addWidget(spisokz)
linii2.addWidget(zamet)
linii2.addWidget(sozz)
linii2.addWidget(delz)
linii2.addWidget(sohz)
linii2.addWidget(sohz)
linii2.addWidget(spisokt)
linii2.addWidget(teg) 
linii2.addWidget(dobz)
linii2.addWidget(otz)
linii2.addWidget(iskz)

linii3.addLayout(linii1)
linii3.addLayout(linii2)
window.setLayout(linii3)
with open("data.json","r") as file:
    notes = json.load(file)
zamet.addItems(notes)

window.show()
app.exec_()