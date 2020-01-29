import speech_recognition as sr
import json


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        print('Recognizing...')
        text = r.recognize_google(audio_data)
        print(text)
        text_to_instruction(text)

def text_to_instruction(text):
    if (('next' in text) or ('ahead' in text) or ('forward' in text)) and ('slide' in text):
        print(json.dumps({"intent": "next_slide"}))
        return json.dumps({"intent": "next_slide"})
    elif (('previous' in text) or ('backward' in text) or ('behind' in text)) and ('slide' in text):
        print(json.dumps({"intent": "previous_slide"}))
        return json.dumps({"intent": "previous_slide"})
    elif ('insert' in text) and ('image' in text):
        print(json.dumps({"intent": "insert_image"}))
        return json.dumps({"intent": "insert_image"})
    else:
        print(json.dumps({"intent": "scrape", "text": text}))
        return json.dumps({"intent": "scrape", "text": text})

speech_to_text()