from question_model import Question
import questions
from quiz_manager import QuizManager

question_bank = []
for data in questions.question_data:
    question_bank.append(Question(data["text"], data["answer"]))


manager = QuizManager(question_bank)

while manager.have_questions_check():
    manager.next_question()
    