# AUTOGENERATED! DO NOT EDIT! File to edit: 01_pomodoro.ipynb (unless otherwise specified).

__all__ = ['WORK', 'BREAK', 'POMODOROS']

# Cell
from time import sleep
from .blocker import Blocker
import sys

WORK = 25
BREAK = 5
POMODOROS = 4

# Cell
if __name__=='__main__':
    blocker = Blocker()
    try: mode = sys.argv[1]
    except: mode = 'stop'
    if mode == 'start':
        turn = 1
        while turn <= POMODOROS:
            blocker.block()
            blocker.notify(f"Pomodoro no. {turn} started, work for {WORK} minutes")
            sleep(WORK*60)
            blocker.unblock()
            if turn < POMODOROS:
                blocker.notify(f"Pomodoro no. {turn} ended, take a {BREAK} minutes break")
                sleep(BREAK*60)
            else:
                blocker.notify(f"Pomodoro session ended, take a longer break. All websites unblocked.", duration=10)
            turn += 1