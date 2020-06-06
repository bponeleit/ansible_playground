from w1thermsensor import W1ThermSensor
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("ankh-morpork.fritz.box")

sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0317018a3bff")
sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "04170197f1ff")
sensor3 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041701abebff")

client.loop_start()

while True:
#    for count, sensor in enumerate(W1ThermSensor.get_available_sensors()):
#        temperature = sensor.get_temperature()
#        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
#        client.publish("/playground/temperature" + str(count), temperature)
    flow_temp = sensor1.get_temperature()
    boiler_temp = sensor2.get_temperature()
    return_temp = sensor3.get_temperature()
    client.publish("/places/our place/cellar/heatingroom/boiler/flow temperature", flow_temp)
    client.publish("/places/our place/cellar/heatingroom/boiler/temperature", boiler_temp)
    client.publish("/places/our place/cellar/heatingroom/boiler/return temperature", return_temp)
    time.sleep(30)
