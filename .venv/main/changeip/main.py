import socks
import socket
import requests
import time
import json
import urllib.request
import subprocess

# Route all socket traffic through Tor's SOCKS5 proxy
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

def restart_tor():
    try:
        subprocess.run(["pkill", "-f", "tor"], check=False)  # Lopeta vanha prosessi
        subprocess.Popen(["tor"])  # Käynnistä uusi
        print("[*] Käynnistettiin Tor uudelleen manuaalisesti")
    except Exception as e:
        print("[!] Virhe Torin käynnistyksessä:", e)


def get_ip_info():
    try:
        ip = requests.get("http://icanhazip.com", timeout=10).text.strip()
        print(f"[+] Current Tor IP: {ip}")

        url = f"http://ipinfo.io/{ip}/json"
        response = urllib.request.urlopen(url)
        data = json.load(response)

        print("[*] IP Details:")
        print(f"IP             : {ip}")
        print(f"Region         : {data.get('region')}")
        print(f"Country        : {data.get('country')}")
        print(f"City           : {data.get('city')}")
        print(f"Org            : {data.get('org')}")
        print(f"Coordinates    : {data.get('loc')}")
        print("##############################################\n")

    except Exception as e:
        print("[!] Error getting IP info:", e)

# Main loop
for i in range(5):  # Change IP 5 times
    restart_tor()
    time.sleep(10)  # Wait for Tor to restart and assign a new circuit
    get_ip_info()