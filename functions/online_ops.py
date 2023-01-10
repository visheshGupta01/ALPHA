import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import wolframalpha


RAPID_API = config("RAPID_API")
def ask_question(question): 

    url = "https://webknox-question-answering.p.rapidapi.com/questions/answers"

    querystring = {"question": question,
                "answerLookup": "checked", "answerSearch": "checked"}

    headers = {
        "X-RapidAPI-Key": "5862671939mshf5e0a4e3c4d1eeap1ad9d7jsn59589337529b",
        "X-RapidAPI-Host": "webknox-question-answering.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return response


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)  # type: ignore
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


TMDB_API_KEY = config("TMDB_API_KEY")


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


WOLFRAMALPHA_API_KEY = config("WOLFRAMALPHA_API_KEY")


def ask_a_question(question):
    client = wolframalpha.Client(WOLFRAMALPHA_API_KEY)
    res = client.query(question)
    print(res)
    answer = next(res.results).text
    return answer


QUOTE_API_KEY = config("RAPID_API")


def get_a_quote(category):

    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {"category": category, "count": "1"}

    headers = {
        "X-RapidAPI-Key": QUOTE_API_KEY,
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response
