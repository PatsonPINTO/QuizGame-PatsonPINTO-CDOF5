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
            self.display_question(q_no)
            answer = self.get_user_answer()
            if self.check_ans(q_no, answer):
                self.correct += 1
            print("\n")
        self.display_result()

    def display_question(self, q_no):
        print(f"Q{q_no + 1}: {self.questions[q_no]}")
        for idx, option in enumerate(self.options[q_no], 1):
            print(f"{idx}. {option}")

    def get_user_answer(self):
        while True:
            try:
                answer = int(input("Votre réponse (1-4): "))
                if 1 <= answer <= 4:
                    return answer
                else:
                    print("Veuillez entrer un nombre entre 1 et 4.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def check_ans(self, q_no, answer):
        return answer == self.answers[q_no]

    def display_result(self):
        wrong_count = self.data_size - self.correct
        score = int(self.correct / self.data_size * 100)
        print(f"Score: {score}%")
        print(f"Correct Answers: {self.correct}")
        print(f"Incorrect Answers: {wrong_count}")
        print("Thank you for playing!")

def load_json_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
    validate_json_data(data)
    return data

def validate_json_data(data):
    if not all(key in data for key in ('question', 'options', 'answer')):
        raise ValueError("JSON data is missing required keys.")
    if not (len(data['question']) == len(data['options']) == len(data['answer'])):
        raise ValueError("JSON data arrays must have the same length.")

# Load and validate the JSON data
data = load_json_data('data.json')

questions = data['question']
options = data['options']
answers = data['answer']

# Initialize and start the quiz
quiz = Quiz(questions, options, answers)

