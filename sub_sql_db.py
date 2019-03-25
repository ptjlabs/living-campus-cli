import paho.mqtt.subscribe as subscribe
import json
import argparse
import sys
import time



__author__ = 'Preston Turner 1398857'

parser = argparse.ArgumentParser(description='This Broker CLI will subscribe to local brokers and send its data to a db')
parser.add_argument(
    '-H', '--host',
    help='enter host ip',
    required='True'
)
parser.add_argument(
    '-t', '--topic',
    help='enter mqtt topic',
    required=True
)
results = parser.parse_args()


if __name__ == "__main__":
    while True:
        try:
            topic = results.topic

            m = subscribe.simple(topic, hostname=results.host,retained=False)
            print(m.topic)
            print(m.payload)

            check = json.loads(m.payload)
            print(check['message1'])
        except KeyboardInterrupt:
            print('\n Exiting program...')
            time.sleep(2)
            sys.exit()
