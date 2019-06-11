from pygame import mixer
import os
import sys

mixer.pre_init(44100, 16, 2, 4096)
mixer.init()


# Using relative paths
root_path = os.path.dirname(sys.modules['__main__'].__file__)
sounds_path = os.path.join(root_path, 'resources/sounds')

MUSIC = mixer.music.load(os.path.join(sounds_path, 'WalterAI.mp3'))

STEPS = [mixer.Sound(os.path.join(sounds_path, 'steps1.wav')),
         mixer.Sound(os.path.join(sounds_path, 'steps2.wav'))]