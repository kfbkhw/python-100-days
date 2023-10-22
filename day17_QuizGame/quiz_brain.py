class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {q.text}\nTrue/False: ").lower()
        self.check_answer(user_answer, q.answer.lower())

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def quiz_complete(self):
        print("\nYou've completed the quiz.")
        print(f"Your final score is {self.score}/{self.question_number}\n")
