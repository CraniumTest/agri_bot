import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("farm/sensors/+")

def on_message(client, userdata, msg):
    print(f"\{msg.topic\} {str(msg.payload)}")  # Process incoming IoT data

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_start()
