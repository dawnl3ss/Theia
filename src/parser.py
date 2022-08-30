import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--adress", help="victim ip-adress")
    parser.add_argument("-s", "--self", help="you own ip-adress")
    parser.parse_args()