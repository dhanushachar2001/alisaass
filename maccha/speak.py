import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
        print("{^^......^^}")
        print(" (...--...)")
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("GOOD MORNING  DHANUSH.")
        elif hour>=12  and hour<18:
            speak("GOOD AFTERNOON  DHANUSH.")
        else:
            speak("GOOD EVENING  DHANUSH. ")

def command():
    a = input("Enter the text to be speaked---------------->>>>")
    print("You have entered::--->>>",a)
    
    if 'exit' in a:
            speak("ok ,I will exit.")
            exit(0)
    elif 'what are you doing' in a:
            speak("nothing special.")
    elif  'who is your master' in a:
            speak("simply dhanush.")
    else:
            speak(a)

   
    

if __name__ == "__main__":
    wishme()
    
    
    while True:
             command()
        
        

