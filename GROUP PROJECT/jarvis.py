import pyttsx3
import speech_recognition as sr
import datetime
import os





engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
 



#TEXT TO SPEECH
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




#SPEECH TO TEXT
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=4,phrase_time_limit=5)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}")
    except Exception as e:
        speak("please run program again")
        return"none"
    return query




#GREET FUNCTION
def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")







if __name__=="__main__":
    greet()
    if 1:
        query=takecommand().lower()
        #LOGIC BUILDING FOR TASK
        if "open notepad" in query:
            path ="C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)
        if "who is the best teacher in the world" in query:
            speak("no doubt, sir umar iqbal is the best teacher in the world")
        if "open word" in query:
            path="C:\\KAM 25\\WORK PROFILE\\ICT\\Semester project 2\\APPS\\word\\Word 2016.lnk"
            os.startfile(path)
        if "open spotify" in query:
            path="C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.174.631.0_x86__zpdnekdrzrea0\\Spotify.exe"
            os.startfile(path)
        if "open camera" in query:
            path="C:\\KAM 25\\WORK PROFILE\\ICT\\Semester project 2\\APPS\\CAMERA\\Camera.lnk"
            os.startfile(path)
        if "open vlc media player" in query:
            path="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(path)
        if "open excel" in query:
            path="C:\\KAM 25\\WORK PROFILE\\ICT\\Semester project 2\\APPS\\Excel\\Excel 2016.lnk"
            os.startfile(path)
        if "open powerpoint" in query:
            path="C:\\KAM 25\\WORK PROFILE\\ICT\\Semester project 2\\APPS\\Powerpoint\\PowerPoint 2016.lnk"
            os.startfile(path)
        if "open teams" in query:
            path="C:\\KAM 25\\WORK PROFILE\\ICT\\Semester project 2\\APPS\\teams\\Microsoft Teams.lnk"
            os.startfile(path)
        if "open utorrent" in query:
            path="C:\\KAM 25\\WORK PROFILE\\ICT\\Semester project 2\\APPS\\utorrent\\µTorrent.lnk"
            os.startfile(path)
        





