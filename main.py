# importing the pyttsx library
import pyttsx3

# initialisation
speak = pyttsx3.init()

# Main Logic
if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1. Created by June")
    speak.say("Welcome to Robo Speaker 1.1. Created by June")
    speak.runAndWait()
    while True:
        speak.say("Enter what you want me to say!")
        speak.runAndWait()
        x = input("Enter what you want me to say: ")
        if x == 'exit':
            speak.say("ok, bye!")
            speak.runAndWait()
            break
        speak.say(f"{x}")
        speak.runAndWait()
