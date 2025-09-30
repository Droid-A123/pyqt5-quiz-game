import sys
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class quizGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz Game")
        self.setGeometry(200, 200, 600, 400)
        self.setWindowIcon(QIcon("download.jpeg"))

        self.questions = [
            {"question": "What is the capital of France?",
             "options": ["Berlin", "Madrid", "Paris", "Rome"],
             "answer": "Paris"},
            {"question": "Which language is used for web apps?",
             "options": ["Python", "JavaScript", "C++", "Java"],
             "answer": "JavaScript"},
            {"question": "Who developed Python?",
             "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
             "answer": "Guido van Rossum"}
        ]

        self.current_question = 0
        self.score = 0

        self.layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.current_question]["question"])
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #09ff00;   /* neon green */
            margin: 15px;
        """)
        self.layout.addWidget(self.question_label)

        self.buttons = []
        for option in self.questions[self.current_question]["options"]:
            btn = QPushButton(option)
            btn.clicked.connect(self.check_answer)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #000000;
                    color: #09ff00;
                    font-size: 22px;
                    border: 2px solid #09ff00;
                    border-radius: 8px;
                    padding: 12px;
                    margin: 5px;
                }
                QPushButton:hover {
                    background-color: #038a2d;
                }
                QPushButton:pressed {
                    background-color: #3d3d3d;
                }
            """)
            self.layout.addWidget(btn)
            self.buttons.append(btn)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-size: 18px;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1e8449;
            }
            QPushButton:pressed {
                background-color: #145a32;
            }
        """)
        self.layout.addWidget(self.next_button)


        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #000000;")

    def check_answer(self):
        sender = self.sender()
        msg = QMessageBox(self)
        msg.setWindowTitle("Result")
        self.setWindowIcon(QIcon("download.jpeg"))
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #000000;
            }
            QLabel {
                color: #09ff00;   /* force neon green for text */
                font-size: 18px;
            }
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-size: 14px;
                border-radius: 6px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #1e8449;
            }
        """)

        if sender.text() == self.questions[self.current_question]["answer"]:
            msg.setInformativeText("😀 Correct! You got it right!") 
            self.score += 1
        else:
            msg.setInformativeText("😥 Wrong answer! Try again.")

        msg.exec_()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.setText(self.questions[self.current_question]["question"])
            options = self.questions[self.current_question]["options"]
            for i, btn in enumerate(self.buttons):
                btn.setText(options[i])
        else:
            self.show_game_over()

    def show_game_over(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        game_over_label = QLabel("GAME OVER")
        game_over_label.setAlignment(Qt.AlignCenter)
        game_over_label.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: #ff0000;  /* red */
            margin: 20px;
        """)
        self.layout.addWidget(game_over_label)

        score_label = QLabel(f"Your Score: {self.score}/{len(self.questions)}")
        score_label.setAlignment(Qt.AlignCenter)
        score_label.setStyleSheet("""
            font-size: 24px;
            color: #09ff00;  /* neon green */
            margin: 15px;
        """)
        self.layout.addWidget(score_label)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        exit_button.setStyleSheet("""
            QPushButton {
                background-color: #c0392b;
                color: white;
                font-size: 18px;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #922b21;
            }
            QPushButton:pressed {
                background-color: #641e16;
            }
        """)
        self.layout.addWidget(exit_button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = quizGame()
    window.show()
    sys.exit(app.exec_())
