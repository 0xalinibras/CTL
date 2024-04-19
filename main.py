from src.app import *
from PyQt5 import QtWidgets
from itertools import product
import string
import sys



#Create App
app = QtWidgets.QApplication(sys.argv)

#Create Main Window
Win_Main = QtWidgets.QMainWindow()
ui = Ui_Win_Main()
ui.setupUi(Win_Main)
Win_Main.show()


def start():
    min_len = ui.minimum_txt.text()
    max_len = ui.maximum_txt.text()
    type = ui.type_txt.currentText()
    cou = 0
    if type == "Number":
        character = "1234567890"
    elif type == "Marks":
        character = "~!@#$%^&*()-_=+\|}{][:;?/>.<,"
    elif type == "Charaters":
        character = "abcdefghijklmnopqrstuvwxyz"

    path = f"src/wordlist/{type}({min_len}-{max_len}).txt"
    file = open(path,"w")

    for i  in range(int(min_len),int(max_len)+1):
        for j in product(character,repeat=i):
            word = "".join(j)
            file.write(word)
            file.write("\n")
            cou += 1
            print(word)
    print("Create List of {}".format(cou))
ui.Start_btn.clicked.connect(start)
sys.exit(app.exec_())