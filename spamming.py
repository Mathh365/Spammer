import pyautogui as auto
from time import sleep
import keyboard


class Spammer:
    def __init__(self):
        self.runningLoop = False

    def send(self, msg: str):
        auto.write(msg)
        auto.press("enter")

    def startLoop(self, msg: str, reps: int | None = None):
         
        self.runningLoop = True
        sleep(3) 
        
        hotkey = keyboard.add_hotkey('esc', self.stop)

        if reps is None:
            # INFINITO
            while self.runningLoop:
                self.send(msg)
        else:
            # FINITO
            for _ in range(reps):
                if not self.runningLoop:
                    break
                self.send(msg)

        self.runningLoop = False
        keyboard.remove_hotkey(hotkey)

    def stop(self):
        self.runningLoop = False