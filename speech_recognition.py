import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand you.")
    except sr.RequestError:
        print("Sorry, there's an error with the speech recognition service.")



listen_for_command()