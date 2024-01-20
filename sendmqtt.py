import paho.mqtt.client as mqtt
# client = mqtt.Client()
# client.connect()
# client.publish("my_topic",)

# Replace with your MQTT broker details
broker_address = "hivemq.webclient.1705333862844"
topic = "MateCLAA"

# Define callback function for received messages (optional)
def on_message(client, userdata, message):
    print("Received message:", message.payload.decode())

client = mqtt.Client()
client.connect(broker_address)

# Publish a command
command = "your_command"
client.publish(topic, command)

# Optionally subscribe to a topic
client.subscribe(topic)  # If you want to receive messages
client.on_message = on_message

# Keep the client running to receive messages (if subscribed)
client.loop_forever()