# AUTOGENERATED! DO NOT EDIT! File to edit: 00_beproductive.ipynb (unless otherwise specified).

__all__ = ['main', 'parse_arguments', 'in_notebook']

# Cell
from .blocker import Blocker
from .pomodoro import pomodoro
import beproductive.config as config
import argparse
import sys
from time import sleep

# Cell
def main(action=None, time=None, break_time=None, pomodoros=None):
    # If no config file is found, create one with the default URLs
    if not config.load_config():
        config.save_config(default=True)

    if action == 'block':
        blocker = Blocker()
        if blocker.adminrights:
            if time:
                blocker.block()
                blocker.notify(f'Websites blocked for {time} minutes.')
                sleep(time*60)
                blocker.unblock(notify=True)
            else:
                blocker.block(notify=True)

    elif action == 'unblock':
        blocker = Blocker()
        if blocker.adminrights:
            blocker.unblock(notify=True)

    elif action == 'pomodoro':
        pomodoro(work_time=time or WORK_TIME, break_time=break_time or BREAK_TIME, pomodoros=pomodoros or POMODOROS)

# Cell
def parse_arguments():
    """
    Parse arguments from shell. All arguments are optional.
    action: ['block', 'unblock', 'pomodoro']
    time: minutes
    break_time: minutes
    pomodoros: int

    Returns: Namespace
    """
    parser = argparse.ArgumentParser(description="Block addictive websites. Study with the Pomodoro technique.")
    parser.add_argument('action',
                        nargs='?',
                        choices=['block', 'unblock', 'pomodoro'],
                        help='Block or unblock websites, or start a Pomodoro session. ')
    parser.add_argument('-t', '--time', type=int,
                        help='How many minutes should websites be blocked?')
    parser.add_argument('-b', '--breaktime', type=int,
                        help='Length of the break between Pomodoros')
    parser.add_argument('-p', '--pomodoros', type=int,
                        help='Number of Pomodoros')
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all blocked websites')
    parser.add_argument('-a', '--add', nargs='+',
                        help='One or more websites that should be added to blocklist')
    parser.add_argument('-r', '--remove', nargs='+',
                        help='One or more websites that should be removed from blocklist')
    args = parser.parse_args()
    return args

# Cell
def in_notebook():
    "Returns True if run in a notebook environment."
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:
            return False
    except:
        return False
    return True

# Cell
if __name__ == '__main__' and not in_notebook():
    # If no config file is found, create one with the default URLs
    if not config.load_config():
        config.save_config(default=True)

    args = parse_arguments()
    if args.add:
        config.add_urls(args.add)
    if args.remove:
        config.remove_urls(args.remove)
    if args.list:
        config.show_blocklist()
    # If action was provided, call main function
    if args.action != None:
        main(args.action, args.time, args.breaktime, args.pomodoros)
    # Default behaviour if no arguments are provided at all: block websites
    if len(sys.argv) <= 1:
        main(action='block')