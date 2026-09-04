# Speech recognition module
import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print("microphone initialized")
    
    def listen(self):
        """Listen or voice command"""
        with self.microphone as source:
             print("Listening...")
             try:
                 audio = self.recognizer.listen(source, timeout=5)
                 command = self.recognizer.recognize_google(audio)
                 print(f"You said : {command}")
                 return command.lower()
             
             except sr.WaitTimeoutError:
                 print("Timeout")
                 return  None
             
             except sr.UnknownValueError:
                 print("couldn't understand your audio")
                 return None
             
             except sr.RequestError:
                 print("Network error")
                 return None
        