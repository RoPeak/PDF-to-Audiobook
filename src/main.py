# Imports
from tts import tts_engine
from log import logger

# Global Variables
engine = None
logFile = None

def program_init():
    global engine, logFile
    logFile = logger()
    try:
        engine = tts_engine()
        logFile.log("TTS engine initialized")
    except:
        logFile.log("Error initializing TTS engine")
        return

def program_close():
    global engine, logFile
    try:
        engine.close()
        logFile.log("TTS engine closed")
    except:
        logFile.log("Error closing TTS engine")
    
    try:
        logFile.close()
    except:
        print("Error closing log file")
        return
    

def main():
    program_init()
    engine.speak("Hello World")
    program_close()

if __name__ == "__main__":
    main()