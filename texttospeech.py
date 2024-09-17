from gtts import gTTS
import playsound
import os

def speak(text):
    text_uppercase = text.lower()
    
    try:
        # Tạo file âm thanh từ văn bản
        output = gTTS(text_uppercase, lang="vi", slow=False)
        output.save("output.mp3")
        
        # Phát âm thanh
        playsound.playsound('output.mp3', True)
        
    except Exception as e:
        print(f"Đã xảy ra lỗi khi phát âm thanh: {e}")
        
    finally:
        # Xóa file âm thanh sau khi phát
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")