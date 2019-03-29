import json
import os
import random
import socket
import ssl
import time
from credentials import *
import paho.mqtt.client as paho


AWSPORT = 8883
connflag = False

def on_connect(client, userdata, flags):
    global connflag
    connflag = True

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def main():
    mqttc = paho.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    mqttc.tls_set(ROOTCA, certfile=CERT, keyfile=PRKEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    mqttc.connect(AWSHOST, AWSPORT, keepalive=60)

    mqttc.loop_start()

    while True:
        result_json = {
            "Time": random.randint(800000, 815000),
            "Latitude": round(random.uniform(-90,90), 5),
            "Longitude": round(random.uniform(-180, 180), 5),
            "Boat_ID": random.randint(1, 100),
            "Speed": round(random.uniform(0, 50), 5),
            "Fuel_flow": round(random.uniform(2, 5), 5),
            "Engine_rpm": random.randint(500, 800)
        }
        """with open('trip1-2.json') as json_file:
            result_json = json.load(json_file)
            for result in result_json:
                time_value = result['Time']
                engine_rpm = result['Engine_rpm']
                depth = result['Depth']
                heading = result['Heading']
                fuel_tank1 = result['Fuel_tank1']
                speed = result['Speed']
                lat = result['Latitude']
                longi = result['Longitude']
                engi_trim = result['Engine_trim']
                fuel_flow = result['Fuel_flow']
                water_temp = result['Water_temp']
                engine_hrs = result['Engine_hours']
                engine_tmp = result['Engine_temp']
                engine2_rmp = result['Engine2_rpm']
                engine2_trim = result['Engine2_trim']
                engine2_hours = result['Engine2_hours']
                engine2_temp = result['Engine2_temp']
                econ = result['Econ']
                fuel_tank2 = result['Fuel_tank2']
                wind_speed = result['Wind_speed']

                json1 = {
                    "Time": time_value,
                    "Engine_rpm": engine_rpm,
                    "Depth": depth,
                    "Heading": heading,
                    "Fuel_tank1": fuel_tank1,
                    "Speed": speed,
                    "lat": lat,
                    "long": longi,
                    "Engine_trim": engi_trim,
                    "Fuel_flow": fuel_flow,
                    "Water_temp": water_temp,
                    "Engine_hours": engine_hrs,
                    "Engine_temp": engine_tmp,
                    "Engine2_rpm": engine2_rmp,
                    "Engine2_trim": engine2_trim,
                    "Engine2_hours": engine2_hours,
                    "Engine2_temp": engine2_temp,
                    "Econ": econ,
                    "Fuel_tank2": fuel_tank2,
                    "Wind_speed": wind_speed
                }"""
        mqttc.publish("coordinates", json.dumps(result_json), qos=1)
        print("Message published")
        print(result_json)
        time.sleep(5)

if __name__ == "__main__":
    main()