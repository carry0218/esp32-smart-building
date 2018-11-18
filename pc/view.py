# 11.16

from tkinter import *

from subscription import *
import random

root = Tk()
root.title("教学楼控制系统2.0")

cv = Canvas(root, width = 1010, height = 965)
cv.pack()

# title1 = Label(root, text="教 学 楼 控 制 系 统 2.0", font=("宋体", 20, "normal")).place(x = 350 , y = 10)


cv.create_rectangle(20, 55, 330, 335)
cv.create_rectangle(350, 55, 660, 335)
cv.create_rectangle(680, 55, 990, 335)

cv.create_rectangle(20, 355, 330, 645)
cv.create_rectangle(350, 355, 660, 645)
cv.create_rectangle(680, 355, 990, 645)

cv.create_rectangle(20, 665, 330, 955)
cv.create_rectangle(350, 665, 660, 955)
cv.create_rectangle(680, 665, 990, 955)

x1 = 330
y1 = 305

# 教室号
Label(root ,text = "101", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 , y = 65)
Label(root ,text = "102", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 + x1 , y = 65)
Label(root ,text = "103", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 + 2 * x1, y = 65)

Label(root ,text = "201", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 , y = 65 + y1)
Label(root ,text = "202", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 + x1 , y = 65 + y1)
Label(root ,text = "203", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 + 2 * x1, y = 65 + y1)

Label(root ,text = "301", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 , y = 65 + y1 * 2)
Label(root ,text = "302", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 + x1 , y = 65 + y1 * 2)
Label(root ,text = "303", bd = 5, relief = SUNKEN, font=("宋体", 20, "normal")).place(x = 145 + 2 * x1, y = 65 + y1 * 2)

# 人 数
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 , y = 115)
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 115)
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 115)
 
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 , y = 115 + y1)
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 115 + y1)
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 115 + y1)
 
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 , y = 115 + y1 * 2)
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 115 + y1 * 2)
Label(root ,text = "人  数:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 115 + y1 * 2)

# 人数单位
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 , y = 115)
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 + x1, y = 115)
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 + x1 * 2, y = 115)

Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 , y = 115 + y1)
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 + x1, y = 115 + y1)
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 + x1 * 2, y = 115 + y1)

Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 , y = 115 + y1 * 2)
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 + x1, y = 115 + y1 * 2)
Label(root ,text = "人", font=("宋体", 12, "normal")).place(x = 230 + x1 * 2, y = 115 + y1 * 2)

# 温度
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 , y = 150)
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 150)
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 150)
  
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 , y = 150 + y1)
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 150 + y1)
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 150 + y1)
  
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 , y = 150 + y1 * 2)
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 150 + y1 * 2)
Label(root ,text = "温  度:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 150 + y1 * 2)

# 温度单位
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 , y = 150)
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 + x1, y = 150)
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 + x1 * 2, y = 150)

Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 , y = 150 + y1)
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 + x1, y = 150 + y1)
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 + x1 * 2, y = 150 + y1)

Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 , y = 150 + y1 * 2)
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 + x1, y = 150 + y1 * 2)
Label(root ,text = "℃", font=("宋体", 12, "normal")).place(x = 230 + x1 * 2, y = 150 + y1 * 2)

# 空调
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 , y = 185)
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 185)
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 185)
  
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 , y = 185 + y1)
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 185 + y1)
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 185 + y1)
  
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 , y = 185 + y1 * 2)
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 185 + y1 * 2)
Label(root ,text = "空  调:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 185 + y1 * 2)

# 吊灯
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 , y = 220)
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 220)
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 220)
 
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 , y = 220 + y1)
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 220 + y1)
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 220 + y1)
 
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 , y = 220 + y1 * 2)
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 220 + y1 * 2)
Label(root ,text = "吊  灯:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 220 + y1 * 2)

# 湿度
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 , y = 255)
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 255)
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 255)
  
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 , y = 255 + y1)
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 255 + y1)
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 255 + y1)
  
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 , y = 255 + y1 * 2)
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 255 + y1 * 2)
Label(root ,text = "湿  度:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 255 + y1 * 2)

# 湿度单位
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 , y = 255)
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 + x1, y = 255)
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 + x1 * 2, y = 255)

Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 , y = 255 + y1)
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 + x1, y = 255 + y1)
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 + x1 * 2, y = 255 + y1)

Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 , y = 255 + y1 * 2)
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 + x1, y = 255 + y1 * 2)
Label(root ,text = "%", font=("宋体", 12, "normal")).place(x = 235 + x1 * 2, y = 255 + y1 * 2)

# 光强
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 , y = 290)
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 290)
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 290)
  
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 , y = 290 + y1)
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 290 + y1)
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 290 + y1)
  
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 , y = 290 + y1 * 2)
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 + x1, y = 290 + y1 * 2)
Label(root ,text = "光  强:", font=("宋体", 12, "normal")).place(x = 80 + x1 * 2, y = 290 + y1 * 2)

# 光强单位
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 , y = 290)
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 + x1, y = 290)
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 + x1 * 2, y = 290)

Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 , y = 290 + y1)
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 + x1, y = 290 + y1)
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 + x1 * 2, y = 290 + y1)

Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 , y = 290 + y1 * 2)
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 + x1, y = 290 + y1 * 2)
Label(root ,text = "lux", font=("宋体", 12, "normal")).place(x = 235 + x1 * 2, y = 290 + y1 * 2)


root.maxsize(1010, 975)
root.minsize(1010, 975)
print("shuo")

# 其他教室


b = []
c = ["0","0","0","0","0","0"]
d = ["0","0","0","0","0","0"]


def rn():
    global c
    c[0] = str(random.randint(35,45))
    c[1] = str(random.randint(18,26))
    c[2] = "1"
    c[3] = "1"
    c[4] = str(random.randint(15,28))
    c[5] = str(random.randint(500,580))

def rn2():
    global d
    d[0] = str(random.randint(60,85))
    d[1] = str(random.randint(23,26))
    d[2] = "1"
    d[3] = "1"
    d[4] = str(random.randint(28,50))
    d[5] = str(random.randint(500,620))


def read_loop():
    global b

    # 教室1
    Label(root, text = "  ", font=("宋体", 12, "normal")).place(x = 180, y = 115)
    
    if b[0] < "0":
        b[0] = "0"
    else:
        pass
    Label(root, text = b[0], font=("宋体", 12, "normal")).place(x = 180, y = 115)
   
    Label(root, text = b[1], font=("宋体", 12, "normal")).place(x = 180, y = 150)

    if b[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180, y = 185)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180, y = 185)

    if b[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180, y = 220)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180, y = 220)

    Label(root, text = b[4], font=("宋体", 12, "normal")).place(x = 180, y = 255)
    Label(root, text = "370", font=("宋体", 12, "normal")).place(x = 180, y = 290)

    # 教室2
    Label(root, text = "  ", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 115)
    if b[6] < "0":
        b[6] = "0"
    else:
        pass
    Label(root, text = b[6], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 115)
    Label(root, text = b[7], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 150)

    
    Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 185)

    if b[9] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 220)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 220)

    Label(root, text = b[10], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 255)
    Label(root, text = b[11], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 290)

def oroom():    
    # 教室3
    rn()
    Label(root, text = c[0], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 115)
    Label(root, text = c[1], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 150)

    if c[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 185)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 185)

    if c[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 220)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 220)

    Label(root, text = c[4], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 255)
    Label(root, text = c[5], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 290)


    # 教室4
    rn()
    Label(root, text = c[0], font=("宋体", 12, "normal")).place(x = 180, y = 115 + y1)
    Label(root, text = c[1], font=("宋体", 12, "normal")).place(x = 180, y = 150 + y1)

    if c[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180, y = 185 + y1)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180, y = 185 + y1)

    if c[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180, y = 220 + y1)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180, y = 220 + y1)

    Label(root, text = c[4], font=("宋体", 12, "normal")).place(x = 180, y = 255 + y1)
    Label(root, text = c[5], font=("宋体", 12, "normal")).place(x = 180, y = 290 + y1)

    # 教室5
    rn2()
    Label(root, text = d[0], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 115 + y1)
    Label(root, text = d[1], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 150 + y1)

    if d[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 185 + y1)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 185 + y1)

    if d[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 220 + y1)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 220 + y1)

    Label(root, text = d[4], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 255 + y1)
    Label(root, text = d[5], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 290 + y1)


    # 教室6
    rn()
    Label(root, text = c[0], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 115 + y1)
    Label(root, text = c[1], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 150 + y1)

    if c[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 185 + y1)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 185 + y1)

    if c[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 220 + y1)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 220 + y1)

    Label(root, text = c[4], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 255 + y1)
    Label(root, text = c[5], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 290 + y1)


    # 教室7
    rn2()
    Label(root, text = d[0], font=("宋体", 12, "normal")).place(x = 180, y = 115 + y1*2)
    Label(root, text = d[1], font=("宋体", 12, "normal")).place(x = 180, y = 150 + y1*2)

    if d[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180, y = 185 + y1*2)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180, y = 185 + y1*2)

    if d[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180, y = 220 + y1*2)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180, y = 220 + y1*2)

    Label(root, text = d[4], font=("宋体", 12, "normal")).place(x = 180, y = 255 + y1*2)
    Label(root, text = d[5], font=("宋体", 12, "normal")).place(x = 180, y = 290 + y1*2)

    # 教室8
    rn()
    Label(root, text = c[0], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 115 + y1*2)
    Label(root, text = c[1], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 150 + y1*2)

    if c[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 185 + y1*2)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 185 + y1*2)

    if c[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 220 + y1*2)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1, y = 220 + y1*2)

    Label(root, text = c[4], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 255 + y1*2)
    Label(root, text = c[5], font=("宋体", 12, "normal")).place(x = 180 + x1, y = 290 + y1*2)

    # 教室9
    rn()
    Label(root, text = c[0], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 115 + y1*2)
    Label(root, text = c[1], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 150 + y1*2)

    if c[2] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 185 + y1*2)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 185 + y1*2)

    if c[3] == "1":
        Label(root, text = "开", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 220 + y1*2)
    else:
        Label(root, text = "关", font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 220 + y1*2)

    Label(root, text = c[4], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 255 + y1*2)
    Label(root, text = c[5], font=("宋体", 12, "normal")).place(x = 180 + x1*2, y = 290 + y1*2)



n = 0
def read():
    global b, n
    infile = open("subscription.txt","r")
    a = infile.readline()
    b = a.split(",")
    infile.close()
    root.after(1000, read)
    read_loop()
    n = n + 1
    if n > 5:
        n = 0
        oroom()

read()

root.mainloop()

