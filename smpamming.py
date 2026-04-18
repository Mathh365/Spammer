import pyautogui as auto
from time import sleep
import msvcrt

def spammer(msg: str, reps: int = None):
    isInfinity = (reps is None)
    sleep(3)
    
    if isInfinity:
        while True:
            send(msg)
            if closeLoop(): break
    
    if not isInfinity:
        for _ in range(reps):
            send(msg)
            

def send(msg: str):
   
    auto.write(msg)
    auto.press('enter') 
    
    
def closeLoop(condicao: bytes = b'\x1b'):
    if msvcrt.kbhit(): # Verifica se há tecla pressionada
        key = msvcrt.getch()
        
        return key == condicao
    
    return False