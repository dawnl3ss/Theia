from src.data_request import req_ip, forbidden_keys
from src.parser import parse_arguments
from src.colors import colors
from src.ascii import get_ascii
import sys
import os

def main():
    os.system("clear")
    print(colors.FAIL + "[/] " + colors.HEADER + "Starting Theia...")
    print(colors.BOLD + colors.HEADER + get_ascii())
    parse_arguments()

    if sys.argv[1] == "-a" or sys.argv[1] == "--adress":
        print(colors.OKBLUE + "┌───── " + colors.HEADER + "IP-Adress lookup [" + sys.argv[2] + "]" + colors.OKBLUE + " ─────┐")
        data = req_ip(sys.argv[2])

        for key in data:
            if key in forbidden_keys: continue
            print(colors.OKCYAN + "[+] " + colors.OKBLUE + key.capitalize() + colors.ENDC + " -> " + colors.OKGREEN + str(data[key]))
        print(colors.OKBLUE + "└───── " + colors.HEADER + "IP-Adress lookup [" + sys.argv[2] + "]" + colors.OKBLUE + " ─────┘" + "\n")

if __name__ == "__main__":
    main()