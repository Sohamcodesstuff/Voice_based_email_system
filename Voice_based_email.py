import speech_recognition as sr

import pyttsx3
import smtplib

engine = pyttsx3.init()

def say_user() :

    hear = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source :

        audio = hear.listen(source)

        text = hear.recognize_google(audio)

        return text

def format_text(text) :

    text = text.lower()

    text = text.replace(" ", "")

    return text

def say_computer(text) :

    engine.say(text)

    engine.runAndWait()


say_computer("Dear User what is your name")

name = say_user()

say_computer("Good Morning " + name)

say_computer(name + " What is your Email ID")

email = say_user()

email = format_text(email)

say_computer(name + " What is your Password")

password = say_user()

password = format_text(password)

print("Email ID : " + email + "\nPassword : " + password)

say_computer(name + " your Email ID is " + email + " and Password is " + password)

say_computer("logging into your email")

s = smtplib.SMTP('smtp.gmail.com', 587) 
  

s.starttls() 
  
 
s.login(email, password) 

say_computer("What do you want to send?")

message = say_user()

say_computer("are you sure you want to send the message")

consent = say_user()

if consent=="yes":
 say_computer("Message was sent")
 s.quit()
else:
    say_computer("message not sent!")
    s.quit



