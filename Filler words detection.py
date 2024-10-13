import speech_recognition
import pyttsx3

count = 0
total_count = 0
used_array = []
filler_words = {
    "well": 0,
    "um": 0,
    "er": 0,
    "uh": 0,
    "hmm": 0,
    "like": 0,
    "actually": 0,
    "basically": 0,
    "seriously": 0,
    "literally": 0,
    "totally": 0,
    "clearly": 0,
    "okay": 0,
    "so": 0,
    "right": 0,
    "mhm": 0,
    "uhhuh": 0,
}

speech = speech_recognition.Recognizer() # Object to pick sound through microphone
while True:

    try:
        with speech_recognition.Microphone() as mic: # captures audio

            speech.adjust_for_ambient_noise(mic, duration = 0.2) # to Recognize when you start and stop talking
            audio = speech.listen(mic)

            text = speech.recognize_google(audio) # source to convert speech to text
            text = text.lower()

            text_array = text.split()
            for word in filler_words:
                count = text_array.count(word.lower())
                total_count += count
                filler_words[word] += count

            print(f"audio {text}")
            print("Number of filler words used",total_count)

            for key, value in filler_words.items():
                if value > 0:
                    used_array.append(key)
            print("filler words used: ", used_array)

    except speech_recognition.UnknownValueError:
        speech = speech_recognition.Recognizer()
        continue
