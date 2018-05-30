import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print "Message received: "  + message.payload

client = mqtt.Client()
client.connect("ankh-morpork.fritz.box")

client.on_message = on_message

client.loop_start()

client.subscribe("python/test")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()