# VirtuJane

VirtuJane là một trợ lý ảo mạnh mẽ được xây dựng bằng Python, thiết kế để thực hiện các lệnh giọng nói và tự động hóa các tác vụ trên máy tính. Dự án sử dụng các công nghệ như `pyautogui`, `speech_recognition`, và `gTTS` để tạo ra một trợ lý ảo thông minh và hiệu quả.

## Tính năng chính

- **Mở ứng dụng:** Mở bất kỳ ứng dụng nào trên máy tính bằng lệnh giọng nói.
- **Đóng ứng dụng:** Đóng bất kỳ ứng dụng nào trên máy tính bằng lệnh giọng nói.
- **Tìm kiếm trên YouTube:** Tìm kiếm và mở video đầu tiên trên YouTube dựa trên tên bài hát hoặc video.
- **Mở trang web:** Mở bất kỳ trang web nào bằng lệnh giọng nói.
- **Tìm kiếm web:** Tìm kiếm thông tin trên web từ lệnh giọng nói.

## Hướng dẫn cài đặt

1. **Clone repository:**
   ```bash
   git clone https://github.com/yourusername/VirtuJane.git
   cd VirtuJane
   ```
2. **Install dependencies:**
  ```bash
    pip install pyautogui
    pip install SpeechRecognition
    pip install pyaudio
    pip install gTTS
    pip install playsound
  ```

  **GIẢI THÍCH THƯ VIỆN:**
  -  pyautogui: Thư viện để tự động hóa các thao tác chuột và bàn phím.
  -  SpeechRecognition: Thư viện để chuyển đổi giọng nói thành văn bản.
  -  pyaudio: Thư viện cần thiết cho SpeechRecognition để xử lý âm thanh.
  -  gTTS: Thư viện để chuyển văn bản thành giọng nói.
  -  playsound: Thư viện để phát file âm thanh MP3.

## Hướng dẫn sử dụng

1. **Chạy ứng dụng:**
  ```bash
    python main.py
  ```
2. **Nhập lệnh bằng giọng nói:**
-  Mở ứng dụng: Nói "mở [tên ứng dụng]" để mở ứng dụng cụ thể.
-  Đóng ứng dụng: Nói "đóng [tên ứng dụng]" để đóng ứng dụng cụ thể.
-  Tìm kiếm video trên YouTube: Nói "mở youtube bài [tên bài hát]" để tìm kiếm và mở video đầu tiên trên YouTube.
-  Mở trang web: Nói "mở trang web [URL]" để mở trang web.
-  Tìm kiếm web: Nói "tìm kiếm [từ khóa]" để tìm kiếm thông tin trên web.
