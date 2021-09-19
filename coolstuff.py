from enum import Enum
import threading
from time import sleep

class loglabels:
    warn = "[ \033[93mWARN\033[0m ]"
    err = "[\033[91mFAILED\033[0m]"
    ok = "[\033[92m  OK  \033[0m]"
    blank = "[      ]"
    blank_nb = "        "
    f_scroll = ["[\033[91m*     \033[0m]",
                "[\033[31m*\033[91m*    \033[0m]",
                "[\033[91m*\033[31m*\033[91m*   \033[0m]",
                "[ \033[91m*\033[31m*\033[91m*  \033[0m]",
                "[  \033[91m*\033[31m*\033[91m* \033[0m]",
                "[   \033[91m*\033[31m*\033[91m*\033[0m]",
                "[    \033[91m*\033[31m*\033[0m]",
                "[     \033[91m*\033[0m]",
                "[    \033[91m*\033[31m*\033[0m]",
                "[   \033[91m*\033[31m*\033[91m*\033[0m]",
                "[  \033[91m*\033[31m*\033[91m* \033[0m]",
                "[ \033[91m*\033[31m*\033[91m*  \033[0m]",
                "[\033[91m*\033[31m*\033[91m*   \033[0m]",
                "[\033[31m*\033[91m*    \033[0m]"]

__GI = 0
__animthread = threading.Thread()
__should_die = False

class levels(Enum):
    OK = 0
    BLANK = -1
    BLANK_NB = -2
    WARN = 1
    ERROR = 2

def Msg(level, msg):
    if level == levels.OK:
        print(f"{loglabels.ok} {msg}")
    elif level == levels.WARN:
        print(f"{loglabels.warn} {msg}")
    elif level == levels.ERROR:
        print(f"{loglabels.err} {msg}")
    elif level == levels.BLANK:
        print(f"{loglabels.blank} {msg}")
    elif level == levels.BLANK_NB:
        print(f"{loglabels.blank_nb} {msg}")
    else:
        raise Exception("Invalid message level")

def MakeAnimatedMsgThread(msg, t):
    global __animthread
    global __should_die
    if type(__animthread) == threading.Thread and __animthread.is_alive():
        __should_die = True
        while True:
            if not __animthread.is_alive():
                break
        __should_die = False
        print("\033[K", end="\r")
    def anim(msg, t):
        while True:
            if __should_die:
                break
            for i in range(len(loglabels.f_scroll)):
                print(f"{loglabels.f_scroll[i]} {msg}", end="\r")
                if __should_die:
                    break
                sleep(t)
    x = threading.Thread(target=anim, args=(msg, t,), daemon=True)
    __animthread = x
    x.start()

def KillAnimatedMsgThread(level, msg):
    global __should_die
    __should_die = True
    while True:
        if not __animthread.is_alive():
            break
    __should_die = False
    print("\033[K", end="\r")
    Msg(level, msg)