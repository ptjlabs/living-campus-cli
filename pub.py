#import context
import paho.mqtt.publish as publish
import json
import time
import random







while True:
    data = random.randint(0,200)
    payload = {
                "id":"12345",
                "sensor_type": "humidty",
                "data": data
            }
    payload = json.dumps(payload)


    publish.single("<campus>/cot/221/example",payload,hostname="<ip-address>")
    print("data sent: {}".format(payload))
    time.sleep(1)
