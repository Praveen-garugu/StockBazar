import pyttsx3

# Text to be converted to speech
def speech(text):

# Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 140)
    # engine.setProperty("volume", 0.9)  # Volume level (0.0 to 1.0)

    # Convert text to speech and play it
    engine.say(text)
    engine.runAndWait()
