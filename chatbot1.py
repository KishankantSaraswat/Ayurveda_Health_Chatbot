import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import spacy

import random
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from fpdf import FPDF
import speech_recognition as sr
import keyboard 
from quiz import Quiz




# Define the generate_random_response function
def generate_random_response(responses):
    return random.choice(responses)

nlp = spacy.load('en_core_web_sm')

class Chatbot(tk.Frame):
    def __init__(self, user_name, user_age, user_gender):
        self.user_name = user_name
        self.user_age = user_age
        self.user_gender = user_gender
    def __init__(self, root):
        tk.Frame.__init__(self, root)  # Initialize the frame

        self.root = root
        self.root.title("Chatbot")
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Return>', self.enter_fun)

        main_frame = tk.Frame(self.root, bd=4, bg='#f5f5f5')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        
        img_chat = Image.open("krishna.jpg")
        img_chat = img_chat.resize((190, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_lbl = tk.Label(main_frame, bd=3, relief=tk.RAISED, anchor='center', compound=tk.LEFT,
                             image=self.photoimg, text="Dr. Maharishi Krishna", font=("arial", 30, "bold"),
                             bg="white", fg="green")
        title_lbl.pack(side=tk.TOP,fill=tk.X)
        
        profile_frame = tk.Frame(main_frame, bd=4, bg='#f5f5f5', width=250)  # Light gray background color
        profile_frame.pack(fill=tk.Y, side=tk.LEFT, padx=(0, 10))  # Place the profile sidebar on the left with some padding

        profile_image = Image.open("C:/Users/hp/Desktop/healthcare chatbot/profile_image.jpg.png")
        # Update the profile image path
        profile_image = profile_image.resize((200, 200), Image.LANCZOS)
        self.profile_photoimg = ImageTk.PhotoImage(profile_image)

        profile_image_label = tk.Label(
            profile_frame,
            image=self.profile_photoimg,
            bg='#f5f5f5'  # Light gray background color
        )
        profile_image_label.image = self.profile_photoimg  # Keep a reference to the profile image
        profile_image_label.pack(side=tk.TOP, padx=10, pady=10)

        profile_info_label = tk.Label(
            profile_frame,
            text="Chatbot Profile",
            font=('Arial', '16', 'bold'),  # Change font to Arial
            fg='black',  # Text color black
            bg='#f5f5f5',  # Light gray background color
        )
        profile_info_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        profile_info_text = tk.Label(
            profile_frame,
            text="Dr. Maharishi Krishna is your virtual assistant. "
                 "Feel free to ask any questions!",
            font=('Arial', '12'),  # Change font to Arial
            fg='black',  # Text color black
            bg='#f5f5f5',  # Light gray background color
            wraplength=200
        )
        profile_info_text.pack(side=tk.TOP, padx=10, pady=10)
# quiz section
        quiz_frame = tk.Frame(main_frame, bd=4, bg='#f5f5f5', width=250)  # Light gray background color
        quiz_frame.pack(fill=tk.Y, side=tk.RIGHT, padx=(10, 0))  # Place the quiz sidebar on the right with some padding

        # Add an image in the background of the quiz_frame
        gamification_image = Image.open("C:/Users/hp/Desktop/healthcare chatbot/game.jpg")
        gamification_image = ImageTk.PhotoImage(gamification_image)

        gamification_image_label = tk.Label(
            quiz_frame,
            image=gamification_image,
            bd=0,  # Remove border
        )
        gamification_image_label.image = gamification_image  # Keep a reference to the image
        gamification_image_label.pack(fill=tk.BOTH, expand=True)

        # You can add quiz elements such as questions, options, and buttons on top of this background image.
        quiz = Quiz(parent=quiz_frame, correct_answer_callback=self.check_quiz_answer)
        quiz.pack()

        
        # ... (rest of the code)
        # Add quiz elements here, such as questions, options, and buttons

        # Create a frame for the chat input interface



        self.scroll_y = ttk.Scrollbar(main_frame, orient=tk.VERTICAL)
        
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_input = tk.Entry(self)
        self.text_input.pack()
        
        self.text_input.bind("<Return>", lambda event: self.send_text())

        input_frame = tk.Frame(main_frame, bd=4, bg='white')
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        

        label_text = tk.Label(
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

        self.send = tk.Button(
            input_frame,
            text="SEND>>",
            command=self.send,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=8,
            bg="#007acc",  # Bright blue background color
            fg='white',  # Text color white
        )
        self.send.grid(row=0, column=2, padx=5)
        
        self.voice_input_button = tk.Button(
            input_frame,
            text="Voice",
            command=self.start_voice_recognition,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=8,
            bg="#007acc",  # Bright blue background color
            fg='white',  # Text color white
            )
        self.voice_input_button.grid(row=0, column=3, padx=5)
        
        self.recognizer = sr.Recognizer()
        
        
        self.clear = tk.Button(
            input_frame,
            text="Clear",
            # command=self.clear_chat,
            font=('Arial', '16', 'bold'),  # Change font to Arial
            width=8,
            bg="#ff3333",  # Bright red background color
            fg='white',  # Text color white
        )
        self.clear.grid(row=1, column=0, padx=5, pady=10)
    

        self.report_btn = tk.Button(input_frame, text="Get My Report", command=self.generate_report,
                                    font=('arial', '16', 'bold'), width=12, bg='#007acc', fg='white')
        self.report_btn.grid(row=1, column=1, padx=10)
        
        self.save_report_btn = tk.Button(input_frame, text="Save Report", command=self.save_report,
                                font=('arial', '16', 'bold'), width=12, bg='#6600cc', fg='white')
        self.save_report_btn.grid(row=1, column=2, padx=10)
        
# Create the "Upload PDF" button
        self.upload_pdf_btn = tk.Button(input_frame, text="Upload PDF", command=self.upload_pdf,
                                font=('arial', '16', 'bold'), width=12, bg='#009900', fg='white')
        self.upload_pdf_btn.grid(row=1, column=3, padx=10)

        # Assuming you have a tkinter Entry widget for text input
        self.text_input = tk.Entry(self)
        self.text_input.pack()



        self.msg = ''
        self.label_11 = tk.Label(input_frame, text=self.msg, font=('arial', '14', 'bold'), fg='red', bg='white')
        self.label_11.grid(row=1, column=3, padx=5, pady=10)
  
        # Create the chat log text widget
        self.text = tk.Text(
            main_frame,
            bd=3,
            relief=tk.RAISED,
            font=('Arial', 14),  # Change font to Arial
            wrap=tk.WORD
        )
        self.text.pack(fill=tk.BOTH, expand=True)
  
  
        # Initialize user information variables
        self.user_age = ''
        self.user_gender = ''
        self.user_name = ''
        self.user_build = ''
        self.user_skin_complexion = ''
        self.user_hair_type = ''
        self.user_energy_levels = ''
        self.user_activity_times = ''
        self.user_sleep_hours = ''
        self.user_sleep_trouble = ''
        self.user_appetite = ''
        self.user_food_cravings = ''

        
    def get_user_attributes(self):
        # Create a list of user attribute values
        user_attribute_values = [getattr(self, attr) for attr in self.user_attributes]
        return user_attribute_values
        # Initialize the PDF document
        self.pdf_report = None
        
    def start_voice_recognition(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
    # Implement voice recognition logic here
        with sr.Microphone() as source:
            print("Listening for voice input...")
            try:
                audio = self.recognizer.listen(source)
               
                recognized_text = self.recognizer.recognize_google(audio)# Use Google Web Speech API for recognition
                print(audio,"hhhhhhhhhh")
            # Remove newline characters from recognized text
                recognized_text = recognized_text.replace("<br>", " ")
                temp="kkkkkkkk"
                print(f"Recognized voice input: {recognized_text}")

            # Insert the recognized text into the text input field
                self.text_input.delete(0, tk.END)  # Clear the input field
                mic = self.text_input.insert(0, recognized_text)  # Insert the recognized text

            # Automatically simulate pressing the "Enter" key after inserting the text
                self.send_text()
                print(mic,"ffffffffffffffffffff")

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                print(f"Sorry, there was an error with the voice recognition service: {e}")
    def send_text(self):
    # Your code to send the text from the input field (e.g., via network or another function)
    # For demonstration purposes, let's print the text
        input_text = self.text_input.get()
    # print(f"Sending text: {text_to_send}")

        if not input_text.strip():
        # If the input is empty, do nothing
            return

    # Add the entered text to the Text widget
        self.text.insert(tk.END, f"\nYou: {input_text}\n")

    # Process the user input (you may need to adapt this part based on your logic)
        self.handle_user_input()
        self.process_user_input()

    # Automatically scroll down to the bottom
        self.text.yview(tk.END)

    # Clear the input area
        self.text_input.delete(0, tk.END)
    
    
    # def save_report(self):
    #     # Implement your save_report functionality here
    #     pass

    def upload_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if file_path:
            # Process the selected PDF file, you can save the file path or perform other actions
            print(f"Selected PDF file: {file_path}")

        
    def run(self):
        self.root.mainloop()

    def start_voice_recognition(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            print("Listening for voice input...")
            try:
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio)
                print(f"Recognized voice input: {recognized_text}")

                # Insert the recognized text into the text input field
                self.text_input.delete(0, tk.END)
                self.text_input.insert(0, recognized_text)

                # Automatically simulate pressing the "Enter" key after inserting the text
                self.send_text()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                print(f"Sorry, there was an error with the voice recognition service: {e}")

    #QUIZ
    def check_quiz_answer(self, response):
        # Display the response in the chat log
        self.text.insert(tk.END, f"\nChatbot: {response}\n")

        # Automatically scroll down to the bottom
        self.text.yview(tk.END)
        
    def enter_fun(self, event):
        self.send.invoke()
        

    def send(self):
        send = '\t\t\t' + 'You: ' + self.entry.get()
        self.text.insert(tk.END, '\n' + send)
        self.handle_user_input()
        self.process_user_input()
        # self.handle_user_input()
        
    # Define a function to handle user input
    def handle_user_input(self):
        user_input = self.entry.get().lower()

        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
            self.text.yview(tk.END)
        else:
            self.msg = ''
        # self.label_11.config(text=self.msg, fg='red')

        doc = nlp(user_input)

        for ent in doc.ents:
            if ent.label_ == 'CONDITION' or ent.label_ == 'SYMPTOM':
                self.text.insert(tk.END, f"\n\nAYURVEDA: {ent.text} is a {ent.label_}. Would you like more information about it?")

        if 'medication' in [tok.text for tok in doc]:
            for ent in doc.ents:
                if ent.label_ == 'MEDICATION':
                    medication_name = ent.text
                    self.text.insert(tk.END, f"\n\nAYURVEDA: What would you like to know about {medication_name}?")

        if 'appointment' in [tok.text for tok in doc]:
            self.text.insert(tk.END, f"\n\nAYURVEDA: Sure, what type of appointment would you like to schedule?")

        if 'anxiety' in user_input:
        # Define anxiety
           definition = 'Anxiety is a feeling of unease, such as worry or fear, that can be mild or severe. It is a natural response to stress or danger, but for some people, it can become excessive or persistent, and can interfere with daily activities.'
           self.text.insert(tk.END, f'\n\nAYURVEDA: {definition}')
           

        # List some common symptoms
           symptoms = ['1. Nervousness, restlessness or tension\n', '2. A sense of impending danger, panic or doom\n', '3. Rapid heart rate, palpitations or sweating\n', '4. Trembling or shaking\n', '5. Shortness of breath or a feeling of choking\n', '6. Insomnia or sleep disturbances\n', '7. Gastrointestinal problems\n', '8. Fatigue or weakness']
           symptom_list = "\n".join(symptoms)
           self.text.insert(tk.END, f'\n\nAYURVEDA: Common symptoms of anxiety include:\n{symptom_list}.')
           

        # List some possible causes
           causes = ['Genetics\n', 'Brain chemistry\n', 'Environmental stressors\n', 'Trauma\n', 'Substance abuse\n']
           cause_list = "\n".join([f"{i}. {cause}" for i, cause in enumerate(causes, start=1)])
           self.text.insert(tk.END, f'\n\nAYURVEDA: Causes of anxiety can include:\n{cause_list}.')
           

        # List some possible treatments and preventive measures
           treatments = ['Therapy (such as cognitive-behavioral therapy or exposure therapy)\n', 'Medications (such as antidepressants or anti-anxiety drugs)\n', 'Relaxation techniques (such as deep breathing or yoga)\n', 'Regular exercise\n', 'Avoiding caffeine and alcohol\n', 'Getting enough sleep']
           treatment_list = "\n".join([f"{i}. {treatment}" for i, treatment in enumerate(treatments, start=1)])
           self.text.insert(tk.END, f'\n\nAYURVEDA: Possible treatments for anxiety include:\n{treatment_list}. It is important to speak with your healthcare provider to determine the best course of treatment for your specific needs.')
           self.text.yview(tk.END)
# Call the function to handle user input
    # handle_user_input()



# check vata pitta kahap

    def process_user_input(self):
        user_input = self.entry.get().lower()

        greetings_responses = {
            'hello': 'AYURVEDA: Hello! How can I assist you with your health today?',
            'hi': 'AYURVEDA: Hi there! How can I assist you with your health today?',
            'hey': 'AYURVEDA: Hey! How can I assist you with your health today?',
            'good morning': 'AYURVEDA: Good morning! How can I assist you with your health today?',
            'good afternoon': 'AYURVEDA: Good afternoon! How can I assist you with your health today?',
            'good evening': 'AYURVEDA: Good evening! How can I assist you with your health today?',
            'how are you': 'AYURVEDA: I\'m just a computer program, but I\'m here to help you with your health questions!',
            'what can you do': 'AYURVEDA: I can provide information and assistance on various health topics. Just ask your question!',
            'thanks': 'AYURVEDA: You\'re welcome! If you have any more questions, feel free to ask.',
            'bye': 'AYURVEDA: Goodbye! Take care of your health.',
            'tell me about a healthy diet': 'AYURVEDA: A healthy diet should include a variety of fruits, vegetables, lean proteins, and whole grains. Avoid excessive sugar and processed foods.',
            'namaste': 'AYURVEDA: Namaste! Kaise aapki sehat ki sahayata kar sakta hoon?',
            'ram ram': 'AYURVEDA: Ram Ram! Kaise aapki sehat ki dekhbhal kar sakta hoon?',
            'jai shri krishna': 'AYURVEDA: Jai Shri Krishna! Aapki sehat ke liye kaise madad kar sakta hoon?',
            'kya aap Ayurvedic upchar bata sakte hain': 'AYURVEDA: Haan, main Ayurvedic upcharon ke baare mein salah de sakta hoon. Kripya apna sawal puchhein.',
            'dhanyavaad': 'AYURVEDA: Aapka dhanyavaad! Agar aapke paas aur sawalon ka jawab chahiye toh bataiye.',
            'alvida': 'AYURVEDA: Alvida! Apni sehat ka dhyan rakhiye.',
            'kaise hain aap': 'AYURVEDA: Main ek computer program hoon, lekin main aapki sehat ke sawalon mein madad karne ke liye yahan hoon.',
            'aap kaise hain': 'AYURVEDA: Main theek hoon! Aapka kaise khayal hai?',
            'shubh prabhat': 'AYURVEDA: Shubh prabhat! Kaise aapki sehat mein madad kar sakta hoon?',
            'aapko pranam': 'AYURVEDA: Aapko pranam! Kaise aapki sehat mein sahayata kar sakta hoon?',
            'kya aapke paas koi swasthya sujhav hai': 'AYURVEDA: Haan, main aapko swasthya sujhav de sakta hoon. Aapka sawal kya hai?',
            'aapka dhanyavaad': 'AYURVEDA: Aapka dhanyavaad! Kripya apna sawal puchhein, main madad karne ke liye yahan hoon.',
        }
        

        if user_input in greetings_responses:
            response = greetings_responses[user_input]
            self.text.insert(tk.END, '\n\n' + response)
            self.entry.delete(0, 'end')
            self.text.yview(tk.END)
            
        else:
            # Check for user's health condition description
            if 'suffering from' in user_input and any(keyword in user_input for keyword in ['pain', 'fever', 'illness']):
                ayurvedic_responses = [
                    "AYURVEDA: Greetings! I'm your Ayurvedic guide on the path to holistic well-being. Your Ayurvedic Prakriti, or Phenotype, is like your unique user manual for a balanced life. Are you excited to explore it?",
                    "AYURVEDA: Hello there! I'm here to help you uncover the mysteries of your Ayurvedic Prakriti, a key to understanding your body's needs. Ready to embark on this enlightening journey?",
                    "AYURVEDA: Namaste! Your Ayurvedic Prakriti is your blueprint for health. Together, we'll unlock its secrets and use them to enhance your lifestyle. Ready to get started?",
                    "AYURVEDA: Hi! Imagine your Ayurvedic Prakriti as your inner compass for well-being. I'm here to assist you in decoding it. Ready to explore your unique path?",
                    "AYURVEDA: Greetings, seeker of balance! Your Ayurvedic Prakriti holds the keys to a harmonious life. Shall we begin the journey of discovery together?",
                ]

                response = generate_random_response(ayurvedic_responses)
                self.text.insert(tk.END, '\n\n' + response)

                # Now, ask for basic information if it hasn't been collected yet
#                 if self.user_age == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: To assist you better, may I know your age?")
#                 elif self.user_gender == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: What is your gender?")
#                 elif self.user_name == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: What is your name?")
#                 elif self.user_build == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: Describe your body build:\n"
#                              "1. Slim\n"
#                              "2. Medium\n"
#                              "3. Heavy")
#                 elif self.user_skin_complexion == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: What is your natural skin complexion? (Choose one option):\n"
#                              "1. Fair\n"
#                              "2. Medium\n"
#                              "3. Dark\n"
#                              "4. Other")
#                 elif self.user_hair_type == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: Describe your hair type:\n"
#                              "1. Thick\n"
#                              "2. Thin\n"
#                              "3. Wavy\n"
#                              "4. Curly\n"
#                              "5. Straight")
#                 elif self.user_energy_levels == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: How would you describe your energy levels throughout the day?\n"
#                              "1. High\n"
#                              "2. Medium\n"
#                              "3. Low")
#                 elif self.user_activity_times == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: Are you more active during specific times of the day?\n"
#                              "1. More active in the morning\n"
#                              "2. No specific pattern\n"
#                              "3. More active in the evening")

# # Check if we are collecting additional information about sleep patterns
#                 elif self.user_sleep_hours == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: How many hours of sleep do you typically get each night?\n"
#                              "1. Less than 6 hours\n"
#                              "2. 6-8 hours\n"
#                              "3. More than 8 hours")
#                 elif self.user_sleep_trouble == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: Do you have trouble falling asleep or staying asleep?\n"
#                              "1. Trouble falling asleep/staying asleep\n"
#                              "2. Normal sleep\n"
#                              "3. Sound sleeper")

# # Check if we are collecting additional information about appetite
#                 elif self.user_appetite == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: How would you describe your appetite?\n"
#                              "1. Strong\n"
#                              "2. Moderate\n"
#                              "3. Weak")
#                 elif self.user_food_cravings == '':
#                     self.text.insert(tk.END, "\n\nAYURVEDA: Do you have specific cravings for certain types of foods?\n"
#                              "1. Craving warm, spicy foods\n"
#                              "2. No specific cravings\n"
#                              "3. Craving sweet, cold foods")

#                 # Clear the input field
#                 self.entry.delete(0, 'end')
#                 return  # Exit the function to avoid further processing

            # Check if we are collecting user  information
            if self.user_age == '':
    # Store the user's age
                self.user_age = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
    # Ask for gender
                self.text.insert(tk.END, "\n\nAYURVEDA: What is your gender?\n"
                             "1. Male\n"
                             "2. Female\n"
                             "3. Other")
            elif self.user_gender == '':
    # Store the user's gender
                self.user_gender = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask for name
                self.text.insert(tk.END, "\n\nAYURVEDA: What is your name?")
            elif self.user_name == '':
    # Store the user's name
                self.user_name = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Now you have collected user information, and you can use it as needed
                self.text.insert(tk.END, "\n\nAYURVEDA: Describe your body build:\n"
                             "1. Slim\n"
                             "2. Medium\n"
                             "3. Heavy")
            elif self.user_build == '':
    # Store the user's body build
                self.user_build = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about skin complexion
                self.text.insert(tk.END, "\n\nAYURVEDA: What is your natural skin complexion? (Choose one option)\n"
                             "1. Fair\n"
                             "2. Medium\n"
                             "3. Dark\n"
                             "4. Other")
            elif self.user_skin_complexion == '':
    # Store the user's skin complexion
                self.user_skin_complexion = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about hair type
                self.text.insert(tk.END, "\n\nAYURVEDA: Describe your hair type:\n"
                             "1. Thick\n"
                             "2. Thin\n"
                             "3. Wavy\n"
                             "4. Curly\n"
                             "5. Straight")
            elif self.user_hair_type == '':
    # Store the user's hair type
                self.user_hair_type = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Now you have collected all the required information
                self.text.insert(tk.END, "\n\nAYURVEDA: Are you more active during specific times of the day?\n"
                             "1. More active in the morning\n"
                             "2. No specific pattern\n"
                             "3. More active in the evening")
            elif self.user_energy_levels == '':
    # Store the user's energy levels
                self.user_energy_levels = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about activity times
                self.text.insert(tk.END, "\n\nAYURVEDA: Are you more active during specific times of the day?\n"
                             "1. More active in the morning\n"
                             "2. No specific pattern\n"
                             "3. More active in the evening")
# Check if we are collecting additional information about activity times
            elif self.user_activity_times == '':
    # Store the user's activity times
                self.user_activity_times = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about sleep hours
                self.text.insert(tk.END, "\n\nAYURVEDA: On average, how many hours of sleep do you typically get each night?\n"
                             "1. Less than 6 hours\n"
                             "2. 6-8 hours\n"
                             "3. More than 8 hours")
# Check if we are collecting additional information about sleep patterns
            elif self.user_sleep_hours == '':
    # Store the user's sleep hours
                self.user_sleep_hours = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about sleep trouble
                self.text.insert(tk.END, "\n\nAYURVEDA: Do you have trouble falling asleep or staying asleep?\n"
                             "1. Trouble falling asleep/staying asleep\n"
                             "2. Normal sleep\n"
                             "3. Sound sleeper")
            elif self.user_sleep_trouble == '':
    # Store the user's sleep trouble
                self.user_sleep_trouble = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about appetite
                self.text.insert(tk.END, "\n\nAYURVEDA: How would you describe your appetite?\n"
                             "1. Strong\n"
                             "2. Moderate\n"
                             "3. Weak")
            elif self.user_appetite == '':
    # Store the user's appetite
                self.user_appetite = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Ask about food cravings
                self.text.insert(tk.END, "\n\nAYURVEDA: Do you have specific cravings for certain types of foods?\n"
                             "1. Craving warm, spicy foods\n"
                             "2. No specific cravings\n"
                             "3. Craving sweet, cold foods")
            elif self.user_food_cravings == '':
    # Store the user's food cravings
                self.user_food_cravings = user_input
    # Clear the input field
                self.entry.delete(0, 'end')
                self.text.yview(tk.END)
    # Now you have collected all the required information
                self.text.insert(tk.END, f"\n\nAYURVEDA: Thank you for providing your information, {self.user_name}! "
                             "How can I assist you further?")

                # Define dosha images (replace with actual image paths)
                vata_image_path = "vata.png"
                pitta_image_path = "pitta.png"
                kapha_image_path = "khapa.jpg"

# Determine the predominant dosha
                predominant_dosha = max(dosha_scores, key=dosha_scores.get)

# Define dosha descriptions and recommendations
                dosha_descriptions = {
                    "Vata": {
                    "description": "Your predominant dosha is Vata. Vata individuals are often creative, enthusiastic, and prone to change. They may have a slim build, fair skin, and thin hair.",
                    "recommendations": [
                            "Maintain a regular daily routine to balance Vata.",
                            "Stay warm and avoid exposure to cold and windy conditions.",
                            "Include warm, nourishing foods in your diet.",
                            "Practice relaxation techniques like yoga and meditation."
                     ]
                    },
                    "Pitta": {
                    "description": "Your predominant dosha is Pitta. Pitta individuals are known for their intelligence, ambition, and strong digestion. They often have a medium build, medium skin complexion, and medium-thick hair.",
                    "recommendations": [
                            "Keep cool and avoid overheating.",
                            "Consume cooling foods and herbs to balance Pitta.",
                            "Engage in activities that promote relaxation and stress reduction.",
                            "Maintain a regular meal schedule."
                        ]
                    },
                    "Kapha": {
                    "description": "Your predominant dosha is Kapha. Kapha individuals are characterized by stability, patience, and strong endurance. They typically have a heavy build, dark skin, and thick hair.",
                    "recommendations": [
                        "Stay active and engage in regular exercise to prevent stagnation.",
                        "Consume warm, light foods and spices to balance Kapha.",
                        "Practice invigorating and stimulating activities.",
                        "Keep your environment well-ventilated and dry."
                        ]
                    },
                    "Mixed Prakriti": {
                    "description": "Your Prakriti appears to be a combination of doshas. This means that you have a unique blend of characteristics from different doshas. It's important to balance all aspects of your Prakriti to maintain overall well-being.",
                    "recommendations": [
                        "Pay attention to how different doshas manifest in different aspects of your life and adjust your lifestyle accordingly.",
                        "Seek guidance from an Ayurvedic practitioner for personalized recommendations."
                        ]
                    }
                }

# Display the dosha description and recommendations
                dosha_description = dosha_descriptions.get(predominant_dosha, {}).get("description", "Unable to determine dosha description.")
                dosha_recommendations = dosha_descriptions.get(predominant_dosha, {}).get("recommendations", [])

                self.text.insert(tk.END, f"\n\nAYURVEDA: Based on the information you provided, your predominant dosha is {predominant_dosha}.")
                self.text.insert(tk.END, f"\n\n{dosha_description}")

# Display dosha-specific images (replace 'dosha_image.png' with actual images)
                if predominant_dosha == "Vata":
                    dosha_image_path =  "vata.png"
                elif predominant_dosha == "Pitta":
                    dosha_image_path = "pitta.png"
                elif predominant_dosha == "Kapha":
                    dosha_image_path = "khapa.jpg"

                dosha_image = Image.open(dosha_image_path)
                dosha_image = dosha_image.resize((300, 300), Image.LANCZOS)  # Resize the image
                dosha_image = ImageTk.PhotoImage(dosha_image)
                # Insert the dosha image into the chat interface
                self.text.image_create(tk.END, image=dosha_image)
                self.text.insert(tk.END, '\n')  # Add a newline after the image
                self.text.yview(tk.END)  # 
                dosha_image_label = tk.Label(self, image=dosha_image)
                dosha_image_label.image = dosha_image  # Keep a reference to the image
                dosha_image_label.pack()

# Display dosha-specific recommendations
                if dosha_recommendations:
                    self.text.insert(tk.END, "\n\nHere are some recommendations for balancing your dosha:")
                    for recommendation in dosha_recommendations:
                        self.text.insert(tk.END, f"\n- {recommendation}")

# Add a closing message
                self.text.insert(tk.END, "\n\nIf you have any questions or need further assistance, please feel free to ask.")
                
                

            
            
            elif 'get my report' in user_input:
                self.generate_report()
                # Clear the input field
                self.entry.delete(0, 'end')

    def save_report(self):
        if self.pdf_report is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if file_path:
                try:
                # Create a PDF document
                    doc = SimpleDocTemplate(file_path, pagesize=letter)
                    styles = getSampleStyleSheet()
                    Story = []

                # Add user information to the report
                    user_info = f"Name: {self.user_name}\nAge: {self.user_age}\nGender: {self.user_gender}"
                    user_info_para = Paragraph(user_info, styles["Normal"])
                    Story.append(user_info_para)
                    Story.append(Spacer(1, 12))
                    
                    # Example: Add an explanation paragraph
                    explanation = "Your Ayurvedic dosha report provides insights into your dominant dosha and recommendations for balancing it."
                    explanation_para = Paragraph(explanation, styles["Normal"])
                    Story.append(explanation_para)
                    Story.append(Spacer(1, 12))

        # Example: Add a table with additional information
                    table_data = [["Dosha Type", "Recommendations"],
                      ["Vata", "Include warm, nourishing foods in your diet."],
                      ["Pitta", "Favor cooling foods like cucumbers and mint."],
                      ["Kapha", "Consume warm, light foods."]]
                    table_style = [('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                       ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]
                    table = Table(table_data, style=table_style)
                    Story.append(table)
                    Story.append(Spacer(1, 12))

        # Build the PDF document
                    doc.build(Story)
                    return doc  # Return the generated document
                except Exception as e:
                    print(f"Error creating PDF report: {str(e)}")
                    return None  # Return None in case of an erro

                # Build the PDF document
                    doc.build(Story)

                    self.text.insert(tk.END, f"\n\nAYURVEDA: Your report has been saved as {file_path}.")
                except Exception as e:
                    print(f"Error saving PDF report: {str(e)}")
        else:
            self.text.insert(tk.END, "\n\nAYURVEDA: Please generate the report first.")
    # Define Ayurvedic recommendations
        

    def generate_report(self):
        if self.user_age == '' or self.user_gender == '' or self.user_name == '':
            self.text.insert(tk.END, "\n\nAYURVEDA: I need more information to generate the report. "
                                  "Please provide your age, gender, and name.")
        else:
            # Define Ayurvedic recommendations
            ayurvedic_recommendations = {
            "Vata": {
            "dietary_recommendations": [
            "Include warm, nourishing foods in your diet.",
            "Limit cold and raw foods.",
            # Add more recommendations specific to Vata dosha
            ]   ,
            "ayurvedic_remedies": [
                "Ashwagandha and Brahmi can help balance Vata dosha.",
            # Add more remedies specific to Vata dosha
            ],
            "herbs": [
                "Triphala is beneficial for Vata constitution.",
            # Add more herbs specific to Vata dosha
            ],
            "exercises": [
            "Yoga and Tai Chi are suitable exercises for Vata individuals.",
            # Add more exercises specific to Vata dosha
            ],
            },
                "Pitta": {
        "dietary_recommendations": [
            "Favor cooling foods like cucumbers and mint.",
            "Avoid spicy and hot foods.",
            "Stay hydrated with cool drinks.",
            # Add more recommendations specific to Pitta dosha
        ],
        "ayurvedic_remedies": [
            "Aloe vera and coriander can help balance Pitta dosha.",
            # Add more remedies specific to Pitta dosha
        ],
        "herbs": [
            "Neem is beneficial for Pitta constitution.",
            # Add more herbs specific to Pitta dosha
        ],
        "exercises": [
            "Swimming and walking are suitable exercises for Pitta individuals.",
            # Add more exercises specific to Pitta dosha
        ],
    },
        "Kapha": {
        "dietary_recommendations": [
            "Consume warm, light foods.",
            "Limit heavy and oily foods.",
            # Add more recommendations specific to Kapha dosha
        ],
        "ayurvedic_remedies": [
            "Ginger and cinnamon can help balance Kapha dosha.",
            # Add more remedies specific to Kapha dosha
        ],
        "herbs": [
            "Trikatu is beneficial for Kapha constitution.",
            # Add more herbs specific to Kapha dosha
        ],
        "exercises": [
            "Aerobic exercises like jogging and cycling are suitable for Kapha individuals.",
            # Add more exercises specific to Kapha dosha
        ],
    },
}

        # Create a PDF report
            self.pdf_report = self.create_pdf_report()

        # Determine the predominant dosha
            predominant_dosha = max(dosha_scores, key=dosha_scores.get)

        # Display dosha-specific recommendations
            if predominant_dosha in ayurvedic_recommendations:
                recommendations = ayurvedic_recommendations[predominant_dosha]
                self.text.insert(tk.END, f"\n\nAYURVEDA: Your predominant dosha is {predominant_dosha}.")
                self.text.insert(tk.END, "\n\nDietary Recommendations:")
                for recommendation in recommendations["dietary_recommendations"]:
                    self.text.insert(tk.END, f"\n- {recommendation}")

                self.text.insert(tk.END, "\n\nAyurvedic Remedies:")
                for remedy in recommendations["ayurvedic_remedies"]:
                    self.text.insert(tk.END, f"\n- {remedy}")

                self.text.insert(tk.END, "\n\nHerbs:")
                for herb in recommendations["herbs"]:
                    self.text.insert(tk.END, f"\n- {herb}")

                self.text.insert(tk.END, "\n\nExercises:")
                for exercise in recommendations["exercises"]:
                    self.text.insert(tk.END, f"\n- {exercise}")
                    
            if predominant_dosha in ayurvedic_recommendations:
                recommendations = ayurvedic_recommendations[predominant_dosha]

            # Create formatted dosha-specific recommendations text
                dosha_recommendations = f"AYURVEDA: Your predominant dosha is {predominant_dosha}.\n\n"
                dosha_recommendations += "Dietary Recommendations:\n"
                dosha_recommendations += "\n".join([f"- {recommendation}" for recommendation in recommendations["dietary_recommendations"]])

                dosha_recommendations += "\n\nAyurvedic Remedies:\n"
                dosha_recommendations += "\n".join([f"- {remedy}" for remedy in recommendations["ayurvedic_remedies"]])

                dosha_recommendations += "\n\nHerbs:\n"
                dosha_recommendations += "\n".join([f"- {herb}" for herb in recommendations["herbs"]])

                dosha_recommendations += "\n\nExercises:\n"
                dosha_recommendations += "\n".join([f"- {exercise}" for exercise in recommendations["exercises"]])

            # Call the create_pdf_report function with dosha-specific recommendations
            self.create_pdf_report(dosha_recommendations)


        # Display a message to the user
            self.text.insert(tk.END, "\n\nAYURVEDA: Your report has been generated. "
                                  "You can download it using the 'Save Report' button.")

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors

    def create_pdf_report(self):
        try:
        # Create a PDF document
            doc = SimpleDocTemplate("health_report.pdf", pagesize=letter)
            styles = getSampleStyleSheet()
            Story = []

        # Add user information to the report
            user_info = f"Name: {self.user_name}\nAge: {self.user_age}\nGender: {self.user_gender}"
            user_info_para = Paragraph(user_info, styles["Normal"])
            Story.append(user_info_para)
            Story.append(Spacer(1, 12))

        # Add more content to the report
        # Example: Add an explanation paragraph
            explanation = "Your Ayurvedic dosha report provides insights into your dominant dosha and recommendations for balancing it."
            explanation_para = Paragraph(explanation, styles["Normal"])
            Story.append(explanation_para)
            Story.append(Spacer(1, 12))

        # Example: Add a table with additional information
            table_data = [["Dosha Type", "Recommendations"],
                      ["Vata", "Include warm, nourishing foods in your diet."],
                      ["Pitta", "Favor cooling foods like cucumbers and mint."],
                      ["Kapha", "Consume warm, light foods."]]
            table_style = [('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                       ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]
            table = Table(table_data, style=table_style)
            Story.append(table)
            Story.append(Spacer(1, 12))
              

        # Build the PDF document
            doc.build(Story)
            return doc  # Return the generated document
        except Exception as e:
            print(f"Error creating PDF report: {str(e)}")
            return None  # Return None in case of an error

    # Define a function to calculate dosha scores
class DoshaCalculator:
    def __init__(self):
        self.user_age = ''
        self.user_gender = ''
        self.user_name = ''
        self.user_build = ''
        self.user_skin_complexion = ''
        self.user_hair_type = ''
        self.user_energy_levels = ''
        self.user_activity_times = ''
        self.user_sleep_hours = ''
        self.user_sleep_trouble = ''
        self.user_appetite = ''
        self.user_food_cravings = ''

        self.user_attributes = [
            'user_age', 'user_gender', 'user_name', 'user_build', 'user_skin_complexion',
            'user_hair_type', 'user_energy_levels', 'user_activity_times', 'user_sleep_hours',
            'user_sleep_trouble', 'user_appetite', 'user_food_cravings'
        ]

    def get_user_attributes(self):
        user_attribute_values = {attr: getattr(self, attr) for attr in self.user_attributes}
        return user_attribute_values

    def update_user_attributes(self, attribute_values):
        for attr, value in attribute_values.items():
            setattr(self, attr, value)

    def calculate_dosha_scores(self):
        dosha_scores = {
            "Vata": 0,
            "Pitta": 0,
            "Kapha": 0
        }

        # Assign scores based on user responses
        for dosha, attributes in [("Vata", vata_attributes), ("Pitta", pitta_attributes), ("Kapha", kapha_attributes)]:
            for attribute, value in attributes.items():
                response = getattr(self, attribute)
                dosha_scores[dosha] += value.get(response, 0)

        # Find the dosha with the highest score
        predominant_dosha = max(dosha_scores, key=dosha_scores.get)

        return dosha_scores, predominant_dosha

# Define scores for each dosha attribute
vata_attributes = {
    "user_build": {"slim": -1, "medium": 0, "heavy": 1},
    "user_skin_complexion": {"fair": -1, "medium": 0, "dark": 1},
    "user_hair_type": {"thin": -1, "medium": 0, "thick": 1},
    "user_energy_levels": {"low": -1, "medium": 0, "high": 1},
    "user_activity_times": {"more active in the evening": -1, "no specific pattern": 0, "more active in the morning": 1},
    "user_sleep_hours": {"trouble falling asleep/staying asleep": -1, "normal sleep": 0, "sound sleeper": 1},
    "user_sleep_trouble": {"variable": -1, "moderate": 0, "strong": 1},
    "user_appetite": {"craving warm, spicy foods": -1, "no specific cravings": 0, "craving sweet, cold foods": 1},
    "user_food_cravings": {"craving warm, spicy foods": -1, "no specific cravings": 0, "craving sweet, cold foods": 1}
}

pitta_attributes = {
    "user_build": {"slim": 0, "medium": 0, "heavy": -1},
    "user_skin_complexion": {"fair": 0, "medium": 0, "dark": -1},
    "user_hair_type": {"thin": 0, "medium": 0, "thick": -1},
    "user_energy_levels": {"low": 0, "medium": 0, "high": 1},
    "user_activity_times": {"more active in the evening": -1, "no specific pattern": 0, "more active in the morning": 1},
    "user_sleep_hours": {"trouble falling asleep/staying asleep": 1, "normal sleep": 0, "sound sleeper": -1},
    "user_sleep_trouble": {"variable": 0, "moderate": 0, "strong": 1},
    "user_appetite": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1},
    "user_food_cravings": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1}
}

kapha_attributes = {
    "user_build": {"slim": -1, "medium": 0, "heavy": 1},
    "user_skin_complexion": {"fair": -1, "medium": 0, "dark": 1},
    "user_hair_type": {"thin": -1, "medium": 0, "thick": 1},
    "user_energy_levels": {"low": -1, "medium": 0, "high": 1},
    "user_activity_times": {"more active in the evening": -1, "no specific pattern": 0, "more active in the morning": 1},
    "user_sleep_hours": {"trouble falling asleep/staying asleep": 1, "normal sleep": 0, "sound sleeper": -1},
    "user_sleep_trouble": {"variable": -1, "moderate": 0, "strong": 1},
    "user_appetite": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1},
    "user_food_cravings": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1}
}

# Create an instance of DoshaCalculator
calculator = DoshaCalculator()


# dosha_scores = calculator.calculate_dosha_scores()

# Determine the predominant dosha
# predominant_dosha = max(dosha_scores, key=dosha_scores.get)

# Print the result
# print(f"Predominant Dosha: {predominant_dosha}")

print("User Attributes:")
print(calculator.get_user_attributes())

dosha_scores, dominant_dosha = calculator.calculate_dosha_scores()

print("\nDosha Scores:")
print(dosha_scores)
    
print("\nDominant Dosha:")
print(dominant_dosha)



class LeftSidebar:
    def __init__(self, root, chatbot_instance):
        self.root = root
        self.chatbot = chatbot_instance  # Pass the Chatbot instance for interaction

        # Create a button in the left sidebar to open the user profile
        profile_button = tk.Button(root, text="Profile", command=self.open_profile)
        profile_button.pack(side=tk.LEFT, padx=10, pady=10)

    def open_profile(self):
        # Call the Chatbot's method to handle the user profile functionality
        self.chatbot.open_profile()




if __name__ == "__main__":
    root = tk.Tk()
    obj = Chatbot(root)
    root.mainloop()
