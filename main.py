from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.attributes('-fullscreen', True)  # Set to fullscreen
        self.root.bind('<Return>', self.enter_fun)

        # Create a main frame for the chat history and input interface
        main_frame = Frame(self.root, bd=4, bg='#f5f5f5')  # Set background color to light gray
        main_frame.pack(fill=BOTH, expand=True)

        # Create a title label with an image
        img_chat = Image.open("krishna.jpg")  # Update the image path
        img_chat = img_chat.resize((190, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_label = Label(
            main_frame,
            text="Dr. Maharishi Krishna",
            font=("Arial", 30, "bold"),  # Change font to Arial
            bg="white",  # Bright blue background color
            fg="black",  # Text color white
            image=self.photoimg,
            compound=LEFT
        )
        title_label.image = self.photoimg  # Keep a reference to the image
        title_label.pack(side=TOP, fill=X)

        # Create a sidebar for profile information (Left Sidebar)
        profile_frame = Frame(main_frame, bd=4, bg='#f5f5f5', width=250)  # Light gray background color
        profile_frame.pack(fill=Y, side=LEFT, padx=(0, 10))  # Place the profile sidebar on the left with some padding

        profile_image = Image.open("C:/Users/hp/Desktop/healthcare chatbot/profile_image.jpg.png")
        # Update the profile image path
        profile_image = profile_image.resize((200, 200), Image.LANCZOS)
        self.profile_photoimg = ImageTk.PhotoImage(profile_image)

        profile_image_label = Label(
            profile_frame,
            image=self.profile_photoimg,
            bg='#f5f5f5'  # Light gray background color
        )
        profile_image_label.image = self.profile_photoimg  # Keep a reference to the profile image
        profile_image_label.pack(side=TOP, padx=10, pady=10)

        profile_info_label = Label(
            profile_frame,
            text="Chatbot Profile",
            font=('Arial', '16', 'bold'),  # Change font to Arial
            fg='black',  # Text color black
            bg='#f5f5f5',  # Light gray background color
        )
        profile_info_label.pack(side=TOP, fill=X, padx=10, pady=10)

        profile_info_text = Label(
            profile_frame,
            text="Dr. Maharishi Krishna is your virtual assistant. "
                 "Feel free to ask any questions!",
            font=('Arial', '12'),  # Change font to Arial
            fg='black',  # Text color black
            bg='#f5f5f5',  # Light gray background color
            wraplength=200
        )
        profile_info_text.pack(side=TOP, padx=10, pady=10)

        quiz_frame = Frame(main_frame, bd=4, bg='#f5f5f5', width=250)  # Light gray background color
        quiz_frame.pack(fill=Y, side=RIGHT, padx=(10, 0))  # Place the quiz sidebar on the right with some padding

        # Add an image in the background of the quiz_frame
        gamification_image = Image.open("C:/Users/hp/Desktop/healthcare chatbot/game.jpg")
        gamification_image = ImageTk.PhotoImage(gamification_image)

        gamification_image_label = Label(
            quiz_frame,
            image=gamification_image,
            bd=0,  # Remove border
        )
        gamification_image_label.image = gamification_image  # Keep a reference to the image
        gamification_image_label.pack(fill=BOTH, expand=True)

        # You can add quiz elements such as questions, options, and buttons on top of this background image.

        # ... (rest of the code)
        # Add quiz elements here, such as questions, options, and buttons

        # Create a frame for the chat input interface
        input_frame = Frame(main_frame, bd=4, bg='white')
        input_frame.pack(side=BOTTOM, fill=X)

        label_text = Label(
            input_frame,
            text="Type Something",
            font=('Arial', '14', 'bold'),  # Change font to Arial
            fg='black',  # Text color black
            bg='white',
        )
        label_text.grid(row=0, column=0, padx=5)

        self.entry = ttk.Entry(
            input_frame,
            width=40,
            font=('Arial', '14', 'bold'),  # Change font to Arial
        )
        self.entry.grid(row=0, column=1, padx=5, pady=12)

        self.send = Button(
            input_frame,
            text="SEND>>",
            command=self.send,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=8,
            bg="#007acc",  # Bright blue background color
            fg='white',  # Text color white
        )
        self.send.grid(row=0, column=2, padx=5)

        self.voice_recognition = Button(
            input_frame,
            text="Voice",
            command=self.voice_recognition_function,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=8,
            bg="#007acc",  # Bright blue background color
            fg='white',  # Text color white
        )
        self.voice_recognition.grid(row=0, column=3, padx=5)

        self.clear = Button(
            input_frame,
            text="Clear",
            command=self.clear_chat,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=8,
            bg="#ff3333",  # Bright red background color
            fg='white',  # Text color white
        )
        self.clear.grid(row=1, column=0, padx=5, pady=10)

        self.get_report = Button(
            input_frame,
            text="Get Report",
            command=self.get_chat_report,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=12,
            bg="#007acc",  # Bright blue background color
            fg='white',  # Text color white
        )
        self.get_report.grid(row=1, column=1, padx=5, pady=10)

        self.save_report = Button(
            input_frame,
            text="Save Report",
            command=self.save_chat_report,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=12,
            bg="#6600cc",  # Bright purple background color
            fg='white',  # Text color white
        )
        self.save_report.grid(row=1, column=2, padx=5, pady=10)

        self.msg = ''
        self.label_11 = Label(
            input_frame,
            text=self.msg,
            font=('Arial', '14', 'bold'),  # Change font to Arial
            fg='red',
            bg='white',
        )
        self.label_11.grid(row=1, column=3, padx=5, pady=10)

        # Create the chat log text widget
        self.text = Text(
            main_frame,
            bd=3,
            relief=RAISED,
            font=('Arial', 14),  # Change font to Arial
            wrap=WORD
        )
        self.text.pack(fill=BOTH, expand=True)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL, command=self.text.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.config(yscrollcommand=self.scroll_y.set)

    def enter_fun(self, event):
        self.send.invoke()

    def send(self):
        send = 'You: ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.entry.delete(0, END)

    def clear_chat(self):
        # Clear the chat history
        self.text.delete(1.0, END)

    def get_chat_report(self):
        # Get and display the chat report (You can customize this function)
        report = self.text.get(1.0, END)
        print(report)

    def save_chat_report(self):
        # Save the chat report to a file (You can customize this function)
        report = self.text.get(1.0, END)
        with open("chat_report.txt", "w") as file:
            file.write(report)

    def voice_recognition_function(self):
        # Add your voice recognition code here
        pass  # Replace 'pass' with your actual code
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class UserProfile:
    def __init__(self, username, profile_picture, health_goals, achievements, points):
        self.username = username
        self.profile_picture = profile_picture
        self.health_goals = health_goals
        self.achievements = achievements
        self.points = points
        progress_bar = ttk.Progressbar(main_frame, orient=HORIZONTAL, length=200, mode='determinate')
        progress_bar.pack()
class Badge:
    def __init__(self, name, image):
        self.name = name
        self.image = image

# Create instances of badges and add them to the user's badge list.
class PointSystem:
    def __init__(self):
        self.points = 0
        self.history = []

    def earn_points(self, action, points_earned):
        self.points += points_earned
        self.history.append((action, points_earned))


if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()