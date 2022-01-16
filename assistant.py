import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import webbrowser
import time
import wolframalpha
import requests
import random

print("Loading your personal AI assistant Google wannabe")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def greeting(text):
    Greeting_Inputs = ['hi', 'hey', 'hola', 'bonjour', 'hello']
    Greeting_Response = ['hi', 'hey', 'hola', 'greetings', 'bonjour', 'hello']

    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Response)
    return ''

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I don't think I understand, could you please repeat?")
            return "None"
        return statement

def wakeWord(text):
    WAKE_WORD = ['Hey Google wannabe']

    text = text.lower()

    for phrase in WAKE_WORD:
        if phrase in text:
            return True
    return False

print("Loading your AI personal assistant Google wannabe")
speak("Loading your AI personal assistant Google wannabe")
wishMe()

if __name__=='__main__':


    while True:
        speak("Let me know how I can help")
        statement = takeCommand().lower()
        if statement==0:
            continue
            
        if "good bye" in statement or "okay bye" in statement or "stop" in statement:
            speak('your personal assistant Google wannabe is shutting down, Good bye')
            print('your personal assistant Google wannabe is shutting down, Good bye')
            break
            
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.ca")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            
        elif "weather" in statement:
            api_key=" "
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
                
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.cbc.ca/news")
            speak('Here are some headlines from CBC, Canadian Broadcasting Corporation news, Happy reading!')
            time.sleep(6)
                                           
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
                                           
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions. What question do you want to ask now')
            question=takeCommand()
            app_id=" "
            client = wolframalpha.Client('')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)       
                                        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your personal assistant. I am programmed to do tasks like'
                  'opening youtube, google chrome, gmail, tell the time, take a photo, search wikipedia, and even predict weather in different cities.' 
                  'I can also get top headline news from CBC news Canada. You can ask me computational or geographical questions too! Let me know how I can help.')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Aarabhi")
            print("I was built by Aarabhi")
			
time.sleep(3)                               
