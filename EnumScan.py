#!/usr/bin/python3
# pip3 install python-nmap tabulate

import sys
import nmap
from tabulate import tabulate

# Initialize nmap
sc = nmap.PortScanner()

def show_help():
    """ Display help """
    print("""
Network scanning tool based on nmap

Usage:
  python3 script.py [option]

Available options:
  --help, -h             Display this help
  1                      Scan active hosts in an IP range
  2                      Scan specific ports of an IP address
  3                      Detect service versions on an IP address
""")

def scan_ports(ip, ports_range):
    """ Scan specific ports of an IP and display results in a table """
    print(f"[INFO] Scanning ports {ports_range[0]}-{ports_range[1]} on {ip}...")
    try:
        sc.scan(ip, ports=f'{ports_range[0]}-{ports_range[1]}', arguments='-sV')
        results = []
        for port in sc[ip]['tcp']:
            service_name = sc[ip]['tcp'][port]['name']
            state = sc[ip]['tcp'][port]['state']
            results.append([ip, service_name, port, state])
        
        print(tabulate(results, headers=["IP", "Service", "Port", "State"], tablefmt="grid"))
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

def scan_network(ip):
    """ Scan the network for active hosts """
    print(f"[INFO] Scanning network {ip}...")
    try:
        sc.scan(hosts=ip, arguments='-sn')
        hosts = sc.all_hosts()
        results = [[host, sc[host].state()] for host in hosts]
        print(tabulate(results, headers=["IP", "State"], tablefmt="grid"))
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

def detect_versions(ip):
    """ Detect service versions on an IP """
    print(f"[INFO] Detecting service versions on {ip}...")
    try:
        sc.scan(ip, arguments='-sV')
        services = [
            [port, sc[ip]['tcp'][port]['name'], sc[ip]['tcp'][port]['version']]
            for port in sc[ip]['tcp']
        ]
        print(tabulate(services, headers=["Port", "Service", "Version"], tablefmt="grid"))
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

def menu():
    """ Display the main menu """
    print("""

 _____                                                                   _____ 
( ___ )-----------------------------------------------------------------( ___ )
 |   |                                                                   |   | 
 |   |  ________                            ______                       |   | 
 |   | |_   __  |                         .' ____ \                      |   | 
 |   |   | |_ \_|_ .--. __   _  _ .--..--.| (___ \_|.---. ,--.  _ .--.   |   | 
 |   |   |  _| _[ `.-. [  | | |[ `.-. .-. |_.____`./ /'`\`'_\ :[ `.-. |  |   | 
 |   |  _| |__/ || | | || \_/ |,| | | | | | \____) | \__.// | |,| | | |  |   | 
 |   | |________[___||__'.__.'_[___||__||__\______.'.___.\'-;__[___||__] |   | 
 |___|                                                                   |___| 
(_____)-----------------------------------------------------------------(_____)
            
              ! BANG BANG !                                                      
""")
    print("1- Scan active hosts")
    print("2- Scan ports")
    print("3- Detect service versions\n")
    
    choice = input("Enter a number: ")

    if choice == '1':
        ip = input("Enter the IP address or IP range (CIDR): ")
        scan_network(ip)
    elif choice == '2':
        ip = input("Enter the IP address: ")
        try:
            ports_range = input("Which port range do you want to scan? (e.g., 1-1024, 0-65535): ").strip().split('-')
            ports_range = (int(ports_range[0]), int(ports_range[1]))
            scan_ports(ip, ports_range)
        except ValueError:
            print("[ERROR] Invalid port range format.")
    elif choice == '3':
        ip = input("Enter the IP address: ")
        detect_versions(ip)
    else:
        print("[ERROR] Please choose a valid number between 1 and 3")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        show_help()
    else:
        menu()
