# Voice Controlled Robot using Python

# Install:

# pip install SpeechRecognition

# pip install PyAudio

import speech_recognition as sr
import time

def move_robot(command):
command = command.lower()

```
if "forward" in command:
    print("Robot: Moving Forward")

elif "backward" in command:
    print("Robot: Moving Backward")

elif "left" in command:
    print("Robot: Turning Left")

elif "right" in command:
    print("Robot: Turning Right")

elif "stop" in command:
    print("Robot: STOPPED")

else:
    print("Robot: Command not recognized")
```

def listen_command():
recognizer = sr.Recognizer()

```
with sr.Microphone() as source:
    print("\nListening...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    try:
        audio = recognizer.listen(source, timeout=5)

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        move_robot(command)

    except sr.WaitTimeoutError:
        print("No voice detected.")

    except sr.UnknownValueError:
        print("Could not understand the voice.")

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
```

print("===== VOICE CONTROLLED ROBOT =====")
print("Say: Forward, Backward, Left, Right, or Stop")
print("Say 'Exit' to close the program.")

while True:
command = input(
"\nPress Enter to give a voice command or type Exit: "
).lower()

```
if command == "exit":
    print("Robot System Closed.")
    break

listen_command()
```
