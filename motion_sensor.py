#!/usr/bin/python3.8

from sys import argv, exit
import requests
import time
import json

ENDPOINT = 'http://localhost:5000/addEvent'
HEADERS = {'content-type': 'application/json'}

if len(argv) != 3:
    print("ERROR: please provide a DeviceID and DeviceName:")
    print(f"\n\texample: {argv[0]} 123 \"front door\"")
    exit(1)

dev_id = argv[1]
dev_name = argv[2]

print('[INFO] motion sensor starting...')
print('[INFO] * press \'q\' or ^C to quit')
print('[INFO] * press ENTER to simulate a motion event')
inp = input('--> ')

while inp.lower() != 'q':
    
    try:
        resp = requests.post(ENDPOINT,
                            data=json.dumps({'deviceID': dev_id, 'deviceName': dev_name, 'timestamp': int(time.time())}),
                            headers=HEADERS)        
        print(f'[INFO] sent event, response: {resp}')
    
    except:
        print('[ERROR] something went wrong...is the API online?')
        exit(1)

    inp = input('--> ')

print('[INFO] motion sensor stopping...')