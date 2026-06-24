import time
import vlc
import random
import musicDataBase

isPlay = False

def oneRandomSong():
    chosen = random.choice(musicDataBase.songs)
    return chosen

def playAllSongs():
    playlist = musicDataBase.songs[:]
    random.shuffle(playlist)

    for song in playlist:
        song.play()
        time.sleep(0.5)
    
        while song.is_playing():
            time.sleep(1)

playAllSongs()

input("Press Enter to quit...")