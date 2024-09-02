from gtts import gTTS
import pygame

def text_to_speech(mytext):
    myobj = gTTS(text=mytext, lang='en', slow=False)

    myobj.save("answer.mp3")
    return "answer.mp3"

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("An error occurred while playing the audio:", e)

