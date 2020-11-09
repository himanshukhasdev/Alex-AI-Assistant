import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
     

def wishme():
    speak("Welcome back sir")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour  >= 6 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak("Alex at your service. please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query  =  r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("say that again...")

        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("himanshukhasdev@gmail.com","himanshu@2208")
    server.sendmail("himanshukhasdev@gmail.com", to, content)
    server.close()

def Screenshot():
    img = pyautogui.screenshot()
    img.save ("G:\\ai\\ss1.png")

def cpu():
    usage = str(psutil.cpu_percent())  
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak (battery.percent)  

def joke():
    speak(pyjokes.get_joke())



if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()


        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak ("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print (result)
            speak (result)

        elif "send email" in query:
            try:
                speak ("what should i say?")
                content = takeCommand()
                to = "khasdevmonika@gmail.com"
                sendEmail(to, content)
                speak ("Email has been sent!")
            except Exception as e:
                print (e)
                speak ("Unable to send the email")

        elif "search in chrome" in query:
            speak ("What should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif "logout" in query:
            os.system ("shutdown /l")

        elif "shutdown" in query:
            os.system ("shutdown /s")

        elif "restart" in query:
            os.system ("shutdown /r")

        elif "play songs" in query:
            songs_dir = "G:\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[4]))

        elif "remember that"  in query:
            speak ("what should i remember sir?")
            data = takeCommand()
            speak ("you said me to remember that"+data)
            remember = open("data.txt","w")
            remember.write (data)
            remember.close()

        elif "do you know anything" in query:
            remember = open ("data.txt", "r")
            speak ("you said me to remember that"+remember.read())

        elif "screenshot" in query:
            Screenshot()
            speak ("done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            joke()


        elif "offline" in query:
            quit()
        


        
