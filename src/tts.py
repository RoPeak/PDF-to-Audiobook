import pyttsx3

class tts_engine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def test_voices(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            print(voice, voice.id)
            self.engine.setProperty('voice', voice.id)
            self.engine.say("Hello World!")
            self.engine.runAndWait()

    def close(self):
        self.engine.stop()