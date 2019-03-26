import paho.mqtt.subscribe as subscribe
import json
import argparse
import sys
import time
import datetime



__author__ = 'Preston Turner'

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
    print('\n')
    print('         Living Campus CLI                 ')
    print('\n')
    print('             (\__/)')
    print('         ⠀   (•ㅅ•)     Preston setting up')
    print('         ＿ノ ヽ ノ＼ __   A broker')
    print('        /　`/ ⌒Ｙ⌒ Ｙ　ヽ')
    print('       ( 　(三ヽ人　 /　 )')
    print('       |　ﾉ⌒＼ ￣￣ヽ　 ノ')
    print('       ヽ＿＿＿＞､＿＿_／')
    print('　　       ｜( 王 ﾉ〈   (\__/)  everyone')
    print('　　        /ﾐ`ー―彡\   (•ㅅ•)    else')
    print('***************************************')
    print(' This CLI will be updated periodically.')
    print('Current Date: {}'.format(str(datetime.datetime.now()))) 
    while True:
        try:
            topic = results.topic
            m = subscribe.simple(topic, hostname=results.host,retained=False)
            print('Message from: {} '.format(m.topic))
            print('Data: {} '.format(m.payload))

        except KeyboardInterrupt:
            print('\n Exiting program...')
            time.sleep(2)
            sys.exit()
