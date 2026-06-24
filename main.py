import vlc
import random
import musicDataBase

def songSelect():
    return random.choice(musicDataBase.songs)

songSelect().play()

input("Press Enter to quit...")