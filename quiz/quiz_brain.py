class QuizBrain:

    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, a):

        if a == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("You got it wrong.")
        print(f"The correct answer is {self.question_list[self.question_number].answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}.\n\n")
        self.question_number += 1

    def next_question(self):
        a = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)").lower()
        return a
