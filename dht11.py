import time
import requests
import Adafruit_DHT

sensor=Adafruit_DHT.DHT11
gpio=17

headers = {
        'Fiware-Service' : 'ridsaert',
        'Fiware-ServicePath' : '/udp_building',
        'Content-Type' : 'application/json',
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


while(True):

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    print('Temp {0:0.1f} C Humidity{1:0.1f}%'.format(temperature, humidity))
    send_values(temperature, humidity)
    time.sleep(300)

