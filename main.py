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
        print(" ")
        songData.printSongData(song)
        time.sleep(3)

        while song.is_playing():
            if keyboard.is_pressed('q'):
                song.stop()
                time.sleep(0.3)
                break
            time.sleep(0.01)

def songPicker():
    playlist = musicDataBase.songs[:]

    i = 1
    for song in playlist:
        print(f"{i}) {songData.getName(song)}")
        i += 1
    choice = int(input("Which song would you like to hear? (Enter the song's number): "))
    return playlist[choice - 1]

songData.clear()
allOrOne = input("Would you like to hear all of your songs on shuffle or just one?(all/one): ")
songData.clear()

if allOrOne == "all":

    playAllSongs()

elif allOrOne == "one":

    song = songPicker()
    songData.clear()
    song.play()
    songData.printSongData(song)
    time.sleep(0.5)

    while song.is_playing():
        if keyboard.is_pressed('q'):
            song.stop()
            break
        time.sleep(0.01)
else:
    song = oneRandomSong()
    song.play()
    songData.printSongData(song)
    time.sleep(0.5)

    while song.is_playing():
        if keyboard.is_pressed('q'):
            song.stop()
            break
        time.sleep(0.1)