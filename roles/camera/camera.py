import paho.mqtt.client as mqtt
import time
import datetime as dt
import picamera

def on_message(client, userdata, message):
    print "Message received: "  + message.payload
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
    # Camera warm-up time
        time.sleep(2)
        camera.rotation = 180
        camera.annotate_text =  dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.annotate_text_size = 25
        camera.exif_tags['GPS.GPSLatitude'] = '49/1,37/1,10/1'
        camera.exif_tags['GPS.GPSLatitude'] = '11/1,11/1,40/1'
        camera.capture('test.jpg')
        camera.close()  

client = mqtt.Client()
client.connect("ankh-morpork.fritz.box")

client.on_message = on_message

client.loop_start()
    
client.subscribe("/python/test")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()