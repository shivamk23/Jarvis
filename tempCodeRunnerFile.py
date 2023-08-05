
from Brain.qna import QuestionAnswer
from Brain.AiBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting Jarvis : Wait for Some Second...")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting Jarvis : Wait for Some Second...")
Speak("Hlo boss")
def MainExecution():

    Speak("Hlo sir ")
    Speak("I am Jarvis")

    while True:

        Data=MicExecution()
        Data=str(Data)

        if len(Data)<3:
            pass
        elif "What is " in Data or "where is" in Data or "question" in Data or "answer" in Data:
            reply=QuestionAnswer(Data)
            Speak(reply)
        else:
            reply=ReplyBrain(Data)
            Speak(reply)

# wakeup






def clapDetect(): 
    query = Tester()
    if "True-Mic" in query:
        Speak("Detected Owner..")
        MainExecution()
    else:
        pass

clapDetect()