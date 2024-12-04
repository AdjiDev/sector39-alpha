import subprocess
import time
from .Cols import warna
from .delay import TimeDelay

def Osas():
    ingfo = f"[   {warna.y}INFO{warna.reset}   ]"
    ok = f"[    {warna.g}OK{warna.reset}    ]"
    fatal = f"[   {warna.r}FATAL{warna.reset}]"
    try:
        tuma = TimeDelay()
        tumo = next(tuma)
        print(f'{tumo}{ingfo} Checking if nodejs installed')
        time.sleep(3)
        result = subprocess.run(['node', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            tumo = next(tuma)
            print(f"{tumo}{ok} Node.js is installed. Version: {result.stdout.strip()}")
            return True
        else:
            tumo = next(tuma)
            print(f"{tumo}{ok} Node.js is not installed.")
            tumo = next(tuma)
            print(f"{tumo} Exiting . . .")
            return False
    except FileNotFoundError:
        tumo = next(tuma)
        print(f"{tumo}{ok} Node.js is not installed.")
        print(f"{tumo}{fatal} Exiting . . .")
        return False