class Quiz:
    def init(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
                "answer": "B"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
                "answer": "D"
            }
        ]
        self.score = 0

    def validate_input(self, user_input):
        return user_input in ["A", "B", "C", "D"]

    def get_user_input(self):
        user_input = input("Your answer (A, B, C, or D): ").strip().upper()
        while not self.validate_input(user_input):
            print("Invalid input. Please enter A, B, C, or D.")
            user_input = input("Your answer (A, B, C, or D): ").strip().upper()
        return user_input

    def provide_feedback(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.\n")

    def display_final_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}.")

    def run(self):
        for idx, q in enumerate(self.questions):
            print(f"Question {idx + 1}: {q['question']}")
            for option in q["options"]:
                print(option)
            user_answer = self.get_user_input()
            self.provide_feedback(user_answer, q["answer"])
        self.display_final_score()

if name == "main":
    quiz = Quiz()
    quiz.run()