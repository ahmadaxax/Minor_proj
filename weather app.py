import requests
import json
import win32com.client
city =input("enter the name of the city \n")
url =f"https://api.weatherapi.com/v1/current.json?key=4b666b5dc4cc44cab40203509242905&q={city}"
r=requests.get(url)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print(w)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(f"say 'the current weather in {city} is {w} degrees celcius\n") 