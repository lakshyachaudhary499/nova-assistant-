import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary
import livenews
import tasks



recognizer= sr.Recognizer()

engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

            
     
            

if __name__== "__main__":
    speak("activating  nova..... ")   
 
 
def processcommand(c):
     if "open google" in c.lower():
         webbrowser.open("https://google.com")
     elif "open youtube" in c.lower():
         webbrowser.open("https://www.youtube.com")    
     elif "open instagram" in c.lower():
         webbrowser.open("https://www.instagram.com")    
     elif "open linkedin" in c.lower():
         webbrowser.open("https://www.linkedin.com")
     elif "open linkedin" in c.lower():
         webbrowser.open("https://www.linkedin.com")
     elif "open facebook" in c.lower():
         webbrowser.open("https://www.facebook.com")    
     elif"open github" in c.lower():
        webbrowser.open("https://www.github.com")
     elif"open twitter" in c.lower():
        webbrowser.open("https://x.com")
     elif"open whatsapp" in c.lower():
        webbrowser.open("https://www.whatsapp.com/")
     elif"open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com")   
     elif"open gmail" in c.lower():
        webbrowser.open("https://www.gmail.com")    
     elif"open maps" in c.lower():
        webbrowser.open("https://www.googlemaps.com")    
     elif"open amazon" in c.lower():
         webbrowser.open("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=2282987013005222396&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9301990&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")  
     elif"open flipkart" in c.lower():
        webbrowser.open("https://www.flipkart.com/")  
     elif"open myntra" in c.lower():
        webbrowser.open("https://www.myntra.com/")    
         
     elif"open telegram" in c.lower():
        webbrowser.open("https://web.telegram.org/k/#-4578198448") 
               
     elif"open discord" in c.lower():
        webbrowser.open("https://www.discord.com/") 
         
         
     elif c.lower().startswith("play"):
         song = c.lower().split(" ")[1]
         link = musiclibrary.music[song] 
         webbrowser.open(link)
         
     elif c.lower().startswith("show"):
         live = c.lower().split(" ")[1]
         link = livenews.news[live] 
         webbrowser.open(link)
     elif c.lower().startswith("open"):
         doit = c.lower().split(" ")[1]
         link = tasks.task[doit] 
         webbrowser.open(link)  
while True:
    r = sr.Recognizer()
   
    print("processing....")

    
    try:
         with sr.Microphone() as source:
           print("listening....")
           audio = r.listen(source,timeout=2,phrase_time_limit=1)
         initializing= r.recognize_google_cloud(audio)  
         print(initializing)
         if (initializing.lower() == "hello"):
             speak("hello sir")
         elif (initializing.lower() == "how are you"):
             speak(" i am good how was your day sir ")  
         elif (initializing.lower() == "who are you"):
             speak(""" hello sir my name is nova i am a project created by lakshya chaudhary  I can play your favorite music stored in my library  and keep you entertained  I can open your favorite social media websites instantly  I provide real-time cricket scores, weather updates, and more  i can open shopping websites for you.
                   I can launch your calculator and handle other basic tasks effortlessly        
                   """)                  
         elif (initializing.lower() == "what can you do"):
             speak("""   I can play your favorite music and keep you entertained  I can open your favorite social media websites instantly  I provide real-time cricket scores, weather updates, and more  i can open shopping websites for you.
                   I can launch your calculator and handle other basic tasks effortlessly  """)
        
               
             with sr.Microphone() as source:
                print("nova is active.....")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
         command= r.recognize_google_cloud(audio)   
         processcommand(command)  
    except Exception as e:
        print("nova error; {0}".format(e))
