import vlc
import time


media = vlc.MediaPlayer('audio/tracychapman.mp3')
#  music_name = 'audio/tracychapman.mp3'


media.play()

time.sleep(256)


while media.is_plaing():
    print('A musica ainda está tocando')

print('A música parou de tocar')
