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
        fileName = file_path.split("/")[5]
        songName = " ".join(re.findall(r'[A-Z][^A-Z]*', fileName.split(".")[0]))

        print("\nNow Playing: " + str(songName))
        print(f"Duration: {minutes} minutes {seconds} seconds")
        # print(f"Bitrate: {tag.bitrate} kbps")
        # print(f"Sample Rate: {tag.samplerate} Hz")

def getName(file):
    media = file.get_media()

    if media:
        mrl = media.get_mrl()
        parsed_url = urllib.parse.urlparse(mrl)
        file_path = urllib.parse.unquote(parsed_url.path)
        if file_path.startswith('/') and file_path[2] == ':':
            file_path = file_path[1:]

        fileName = file_path.split("/")[5]
        songName = " ".join(re.findall(r'[A-Z][^A-Z]*', fileName.split(".")[0]))

        return songName
    