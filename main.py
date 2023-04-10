import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import winshell as winshell

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    # engine.say('What can i do for you')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")

    elif 'fine' in command or "good" in command:
        talk("It's good to know that your fine")



    elif "who made you" in command or "who created you" in command:
        talk("I have been created by Harshal.")


    elif 'empty recycle bin' in command or "clean my recycle bin" in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        talk("Recycle Bin is Cleared")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is ' in command:
        person = command.replace('Who is the', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'are you single' in command:
        talk('iam already in with wifi')


    elif 'joke' in command:
        talk(pyjokes.get_joke())


    elif 'government polytechnic pen' in command:
        talk('The Government Polytechnic Pen is an institute of technology located in Pen, Raigad district in the Indian state of Maharashtra. It was established in 1990 by the Government of Maharashtra and was initially located in Alibag.')



    elif 'what is' in command:
        obj_1 = command.replace('what is', '')
        info1 = wikipedia.summary(obj_1, 2)
        print(info1)
        talk(info1)


    elif 'who found' in command:
        obj_2 = command.replace('who found', '')
        info2 = wikipedia.summary(obj_2, 2)
        print(info2)
        talk(info2)

    elif 'competitor' in command:
        talk("my competition is Alexa and Google Voice assistant")

    elif 'open google' in command:
        obj_3 = webbrowser.open('https://www.google.com/')
        talk('opening google')
        # talk('opening google')


    elif 'open youtube' in command:
        obj_4 = webbrowser.open('https://www.youtube.com/')
        talk('opening youtube')
        # print(obj_4)


    # elif 'location' in command:
    #     obj_5 = geocoder.ip('me')
    #     talk(obj_5.latlng)

    else:
        # talk('please say command again')
        print('Please say command again......!')
        talk('Please say command again')


while True:
    run_alexa()



