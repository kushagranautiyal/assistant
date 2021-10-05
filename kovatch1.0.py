import pyttsx3       #text to speech conv. lib
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

        try:
            print("Recognizing")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}")

        except Exception as e:
            speak("say that again please...")
            return "none"
        return query


if __name__ == "__main__":
    takecommand()
    #speak("hello sir")