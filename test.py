'''import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

def takecommand():
	r=sr.Recogniser()
	with sr.Microphone() as source:
		print("Listening")
		r.pause_threshold=0.5
		audio=r.listen(source)
		try:
			print("RECOGNISING")
			query=r.recognize_google(audio, language='en_in')
			print("the given command- ",query)
			
		except:
			print("Say that again sir")
			return "NONE"
		return query
		
def speak(audio):
	engine =pyttsx3.init()
	voices=engine.getProperty('voices')
	engine.setProperty('voices',voices['0'].id)
	engine.say(audio)
	engine.runAndWait()

def tellday():
	day=datetime.datetime.today().weekday()+1
	daydict={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
	if day in daydict.keys():
		dayow=daydict[day]
		print(dayow)
		speak("The day is " + dayow)

def telltime():
	time=str(datetime.datetime.now())
	print(time)
	speak("The time is " + time)
	
def hello():
	speak("Hello Boss! I am a noob mobile assistant./ How can I help you")

def takequery():
	hello()
	while(True):
		query=takecommand().lower()
		if "which day it is" in query:
			tellday()
			continue
		elif "what time it is" in query:
			telltime()
			continue
		elif "bye" in query:
			speak("Bye. Have a fruitful day")
			exit()
		elif "from wikipedia" in query:
			speak("Searching wikipedia")
			query=query.replace("wikipedia"," ")
			res=wikipedia.summary(query, sntences=4)
			speak(res)
		elif "what is your name" in query:
			speak("My creator is a stingy person, so he did not give me a name.")

if __name__ == '__main__':
        takequery()
'''
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.10.0')

# common modules
import sys
import os
import time
import signal
from multiprocessing import Process

# Flask modules
from flask import Flask

# wsgi (Web Server Gateway Interface) modules
import eventlet
from eventlet import wsgi

# async server setup
app = Flask(__name__)

def signal_handler(signal, frame):
    print (" CTRL + C detected, exiting ... ")
    exit(0)
     
class MainScreen(Screen):
    def __init__(self, **kwargs):
        self.name="MAIN SCREEN"
        super(Screen, self).__init__(**kwargs)

class MainApp(App):
    MainScreenTitle = "MainScreen title"
    MainScreenLabel = "MainScreen label"
    MessageButtonEnter = "START"
    MessageButtonExit = "EXIT"

    def start_Flask(self):
        print("Starting Flask...")
        wsgi.server(eventlet.listen(('', 5000)), app)     # deploy as an eventlet WSGI server

    def stop(self):
        print("terminating Flask and exiting...")
        global p1
        p1.terminate()
        exit(1)

    def start(self):
        print ("starting Flask as process...")
        global p1
        p1 = Process(target=self.start_Flask) # assign Flask to a process
        p1.daemon = True
        p1.start()  #launch Flask as separate process

    def build(self):
        sm = Builder.load_string("""

ScreenManager
    MainScreen:
        size_hint: 1, .7
        auto_dismiss: False
        title: app.MainScreenTitle       
        title_align: "center"

        BoxLayout:
            orientation: "vertical"
            Label:
                text: app.MainScreenLabel
            BoxLayout:
                orientation: "horizontal"
                spacing: 10
                size_hint: 1, .5
                Button:
                    text: app.MessageButtonEnter  # start app
                    on_press:
                        app.start()
                Button:
                    text: app.MessageButtonExit  # exit app
                    on_press:
                        app.stop()

        """)

        return sm


# main ################################################
if __name__ == '__main__':

    #CTRL+C signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    MainApp().run()