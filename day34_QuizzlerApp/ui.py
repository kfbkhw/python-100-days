from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, width=260, text="", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=20)

        true_img = PhotoImage(file="./images/true.png")
        self.true = Button(image=true_img, command=self.true_clicked, highlightbackground=THEME_COLOR)
        self.true.grid(column=1, row=3)

        false_img = PhotoImage(file="./images/false.png")
        self.false = Button(image=false_img, command=self.false_clicked, highlightbackground=THEME_COLOR)
        self.false.grid(column=2, row=3)

        self.new_q()

        self.window.mainloop()

    def new_q(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        if q_text == "~ End of the Quiz ~":
            self.true.config(state="disabled")
            self.false.config(state="disabled")
            self.window.after(2500, self.show_score)

    def true_clicked(self):
        correct = self.quiz.check_answer("True")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.feedback(correct)

    def false_clicked(self):
        correct = self.quiz.check_answer("False")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.feedback(correct)

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.new_q)

    def show_score(self):
        score = f"Final Score: {self.quiz.score}/{self.quiz.question_number}"
        self.canvas.itemconfig(self.question_text, text=score)
