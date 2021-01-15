# hubzigbee
Development of a Hub using Zigbee and MQTT protocol. 


Description  - MQTT control between zigbee2mqtt and MOSQUITTO broker


CONFIG: 
    # Clone Zigbee2MQTT repository
          sudo git clone https://github.com/Koenkk/zigbee2mqtt.git /opt/zigbee2mqtt
    
    instructions: https://www.zigbee2mqtt.io/getting_started/running_zigbee2mqtt.html
    
    # Raspberry terminal : nano /opt/zigbee2mqtt/data/configuration.yaml -> change IP
    # HUB_zigbee: change broker IP (MOSQUITTO_ADDRESS)
    # Optional: run zigbee2mqtt cd /opt/zigbee2mqtt &&  npm start
