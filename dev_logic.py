import speech_recognition as sr
import requests
import datetime
import webbrowser
import os
import random
import subprocess
import pyjokes
from playsound import playsound
import os
import uuid
import asyncio
import edge_tts
from yt_dlp import YoutubeDL
import re


VOICE = "en-US-GuyNeural"

recognizer = sr.Recognizer()
chat_memory = ["You are a helpful assistant. Keep your replies short and direct."]
MUSIC_DIR = "C:\\Users\\Rishi\\Music"  # Update if needed


async def tts_async(text):
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    try:
        communicate = edge_tts.Communicate(text=text, voice=VOICE)
        await communicate.save(filename)
        playsound(filename)
    except Exception as e:
        print("TTS error:", e)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def speak(text, speak_out_loud=True):
    print("Dev -->", text)
    if speak_out_loud:
        try:
            asyncio.run(tts_async(text))
        except RuntimeError:
            # If there's already an event loop running (e.g. in Streamlit)
            loop = asyncio.get_event_loop()
            loop.create_task(tts_async(text))

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print("Me  -->", text)
            return text
        except Exception as e:
            print("Listening error:", e)
            return ""

'''def open_website(query):
    if "google" in query:
        return "[Opening Google...](https://www.google.com)"
    elif "youtube" in query:
        return "[Opening YouTube...](https://www.youtube.com)"
    elif "github" in query:
        return "[Opening GitHub...](https://www.github.com)"
    else:
        return "I can only open Google, YouTube, or GitHub for now."
'''
def open_website(query):
    """Opens a specific website based on the query."""
    if "google" in query:
        webbrowser.open("https://www.google.com")
        return "[Opening Google...](https://www.google.com)"
    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "[Opening YouTube...](https://www.youtube.com)"
    elif "github" in query:
        webbrowser.open("https://www.github.com")
        return "[Opening GitHub...](https://www.github.com)"
    else:
        return "I can only open Google, YouTube, or GitHub for now."


def get_time():
    return "It's " + datetime.datetime.now().strftime("%I:%M %p")

def play_music():
    try:
        songs = os.listdir(MUSIC_DIR)
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(MUSIC_DIR, song))
            return f"Playing {song}"
        else:
            return "No music files found."
    except Exception as e:
        return "Error: " + str(e)

'''def play_youtube_video(query):
    try:
        song = query.replace("play", "").replace("on youtube", "").strip()
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube."
    except:
        return "Couldn't play that video."
        '''

'''def play_youtube_video(query):
    search_query = query.lower().replace("play", "").replace("on youtube", "").strip()

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'best',
        'default_search': 'ytsearch1',  # search and return top 1
        'extract_flat': 'in_playlist'
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_query, download=False)
            if "entries" in info and len(info["entries"]) > 0:
                video_url = info["entries"][0]
                #full_url = f"https://www.youtube.com/watch?v={video_url}"
                final_url = video_url.get("webpage_url")
                webbrowser.open(final_url)
                return f"[Playing top result on YouTube for '{search_query}']({final_url})"
            else:
                return "No results found on YouTube."
    except Exception as e:
        return f"Error searching YouTube: {str(e)}"
        
    '''
def play_youtube_video(query):
    import urllib.parse
    search_query = query.lower().replace("play", "").replace("on youtube", "").strip()
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(search_query)}"
    webbrowser.open(url)
    return f"[Searching YouTube for '{search_query}']({url})"


def google_search(query):
    search_query = query.replace("search", "").strip()
    url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(url)
    return f"Searching Google for {search_query}"

def get_weather():
    try:
        response = requests.get("https://wttr.in/?format=3")
        return "Weather: " + response.text
    except:
        return "Couldn't fetch weather."

def tell_joke():
    return pyjokes.get_joke()

def calculate(query):
    try:
        result = eval(query.replace("calculate", "").strip())
        return f"The result is {result}"
    except:
        return "Couldn't calculate that."

'''def close_browser():
    try:
        subprocess.call("taskkill /IM chrome.exe /F", shell=True)
        subprocess.call("taskkill /IM msedge.exe /F", shell=True)
        subprocess.call("taskkill /IM firefox.exe /F", shell=True)
        return "Closed browser windows."
    except Exception as e:
        return "Couldn't close browser: " + str(e)
'''

def close_browser():
    """Closes common browser processes (Windows specific)."""
    try:
        # Note: This is a Windows-specific command
        subprocess.call("taskkill /F /IM chrome.exe", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.call("taskkill /F /IM msedge.exe", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.call("taskkill /F /IM firefox.exe", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        return "Closed browser windows."
    except Exception as e:
        return f"Couldn't close browsers: {e}"

def generate_response(message):
    chat_memory.append(f"User: {message}")
    prompt = "\n".join(chat_memory) + "\nAssistant:"
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()
        if "response" in result:
            #reply = result["response"].strip().split(". ")[0]
            full_response = result["response"].strip()
            sentences = re.split(r'(?<=[.?!])\s+', full_response)
            reply = ' '.join(sentences[:2])
            chat_memory.append(f"Assistant: {reply}")
            return reply
        else:
            return "Can't respond right now."
    except:
        return "Error generating a reply."
