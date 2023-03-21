class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        no_of_questions = len(self.question_list)
        return self.question_number < no_of_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right.")
            self.score += 1
        else:
            print("You're Wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"You're score is {self.score}/{self.question_number}")
        print("\n")

# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

4
# print(question_bank[0].text)
