import time
import keyboard
import vlc
import random
import musicDataBase
import songData

isPlay = False

def oneRandomSong():
    chosen = random.choice(musicDataBase.songs)
    return chosen

def playAllSongs():
    playlist = musicDataBase.songs[:]
    random.shuffle(playlist)

    for song in playlist:
        song.play()
        songData.getSongData(song)
        time.sleep(0.5)

        while song.is_playing():
            if keyboard.is_pressed('n'):  # press N to skip
                song.stop()
                time.sleep(0.3)
                break
            time.sleep(0.1)

songData.clear()
playAllSongs()