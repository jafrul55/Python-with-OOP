# # import pyttsx3
# from gtts import gTTS
# import gtts #for nural voice

# # engine = pyttsx3.init()

# def text_to_speech(text, output_file_name):
#     # engine.setProperty('rate',150)
#     # engine.save_to_file(text, output_file_name + '.mp3')
#     # engine.runAndWait()
#     tss = gTTS(text=text,lang='en')
#     tss.save(output_file_name + '.mp3')

# input_text = input("Enter Text: ")

# output_file_name = 'output'

# text_to_speech(input_text, output_file_name)


import pyttsx3

engine = pyttsx3.init()

def text_to_speech(text, output_file_name):
    engine.setProperty('rate', 150) # Set the speech rate to 150 words per minute
    engine.setProperty('volume', 0.5) # Set the volume to 0.5 (50%)
    engine.setProperty('voice', 'en') # Set the voice to a female voice
    engine.setProperty('pitch', 100) # Set the pitch to 100 (normal)
    engine.save_to_file(text, output_file_name + '.mp3')
    engine.runAndWait()

input_text = input('Enter Text: ')

output_file_name = 'output'

text_to_speech(input_text, output_file_name)

