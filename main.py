from action import handle_command
from speechtotext import recognizer
from texttospeech import speak
 
if __name__ == "__main__":
    while True:
        message = recognizer().lower()
        if handle_command(message):
            break