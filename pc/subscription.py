import paho.mqtt.client as mqtt
import time

HOST = "host.ip"
PORT = "port"

def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id) # ClientId不能重复，所以使用当前时间 
    client.username_pw_set("mqtt.user", "password") # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sendmsg")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))
    outfile = open("subscription.txt","w")
    outfile.write(msg.payload.decode("utf-8"))
    outfile.close()


if __name__ == '__main__':
    client_loop()