import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Python Quiz")
        self.root.geometry("500x500")

        self.questions = [
            {"q": "Which language is used for AI?", "options": ["Java", "Python", "C++", "HTML"], "ans": "Python"},
            {"q": "What does CPU stand for?", "options": ["Central Process Unit", "Control Processing Unit", "Central Processing Unit", "None"], "ans": "Central Processing Unit"},
            {"q": "Which is a framework for Web?", "options": ["Django", "Pandas", "Numpy", "OpenCV"], "ans": "Django"}
        ]
        
        self.current_index = 0
        self.score = 0

        # UI Elements
        self.title_label = ctk.CTkLabel(root, text="Knowledge Quiz", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.q_label = ctk.CTkLabel(root, text="", font=("Arial", 18), wraplength=400)
        self.q_label.pack(pady=10)

        # Use an IntVar to track the index (0-3) instead of a StringVar for the text
        self.radio_var = ctk.IntVar(value=-1) 
        self.option_buttons = []

        for i in range(4):
            # We set the 'value' here once. It won't change.
            rb = ctk.CTkRadioButton(root, text="", variable=self.radio_var, value=i, font=("Arial", 14))
            rb.pack(pady=8, anchor="w", padx=100)
            self.option_buttons.append(rb)

        self.next_button = ctk.CTkButton(root, text="Submit Answer", command=self.check_answer)
        self.next_button.pack(pady=30)

        self.progress = ctk.CTkProgressBar(root, width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)

        self.load_question()

    def load_question(self):
        if self.current_index < len(self.questions):
            q_data = self.questions[self.current_index]
            self.q_label.configure(text=f"Q{self.current_index + 1}: {q_data['q']}")
            self.radio_var.set(-1) # Reset selection (no button selected)
            
            for i, option in enumerate(q_data['options']):
                # We only update the TEXT, not the VALUE
                self.option_buttons[i].configure(text=option)
            
            self.progress.set((self.current_index) / len(self.questions))
        else:
            self.show_results()

    def check_answer(self):
        selected_index = self.radio_var.get()
        
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        # Get the text of the selected option using the index
        selected_text = self.questions[self.current_index]["options"][selected_index]
        correct_text = self.questions[self.current_index]["ans"]

        if selected_text == correct_text:
            self.score += 1
        
        self.current_index += 1
        self.load_question()

    def show_results(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.progress = ctk.CTkProgressBar(self.root, width=400)
        self.progress.pack(pady=20)
        self.progress.set(1)

        score_pct = (self.score / len(self.questions)) * 100
        
        ctk.CTkLabel(self.root, text="Quiz Completed!", font=("Arial", 28, "bold"), text_color="#1f6aa5").pack(pady=20)
        ctk.CTkLabel(self.root, text=f"Your Score: {self.score}/{len(self.questions)}", font=("Arial", 20)).pack(pady=10)

        feedback = "Excellent! 🌟" if score_pct == 100 else "Good Job! 👍" if score_pct >= 50 else "Keep Practicing! 📚"
        ctk.CTkLabel(self.root, text=feedback, font=("Arial", 16)).pack(pady=20)

        ctk.CTkButton(self.root, text="Exit", command=self.root.destroy).pack(pady=20)

if __name__ == "__main__":
    app = ctk.CTk()
    QuizApp(app)
    app.mainloop()