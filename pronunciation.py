import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def pronounce_text():
    """Pronounce the text entered in the input box."""
    text = text_input.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text to pronounce.")
        return
    engine.say(text)
    engine.runAndWait()

# Create the main application window
app = tk.Tk()
app.title("Pronunciation App")
app.geometry("400x200")

# Add a label
label = tk.Label(app, text="Enter text to pronounce:", font=("Arial", 14))
label.pack(pady=10)

# Add a text entry field
text_input = tk.Entry(app, width=40, font=("Arial", 12))
text_input.pack(pady=5)

# Add a button to trigger pronunciation
pronounce_button = tk.Button(app, text="Pronounce", font=("Arial", 12), command=pronounce_text)
pronounce_button.pack(pady=10)

# Start the tkinter event loop
app.mainloop()
