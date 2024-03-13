import speech_recognition as sr
import pyttsx3
import pywhatkit

name = "Jarvis"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Te estoy escuchando...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            rec = listener.recognize_google(audio, language="es-ES")
            rec = rec.lower()
            print("Has dicho: ", rec)
            return rec
    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")  
        return ""
    except sr.RequestError as e:
        print(f"No se puede obtener la respuesta del servicio de reconocimiento de voz; {e}")
        return ""

def run_Jarvis():
    rec = listen()
    if rec:
        if "reproduce" in rec:
            music = rec.replace("reproduce", "")
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
        else:
            print("Comando no reconocido")

if __name__ == "__main__":
    run_Jarvis()