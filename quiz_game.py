import json

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.correct = 0
        self.data_size = len(question)
        self.run_quiz()

    def run_quiz(self):
        for q_no in range(self.data_size):
            print(f"Q{q_no + 1}: {question[q_no]}")
            for idx, option in enumerate(options[q_no], 1):
                print(f"{idx}. {option}")
            answer = input("Votre réponse (1-4): ")
            if self.check_ans(q_no, int(answer)):
                self.correct += 1
            print("\n")
        self.display_result()

    def check_ans(self, q_no, answer):
        return answer == answers[q_no]

    def display_result(self):
        wrong_count = self.data_size - self.correct
        score = int(self.correct / self.data_size * 100)
        print(f"Score: {score}%")
        print(f"Correctes: {self.correct}")
        print(f"Incorrectes: {wrong_count}")

with open('data.json') as f:
    data = json.load(f)

question = data['question']
options = data['options']
answers = data['answer']

quiz = Quiz()
