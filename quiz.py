# quiz.py
import tkinter as tk
from tkinter import ttk

class Quiz(tk.Frame):
    def __init__(self, parent, correct_answer_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.correct_answer_callback = correct_answer_callback
        self.current_question_index = 0
        self.correct_answers = 0

        # Define your quiz questions
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Berlin', 'Paris', 'London'],
                'correct_answer': 'Paris',
                'explanation': 'Paris is the capital of France.',
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Earth', 'Mars', 'Venus'],
                'correct_answer': 'Mars',
                'explanation': 'Mars is often referred to as the Red Planet.',
            },
            {
                'question': 'This is a very long question that should break into two lines to fit the frame. How do you handle multiline questions in your game?',
                'options': ['Option A', 'Option B', 'Option C'],
                'correct_answer': 'Option A',
                'explanation': 'Explanation for the long question.',
            },
            # Add more questions as needed
        ]

        self.setup_ui()

    def setup_ui(self):
        # Quiz Question
        self.question_label = tk.Label(
            self,
            text=self.questions[self.current_question_index]['question'],
            font=('Arial', '14', 'bold'),
            bg='#f5f5f5',
            wraplength=300,  # Set the maximum width for wrapping
        )
        self.question_label.pack(side=tk.TOP, anchor=tk.CENTER, pady=(20, 0))

        # Answer Options
        self.answer_options = self.questions[self.current_question_index]['options']
        for option in self.answer_options:
            option_button = tk.Button(
                self,
                text=option,
                command=lambda ans=option: self.check_answer(ans),
                font=('Arial', '12'),
                bg="#007acc",
                fg='white',
                width=15,
                pady=5,
            )
            option_button.pack(side=tk.TOP, anchor=tk.N)

        # Score Calculator
        self.score_label = tk.Label(
            self,
            text=f"Score: {self.correct_answers}/{len(self.questions)}",
            font=('Arial', '12', 'bold'),
            bg='#f5f5f5',
        )
        self.score_label.pack(side=tk.BOTTOM, anchor=tk.S, pady=(0, 20))

    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question_index]['correct_answer']
        if selected_answer == correct_answer:
            self.correct_answers += 1

        response = (
            "Correct! " + self.questions[self.current_question_index]['explanation']
            if selected_answer == correct_answer
            else f"Incorrect. The correct answer is {correct_answer}. {self.questions[self.current_question_index]['explanation']}"
        )

        # Display the response in the chat log
        self.correct_answer_callback(response)

        # Move to the next question or finish the quiz
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.update_question()
        else:
            self.finish_quiz()

    def update_question(self):
        # Update the question label and answer options for the next question
        self.question_label.config(text=self.questions[self.current_question_index]['question'])

        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        self.answer_options = self.questions[self.current_question_index]['options']
        for option in self.answer_options:
            option_button = tk.Button(
                self,
                text=option,
                command=lambda ans=option: self.check_answer(ans),
                font=('Arial', '12'),
                bg="#007acc",
                fg='white',
                width=15,
                pady=5,
            )
            option_button.pack()

        # Update the score label
        self.score_label.config(text=f"Score: {self.correct_answers}/{len(self.questions)}")

    def finish_quiz(self):
        # You can implement additional logic for finishing the quiz
        pass
