import tkinter as tk
from tkinter import ttk
from threading import Thread
from assistant.listener import take_command
from assistant.speaker import talk
from assistant.action import handle_command
import os

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(False, False)

        # Style config
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=6)
        self.style.configure("TLabel", font=("Arial", 12))

        # Main frame
        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(expand=True, fill="both")

        # Title
        self.title_label = ttk.Label(
            self.main_frame,
            text="🎙️ Voice Assistant",
            font=("Helvetica", 20, "bold"),
            foreground="#333"
        )
        self.title_label.pack(pady=(0, 15))

        # Status
        self.status_label = ttk.Label(
            self.main_frame,
            text="Status: Idle",
            foreground="#555"
        )
        self.status_label.pack(pady=(0, 10))

        # Live transcript preview
        self.transcript_var = tk.StringVar(value="Say something...")
        self.transcript_label = ttk.Label(
            self.main_frame,
            textvariable=self.transcript_var,
            foreground="#007acc",
            font=("Arial", 11, "italic"),
            wraplength=400
        )
        self.transcript_label.pack(pady=(0, 10))

        # Spinner
        self.spinner = ttk.Progressbar(
            self.main_frame, mode='indeterminate', length=200
        )
        self.spinner.pack(pady=10)
        self.spinner.stop()

        # Mic button
        mic_path = os.path.join("assets", "mic.png")
        self.mic_image = tk.PhotoImage(file=mic_path)

        self.mic_button = tk.Button(
            self.main_frame,
            image=self.mic_image,
            command=self.start_listening,
            borderwidth=0,
            bg="#f0f8ff",
            activebackground="#d0eaff",
            cursor="hand2"
        )
        self.mic_button.pack(pady=10)

        # Command log
        self.log_label = ttk.Label(self.main_frame, text="Command History:")
        self.log_label.pack(pady=(10, 0))

        self.log_text = tk.Text(self.main_frame, height=8, state='disabled', wrap='word')
        self.log_text.pack(expand=True, fill="both", pady=5)

        # Exit button
        self.exit_button = ttk.Button(
            self.main_frame,
            text="Exit",
            command=self.exit_app
        )
        self.exit_button.pack(pady=10)

    def start_listening(self):
        thread = Thread(target=self.run_voice_assistant)
        thread.start()

    def run_voice_assistant(self):
        self.update_status("Listening...")
        self.spinner.start()
        self.transcript_var.set("Listening...")

        talk("I am your voice assistant. How can I help you?")
        command = take_command()

        self.spinner.stop()
        self.transcript_var.set(command if command else "Didn't catch that.")

        if command:
            self.add_to_log(command)
            if 'exit' in command or 'stop' in command:
                self.update_status("Exiting...")
                talk("Goodbye!")
                self.root.quit()
            else:
                self.update_status(f"Processing: '{command}'")
                handle_command(command)
        else:
            talk("Please say that again.")

        self.update_status("Idle")

    def update_status(self, message):
        self.status_label.config(text=f"Status: {message}")

    def add_to_log(self, text):
        self.log_text.config(state='normal')
        self.log_text.insert('end', f"> {text}\n")
        self.log_text.config(state='disabled')
        self.log_text.see('end')

    def exit_app(self):
        self.root.quit()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()


        