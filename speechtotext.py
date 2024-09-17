import speech_recognition as sr

def recognizer():
    r = sr.Recognizer()
    text = ""  # Khởi tạo biến text với giá trị mặc định

    with sr.Microphone() as source:
        print("Mời bạn nói: ")
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language="vi-VI")
            print("Bạn -->: {}".format(text))
        except sr.UnknownValueError:
            print("Xin lỗi, tôi không nhận được voice!")
        except sr.RequestError as e:
            print(f"Xin lỗi, có lỗi xảy ra với dịch vụ nhận diện giọng nói: {e}")

    return text