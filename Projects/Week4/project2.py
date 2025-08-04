#  Project 2: Quiz App (OOP + File I/O + Random)

#  Concepts:
# random.shuffle() for randomizing questions
# File read for questions (optional)
# OOP to encapsulate quiz logic

# Quiz App

import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for q in self.questions:
            ans = input(q.prompt + " ")
            if ans.lower().strip() == q.answer.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong. Correct: {q.answer}\n")
        print(f"Final Score: {self.score}/{len(self.questions)}")

# Questions
question_list = [
    Question("What does CPU stand for?\n(a) Central Processing Unit\n(b) Computer Personal Unit\n(c) Central Print Unit\n> ", "a"),
    Question("Which language is used for AI?\n(a) Java\n(b) Python\n(c) HTML\n> ", "b"),
    Question("What is the square root of 16?\n(a) 4\n(b) 8\n(c) 2\n> ", "a")
]

random.shuffle(question_list)
quiz = Quiz(question_list)
quiz.run()
