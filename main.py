#!/usr/bin/python3
import yaml
import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='F', type=str, nargs=1, help='')
args = parser.parse_args()
file = args.file[0]

def main():
    print(yaml.dump(encode(file), default_flow_style=False))

def encode(file):
    with open(file, 'r') as stream:
        document = yaml.load(stream.read(), Loader=yaml.Loader)
    if 'data' in document:
        for key in document['data']:
            value = document['data'][key]
            document['data'][key] = base64.b64encode(bytes(value, 'utf8')).decode()
    if 'stringData' in document:
        for key in document['stringData']:
            value = document['stringData'][key]
            document['stringData'][key] = base64.b64encode(bytes(value, 'utf8')).decode()
    return document

main()
