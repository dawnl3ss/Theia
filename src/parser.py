import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--adress", help="victim ip-adress")
    parser.parse_args()