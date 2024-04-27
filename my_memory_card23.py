from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,  QGroupBox, QButtonGroup,QMessageBox
from random import shuffle, randint, choice
from PyQt5.QtGui import QFont

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def SendMessage():
    msg_win = QMessageBox()
    msg_win.setWindowTitle('предупед')
    msg_win.setText('Вы должны выбрать вариант ответа!')
    msg_win.exec_()
def  show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    RadioGroupBtns.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroupBtns.setExclusive(True)
    btn_ok.setText('Ответить')

def ask(q : Question):
    q_txt.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Ib_correct.setText(q.right_ans)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        mw.score += 1
    else:
        show_correct('Неправильно')
    print('Рейтинг', round(mw.score/mw.total*100,2),'%')
def show_correct(res):
    if res == 'Правильно':
        Ib_result.setStyleSheet('color:rgb(10, 190, 10)')
    else:
        Ib_result.setStyleSheet('color:rgb(190, 10, 10)')
    Ib_result.setText(res)
    show_result()       
def next_question():
    mw.total += 1
    cur_question = choice(q_ls)
    q_ls.remove(cur_question)
    if len(q_ls) <= 0:
        for q in questions:
            q_ls.append(q)
        print('Заново')      
    ask(cur_question)
def click_ok():
    if answers[0].isChecked() or answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        if btn_ok.text() == 'Ответить':
            check_answer()
        else:
            next_question()
    else:
        SendMessage()

questions = []
q_ls = []
questions.append(Question('В каком году созадл алгоритмика', '2016', '2010', '2017', '2018'))
questions.append(Question('2+2', '4', '5000', '5', '2'))
questions.append(Question('Температура плавления свинца', '327,5°C', '1749°C.', '758,6°C', '453°C'))
questions.append(Question('Самый плотный метал', 'Осмий', 'Платина', 'золото', 'Титан'))
questions.append(Question('Самый Твердый материал', 'Алмаз', 'Платина', 'Осмий', 'Титан'))
for q in questions:
    q_ls.append(q)
app = QApplication([])
mw = QWidget()
mw.total = 0
mw.score = 0
font = QFont('Times', 20, QFont.Bold)
mw.setWindowTitle('Memory Card')
mw.resize(250,200)
q_txt = QLabel('В каком году создали алгоритмика')
RadioGroupBox = QGroupBox()
RadioGroupBtns = QButtonGroup()
rbtn1 = QRadioButton('2017')
rbtn2 = QRadioButton('2022')
rbtn3 = QRadioButton('2016')
rbtn4 = QRadioButton('2015')
answers = [rbtn1, rbtn2, rbtn3, rbtn4]
RadioGroupBtns.addButton(rbtn1)
RadioGroupBtns.addButton(rbtn2)
RadioGroupBtns.addButton(rbtn3)
RadioGroupBtns.addButton(rbtn4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3= QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
Ib_result = QLabel('Правильно/Неправильно')
Ib_correct = QLabel('Сам ответ')
Ib_correct.setFont(font)
layout_res = QVBoxLayout()
layout_res.addWidget(Ib_result, alignment=(Qt.AlignLeft| Qt.AlignTop))
layout_res.addWidget(Ib_correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
btn_ok = QPushButton('Ответить')
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(q_txt, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
mw.setLayout(layout_card)
btn_ok.clicked.connect(click_ok)
ask(Question('В каком году созадл алгоритмика', '2016', '2010', '2017', '2018'))
next_question()
mw.show()
app.exec_()
