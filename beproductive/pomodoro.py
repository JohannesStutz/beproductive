# AUTOGENERATED! DO NOT EDIT! File to edit: 02_pomodoro.ipynb (unless otherwise specified).

__all__ = ['WORK_TIME', 'BREAK_TIME', 'POMODOROS', 'pomodoro']

# Cell
from time import sleep
from .blocker import *
import sys

WORK_TIME = 25 # minutes
BREAK_TIME = 5 # minutes
POMODOROS = 4

# Cell
def pomodoro(work_time=WORK_TIME, break_time=BREAK_TIME, pomodoros=POMODOROS):
    blocker = Blocker()
    turn = 1
    while turn <= pomodoros:
        if blocker.block():
            blocker.notify(f"Pomodoro no. {turn} started, work for {work_time} minutes")
        else:
            blocker.notify("An error occured.")
        sleep(work_time*60)
        blocker.unblock()
        if turn < pomodoros:
            blocker.notify(f"Pomodoro no. {turn} ended, take a {break_time} minutes break")
            sleep(break_time*60)
        else:
            blocker.notify(f"Pomodoro session ended, take a longer break. All websites unblocked.", duration=10)
        turn += 1

# Cell
if __name__=='__main__':
    try: mode = sys.argv[1]
    except: mode = 'stop'
    if mode == 'start':
        pomodoro()