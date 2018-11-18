# 导入类库
from machine import I2C, Pin, Timer
from mqtt import MQTTClient
import network
import bh1750
import time
import dht

# 初始化传感器
# 第一间教室
i2c = I2C(scl=Pin(22), sda=Pin(21))
dht1 = dht.DHT11(Pin(19))
num1 = Pin(5,Pin.IN)
num2 = Pin(17,Pin.IN)
led = Pin(16,Pin.OUT)

# 第二间教室
two_dht1 = dht.DHT11(Pin(25))
two_num1 = Pin(14,Pin.IN)
two_num2 = Pin(27,Pin.IN)
two_led = Pin(26,Pin.OUT)
# 初始化MQTT及网络
SSID = "SSID"
PASSWORD = "SSID-password"
SERVER = "server.id"
SERVER_PORT = "server.port"
CLIENT_ID = "carry" #任意设置，本身ESP32自己ID
username = "MQTT_userName"  
password = "MQTT_userPassWord"
c = None    # 连接对象
# 定义第一间教室data数据
tem = 0
hum = 0
lux = 0
old_total = 0
total = 0
led_state = "0"
cold_state = "1"
# 定义第二间教室data数据
two_tem = 0
two_hum = 0
two_lux = 0
two_old_total = 0
two_total = 0
two_led_state = "0"
two_cold_state = "1"
def connect_WIFI(ssid,password):
  global wlan
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,password)
  while(wlan.ifconfig()[0] == '0.0.0.0'):  # 等待连接
    time.sleep(1)
  
# 通过接受订阅信息发布信息
def handlemsg(topic,msg):  
  print(msg)
  if msg == b"tem":
    c.publish("sendmsg",str(tem).encode("utf-8"))
  elif msg == b"hum":
    c.publish("sendmsg",str(hum).encode("utf-8"))
  elif msg == b"lux":
    c.publish("sendmsg",str(lux).encode("utf-8"))
  elif msg == b"total":
    c.publish("sendmsg",str(total).encode("utf-8"))
  elif msg == b"all":
    m = str(tem)+ "," + str(hum) + "," + str(lux) + "," + str(total)
    c.publish("sendmsg",m.encode("utf-8"))
  else:
    c.publish("sendmsg",b"error command")
  
  
try:
  connect_WIFI(SSID,PASSWORD)
  server = SERVER
  c = MQTTClient(CLIENT_ID,server,SERVER_PORT,username,password)    # 连接MQTT服务
  c.set_callback(handlemsg) # 回调函数
  c.connect()
  c.subscribe("test_subscribe") # 订阅
  c.publish("sendmsg","")   # 发布

  while True:
    # 第一间教室
    # 统计人数
    if num1.value() == 1:
      while num1.value():
        if num2.value() == 1:
          total+=1
          print(total)
          while num1.value() | num2.value():
            pass
          break
    if num2.value() == 1:
      while num2.value():
        if num1.value() == 1:
          total-=1
          print(total)
          while num1.value() | num2.value():
            pass
          break
    if tem < 22:    # 温度控制
      cold_state = "1"
    else:
      cold_state = "0"
    if total < 1:   # 人数控制
      led.value(1)
      led_state = "0"
    else:
      led.value(0)
      led_state = "1"
      
      
    # 第二间教室
    # 统计人数
    if two_num1.value() == 1:
      while two_num1.value():
        if two_num2.value() == 1:
          two_total+=1
          print(two_total)
          while two_num1.value() | two_num2.value():
            pass
          break
    if two_num2.value() == 1:
      while two_num2.value():
        if two_num1.value() == 1:
          two_total-=1
          print(two_total)
          while two_num1.value() | two_num2.value():
            pass
          break
    if two_tem < 22:
      two_cold_state = "1"
    else:
      two_cold_state = "0"
    if two_total < 1:

      two_led.value(1)
      two_led_state = "0"
    else:
      two_led.value(0)
      two_led_state = "1"
    if (two_old_total != two_total) | (old_total != total): # 只有人数变化时做出判断
      dht1.measure()  # 读取dht1数据
      lux = bh1750.sample(i2c,i2c_addr=0x5c)   # 读取bh1750数据
      tem = dht1.temperature()
      hum = dht1.humidity()
      data = str(total)+","+str(tem)+","+cold_state+","+led_state+","+str(hum)+","+str(lux)
      old_total = total
      two_dht1.measure()  # 读取dht1数据
      two_lux = bh1750.sample(i2c)   # 读取bh1750数据
      two_tem = two_dht1.temperature()
      two_hum = two_dht1.humidity()
      two_data = str(two_total)+","+str(two_tem)+","+two_cold_state+","+two_led_state+","+str(two_hum)+","+str(two_lux)
      total_data = data +","+ two_data
      c.publish("sendmsg",total_data)
      print(total_data)
      two_old_total = two_total
finally:
  if c is not None:
    c.disconnect()
    wlan.disconnect()
    wlan.active(False)
  print("It is over.")