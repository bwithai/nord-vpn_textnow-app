import os
import platform
import random
import time


# NordVPN function to connect to a US server
def nordvpn_connect():
    version = platform.system()
    if version == "Linux":
        server = "nordvpn connect us"
        os.system(server)
    elif version == "Windows":
        server = "nordvpn -c -g United States"
        os.system(server)
    time.sleep(10)


# NordVPN function to disconnect
def nordvpn_disconnect():
    os.system("nordvpn disconnect")
