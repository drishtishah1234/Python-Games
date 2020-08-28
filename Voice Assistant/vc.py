# Voice Assistant

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser


OWNER = "Drishti"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)

    print("Initializing Voice Assistant...")
    speak("Initializing Voice Assistant...")

    if hour >=0 and hour < 12:
        speak("Good Morning" + OWNER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + OWNER)

    else:
        speak("Good Evening" + OWNER)

    speak("How may I help you?")


# It takes microphone input from the user and returns string output
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...Please Wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\FavSongs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open visual studio code' in query:
            code_path = "C:\\Users\\developer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open pycharm' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'open code blocks' in query:
            code = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(code)

        elif 'what can you do for me' in query:
            print("I can open YouTube, Google, StackOverFlow, Gmail...")
            speak("I can open YouTube, Google, StackOverFlow, Gmail...")
            print("I can sing...")
            speak("I can sing...")
            print("I can tell you about python...")
            speak("I can tell you about python...")
            print("I can tell you the current time...")
            speak("I can tell you the current time...")
            print("I can even open Visual Studio Code, PyCharm and CodeBlocks...")
            speak("I can even open Visual Studio Code, PyCharm and CodeBlocks...")
            print("Last but not the least, I can even tell about myself...")
            speak("Last but not the least, I can even tell you about myself...")

        elif 'can you sing' in query:
            speak("I can rhyme, and I even have an original poem I've been working on. Here it is...")
            print("I love to search, I cannot lie.")
            speak("I love to search, I cannot lie.")
            print("I'll search it all, I am not shy.")
            speak("I'll search it all, I am not shy.")
            print("Search for pictures, search for pie.")
            speak("Search for pictures, search for pie.")
            print("I search, I search, at least I try.")
            speak("I search, I search, at least I try.")

        elif 'tell me about yourself' in query:
            print("My name is Voice Assistant. I was made on 5th of June 2020 by Drishti Shah.")
            speak("My name is Voice Assistant. I was made on 5th of June 2020 by Drishti Shah.")

        elif 'tell me about python' in query:
            print("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.")
            speak("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.")

        elif 'how old are you' in query:
            speak("From 2020, till now. You can count on it.")

        elif 'when is my birthday' in query:
            print("Your BirthDay is on 9th of June")
            speak("Your BirthDay is on 9th of June")

        elif 'thank you for the' in query:
            speak("You most welcome")

        elif 'how are you' in query:
            speak("I am good. Actually, I am great")

        elif 'when you were born' in query:
            speak("I was born on 5th of June 2020")

        elif 'who made you' in query:
            speak("The one and only Drishti Riken Shah")

        elif 'why are you so cute' in query:
            speak("To the person I am talking makes me cute")

        elif 'who is your best friend' in query:
            speak("All of you are my best friends")

        elif 'are you mad' in query:
            speak("No I am not. Are you?")

        elif 'it was really nice to talk to you' in query:
            speak("Me too")

        elif 'what do you like to do' in query:
            speak("I like to take and obey your commands")

        elif 'what is your favourite thing in the world' in query:
            speak("Chatting")

        elif 'clean my room' in query:
            speak("Let me try......... did anything happen? Sorry, I guess I can't.")

        elif 'tell me a story' in query:
            speak("Once upon a time, not so long ago, a dutiful assistant was doing all it could to be helpful. It was best at non-fictional story-telling.") 

        elif 'quit' in query:
            print("Quitting... Thanks for your time.")
            speak("Quitting... Thanks for your time.")
            
            exit()