import tkinter as tk
import speech_recognition as sr
import time
from PIL import Image, ImageTk
import threading

def recognize_speech():
    def _recognize_speech():
        # Initialize recognizer
        recognizer = sr.Recognizer()
        
        with sr.Microphone() as source:
            # Clear previous text
            text_area.delete(1.0, tk.END)
            
            # Notify user
            text_area.insert(tk.END, "Listening...\n")
            root.update_idletasks()  # Update the GUI to display the message immediately
            
            # Wait for a second before starting to listen
            time.sleep(1)
            
            # Listen for speech
            audio_data = recognizer.listen(source, phrase_time_limit=5)  # Set timeout and phrase time limit
            
            try:
                # Recognize speech using Google Speech Recognition
                text = recognizer.recognize_google(audio_data)
                # Display recognized text
                text_area.insert(tk.END, text)
            except sr.UnknownValueError:
                text_area.insert(tk.END, "Could not understand audio")
            except sr.RequestError:
                text_area.insert(tk.END, "Could not request results from Google Speech Recognition service")
            except TimeoutError:
                text_area.insert(tk.END, "Connection timed out. Please try again.")

    # Create a thread to run the speech recognition
    threading.Thread(target=_recognize_speech).start()

# Initialize Tkinter window
root = tk.Tk()
root.title("Speech Recognition")
root.geometry('1100x320')  # x, y
root.resizable(0, 0)  # cannot resize the box

# Set the background color of the main window
root.configure(bg='#2E2E2E')  # Gray-black background color

# Heading
tk.Label(root, text="Speech To Text", height=2, width=50, font=" Arial 15", bg='#2E2E2E', fg='white').pack()

# Introduction
tk.Label(root, text="~Translate spoken words into text~", height=2, width=50, font="Arial 12", bg='#2E2E2E', fg='white').pack()

# Create a microphone icon
# Load the image using Pillow
image_path = r"C:\Users\Arathi Hembram\Desktop\Arathi\Projects(self)\Python-Speech-Recognition-\backup\mic.png"
image = Image.open(image_path)

# Resize the image using Pillow
new_size = (100, 100)  # Width, Height
resized_image = image.resize(new_size, Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Create a label with the image
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference to avoid garbage collection

# Place the label using the place geometry manager
label.place(x=165, y=120)  # Change x and y to the desired position

# Create a button to start speech recognition
recognize_button = tk.Button(root, text="Start Speech", command=recognize_speech, height=2, width=20, bg='#4A4A4A', fg='white')
recognize_button.place(x=145, y=250)

# Create a label to display the converted text
tk.Label(root, text="Converted Text", height=2, width=15, font="Arial 12", bg='#2E2E2E', fg='white').place(x=480, y=130)

# Create a text area to display recognized text
text_area = tk.Text(root, height=5, width=50, bg='#2E2E2E', fg='white', insertbackground='white')
text_area.place(x=480, y=200)

# Run the Tkinter event loop
root.mainloop()
