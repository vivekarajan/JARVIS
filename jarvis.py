import pyttsx3
import datetime
import speech_recognition as sr
import smtplib # send email library
from secret import senderemail,epwd,to
from email.message import EmailMessage
import wikipedia
import webbrowser as wb
import pywhatkit
from newsapi.newsapi_client import NewsApiClient
from nltk.tokenize import word_tokenize
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("today is")
    speak(date)
    speak(month)
    speak(year)

#date()
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning")
    elif hour >=12 and hour <18:
        speak("good afternoon")
    elif hour >=18 and hour <24:
        speak("good evening")
    else:
        speak("good night")
#greeting()

def wish():
    speak("welcome back sir")
    time()
    date()
    greeting()
    speak("jarvis at your service, please tell me how can i help you?")
#wish()

def sendEmail(senderemail, epwd, receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

#sendEmail(senderemail, epwd, to, "test", "This is a test email from Jarvis AI assistant.")

def google_search():
    speak("what should i search for?")
    search = takeCommandMIC()
    wb.open("https://www.google.com/search?q="+search)


def takeCommandCMD():
    query= input("please tell me how can i help you?\n")
    return query

def takeCommandMIC():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio,language="en-IN")
        print("user said :"+query)
    except  Exception as e:
            print(e)
            speak("say that again")
            return "None"
    return query

def search_yt():
    speak("what should i search for on Youtube?")
    topic =takeCommandMIC()
    pywhatkit.playonyt(topic)

def news():
    newsapi = NewsApiClient(api_key="f79380f6e1684319ad01993b39cf2cf6")
    speak("what topic you need the news about?")
    topic = takeCommandMIC()
    data= newsapi.get_top_headlines(q=topic,
                                    language="en",
                                    page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("that's it for now i'll update you in sometime")



if __name__ == "__main__":
    #wish()
    speak("hello i am jarvis")
    wakeward = "jarvis"
    while True:
        query=takeCommandMIC().lower()
        query=word_tokenize(query)
        print(query)
        if wakeward in query:
            if "time" in query:
                time()
            elif "date" in query:
                date()
            elif 'email' in query:
                try:
                    speak('what is the subject for  the email?')
                    subject = takeCommandMIC()
                    speak("what should i say?")
                    content = takeCommandMIC()
                    sendEmail(senderemail,epwd,to,subject,content)
                    speak("succesfully sent the email")

                except Exception as e:
                    print(e)
                    speak("unable to send the email!")

            elif 'wikipedia' in query:
                speak("searching on wikipedia...")
                query1 = query.replace("wikipedia"," ")
                result = wikipedia.summary(query1, sentences = 2)
                print(result)
                speak(result)
            elif "search" in query:
                google_search()
            elif 'youtube' in query:
                search_yt()
            elif 'news' in query:
                news()