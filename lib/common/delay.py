import time
from .Cols import warna

def TimeDelay():
    while True:
        dongo = time.strftime("%H:%M:%S", time.localtime())
        adjiu = f"[   {warna.b}{dongo}{warna.reset}   ]"
        yield adjiu
        time.sleep(1)

def Waktunya():
    while True:
        dongo = time.strftime("%H:%M:%S", time.localtime())
        adjiu = f"[   {warna.b}{dongo}{warna.reset}   ]"
        print(adjiu, end="\r", flush=True)
        time.sleep(1)