import uuid
import datetime
import random
import json
from azure.servicebus import ServiceBusService

sbs = ServiceBusService(service_namespace='cpvevh1', shared_access_key_name='first', shared_access_key_value='WZnrLkWdsWCDehbO5OAUEGIVXpiE+V9Yn9CZqGX/gMs=')
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

for y in range(0,20):
    for dev in devices:
        reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'uv': random.random(), 'temperature': random.randint(70, 100), 'humidity': random.randint(70, 100)}
        s = json.dumps(reading)
        sbs.send_event('ev1', s)
    print(y)
