
'''
import pywhatkit
import datetime
import wikipedia
import os
import psutil
from assistant.speaker import talk

# Track opened applications
opened_apps = []

def handle_command(command):
    command = command.lower()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
        if "chrome.exe" not in opened_apps:
            opened_apps.append("chrome.exe")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {current_time}")

    elif 'who is' in command or 'what is' in command:
        topic = command.replace('who is', '').replace('what is', '').strip()
        try:
            info = wikipedia.summary(topic, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn't find information.")

    elif 'search' in command:
        query = command.replace('search', '').strip()
        talk(f"Searching for {query}")
        pywhatkit.search(query)

    elif 'open' in command:
        app = command.replace('open', '').strip().lower()
        if 'youtube' in app:
            talk("Opening YouTube")
            os.system('start https://www.youtube.com')
            if "chrome.exe" not in opened_apps:
                opened_apps.append("chrome.exe")
        elif 'google' in app:
            talk("Opening Google")
            os.system('start https://www.google.com')
            if "chrome.exe" not in opened_apps:
                opened_apps.append("chrome.exe")
        elif 'gmail' in app:
            talk("Opening Gmail")
            os.system('start https://mail.google.com')
            if "chrome.exe" not in opened_apps:
                opened_apps.append("chrome.exe")
        elif 'facebook' in app:
            talk("Opening Facebook")
            os.system('start https://www.facebook.com')
            if "chrome.exe" not in opened_apps:
                opened_apps.append("chrome.exe")
        elif 'instagram' in app:
            talk("Opening Instagram")
            os.system('start https://www.instagram.com')
            if "chrome.exe" not in opened_apps:
                opened_apps.append("chrome.exe")
        else:
            talk(f"Opening {app}")
            open_application(app)

    elif 'stop' in command:
        if 'youtube' in command:
            talk("Closing YouTube")
            close_specific_app("chrome.exe")
        elif 'notepad' in command:
            talk("Closing Notepad")
            close_specific_app("notepad.exe")
        elif 'chrome' in command:
            talk("Closing Chrome")
            close_specific_app("chrome.exe")
        elif 'calculator' in command:
            talk("Closing Calculator")
            close_specific_app("calculator.exe")
        elif 'assistant' in command or 'exit' in command or 'bye' in command:
            talk("Goodbye! Exiting the assistant.")
            os._exit(0)
        else:
            talk("Tell me which app to close.")

    elif 'exit' in command or 'bye' in command:
        talk("Goodbye! See you later.")
        os._exit(0)

    else:
        talk("I didn't understand that command.")

def open_application(app):
    if 'notepad' in app:
        os.system("notepad.exe")
        if "notepad.exe" not in opened_apps:
            opened_apps.append("notepad.exe")
    elif 'calculator' in app:
        os.system("calc.exe")
        if "calculator.exe" not in opened_apps:
            opened_apps.append("calculator.exe")
    elif 'chrome' in app:
        os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
        if "chrome.exe" not in opened_apps:
            opened_apps.append("chrome.exe")
    elif 'vscode' in app or 'code' in app:
        os.system(r'"C:\Program Files\Microsoft VS Code\Code.exe"')
        if "Code.exe" not in opened_apps:
            opened_apps.append("Code.exe")
    elif 'wireshark' in app:
        os.system(r'"C:\Program Files\Wireshark\Wireshark.exe"')
        if "Wireshark.exe" not in opened_apps:
            opened_apps.append("Wireshark.exe")
    elif 'edge' in app or 'microsoftedge' in app:
        os.system(r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')
        if "msedge.exe" not in opened_apps:
            opened_apps.append("msedge.exe")
    else:
        talk("I don't know that application.")

def close_specific_app(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                proc.kill()
                if process_name in opened_apps:
                    opened_apps.remove(process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

'''



import pywhatkit
import datetime
import wikipedia
import os
import psutil
from assistant.speaker import talk

# Track opened applications
opened_apps = []

def handle_command(command):
    command = command.lower()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
        if "chrome.exe" not in opened_apps:
            opened_apps.append("chrome.exe")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {current_time}")

    elif 'who is' in command or 'what is' in command:
        topic = command.replace('who is', '').replace('what is', '').strip()
        try:
            info = wikipedia.summary(topic, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn't find information.")

    elif 'search' in command:
        query = command.replace('search', '').strip()
        talk(f"Searching for {query}")
        pywhatkit.search(query)

    elif 'open' in command:
        app = command.replace('open', '').strip().lower()
        talk(f"Opening {app}")
        open_application(app)

    elif 'stop' in command or 'close' in command:
        app = command.replace('stop', '').replace('close', '').strip().lower()
        talk(f"Closing {app}")
        close_specific_app(get_process_name(app))

    elif 'exit' in command or 'bye' in command:
        talk("Goodbye! See you later.")
        os._exit(0)

    else:
        talk("I didn't understand that command.")

def open_application(app):
    app_map = {
        'notepad': "notepad.exe",
        'calculator': "calc.exe",
        'chrome': r'"C:\Program Files\Google\Chrome\Application\chrome.exe"',
        'vscode': r'"C:\Program Files\Microsoft VS Code\Code.exe"',
        'code': r'"C:\Program Files\Microsoft VS Code\Code.exe"',
        'edge': r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"',
        'microsoft edge': r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"',
        'wireshark': r'"C:\Program Files\Wireshark\Wireshark.exe"',
        'spotify': r'"C:\Users\Public\Desktop\Spotify.lnk"',
        'paint': "mspaint.exe",
        'command prompt': "cmd.exe",
        'cmd': "cmd.exe",
        'task manager': "taskmgr.exe",
        'camera': "start microsoft.windows.camera:",
        'control panel': "control",
        'zoom': r'"C:\Users\YourUsername\AppData\Roaming\Zoom\bin\Zoom.exe"',
        'file explorer': "explorer.exe",
        'settings': "start ms-settings:",
        'battery': "powercfg.cpl"
    }

    urls = {
        'youtube': 'https://www.youtube.com',
        'google': 'https://www.google.com',
        'gmail': 'https://mail.google.com',
        'facebook': 'https://www.facebook.com',
        'instagram': 'https://www.instagram.com'
    }

    if app in urls:
        os.system(f'start {urls[app]}')
        if "chrome.exe" not in opened_apps:
            opened_apps.append("chrome.exe")
    elif app in app_map:
        os.system(app_map[app])
        process_name = get_process_name(app)
        if process_name and process_name not in opened_apps:
            opened_apps.append(process_name)
    else:
        talk("I don't know that application.")

def get_process_name(app):
    process_map = {
        'notepad': "notepad.exe",
        'calculator': "calculator.exe",
        'chrome': "chrome.exe",
        'vscode': "Code.exe",
        'code': "Code.exe",
        'edge': "msedge.exe",
        'microsoft edge': "msedge.exe",
        'wireshark': "Wireshark.exe",
        'spotify': "Spotify.exe",
        'paint': "mspaint.exe",
        'command prompt': "cmd.exe",
        'cmd': "cmd.exe",
        'task manager': "taskmgr.exe",
        'zoom': "Zoom.exe",
        'file explorer': "explorer.exe",
        'settings': "SystemSettings.exe",  # May vary
        'battery': "powercfg.exe",
    }
    return process_map.get(app, None)

def close_specific_app(process_name):
    if not process_name:
        talk("I didn't recognize which application to close.")
        return

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                proc.kill()
                talk(f"{process_name} closed.")
                if process_name in opened_apps:
                    opened_apps.remove(process_name)
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    talk(f"{process_name} was not running.")



