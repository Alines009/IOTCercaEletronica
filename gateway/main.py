import socket
from geopy import distance
import json
import paho.mqtt.publish as publish

mqtt_broker = 'broker.mqttdashboard.com'
mqtt_port = 1883
mqtt_topic = "iot/cercaEletronica"

HOST = ''
PORT = 5556
checkpoints = []
verificationDistances = []

def readCheckpoints():
    f = open("../checkpoints.json")
    data = json.loads(f.read())
    f.close()
    for i in data['checkpoints']:
        checkpoints.append((i["lat"],i["lng"]))

def calculateDistance():
    distancia = 0
    for i in range(len(checkpoints)):
        if i != (len(checkpoints)-1):
            distancia = distance.distance(checkpoints[i],checkpoints[i+1]).km
        verificationDistances.append(distancia)
    print("Distâncias: ")
    print(verificationDistances)

def main():
    readCheckpoints()
    calculateDistance()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Aguardando dados ...' )
        while (True):
            message, address = s.recvfrom(8192)
            sensor_data = str(message).split(",")
            timestamp = sensor_data[0].replace("b'", "")
            if(len(sensor_data) > 15):
                lat_movel = sensor_data[2]
                lon_movel = sensor_data[3]
                atual = (float(lat_movel),float(lon_movel))
                alert = True
                for i in range(len(checkpoints)):
                    if (distance.distance(checkpoints[i],atual).km < verificationDistances[i]):
                        alert = False
                        break
                msg = str(alert)+"#"+str(atual)
                print(msg)
                publish.single(mqtt_topic, msg, hostname=mqtt_broker, port=mqtt_port)

if __name__ == "__main__":
    main()