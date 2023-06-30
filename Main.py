import smtplib
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia  
import webbrowser
import os
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("\nI am Jarvis Sir. ")
    speak("I am Jarvis Sir. ")


def login(i):
    while (i != -1):
        print("Please tell me your name: ")
        speak("Please tell me your name: ")
        name = input()
        print("Please tell me your password")
        speak("Please tell me your password")
        password = input()
        if name == "admin" and password == "Shaksham":
            print("Access granted !!!")
            speak("Access granted ")
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    try:
                        print('Searching Wikipedia...')
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query,auto_suggest=False)
                        print("According to Wikipedia")
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    except:
                        speak("Result not found ")
                        print("Result not found ")
                elif 'open youtube' in query:

                    url = 'https://youtube.com'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                        "C:\\Users\\gshdh\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open_new(url)

                elif 'open google' in query:
                    url = 'https://google.com'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                        "C:\\Users\\gshdh\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open_new(url)

                elif 'open stack overflow' in query:
                    url = 'https://stackoverflow.com'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                        "C:\\Users\\gshdh\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open_new(url)
                elif 'open github' in query:
                    url = 'https://github.com'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                        "C:\\Users\\gshdh\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open_new(url)
                elif 'open linkedin' in query:
                    url = 'https://linkedin.com'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                        "C:\\Users\\gshdh\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open_new(url)

                elif 'play music' in query:
                    music_dir = 'C:\\Users\\gshdh\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, the time is {strTime}")
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\gshdh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'bye' in query:
                    keyboard.press_and_release("Alt+F4")

                elif 'send mail' in query:
                    try:
                        print("What should I say?")
                        speak("What should I say?")
                        content = takeCommand()
                        to = input("Enter mail Id of receiver: ")
                        print("Sending mail to {}".format(to))
                        speak("Sending mail to {}".format(to))
                        sendEmail(to, content)
                        print("Email has been sent!")
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak(
                            "Sorry my friend saksham. I am not able to send this email")
        elif name != "admin" or password != "Shaksham":
            print("Access denied !!!")
            speak("Access denied ")
            print("{} attempts left".format(i))
            speak("{} attempts left".format(i))
            login(i-1)
    if (i == -1):
        print("Maximum amount of attempts reached....")
        speak("Maximum amount of attempts reached")
        exit()


def takeCommand():
    # It takes microphone input from the user and returns string output

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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gshaksham3@gmail.com', 'yavehbhcgtqssvnj')
    server.sendmail('gshaksham3@gmail.com', to, content)
    server.close()


def abcd():
    wishMe()
    login(2)


if __name__ == "__main__":
    abcd()

  
