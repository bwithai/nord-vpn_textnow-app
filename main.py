from automation import perform_automation
from vpn import nordvpn_connect

import requests
ip = requests.get('https://api.ipify.org').text
print(f"\nBefore Using NordVpn\nIp:\t{ip}")

# Establish the NordVPN connection
nordvpn_connect()

# Continue with your Selenium automation code
perform_automation()
