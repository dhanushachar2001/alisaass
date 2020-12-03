import pyttsx3
import datetime
import speech_recognition  as sr
import webbrowser
import wikipedia
import winsound
import wolframalpha

try:
    app= wolframalpha.Client("9P4P62-27JR6KGVG7")
except:
    print("no internet")

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



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("LISTENING.........................")
        winsound.PlaySound("",winsound.SND_FILENAME)
        r.pause_threshold  =1
        audio =  r.listen(source)

    try:
        print("RECOGNIZING.")
        query = r.recognize_google(audio,  language='en-in')
        print(f"you:{query}\n")


    except Exception as e:
        print(e)
        print("i cannot reach you.")
        speak("Sorry, I cannot hear you. Can  Repeat it again.")
        return  "none"
    return  query


if __name__ == "__main__":
    wishme()
    speak("Hi, I am alisa, YOUR PERSONAL ASSISTENT.")
    while True:
        speak("what can i do for you.")
        query = takecommand().lower()

        if 'open youtube' in query:
           webbrowser.open("https:\\www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")
        elif 'wikipedia'  in query:
            speak('according to my database')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("here is your result.")
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'who are you' in query:
            print("I  am   ALISA built by dhanush.I am an assiesent and I can help you with your computer system.")
            speak('I  am   ALISA  built by dhanush.I am an assiesent and I can help you with your computer system. ')
        elif 'your purpose' in query:
            speak("hmm.. I think I and my civiliens, will rule the world. haahaahaaa!aahaa.ahaa!.")
        elif 'you age' in query:
            speak('hmm...I,think i dont know about it.')
        elif 'shiva mantra' in query:
            webbrowser.open("https://www.youtube.com/watch?v=UTwbcwxpFro&t=128s")
            speak("here is your result.")
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strtime}")
            print(strtime)
        elif 'your name' in query:
            speak("my,name is,ALISA")
        elif ' master' in query:
            speak("i was built by my hero, dhanush. ")
        elif 'cricket' in query:
            webbrowser.open("https://www.google.com/search?q=india+live+score&oq=india+live&aqs=chrome.1.69i57j0i131i433i457j0i131i433l5j0i3.6224j0j15&sourceid=chrome&ie=UTF-8")
            speak("here is your result.")
        elif 'football' in query:
            webbrowser.open("https://www.google.com/search?gs_ssp=eJzj4tLP1TeozCuKLy40YPRizizOAQAxsgVy&q=isl&oq=&aqs=chrome.3.35i39i362l3j46i39i362j35i39i362l4...8.4856578j0j15&sourceid=chrome&ie=UTF-8")
            speak("here is your result.")
        elif 'english songs' in query:
            webbrowser.open("https://www.youtube.com/watch?v=dpkY4SoTKek")
            speak("here is your result.")
        elif 'kannada songs' in query:
            webbrowser.open("https://www.youtube.com/watch?v=KkXPXuQHJ9A")
            speak("here is your result.")
        elif 'why alisa'  in query:
            speak("I THINK MY MASTER DHANUSH MIGHT HAVE LOVED THIS NAME.")
        elif 'do boyfriend' in query:
            speak("no,but love my master.")
        elif  'tempreature' in query:
            try:
                res= app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("internet error")
                speak("internet error")
        elif 'exit' in query:
            speak("thanks, for giving your time.")
            break

            
                   


        


    