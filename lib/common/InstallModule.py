import subprocess
import sys
import time
from .Cols import warna

def InstallModule(namanya):
    ingfo = f"[   {warna.y}INFO{warna.reset}   ]"
    caulila = f"[   {warna.g}OK{warna.reset}   ]"
    meki = f"[   {warna.r}FATAL{warna.reset}]"
    dongo = time.strftime("%H:%M:%S", time.localtime())
    sempak = f"[   {warna.b}{dongo}{warna.reset}   ]"
    try:
        __import__(namanya)  
        print(f"{sempak}{caulila} Module {namanya} is installed!")
    except ImportError:
        print(f"{sempak}{meki} Module '{namanya}' is not installed")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", namanya],
                stdout=subprocess.DEVNULL,  
                stderr=subprocess.DEVNULL  
            )
            print(f"{sempak}{caulila}Module '{namanya}' was successfully installed.")
        except Exception as e:
            print(f"{sempak}{meki} Error installing module '{namanya}': {e}")
    finally:
        pass
