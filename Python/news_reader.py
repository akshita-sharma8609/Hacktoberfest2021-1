# A NEWS READER - that reads news fetching from news api
# Note: To run this program, first Enter your API key in the apikey variable from NEWS API (https://newsapi.org/)

import requests        #install this module  as this is not a builtin module
import json            #builtin module


#function to convert text into speech
def speak(str):
      from win32com.client import Dispatch
      speak = Dispatch("SAPI.SpVoice")
      speak.Speak(str)


if __name__== '__main__':
     speak("news for you")
     apikey="Enter your api key"        #Enter your api key here
     url=f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apikey}"
     news=requests.get(url).text
     news_json=json.loads(news)
     arts=news_json['articles']
     count=5                         #number of news to listen
     speak("Todays news are")
     for i in arts:
           print(i['title'])
           speak(i['title'])
           if(count!=1):
                 speak("next news is")
           if(count==1):
                 speak("thanks for listening")
                 break
           count-=1
