import vlc
import time


music_name = 'audio/tracychapman.mp3'
player = vlc.MediaPlayer(music_name)

player.play()

time.sleep(256)


while player.is_plaing():
    print('A musica ainda está tocando')

print('A música parou de tocar')
