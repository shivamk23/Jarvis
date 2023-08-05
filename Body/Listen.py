# Command in hindi or English 
# Respose in English

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0


# 1-Listen Hindi Or English
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,20)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en')
       
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    query =str(query).lower()
    return query

# 2- Translation
def TranslationHinToEng(Text):
    line =str(Text)
    translator = Translator()
    result = translator.translate(line)
    data= result.text
    print(f"User Said: {data}\n")
    return data

#- connecting Lisen with translation
def MicExecution():
    query=Listen()
    data=TranslationHinToEng(query)
    return data

