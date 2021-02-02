# Be Productive
> A tool that let's you focus on your work by blocking distracting websites. Optionally with a timer for work sessions, using the Pomodoro technique.


## Install

I'm working on making this program `pip` installable. In the meantime: download all files from the `beproductive` folder and place them in the same directory.

If you want to use Pomodoro and use Windows, it's recommended to `pip install win10toast` for [nice Windows notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications). 

![](pomodoro-notification.png)

You don't have to install `win10toast`, but then you will not get visible and audible notifications for Pomodoro. All notifications are also printed in your command line tool however.

## Blocked Websites

These websites are blocked per default, but you can always edit `blocklist.txt` and add your personal time killers.

```python
#collapse_input
with open(BLOCKLIST) as file:
    print(" ".join([line.rstrip() for line in file]))
```

    twitter.com youtube.com facebook.com instagram.com reddit.com netflix.com amazon.com 
    

## How to Block / Unblock Websites

### Windows
To run the blocker script, **you have to run your command line tool with administrator privileges.**

To block websites:
```
cd /directory/of/beproductive
python -m beproductive [block]
```
To unblock all websites:
```
python -m beproductive unblock
```

To start a Pomodoro session:
```
python -m beproductive pomodoro
```

### Linux (and MacOS?)
To block websites:
```
cd /directory/of/beproductive
sudo python -m beproductive [block]
```
To unblock all websites:
```
sudo python -m beproductive unblock
```

To start a Pomodoro session:
```
sudo python -m beproductive pomodoro
```

The [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) feature blocks your defined websites for 25 minutes. It notifies you after the 25 minutes are over and gives you access to all websites for 5 minutes. Although I recommend getting up and stretching instead :) This cycle is repeated 4 times.

## Behind the Scenes
The script blocks URLs by modifying the `hosts` file. Blocked URLs are redirected to `127.0.0.1`. The script backs up the original `hosts` file. You will not lose any customizations and you can always reset to the original state.

## Roadmap
- Turn scripts into installable Python package
- Extend to Linux and MacOS
- Add ability to schedule or block for specific period of time
