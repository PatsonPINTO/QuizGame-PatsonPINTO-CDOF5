import json

class Quiz:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers
        self.q_no = 0
        self.correct = 0
        self.data_size = len(questions)
        self.run_quiz()

    def run_quiz(self):
        for q_no in range(self.data_size):
            print(f"Q{q_no + 1}: {self.questions[q_no]}")
            for idx, option in enumerate(self.options[q_no], 1):
                print(f"{idx}. {option}")
            while True:
                try:
                    answer = int(input("Votre réponse (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("Veuillez entrer un nombre entre 1 et 4.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            if self.check_ans(q_no, answer):
                self.correct += 1
            print("\n")
        self.display_result()

    def check_ans(self, q_no, answer):
        return answer == self.answers[q_no]

    def display_result(self):
        wrong_count = self.data_size - self.correct
        score = int(self.correct / self.data_size * 100)
        print(f"Score: {score}%")
        print(f"Correctes: {self.correct}")
        print(f"Incorrectes: {wrong_count}")

# Charger les données depuis le fichier JSON
with open('data.json') as f:
    data = json.load(f)

questions = data['question']
options = data['options']
answers = data['answer']

# Initialiser et démarrer le quiz
quiz = Quiz(questions, options, answers)

