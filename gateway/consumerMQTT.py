import paho.mqtt.client as paho

broker = 'broker.mqttdashboard.com'
port = 1883
topic = "iot/cercaEletronica"
sensor_data = ['']

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    f = open("../alert.txt", "w")
    f.write(data)
    print(data)
    f.close()

client = paho.Client("user")  # create client object
client.on_message = on_message

print("connecting to broker host", broker)
client.connect(broker)  # connection establishment with broker
print("subscribing begins here")
client.subscribe(topic)  # subscribe topic test

def run():
    client.loop_forever()  # contineously checking for message

if __name__ == '__main__':
    f = open("../alert.txt", "w")
    f.write("False")
    f.close()
    run()


