from w1thermsensor import W1ThermSensor
import paho.mqtt.client as mqtt
import time

sensor = W1ThermSensor()
client = mqtt.Client()
client.connect("ankh-morpork.fritz.box")

client.loop_start()

while True:
    for sensor in W1ThermSensor.get_available_sensors():
        temperature = sensor.get_temperature()
        client.publish("/playground/temperature", temperature)
    time.sleep(0.5)
