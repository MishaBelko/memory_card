#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QMessageBox, QButtonGroup
from random import shuffle, randint
class Questions():
    def __init__(self, question, right_answer, no_ans1, no_ans2, no_ans3):
        self.question = question
        self.right_answer = right_answer
        self.no_ans1 = no_ans1
        self.no_ans2 = no_ans2
        self.no_ans3 = no_ans3

questions_list = [] 
questions_list.append(Questions('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Questions('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Questions('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

points = 0
question_count = 0

app = QApplication([])

main_win = QWidget()

main_win.resize(400, 300)

Lb_Question = QLabel('Самый сложный вопрос в мире!')
answer = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
Lb_Result = QLabel('прав ты или нет?')
Lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(Lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

ResultGroupBox = QGroupBox('Результат тестирования')
Lb_Result_Test = QLabel('')

layout_test_res = QVBoxLayout()
layout_test_res.addWidget(Lb_Result_Test)
ResultGroupBox.setLayout(layout_test_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_main = QVBoxLayout()

layout_line1.addWidget(Lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(ResultGroupBox)
AnsGroupBox.hide()
ResultGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(answer, stretch=2)
layout_line3.addStretch(1)

layout_main.addLayout(layout_line1, stretch=2)
layout_main.addLayout(layout_line2, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch=1)
layout_main.addStretch(1)

main_win.cur_question = -1 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.no_ans1)
    answers[2].setText(q.no_ans2)
    answers[3].setText(q.no_ans3)
    Lb_Question.setText(q.Questions)
    Lb_Correct.setText(q.right_answer)
    questions_list.remove(q)
    show_question()  

def show_correct(res):
    Lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        points += 1
        question_count += 1
        show_correct('Правильно! У вас ', str(points),'очко(в)')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    if len(questions_list) == 0:
        show_test_result()
    main_win.cur_question = randint(0, len(Questions_list)-1)
    q = Questions_list[main_win.cur_question]
    ask(q)

def show_test_result():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    Lb_Result_Test.setText()

def start_test():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

answer.clicked.connect(start_test)

main_win.setLayout(layout_main)
main_win.show()
main_win.setWindowTitle('Memo Card')
main_win.cur_question = -1 
app.exec_()