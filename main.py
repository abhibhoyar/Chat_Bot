from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

lucifer = ChatBot("My bot")

convo = {
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is lucifer , I am created by Abhishek ',
    'how are you ?',
    'I am doing great this days',
    'thankyou',
    'In which city you live ?',
    'I live in Pune',
    'In which language you talk ?',
    'I mostly talk english'
}

trainer = ListTrainer(lucifer)

# # now trainning the bot

trainer.train(convo)

# # answer = lucifer.get_response("?")
# # print(answer)

# while True:
#     print("Talk with lucifer")
#     query = input()
#     if query == 'exit':
#         break
#     answer = lucifer.get_response(query)
#     print("lucifer:",answer)

def takeQuery():
    sr = s.Recognizer()
    sr.phrase_threshold = 1
    print("you bot is listning try to speak")
    with s.Microphone() as m:
        audio = sr.listen(m)
        query = sr.recognize_google(audio,language='eng-in')
        print(query)
        textF.delete(0,END)
        textF.insert(0,query)
        ask_from_bot()

def ask_from_bot():
    query = textF.get()
    answer_from_bot = lucifer.get_response(query)
    msgs.insert(END,"you: "+query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot: "+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

main = Tk()

main.geometry("500x650")

main.title("My chat bot")
img = PhotoImage(file = "a.png")

PhotoL = Label(main,image=img)

PhotoL.pack(pady=5)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=10 , yscrollcommand = sc.set)


sc.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT , fill=BOTH,pady=10)

frame.pack()

textF = Entry(main, font=("Verdana",20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot",font=("Verdana",20),command = ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>' ,enter_function)

def repartL():
    while True:
        takeQuery()

t=threading.Thread(target=repartL)

t.start()

main.mainloop()