import paho.mqtt.client as mqttClient
import time
import json
import subprocess
import sys

from pprint import pprint

with open('intertechno.json') as f:
    data = json.load(f)

devices = {
    'a' : '1',
    'b' : '2',
    'c' : '3',
    'd' : '4'
}

commands = {
    'ON' : '1',
    'OFF' : '0'
}

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection 

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    sys.stdout.write("Message received: "  + message.topic[23:] + '/' + message.payload + '\n')
    sys.stdout.flush()
    print "Message received: "  + message.topic[23:] + '/' + message.payload 
    system, device = message.topic[23:].split('/')
    command = commands.get(message.payload)
    system = format(int(system), '005b')
    device = devices.get(device)
    sys.stdout.write('/home/pi/433Utils/RPi_utils/send ' + system + ' ' + device + ' ' + str(command) + '\n')
    sys.stdout.flush()
    print '/home/pi/433Utils/RPi_utils/send ' + system + ' ' + device + ' ' + str(command) 
    subprocess.call(['/home/pi/433Utils/RPi_utils/send', system, device, str(command)])

def on_intertechno_message(client, userdata, message):
    sys.stdout.write("Intertechno: " + message.topic[23:] + '/' + message.payload + '\n')
    sys.stdout.flush()
    # print "Intertechno: " + message.topic[23:] + '/' + message.payload 
    group, device = message.topic[23:].split('/')
    code = int(data.get(group).get(device))
    command = commands.get(message.payload)
    code += int(command)
    sys.stdout.write('/home/pi/433Utils/RPi_utils/codesend ' + str(code) + '\n')
    sys.stdout.flush()  
    # print '/home/pi/433Utils/RPi_utils/codesend ' + str(code)
    subprocess.call(['/home/pi/433Utils/RPi_utils/codesend', str(code)])

Connected = False   #global variable for the state of the connection

broker_address= "ankh-morpork.fritz.box"  #Broker address
port = 1883                         #Broker port
# user = "yourUser"                    #Connection username
# password = "yourPassword"            #Connection password

client = mqttClient.Client("Python")               #create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.message_callback_add("/our place/commands/rf/a/#", on_intertechno_message)
client.message_callback_add("/our place/commands/rf/b/#", on_intertechno_message)
client.message_callback_add("/our place/commands/rf/c/#", on_intertechno_message)
client.message_callback_add("/our place/commands/rf/d/#", on_intertechno_message)


client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("/our place/commands/rf/#")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()