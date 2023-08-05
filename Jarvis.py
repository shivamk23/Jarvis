
from Brain.qna import QuestionAnswer
from Brain.AiBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting Jarvis : Wait for Some Second...")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting Jarvis : Wait for Some Second...")

def MainExecution():

    Speak("Hlo sir ")
    Speak("How may I help You...?")

    while True:

        Data=MicExecution()
        Data=str(Data)

        if len(Data)<3:
            pass
        elif "what is " in Data or "where is" in Data or "question" in Data or "answer" in Data:
            reply=QuestionAnswer(Data)
            Speak(reply)
        elif "shutdown" in Data:
            Speak("Shutting Down, Have a good Day...")
            break
        else:
            reply=ReplyBrain(Data)
            Speak(reply)

# wakeup






def clapDetect(): 
    query = Tester()
    if "True-Mic" in query:
        Speak("Initializing Program... ")
        Speak("Hlo sir....Please provide your security code to authorize.")
        query1=MicExecution()
        if "shiva" in query1:
             MainExecution()

    else:
        pass
clapDetect()