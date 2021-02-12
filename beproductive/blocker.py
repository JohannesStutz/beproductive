# AUTOGENERATED! DO NOT EDIT! File to edit: 01_blocker.ipynb (unless otherwise specified).

__all__ = ['APP_NAME', 'REDIRECT', 'WIN_PATH', 'LINUX_PATH', 'NOTIFY_DURATION', 'ICON_PATH', 'host_fp', 'host_fp_copy',
           'host_fp_blocked', 'Blocker']

# Cell
from pathlib import Path
from shutil import copy
import beproductive.config as config
import sys
try:
    from win10toast import ToastNotifier
    win_notify = ToastNotifier()
except:
    win_notify = False

# Cell
APP_NAME = 'Be Productive'
REDIRECT = '127.0.0.1'
WIN_PATH = r'C:\Windows\System32\drivers\etc'
LINUX_PATH = r'/etc'
NOTIFY_DURATION = 1 # CHANGE TO 5 FOR PRODUCTION
ICON_PATH = 'icon.ico'

if sys.platform == 'win32':
    host_path = Path(WIN_PATH)
else:
    host_path = Path(LINUX_PATH)
host_fp = host_path/'hosts'
host_fp_copy = host_path/'hosts.original'
host_fp_blocked = host_path/'hosts.blocked'

# Cell
class Blocker():
    "The core of the package. It modifies the hosts file of the OS."
    def __init__(self, redirect=REDIRECT):
        self.adminrights = False
        self.redirect = redirect
        self.blocklist = config.load_config()
        if not host_fp_copy.exists():
            self._setup()
        if self._create_blocked_list():
            self.adminrights = True

    def _setup(self):
        "Creates a copy of the `hosts` file and saves it as `hosts.original`"
        try:
            copy(host_fp, host_fp_copy)
            self.notify("Setup successful")
        except PermissionError:
            self._raise_permission_error()

    def _create_blocked_list(self):
        "Creates a copy of `hosts.original` and saves it to `hosts.blocked`. Then adds all blocked sites."
        try:
            copy(host_fp_copy, host_fp_blocked)
            with open(host_fp_blocked, "a") as blocked_file:
                for url in self.blocklist:
                    # TODO: refine, add www only if not in url, remove www if in url
                    blocked_file.write(f"{self.redirect} {url} www.{url} api.{url}\n")
                    # Special case for Twitter which has a special API URL
                    if url == 'twitter.com':
                        blocked_file.write(f"{self.redirect} tpop-api.twitter.com\n")
            return True
        except PermissionError:
            self._raise_permission_error()
            return False

    def block(self, notify=False):
        "Blocks all specified websites by replacing `hosts` file with `hosts.blocked`"
        try:
            copy(host_fp_blocked, host_fp)
        except PermissionError:
            self._raise_permission_error()
            return False
        if notify:
            self.notify("Websites blocked, enjoy your work")
        return "Websites blocked"

    def unblock(self, notify=False):
        "Unblocks all websites by restoring the original `hosts` file"
        try:
            copy(host_fp_copy, host_fp)
        except PermissionError:
            self._raise_permission_error()
            return False
        if notify:
            self.notify("All websites unblocked, have fun")
        return "Websites unblocked"

    def notify(self, message, title=APP_NAME, duration=NOTIFY_DURATION):
        "Sends notification to CLI and - if available - to GUI"
        print(message)
        if win_notify:
            win_notify.show_toast(title, message, duration=duration)

    def _raise_permission_error(self):
        self.notify("Permission Error. Please run the command line tool as ADMINISTRATOR.")