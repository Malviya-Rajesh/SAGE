"""
AI voice assistant "SAGE"
his program is a AI voice assistant which is use to play movies and search on google and
open youtube some basic question to ai like his name and age etc.
"""

from os import *
import os
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import subprocess
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

"""
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for "
          "`Microphone(device_index={0})`".format(index, name))
"""


# speak function actual speak as assistant
def speak(text):
    engine.say(text)
    engine.runAndWait()


# wishMe function wish you as per time
def wishme():
    hour = float(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak('good morning sir')

    elif 12 <= hour < 18:
        speak('good afternoon sir')

    else:
        speak('good evening sir')


# take command take voice command from user and change in to a string named "query"
def takecommand():
    r = sr.Recognizer()
    r.energy_threshold = 300

    with sr.Microphone(device_index=1) as source:
        print('listening...')
        while True:
            audio = r.listen(source)
            if audio is not None:
                break

    try:
        print('Recognising....')
        query = r.recognize_google(audio)
        print("you said: " + query)

    except Exception as e:
        print('say that again')
        query = None

    return query


# main program start from here

if __name__ == "__main__":

    wishme()  # wishme function calling

    years_str = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                 'november', 'december']

    date_str = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31st']

    # while loop is use for infinity time
    while True:

        # logic for executing task as per query
        query = takecommand()
        i = random.randint(0, 15)

        if query is not None:  # if query has no string then it not goes in

            # if you speak "wikipedia" in your query then what you say it search it on wikipedia
            if 'wikipedia' in query.lower():
                speak('searching wikipedia')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=1)
                speak(result)

            # if this condition is true then it open youtube on google-chrome
            elif 'open youtube' in query.lower():
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                url = "youtube.com"
                webbrowser.get(chrome_path).open(url)

            # if this condition is true then it open google chrome and it also search any url you speak
            # for this you have to say search "url(you want)"
            elif 'open google' in query.lower() or 'search' in query.lower():
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                query = query.replace("open google", "")
                if 'search' in query.lower():
                    query = query.split("search")
                    if " " in query:
                        query[1] = query[1].remove(" ", "")

                    url = query[1]

                else:
                    url = "google.com"

                webbrowser.get(chrome_path).open(url)

            # if this condition is true then it speak its name
            elif 'your name' in query.lower():
                speak("my name describe my game. Sage. how i can help you?")

            # if this condition is true then it close it self
            elif 'good bye' in query.lower() or 'goodbye' in query.lower() or 'bye' in query.lower() or 'shutdown' in query.lower():
                speak('good bye sir')
                os._exit(1)

            # if this condition is true then it speak its age
            elif 'how old are you' in query.lower() or 'what is your age' in query.lower():
                speak("I am created in year 2020")
                years = int(datetime.datetime.now().year)
                old = years - 2020
                speak('so ,i am ' + str(old) + 'year old')

            # if this condition is true then it replay your hello,hy,hey query
            elif 'hello' in query.lower() or 'hay' in query.lower() or 'hy' in query.lower() or 'hai' in query.lower():
                speak('hello, i am Sage')

            # if this condition is true then it try to open calculator
            elif 'open calculator' in query.lower():
                subprocess.call('calc.exe')

            elif 'close calculator' in query.lower():
                subprocess.call('TASKKILL /F /IM calc.exe')

            # if this condition is true then it try to open cmd
            elif 'open cmd' in query.lower() or 'open command prompt' in query.lower():
                subprocess.call('cmd.exe')

            # at this condition if true then it will play a random movie from your direct.
            elif 'play any movie' in query.lower():
                movie_dir = 'D:\\movies'
                movie = listdir(movie_dir)
                startfile(path.join(movie_dir, movie[i]))

            elif 'how are you' in query.lower():
                speak("i'm great. what i can do for you")

            elif 'i am fine' in query.lower():
                speak("i'm glad to hear it")

            elif 'flip a coin' in query.lower():
                coin_flip = random.randint(0, 1)
                if coin_flip == 1:
                    speak("its head")
                else:
                    speak("it's tail")

            elif 'what is your favourite colour' in query.lower():
                speak("i love rainbows, it makes me happy to see so many colours together")

            elif 'what is your favourite number' in query.lower():
                speak("Pi!")

            elif 'what is date' in query.lower():
                dates = datetime.datetime.now().day
                months = int(datetime.datetime.now().month)
                years = int(datetime.datetime.now().year)
                speak("Today is " + date_str[dates - 1] + years_str[months - 1] + str(years))
