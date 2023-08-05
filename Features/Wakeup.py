import speech_recognition as sr
import os 

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en')
       
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    query =str(query).lower()
    print(query)
    return query


def wakeupDetected():
    query= Listen().lower()

    if "wake up" in query:
        print("Detected Owner..")       
        
        # os.startfile("C:/Users/HP/Desktop/university/jarvis/main.py")
    else:
        pass
    
while True:

    query=wakeupDetected()
    if "wake up" in query:
        break