import paho.mqtt.client as mqtt
from azure.iot.device import IoTHubDeviceClient, Message  
import os


######  AZURE - cloud connection test  ###############
CONNECTION_STRING = "HostName=hubEMIDIT.azure-devices.net;DeviceId=gatewayRasp;SharedAccessKey=l8tVvb3Vn7nlU8mep7UEFqJ2Qd+tK0P2HDHuAy3wrSI="  

def iothub_client_init():  
    clientAzure = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return clientAzure  
  
#Start Azure client instance
clientAzure = iothub_client_init()

####### system zigbee2mqtt init ################
os.system('mosquitto')
os.system('cd /opt/zigbee2mqtt &&  npm start')

####### MQTT Configuration #################
MOSQUITTO_ADDRESS = '192.168.0.101'
#MQTT_USER = 'cdavid'
#MQTT_PASSWORD = 'cdavid'
MOSQUITTO_TOPIC = 'zigbee2mqtt/smoke sensor'
#MQTT_TOPIC   = "zigbee2mqtt/bridge/log"
#zigbee2mqtt_TOPIC = 'zigbee2mqtt/smoke sensor/get'

############# Clients queue - python list -> each client has different topics ##########
clients=[]
nclients=20
mqtt.Client.connected_flag=False


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MOSQUITTO_TOPIC)
    
def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    #client.subscribe('zigbee2mqtt/bridge/config/devices')
    print(msg.topic + ' ' + str(msg.payload))
    client.publish("nodered_test",msg.payload)
    clientAzure.send_message(msg.payload)
    

def main():
    #creating a Client instance
    mqtt_client = mqtt.Client()   

    #mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    #multithreading operation
    #  create clients
    ##    for i  in range(nclients):
    ##       cname="Client"+str(i)
    ##       client= mqtt.Client(cname)
    ##       clients.append(client)
    ##    for client in clients:
    ##      client.connect(broker)
    ##      client.loop_start()
   
    mqtt_client.on_connect = on_connect

    #Attach function to callback
    mqtt_client.on_message = on_message

    #Connecting to broker - Mosquitto Raspberry pi (conf IP rasp)
    mqtt_client.connect(MOSQUITTO_ADDRESS, 1883)

    #Loop  - waiting for callbacks     
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()

