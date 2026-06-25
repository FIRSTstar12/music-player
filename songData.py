import re
from tinytag import TinyTag
import vlc
import urllib.parse
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSongData(file):
    media = file.get_media()

    if media:
        mrl = media.get_mrl()
        parsed_url = urllib.parse.urlparse(mrl)
        file_path = urllib.parse.unquote(parsed_url.path)
        if file_path.startswith('/') and file_path[2] == ':':
            file_path = file_path[1:]

        tag = TinyTag.get(file_path)
        total_seconds = int(tag.duration)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        

        print(f"Now Playing: {tag.title} by {tag.artist}")
        print(f"Album: {tag.album}")
        print(f"Duration: {minutes} minutes {seconds} seconds")
        # print(f"Bitrate: {tag.bitrate} kbps")
        # print(f"Sample Rate: {tag.samplerate} Hz")

def getName(file):
    songName = "Untitled Song"
    media = file.get_media()

    if media:
        mrl = media.get_mrl()
        parsed_url = urllib.parse.urlparse(mrl)
        file_path = urllib.parse.unquote(parsed_url.path)
        if file_path.startswith('/') and file_path[2] == ':':
            file_path = file_path[1:]

        tag = TinyTag.get(file_path)
        songName = tag.title + " by " + tag.artist
    return songName
    