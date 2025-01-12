import tkinter as tk 
import random
import time

texts = [
    "I wanna new life and i want it with you",
    "Can we go back to the day our love was strong",
    "Can you tell me how a perfect love goes wrong",
    "Can somebody tell me how to get things back the way they used to be",
    "oh god give me a reason i'm down on bended knee"
]

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.start_time = None
        self.timer_running = False
        self.wpm = 0

        
        self.text_to_type = random.choice(texts)
        self.text_label = tk.Label(root, text=self.text_to_type, wraplength=400, font=("Helvetica", 14))
        self.text_label.pack(pady=20)

        
        self.user_input = tk.Entry(root, font=("Helvetica", 14), width=50)
        self.user_input.pack(pady=20)
        self.user_input.bind("<KeyRelease>", self.check_input)

        
        self.start_button = tk.Button(root, text="Start Test", font=("Helvetica", 14), command=self.start_test)
        self.start_button.pack(pady=10)

        
        self.wpm_label = tk.Label(root, text="WPM: 0", font=("Helvetica", 14))
        self.wpm_label.pack(pady=10)

    def start_test(self):
        """Start the typing test."""
        self.user_input.delete(0, tk.END)
        self.text_to_type = random.choice(texts)
        self.text_label.config(text=self.text_to_type)
        self.start_button.config(state=tk.DISABLED)
        self.start_time = time.time()
        self.timer_running = True
        self.user_input.focus()

    def check_input(self, event):
        """Check if the input is correct and calculate WPM."""
        if self.timer_running:
            typed_text = self.user_input.get()
            if typed_text == self.text_to_type:
                elapsed_time = time.time() - self.start_time
                words = len(typed_text.split())
                self.wpm = (words / elapsed_time) * 60
                self.wpm_label.config(text=f"WPM: {int(self.wpm)}")
                self.timer_running = False
                self.start_button.config(state=tk.NORMAL)
                self.user_input.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()

