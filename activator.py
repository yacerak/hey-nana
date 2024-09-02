from speech_recognition import *

def ask():
    # Initialize recognizer and microphone
    recognizer = Recognizer()
    microphone = Microphone()

    # Continuously listen for audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print("speak")
            activate = recognizer.listen(source)
            print("wait")
            try:
                act_text = recognizer.recognize_google(activate)

                if act_text.lower() == ("hey nana" or "nana" or "listen nana"):
                    print("i am lestning")
                    order = recognizer.listen(source)
                    ord_text = recognizer.recognize_google(order)
                    #print(ord_text)
                    return ord_text
                    break

            except UnknownValueError:
                print("Could not understand audio")
            except RequestError as e:
                print(f"Request failed: {e}")

#ask()