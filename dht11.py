import time
import requests
import Adafruit_DHT
import csv
from datetime import datetime

sensor = Adafruit_DHT.DHT11
gpio = 17

headers = {
    'Fiware-Service': 'ridsaert',
    'Fiware-ServicePath': '/udp_building',
    'Content-Type': 'application/json',
}


def send_values(temperature, humidity):
    json_data = {
        'temperature': {
            'type': 'Integer',
            'value': temperature,
        },
        'humidity': {
            'type': 'Integer',
            'value': humidity,
        },
    }

    requests.post('http://20.16.84.167:1026/v2/entities/dht11/attrs', headers=headers, json=json_data)

def save_to_csv(data):
    with open('/home/rids/raspberry_multisensor/data.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

while (True):
    humidity, temperature = Adafruit_DHT.read(sensor, gpio)
    
    if humidity is not None and temperature is not None:
        print('Temp {0:0.1f} C Humidity{1:0.1f}%'.format(temperature, humidity))
        save_to_csv([temperature, humidity, datetime.timestamp(datetime.now())])
    else:
        print('Sensor failure. Check wiring.')
    #send_values(temperature, humidity)
    
    time.sleep(300)
