#!python
import sys

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VerticalLabel(QLabel):

    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        self.setFixedSize(30, 100)

        painter = QtGui.QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        painter.drawText(0, self.width() / 2, self.text())
        painter.end()


def window():
    app = QApplication(sys.argv)
    w = QWidget()


    #Layout = QVBoxLayout()
    #mainw.setLayout(Layout)
    Title = "Teste de Personalidade do Tipo D"
    b = QLabel(w)
    b.setText(Title)
    b.move(10,20)

    #mainw.setGeometry(1,1,800,800)
    w.setWindowTitle(Title)

    buttonGroups = []
    allCH = []
    questions = load_questions("typeD_questions.txt")

    QY = 120
    draw_option_information(w, QY)
    for q, question in enumerate(questions):
        group, boxes = make_question(w, question, QY + q * 16)
        buttonGroups.append(group)
        allCH += boxes


    ok = QPushButton("Calcular", w)
    ok.move(150, QY + len(questions) * 16 + 60)

    result = QLabel(w)
    result.setFixedSize(900, 300)
    result.move(80,430)

    def show_results():
        res = read_results(buttonGroups)

        m = result_message(res)
        result.setText(m)

    ok.clicked.connect(show_results)

    #w.setCentralWidget(mainw)
    w.show()


    sys.exit(app.exec_())


def draw_option_information(win, Y):
    options = ["FALSE", "RATHER FALSE", "NEUTRAL", "RATHER TRUE", "TRUE"]
    for i, V in enumerate(options):
        r = VerticalLabel(V, win)

        r.move(598 + i * 15, Y - 105)


def make_question(win, text, Y):
    #question = QWidget(win)
    #question.setLayout(win)
    q = QLabel(win)

    q.setText(text)
    q.move(50, Y)

    boxes = []
    group = QButtonGroup(win)
    for i in range(5):
        chk = QRadioButton(win)
        chk.ID = i
        chk.move(600 + i * 15, Y)
        boxes.append(chk)
        group.addButton(chk)

    return group, boxes

def load_questions(fpath):
    with open(fpath) as f:
        return f.readlines()

def read_results(groups):
    def read_group(group):
        res = group.checkedButton()
        if res is not None:
            return res.ID
    return [
        read_group(g) for g in groups
    ]


def typeD_interprete_results(R):
    def flip(v):
        return 4 - v
    R[0] = flip(R[0])
    R[2] = flip(R[2])

    indexes = { # 1 INDEXED!
        "NA": [2, 4, 5, 7, 9, 12, 13],
        "SI": [1, 3, 6, 8, 10, 11, 14]
    }

    return {
        l: sum([R[x - 1] for x in V])
        for (l, V) in indexes.items()
    }


def result_message(results):
    if None in results:
        return "Você deixou alguma questão em branco :{"
    else:
        res = typeD_interprete_results(results)

        base = f"""Sua pontuação é:
        Afeição Negativa: {res['NA']}
        Inibição Social: {res['SI']}
        """

        if res['NA'] < 10 and res['SI'] < 10:
            extra = "Parabéns, como você ficou abaixo dos 10 pontos em cada um dos critérios,\n   sua personalidade não é a do tipo D 😀"

        elif res['NA'] >= 10 and res['SI'] >= 10:
            extra = """Que pena, você ultrapassou os 10 pontos em ambos os critérios:
            Você possui a personalidade tipo D.
            Por favor, não fique (ainda mais) tristi 😱😳"""

        else:
            extra = "Você ultrapassou os 10 pontos em apenas um critério: Não possui a personalidade tipo D, mas está quase lá."

        return base + extra


def main():
    window()


if __name__ == '__main__':
   main()


