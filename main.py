import time
import vlc
import random
import musicDataBase
import songData

isPlay = False

def oneRandomSong():
    chosen = random.choice(musicDataBase.songs)
    return chosen

songData.clear()

def playAllSongs():
    playlist = musicDataBase.songs[:]
    random.shuffle(playlist)

    for song in playlist:
        song.play()
        songData.getSongData(song)
        time.sleep(0.5)
    
        while song.is_playing():
            time.sleep(1)
        input("Press Enter to continue...")

songData.clear()
playAllSongs()