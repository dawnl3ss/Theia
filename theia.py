from src.data_request import req_ip, forbidden_keys
from src.colors import colors
from src.ascii import get_ascii
import sys
import os

def main():
    os.system("clear")
    print(colors.FAIL + "[/] " + colors.HEADER + "Starting Theia...")
    print(colors.BOLD + colors.HEADER + get_ascii())

    if sys.argv[1] == "-a":
        print(colors.OKBLUE + "┌───── " + colors.HEADER + "IP-Adress lookup [" + sys.argv[2] + "]" + colors.OKBLUE + " ─────┐")
        data = req_ip(sys.argv[2])

        for key in data:
            if key in forbidden_keys: continue
            print(colors.OKCYAN + "[+] " + colors.OKBLUE + key.capitalize() + colors.ENDC + " -> " + colors.OKGREEN + str(data[key]))
        print(colors.OKBLUE + "└───── " + colors.HEADER + "IP-Adress lookup [" + sys.argv[2] + "]" + colors.OKBLUE + " ─────┘" + "\n")
    else:
        print(colors.FAIL + "[-] " + colors.WARNING + "Wrong argument.")

if __name__ == "__main__":
    main()