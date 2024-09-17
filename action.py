from texttospeech import speak
from googleapiclient.discovery import build
import pyautogui
import time
import webbrowser
import os
import threading

def reminder(message, delay):
    def remind():
        time.sleep(delay)
        speak(message)
    
    thread = threading.Thread(target=remind)
    thread.start()

def open_website(url):
    webbrowser.open(url)
    speak(f'Đang mở trang web {url}')

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f'Đang tìm kiếm {query} trên web')

def open_file(file_path):
    try:
        os.startfile(file_path)
        speak(f'Đang mở file {file_path}')
    except Exception as e:
        speak(f'Đã xảy ra lỗi khi mở file: {e}')

def open_application(app_name):
    speak(f'Đang mở {app_name}')
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write(app_name, interval=0.25)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)

def close_application(app_name):
    speak(f'Đang đóng {app_name}')
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write(app_name, interval=0.25)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("alt", "f4")
    time.sleep(1)

YOUTUBE_API_KEY = 'AIzaSyBMXLmi4k7XuLkApQ7weKwAJbpm3e-eYys'
def search_youtube(video_name):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        part='snippet',
        q=video_name,
        type='video',
        maxResults=1
    )
    response = request.execute()
    
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(video_url)
        speak(f'Đang mở video {video_name} trên YouTube')
    else:
        speak('Không tìm thấy video nào phù hợp.')

def handle_command(command):
    if command.startswith("mở ứng dụng"):
        app_name = command.replace("mở ứng dụng", "").strip()
        open_application(app_name)
    elif command.startswith("đóng ứng dụng"):
        app_name = command.replace("đóng ứng dụng", "").strip()
        close_application(app_name)
    elif command.startswith("mở trang web"):
        url = command.replace("mở trang web", "").strip()
        open_website(url)
    # elif command.startswith("gửi email"):
    #     # Format: gửi email đến [email] với chủ đề [subject] và nội dung [body]
    #     # Implement email sending based on your needs
    #     pass
    elif command.startswith("mở file"):
        file_path = command.replace("mở file", "").strip()
        open_file(file_path)
    elif command.startswith("tìm kiếm"):
        query = command.replace("tìm kiếm", "").strip()
        search_web(query)
    elif command.startswith("mở youtube bài"):
        video_name = command.replace("mở youtube bài", "").strip()
        if video_name:
            search_youtube(video_name)
        else:
            speak("Vui lòng cung cấp tên video.")
    elif command.startswith("nhắc nhở"):
        # Format: nhắc nhở [message] sau [delay] giây
        # Implement reminder based on your needs
        pass
    elif command == 'dừng chương trình':
        speak("Tạm biệt bạn")
        return True
    return False