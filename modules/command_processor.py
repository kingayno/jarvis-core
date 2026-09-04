 #command processor module
import datetime
import webbrowser
import requests

class CommandProcessor:
        def __init__(self):
          self.commands = {
            "time": self.get_time,
            "date": self.get_date,
            "search": self.search_web,
            "open": self.open_website,
            "weather": self.get_weather
        }

        def process(self, command):
            """process user command"""
            if not command:
                return "i didnt catch that"
            
            if 'exit' in command or 'quit' in command:
                return "exit"
            if 'hello' in command or 'hi' in command:
                return "hello! What can I help you"
            
            for keyword, func in self.commands.item():
                if keyword in command:
                    return func(command)
            
            return "I am not sure how to help with that!"
        def get_time(self, command):
            current_time = datetime.datetime.now().strftime("%I:%M %P")
            return f"todays time is: {current_time}"
        
        def get_date(self, command):
            current_date = datetime.datetime.now().strftime("%A, %B, %B, %Y")
            return f"today is {current_date}"
        
        def search_web(self, command):
            query = command.replace("search", "").replace("for", "").strip()
            if query:
                webbrowser.open(f"https://google.com/search?q={query}")
                return f"serching for {query}"
            return "what would you like to search for?"
        
        def open_website(self, command):
            if 'youtube' in command:
                webbrowser.open("https://youtube.com")
                return "opening youtube"
            elif 'google' in command:
                webbrowser.open("https://google,com")
                return "opening google"
            return "I can open YouTube or Google"
        def get_weather(self, command):
            try:
                from config import Config
                city = "London"
                if "in" in command:
                    city = command.split('in')[1].strip()
                
                url = "https://api.openweathermap.org/data/2.5/weather"
                params = {
                    'q' : city,
                    'appid' : Config.OPENWEATHER_API_KEY,
                    'units' : 'metric'
                }
                response = requests.get(url, params=params)
                data = response.json()

                temp = data['main']['temp']
                desc = data['weather'][0]['discription']

                return f"the tempreture in {city} is {temp}°C with {desc}"
            except:
                return "could not fetch weather"