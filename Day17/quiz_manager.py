class QuizManager:
    def __init__(self, question_list, question_number=0, score=0):
        self.question_number = question_number
        self.question_list = question_list
        self.score = score

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question.{self.question_number}: {current_question.question_text} (True/False)")
        self.check_answer(user_answer, current_question.question_answer)
        return

    def have_questions_check(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_question_answer):
        if user_answer.lower() == correct_question_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
            print(f"The correct answer was {correct_question_answer}")
        print(f"Score is {self.score}/{self.question_number}")
        print("\n")
