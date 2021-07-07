import speech_recognition as sr


def voice_rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return 'no match'
    except sr.RequestError as e:
        print('server error')


print(voice_rec())