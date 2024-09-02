import speaker
import gemini
import activator

qst = activator.ask()
print(qst)
print("\n wait a minute!")
answer = gemini.assitant(qst=qst)
audio_path = speaker.text_to_speech(answer)
print(answer)
speaker.play_audio(audio_path)
