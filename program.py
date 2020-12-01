from pygame import mixer
from datetime import datetime 
from time import time

def musiconloop(codefile, stopper):
    mixer.init()
    mixer.music.load(codefile)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water =  time()
    init_eyes =  time()
    init_exercise =  time()
    watersecs = 1800
    exsec = 2100
    eyesecs = 2400
    
    while True:
        if time() - init_water >watersecs:
            print("Water drinking time.Enter 'drank' to stop the alarm")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank water at")
        if time() - init_eyes >eyesecs:
            print("Eyes exercise time.Enter 'doneeyes' to stop the alarm")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes relaxed at")
        if time() - init_exercise >exsec:
            print("Physical exercise time.Enter 'donephy' to stop the alarm")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Done physical exercise at")