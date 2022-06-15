from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q = i['text']
    a = i['answer']
    question_bank.append(Question(q, a))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    a = quiz.next_question()
    quiz.check_answer(a)

