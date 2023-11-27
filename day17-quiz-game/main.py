from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()

for item in question_data:
    q_text = item["text"]
    q_answer = item["answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_question()
quiz.quiz_complete()
