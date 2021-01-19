#!/usr/bin/python3
import yaml
import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='F', type=str, nargs=1, help='')
args = parser.parse_args()
file = args.file[0]

def main():
    print(encode(file))

def encode(file):
    with open(file, 'r') as stream:
        data = yaml.load(stream.read())
    print(data)
