#main.py
import sys
from config import Config
from modules.speech_recognizer import SpeechRecognizer
from modules.text_to_speech import TextToSpeech
from modules.command_processor import CommandProcessor



class JARVIS:

    def __init__(self):

        print(" Initialize JARVIS....")

        Config.validate_keys()
        #Initialize modules

        self.speech = SpeechRecognizer()
        self.tts = TextToSpeech(
            rate= Config.VOICE_RATE,
            volume= Config.VOICE_VOLUME
        )

        self.processor = CommandProcessor()
        print(f"Hello, I am {Config.ASSISTANT_NAME}")

    def run(self):
        """main loop"""
        while True:
            #listen for command

            command = self.speech.listen()
            
            if command:
                #process command
               response = self.processor.process(command)

               if response == 'exit':
                   self.tts.speak('Goodbye')
                   break

               self.tts.speak(response)

if __name__ == "__main__":
    try:
        assistant = JARVIS()
        assistant.run()

    except KeyboardInterrupt:
        print("\n JARVIS terminated")
    except Exception as e:
        print(f"❌ Error: {e}")

