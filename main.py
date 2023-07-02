from datetime import datetime
import pyttsx3
from decouple import config
import speech_recognition as sr
from random import choice
from utils import opening_text, hello
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, \
    get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message, \
    ask_a_question, get_a_quote,play_song
from functions.os_ops import open_app, decrease_volume,increase_volume,mute_volume,play_next,pause,play_previous
from pprint import pprint
from win10toast import ToastNotifier
import os

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

toast = ToastNotifier()
toast.show_toast("Alpha", "The assistant will be started soon!!", duration=30)

os.chdir("E:\Projects\ALPHA")  # type: ignore

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 150)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to Speech Conversion


def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME} sir")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME} sir")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME} sir")
    speak(f"I am {BOTNAME}. How may I assist you?")


workingState = True


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    global workingState

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)

        if 'wake up Alpha' in query:
            speak('Yes sir, Alpha in your service!')
            workingState = True
        if "that's all" in query or "not now" in query or 'please wait alpha' in query:
            workingState = False
            speak("You can call me if you want...")
    except Exception:
        if workingState == True:
            speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()

    while True:
        query = take_user_input().lower()  # type: ignore

        if 'open' in query and workingState == True:
            app = query.split(" ", 1)
            speak(choice(opening_text))
            open_app(app[1])

        elif 'hello' in query and workingState == True or 'hai' in query and workingState == True or 'hi' in query and workingState == True:
            speak(choice(hello))

        elif 'ip address' in query and workingState == True:
            speak(choice(opening_text))
            ip_address = find_my_ip()
            speak(
                f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query and workingState == True:
            speak(choice(opening_text))
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()  # type: ignore
            print(search_query)
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query and workingState == True:
            speak(choice(opening_text))
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()  # type: ignore
            play_on_youtube(video)

        elif 'search on google' in query and workingState == True:
            speak(choice(opening_text))
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()  # type: ignore
            search_on_google(query)

        elif "send whatsapp message" in query and workingState == True:
            speak(choice(opening_text))
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()  # type: ignore
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "email" in query and workingState == True:
            speak(choice(opening_text))
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()  # type: ignore
            speak("What is the message sir?")
            message = take_user_input().capitalize()  # type: ignore
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak(
                    "Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query and workingState == True:
            speak(choice(opening_text))
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query and workingState == True:
            speak(choice(opening_text))
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query and workingState == True:
            speak(choice(opening_text))
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query and workingState == True:
            speak(choice(opening_text))
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query and workingState == True:
            speak(choice(opening_text))
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(
                f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(
                f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'ask' in query or 'math' in query and workingState == True:
            speak(choice(opening_text))
            speak('What do you want to ask, sir?')
            question = take_user_input().lower() # type: ignore
            answer = ask_a_question(question)
            print(answer)
            if answer in locals():
                speak(f"The answer is,{answer}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(answer)
            else:
                speak("I can't find answer to this question!")

        elif 'exit' in query:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()

        elif 'quote' in query and workingState == True:
            speak(choice(opening_text))
            speak("On what topic did you want a quote ,sir")
            category = take_user_input().lower() # type: ignore
            if category == "random":
                category = "all"
            quote = get_a_quote(category)
            speak("Here is a quote for you sir")
            speak(quote.text)
        
        elif 'increase volume' in query and workingState == True:
            speak(choice(opening_text))
            increase_volume()

        elif 'decrease volume' in query and workingState == True:
            speak(choice(opening_text))
            decrease_volume()

        elif 'mute volume' in query and workingState == True or 'unmute volume' in query and workingState == True:
            speak(choice(opening_text))
            mute_volume()

        elif 'play next' in query and workingState == True:
            speak(choice(opening_text))
            play_next()

        elif 'play previous' in query and workingState == True:
            speak(choice(opening_text))
            play_previous()
            
        elif 'pause' in query and workingState == True or 'pose' in query and workingState == True:
            speak(choice(opening_text))
            pause()

        elif 'play song' in query and workingState == True:
            speak(choice(opening_text))
            speak("What is the name of the song you want to play?")
            song_name = take_user_input().lower()
            play_song(song_name)
            speak("The song has been played")