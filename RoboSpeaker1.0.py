import pyttsx3
#this is python module for converting text to speech

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.0")
    speaker = pyttsx3.init()
    while True:
        txt = input("Enter what you want to speak:")
        if txt == 'q':
            speaker.say("bye bye  my  friend")
            speaker.runAndWait()
            break
        speaker.say(txt)
        speaker.runAndWait()
#runAndWait is basically for the output to be generated and then proceed with further code!