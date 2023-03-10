from pkgutil import ImpImporter
from kafka import KafkaConsumer
from kubo import KuboOrder
from kubo import KuboInfo
import time
import json

# from kubosql import KuboStability
# import matplotlib.pyplot as plt
# import matplotlib
# from matplotlib.pyplot import MultipleLocator, FormatStrFormatter
# 称重测试
# f = open('test1.txt','a')

marker_robot = KuboOrder("172.21.10.240", "9092", "STANDARD0")
# marker_robot.robot_internal_fork('4160',0,0)
# marker_robot.robot_internal_tray('4160',0,5)
marker_robot.robot_init('218')
# marker_robot.robot_internal_inventory('75',0,0)
# marker_robot.robot_move('4160',{'x':69.25,'y':42.92,'theta':1.57},1,500,0)
# marker_robot.robot_setup('4160', 'system::action','enter_low_power')
# marker_robot.robot_setup('4160', 'system::action','leave_low_power')
# a = False
# b = True
# marker_robot.robot_external("4160","TAKE",0,{'x':69.25,'y':42.92,'theta':0},1380,0)

# marker_robot.robot_setup('4160','system::sleep',{"auto_sleep_enable": b,"auto_sleep_wait_time":1800})
# marker_robot.robot_external("4160","PUT",0,{'x':69.25,'y':42.92,'theta':0},1380,0)

# marker_robot.robot_setup('4160','system::low_power',{"auto_low_power_enable": a,"auto_low_power_wait_time":800})

# print(marker_robot.get_info('4160'))
# marker_robot.robot_move('4160',{'x':69.25,'y':42.92,'theta':1.57},1,625,0)
# marker_robot.robot_internal_fork('4160',0,1)
# marker_robot.robot_move('4160',{'x':42.69,'y':48.94,'theta':3.14},2,625,0)
# marker_robot.robot_external("4160","PUT",10,{'x':69.25,'y':42.92,'theta':0},1380,0)

# marker_robot.robot_external("4160","PUT",10,{'x':69.25,'y':42.92,'theta':0},1380,0)
# marker_robot.robot_external_inventory('4160',{'x':69.25,'y':42.92,'theta':0},1380,0,1)

# robot_info = KuboInfo("172.21.10.240")
# marker_robot.robot_external("4160","TAKE",10,{'x':69.25,'y':42.92,'theta':0},1380,0)

# marker_robot.robot_external("4160","PUT",10,{'x':69.25,'y':42.92,'theta':0},1380,0)
# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)

# marker_robot.robot_init('4160')
# f.write("init"+"\n")
# marker_robot.robot_resume('218')
# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)

# marker_robot.robot_external_kiva('218',"TAKE",{'x':37.88,'y':53.67,'theta':1.57},{'x':37.85,'y':52.75,'theta':1.57},400,10,30)
# for i in range(100):
# print(robot_info.get_info('4160'))
# print(robot_info.get_info('4160'))

# marker_robot = KuboOrder("172.21.10.240","9092","STANDARD0")

# for i in range(1000):
#     time.sleep(0.2)
#     f.write(str(marker_robot.get_info('4160'))+"\n")
#     print(marker_robot.get_info('4160'))

# # marker_robot.robot_move('142',{'x':39.85,'y':52.77,'theta':3.14},1,1390,-1.57)
# # marker_robot.robot_move('142',{'x':48.85,'y':52.77,'theta':3.14},1,400,0)
# # marker_robot.robot_move('184',{'x':42.96,'y':61.44,'theta':3.14},3,400,0)
# marker_robot.robot_move('184',{'x':39.00,'y':61.44,'theta':3.14},3,400,-1.57)

# marker_robot.robot_external('142',"TAKE",0,{'x':39.85,'y':52.77,'theta':-1.57},1390.0,0)

# marker_robot.robot_external('184',"PUT",0,{'x':39.00,'y':61.44,'theta':-1.57},1390.0,0)

# marker_robot.robot_internal_tray('4160',0,0)
# marker_robot.robot_internal_fork('4160',0,1)

# marker_robot.robot_internal_inventory('4160',1,0)
# marker_robot.robot_move('4160',{'x':37.88,'y':48.94,'theta':3.14},1,400,0)
# marker_robot.robot_move('145',{'x':24.69,'y':52.93,'theta':3.14},1,625,0)
# marker_robot.robot_move('145',{'x':34.77,'y':52.93,'theta':0},1,625,0)

# marker_robot.robot_move('145',{'x':32.79,'y':52.93,'theta':0},1,625,0)
# marker_robot.robot_move('72',{'x':33.28,'y':43.68,'theta':3.14},1,625,0)

# marker_robot.robot_external('4160',"PUT",0,{'x':40.38,'y':48.94,'theta':1.57},1825.0,0)
# marker_robot.robot_external('72',"TAKE",0,{'x':33.28,'y':43.68,'theta':-1.57},650.0,0)
# marker_robot.robot_external('72',"PUT",0,{'x':33.28,'y':43.68,'theta':-1.57},650.0,0)

# marker_robot.robot_external('4160',"TAKE",0,{'x':40.38,'y':48.94,'theta':1.57},1425.0,0)
# marker_robot.robot_external('4160',"PUT",0,{'x':37.88,'y':48.94,'theta':-1.57},1425.0,0)

# marker_robot.robot_move('147',{'x':24.69,'y':52.93,'theta':3.14},1,400,0)
# marker_robot.robot_move('147',{'x':34.75,'y':52.93,'theta':3.14},1,400,0)
# marker_robot.robot_move('147',{'x':33.28,'y':52.93,'theta':3.14},1,400,0)
# marker_robot.robot_move('147',{'x':33.28,'y':52.93,'theta':3.14},1,650,1.57)
# marker_robot.robot_external('145',"TAKE",0,{'x':32.79,'y':52.93,'theta':1.57},650.0,0)
# marker_robot.robot_external('145',"PUT",0,{'x':32.79,'y':52.93,'theta':1.57},650.0,0)
# robot_info = KuboInfo("172.23.200.160")

# print(robot_info.get_info('150'))


# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)
# marker_robot.robot_external("4160","TAKE",10,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_internal_fork('4160',0,0)
# marker_robot.robot_internal_inventory('129',0,1)
# marker_robot.robot_external("4160","PUT",10,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_init('150')

# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)
# marker_robot.robot_external("4160", "TAKE", 0, {'x': 69.25, 'y': 42.92, 'theta': 0}, 1380, 0)
# marker_robot.robot_external("4160", "PUT", 10, {'x': 69.25, 'y': 42.92, 'theta': 0}, 1380, 0)
marker_robot.robot_move_chassis('218', {'x': 37.88, 'y': 52.75, 'theta': 1.57}, 1)
# time.sleep(1)
# marker_robot.robot_move_chassis('218',{'x':37.88,'y':52.75,'theta':1.57},0)
# # time.sleep(1)

# marker_robot.robot_move_chassis('218',{'x':46.77,'y':52.75,'theta':0},0)
# # time.sleep(1)


# # marker_robot.robot_move_chassis('220',{'x':37.88,'y':48.94,'theta':1.57},0)

# marker_robot.robot_pause('218',"STOP_ACTION")
# 放货
# sending message: head(usMagic=0xfacedead usSize=2080 channel=4 msgSeq=12215431 devSeq=220 crcBody=0x146 crcHead=0x1dde) data
# ({"executionDetail":{"StatisticsInfo":{"MoveDistance":{"finger":0,"lift":76.709,"rotate":0.0,"stretch":0.0}},
# "message":{"binId":"external PUT goods","entrancePosition":{"theta":1.57,"x":37.85,"y":53.67},"locationType":30,
# "msgType":2,"opType":0,"robotId":"220","seqNum":1663930174153,"targetHeight":400,"targetPosition":{"theta":1.57,"x":37.85,"y":52.75}},
# "recvTimeStamp":"2022-09-23 18:49:34.582290","sendTimeStamp":"2022-09-23 18:49:39.467128","stateDetails":[
# {"chassisPosition":{"theta":1.571429967880249,"x":37.860599517822266,"y":53.6703987121582},"fingerPosition":0.0,"liftPosition":379.523,
# "rotatePosition":0.0,"state":"START","stretchPosition":0.0,"timeStamp":"2022-09-23 18:49:34.583965"},{"chassisPosition":
# {"theta":1.571429967880249,"x":37.860599517822266,"y":53.6703987121582},"fingerPosition":0.0,"liftPosition":379.521,"rotatePosition":0.0,
# "state":"PREPARE","stretchPosition":0.0,"timeStamp":"2022-09-23 18:49:34.589804"},{"chassisPosition":
# {"theta":1.571470022201538,"x":37.860599517822266,"y":53.67060089111328},"fingerPosition":0.0,"liftPosition":418.525,
# "rotatePosition":0.0,"state":"JACK","stretchPosition":0.0,"timeStamp":"2022-09-23 18:49:35.992272"},{"chassisPosition":
# {"theta":1.565369963645935,"x":37.8557014465332,"y":52.81610107421875},"fingerPosition":0.0,"liftPosition":418.961,"rotatePosition":0.0,"state":
# "ENTER_LOCATION","stretchPosition":0.0,"timeStamp":"2022-09-23 18:49:38.200660"},{"chassisPosition":{"theta":1.5737700462341309,"x":37.88520050048828,
# "y":52.749900817871094},"fingerPosition":0.0,"liftPosition":381.694,"rotatePosition":0.0,"state":"DOWN","stretchPosition":0.0,"timeStamp":"2022-09-23 18:49:39.461606"}
# ,{"chassisPosition":{"theta":1.5737700462341309,"x":37.88520050048828,"y":52.749900817871094},"fingerPosition":0.0,"liftPosition":381.694,"rotatePosition":0.0,"state":"SUCC",
# "stretchPosition":0.0,"timeStamp":"2022-09-23 18:49:39.461957"}]},"executionResult":0,"msgType":7,"operatingHeight":420.0,"operatingPosition":{"theta":-1.5715926885604858,"x":37.849998474121094,
# "y":53.66999816894531},"robotId":"220","seqNum":1663930174153})
# time.sleep(1)


# marker_robot.robot_internal_tray('4183',0,0) 
# time.sleep(2)
# for i in range(0,100):
#     print(robot_info.get_info('4183'))
#     time.sleep(0.2)

# marker_robot = KuboOrder("172.23.200.160","9092","STANDARD0")
# marker_robot = KuboOrder("172.21.10.240","9092","STANDARD0")
# marker_robot.robot_init('4160')
# marker_robot.robot_move('4160',{'x':37.88,'y':48.94,'theta':3.14},1,625,0)
# marker_robot.robot_move('4160',{'x':69.25,'y':42.92,'theta':1.57},1,625,0)
# marker_robot.robot_external_inventory('129',{"x":68.45,"y":33.51,"theta":-1.57},1200,0,1)
# marker_robot.robot_internal_fork('4160',0,2)
# marker_robot.robot_external("4160","TAKE",10,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_external("4160","PUT",10,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)
# marker_robot.robot_external("4160","PUT",10,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)

# marker_robot.robot_move('148',{'x':24.69,'y':54.65,'theta':1.57},1,625,0)
# marker_robot.robot_external("4160","TAKE",10,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_external("4160","PUT",0,{'x':69.25,'y':42.92,'theta':0},1390,0)
# marker_robot.robot_move('4160',{'x':69.25,'y':43.98,'theta':1.57},1,625,0)

# marker_robot.robot_external('4160',"PUT",0,{'x':40.38,'y':48.94,'theta':1.57},1425.0,0)

# marker_robot.robot_internal_inventory("4160",2,1)

# marker_robot.robot_init('4150')
# marker_robot.robot_external("152","TAKE",0,{'x':12.73,'y':63.43,'theta':-1.57},1390,10)

# marker_robot.robot_internal_tray('152',10,1)
# marker_robot.robot_move('152',{'x':17.27,'y':63.43,'theta':3.14},1,400,0)
# marker_robot.robot_move('4084',{'x':42.11,'y':61.44,'theta':3.14},1,1000,1.57)
# marker_robot.robot_move('4084',{'x':36.10,'y':61.44,'theta':3.14},1,1000,1.57)

# marker_robot.robot_external("152","TAKE",10,{'x':12.73,'y':63.43,'theta':-1.57},1390,10)

# marker_robot.robot_external("152","PUT",10,{'x':12.73,'y':63.43,'theta':-1.57},1390,10)

# marker_robot.robot_internal_fork('152',10,1)
# marker_robot.robot_move('182',{'x':39.62,'y':78.16,'theta':3.14},1,625,0)
# marker_robot.robot_external("152","TAKE",10,{'x':12.73,'y':63.43,'theta':-1.57},1390,0)
# for i in range(0,100):
#     marker_robot.robot_external_inventory('4084',{'x':36.10,'y':61.44,'theta':1.57},3800,0,1)
#     time.sleep(2)
# marker_robot.robot_external_inventory('4084',{'x':36.10,'y':61.44,'theta':1.57},3800,0,1)
# marker_robot = KuboOrder("172.23.200.160","9092","STANDARD0")
# marker_robot.robot_move('4150',{'x':3.16,'y':63.43,'theta':3.14},1,4800,0)

# marker_robot.robot_move('182',{'x':35.57,'y':78.16,'theta':3.14},1,625,0)
# marker_robot.robot_external_inventory('4150',{'x':34.59,'y':78.16,'theta':-1.57},1390,0,1)
# marker_robot.robot_move('4150',{'x':3.16,'y':63.43,'theta':3.14},1,625,0)
# marker_robot.robot_move('4150',{'x':2.21,'y':63.43,'theta':3.14},1,625,0)

# marker_robot.robot_external_inventory('4150',{'x':3.16,'y':63.43,'theta':-1.57},1390,0,1)
# marker_robot.robot_external("152","PUT",10,{'x':12.73,'y':63.43,'theta':-1.57},1350.0,0)

# marker_robot.robot_external("4150","TAKE",0,{'x':3.16,'y':63.43,'theta':-1.57},1350.0,0)
# marker_robot.robot_external("4150","PUT",0,{'x':3.16,'y':63.43,'theta':-1.57},1350.0,0)
# marker_robot.robot_move('4150',{'x':2.21,'y':63.43,'theta':3.14},1,625,0)

# marker_robot.robot_move('4150',{'x':2.21,'y':63.43,'theta':3.14},1,625,0)

# marker_robot.robot_external("1150","PUT",0,{'x':4.14,'y':63.43,'theta':-1.57},1350.0,0)
# marker_robot.robot_move('1150',{'x':6.42,'y':63.43,'theta':3.14},1,400,0)

# # marker_robot.robot_move('4182',{'x':39.62,'y':78.16,'theta':3.14},1,1390,0)
# marker_robot.robot_move('182',{'x':34.59,'y':78.16,'theta':3.14},1,1390,0)


# marker_robot.robot_external("160","PUT",0,{'x':40.37,'y':48.94,'theta':1.57},1425,0)
# marker_robot.robot_external("160","PUT",0,{"x":69.80,"y":45.56,"theta":-1.57},2190.0,0)

# marker_robot = KuboOrder("172.23.200.160","9092","STANDARD0")# marker_robot.robot_move('4160', {'x':37.88,'y':48.94,'theta':3.14},1,1425,0)

# marker_robot.robot_external_inventory('4160',{'x':40.38,'y':48.94,'theta':1.57},1420,0,0)    
# marker_robot.robot_external('148',"PUT",0,{'x':33.28,'y':50.61,'theta':1.57},650.0,0)
# marker_robot = KuboOrder("172.23.200.160","9092","STANDARD0")
# marker_robot = KuboOrder("172.21.10.240","9092","CUSTOM0-SIZE0.4x0.30x0.15")
# marker_robot = KuboOrder("172.21.10.240","9092","STANDARD0")
# marker_robot.robot_move('147',{'x':24.69,'y':50.66,'theta':3.14},1,625,0)
# marker_robot.robot_move('147',{'x':24.69,'y':52.93,'theta':3.14},1,625,0)
# marker_robot.robot_init('147')
# marker_robot.robot_move('147',{'x':33.28,'y':50.66,'theta':3.14},1,625,0)

# marker_robot.robot_external('147',"TAKE",0,{'x':33.28,'y':50.66,'theta':1.57},650.0,0)
# marker_robot.robot_internal_fork('147',0,0)
# marker_robot.robot_internal_tray('147',0,0)

# # time.sleep(0.1)
# marker_robot.robot_external('147',"PUT",0,{'x':33.28,'y':52.93,'theta':1.57},1050.0,0)

# marker_robot.robot_external_inventory('148',{'x':33.28,'y':50.61,'theta':1.57},650,0,1)


# marker_robot.robot_external_inventory('4084',{'x':35.52,'y':78.15,'theta':1.57},600,0,1)
# marker_robot.robot_setup('160','system::action','recovery')\
# marker_robot.robot_pause('160','STOP_COMMAND')
# marker_robot = KuboOrder("172.23.200.160","9092","STANDARD0")
# marker_robot.robot_pause('145','STOP_COMMAND')

# marker_robot.robot_resume('145')

# marker_robot = KuboOrder("172.21.20.6","9092","CUSTOM0-SIZE0.60x0.40x0.28")
# marker_robot.robot_move('4160',{'x':37.88,'y':48.94,'theta':3.14},0,400,0)

# marker_robot.robot_move('4160',{'x':40.37,'y':48.94,'theta':3.14},0,400,0)
# marker_robot.robot_external("4160","TAKE",0,{'x':40.37,'y':48.94,'theta':1.57},1425,0)
# marker_robot.robot_external("4160","PUT",0,{'x':40.37,'y':48.94,'theta':1.57},1425,0)

# time.sleep(1)
# marker_robot.robot_external("159","TAKE",10,{'x':40.37,'y':48.94,'theta':-1.57},1425,0)
# marker_robot.robot_internal_fork('160',0,2)
# marker_robot.robot_internal_tray('148',0,1)
# time.sleep(1)
# marker_robot.robot_move('160',{'x':69.77,'y':45.56,'theta':1.57},0,625,0)
# marker_robot.robot_external("160","PUT",0,{"x":69.77,"y":45.56,"theta":0},590.0,0)
# # time.sleep
# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,625,0)
# time.sleep(1)
# marker_robot.robot_move('4182',{'x':39.62,'y':78.16,'theta':3.14},1,1390,0)
# marker_robot.robot_move('4182',{'x':35.57,'y':78.16,'theta':3.14},1,1390,0)

# marker_robot.robot_external("160","PUT",0,{'x':40.38,'y':48.94,'theta':1.57},1420,0)
# marker_robot.robot_internal_fork('160',0,1)
# marker_robot.robot_move('160',{'x':-140.88,'y':-248.94,'theta':3.14},1,400,0)
# 目标点
# tagposition = {'x':37.88,'y':48.94}

# robot_info = KuboInfo("172.21.20.6")
# # print(robot_info.motionSpeed("160"))
# speed_list_x = []
# speed_list_y = []
# while True:
#     robot_info = KuboInfo("172.21.20.6")
#     # print(robot_info)
#     robot_position = robot_info.mapPosition('160')
#     robot_speed = robot_info.motionSpeed('160')
#     speed_list_x.append(abs(robot_speed['x']))
#     speed_list_y.append(abs(robot_speed['y']))
#     if abs(robot_position['x'] - tagposition['x']) < 0.2 and abs(robot_position['y'] - tagposition['y']) < 0.2:
#         break
#     else:
#         time.sleep(0.2)
#         continue

# # print(speed_list_x)
# # print(speed_list_y)
# x = [i*0.2 for i in range(0, len(speed_list_x))]
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# x_max_speed = max([abs(a) for a in speed_list_x])
# y_max_speed = max([abs(b) for b in speed_list_y])
# plt.figure(figsize=(10, 5))
# plt.grid(ls='--')
# plt.plot(x, speed_list_x, color='red', label='x max:' + str(x_max_speed))
# plt.plot(x, speed_list_y, color='black', label='y max:' + str(y_max_speed))
# plt.title('robot move speed')
# plt.xlabel('time(s)')
# plt.ylabel('speed(m/s)')
# from matplotlib.pyplot import MultipleLocator, FormatStrFormatter
# x_major_locator = MultipleLocator(1)
# x_major_Formatter = FormatStrFormatter('%1.0f')
# x_minor_Locator = MultipleLocator(0.2)
# y_major_locator = MultipleLocator(0.2)
# y_major_Formatter = FormatStrFormatter('%1.1f')
# y_minor_Locator = MultipleLocator(0.05)
# ax = plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# ax.xaxis.set_major_formatter(x_major_Formatter)
# ax.yaxis.set_major_locator(y_major_locator)
# ax.yaxis.set_major_formatter(y_major_Formatter)
# ax.xaxis.set_minor_locator(x_minor_Locator)
# ax.yaxis.set_minor_locator(y_minor_Locator)
# ax.xaxis.grid(True, ls='--', which='minor')
# ax.yaxis.grid(True, ls='--', which='minor')
# plt.legend()
# plt.show()
# x = [i*0.2 for i in range(0, len(speed_list_x))]
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# x_max_speed = max([abs(a) for a in speed_list_x])
# y_max_speed = max([abs(b) for b in speed_list_y])
# plt.figure(figsize=(10, 5))
# plt.grid(ls='--')
# plt.plot(x, speed_list_x, color='red', label='x max:' + str(x_max_speed))
# plt.plot(x, speed_list_y, color='black', label='y max:' + str(y_max_speed))
# plt.title(robotid + ' robot move speed')
# plt.xlabel('time(s)')
# plt.ylabel('speed(m/s)')

# x_major_locator = MultipleLocator(1)
# x_major_Formatter = FormatStrFormatter('%1.0f')
# x_minor_Locator = MultipleLocator(0.2)
# y_major_locator = MultipleLocator(0.2)
# y_major_Formatter = FormatStrFormatter('%1.1f')
# y_minor_Locator = MultipleLocator(0.05)
# ax = plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# ax.xaxis.set_major_formatter(x_major_Formatter)
# ax.yaxis.set_major_locator(y_major_locator)
# ax.yaxis.set_major_formatter(y_major_Formatter)
# ax.xaxis.set_minor_locator(x_minor_Locator)
# ax.yaxis.set_minor_locator(y_minor_Locator)
# ax.xaxis.grid(True, ls='--', which='minor')
# ax.yaxis.grid(True, ls='--', which='minor')
# plt.legend()
# # plt.show()
# plt.savefig("move_speed.png")
# import base64
# file = open(u'move_speed.png', 'rb')
# result = file.read()
# imdata = base64.b64encode(result)
# from django.http import HttpResponse
# return HttpResponse(imdata, content_type='image/png')
# mpl.rcParams['font.sans-serif'] = ['SimHei']

# names = ['5', '10', '15', '20', '25']
# x = range(len(names))
# y = [0.855, 0.84, 0.835, 0.815, 0.81]
# y1=[0.86,0.85,0.853,0.849,0.83]
# #plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# pl.xlim(-1, 11) # 限定横轴的范围
# pl.ylim(-1, 110) # 限定纵轴的范围
# plt.plot(x, y, marker='o', mec='r', mfc='w')
# plt.plot(x, y1, marker='*', ms=10)
# plt.legend() # 让图例生效
# plt.xticks(x, names, rotation=45)
# plt.margins(0)
# plt.subplots_adjust(bottom=0.15)

# plt.xlabel(u"time(s)") #X轴标签
# plt.ylabel("speed(m/s)") #Y轴标签
# plt.title("robot speed") #标题

# plt.show()


# marker_robot = KuboOrder("172.21.20.6","9092","STANDARD0")
# # marker_robot.robot_internal_inspect('160',0)
# marker_robot = KuboOrder("172.21.20.6","9092","STANDARD0")
# marker_robot.robot_init("160")
# time.sleep(1)
# CUSTOM0-SIZE0.60x0.40x0.28
# marker_robot.robot_internal_fork('160',0,0)
# marker_robot.robot_internal_tray('160',0,1)
# time.sleep(1)
# marker_robot = KuboOrder("172.21.20.6","9092","STANDARD0")
# marker_robot = KuboOrder("172.21.20.6","9092","STANDARD0")
# # marker_robot.robot_init("129")
# #CUSTOM0-SIZE0.60x0.40x0.28
# # marker_robot.robot_internal_fork('159',0,1)
# for i in range(100):
#     marker_robot.robot_external("159","TAKE",10,{'x':62.89,'y':42.91,'theta':-1.57},1530,0)
#     time.sleep(1)
#     marker_robot.robot_external("159","PUT",10,{'x':62.89,'y':42.91,'theta':-1.57},1530,0)
# marker_robot.robot_move('160',{'x':-0.25,'y':-6.7,'theta':0},1,625,0)


# #旋转点
# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':-1.57},1,400,0)
# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,400,0)
# marker_robot.robot_move('160',{'x':37.89 ,'y':50.85,'theta':-1.57},1,400,0)
#
# marker_robot.robot_move('160',{'x':48.86,'y':45.13,'theta':-1.57},1,400,0)
# marker_robot.robot_move('160',{'x':40.38,'y':48.94,'theta':3.14},1,400,0)
# for i in range(0,5):     
# marker_robot.robot_external("160","TAKE",0,{'x':40.38,'y':48.94,'theta':1.57},1420,0)
# marker_robot.robot_external("160","PUT",0,{'x':40.38,'y':48.94,'theta':1.57},1420,0)
# marker_robot.robot_move('160',{'x':38.79, 'y':48.94,'theta':3.14},1,400,0)
# marker_robot.robot_external_inspect('160',{'x':38.79, 'y':48.94,'theta':-1.57},1420,0)
# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':-1.57},1,400,0)
# marker_robot.robot_external("160","TAKE",10,{'x':37.88,'y':48.94,'theta':-1.57},1420,10)
# time.sleep(1)
# marker_robot.robot_external("160","PUT",10,{'x':38.79,'y':48.94,'theta':-1.57},1420,0)

# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,400,0)

# marker_robot.robot_external("160","TAKE",0,{'x':37.88,'y':47.98,'theta':3.14},400,0)
# marker_robot.robot_external("160","PUT",0,{'x':40.38,'y':48.94,'theta':-1.57},1420,0)
# marker_robot.robot_internal_inspect('160',1)
# marker_robot.robot_external_inspect("160",{'x':40.38,'y':48.94,'theta':1.57},1400,0)
# marker_robot.robot_external_inspect("160",{'x':38.79,'y':48.94,'theta':-1.57},1420,0)

# marker_robot.robot_move('160',{'x':116.70,'y':-216.20,'theta':1.57},1,400,0)
# marker_robot.robot_move('160',{'x':116.70,'y':-216.70,'theta':1.57},1,400,0)

# marker_robot.robot_move('160',{'x':-116.20,'y':216.70,'theta':0},1,400,0) 
# marker_robot.robot_move('160',{'x':-116.70,'y':216.70,'theta':0},1,400,0)

# marker_robot.robot_move('160',{'x':0.25,'y':216.70,'theta':0},1,400,0)
# marker_robot.robot_move('160',{'x':-116.70,'y':216.70,'theta':0},1,400,0)

# marker_robot.robot_move('160',{'x':0.25,'y':-6.70,'theta':3.14},1,400,0)
# marker_robot.robot_move('160',{'x':2.25,'y':6.70,'theta':0},1,400,0)


# 充电点
# marker_robot.robot_move('160',{'x':37.88,'y':47.98,'theta':-1.57},1,400,0)
# #巷道取放货
# marker_robot.robot_move('160',{'x':48.85,'y':48.94,'theta':3.14},1,400,0)
# marker_robot.robot_move('160',{'x':48.85,'y':53.67,'theta':-1.57},1,400,0)

# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,400,0)

# marker_robot.robot_external("160","PUT",0,{'x':48.85,'y':45.13,'theta':3.14},1425,0)
# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,1425,0)

# marker_robot = KuboOrder("172.18,81.62","9092","STANDARD0") 
# marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,625,1.5801)
# def task():
#     marker_robot = KuboOrder("172.23.200.160","9092","STANDARD0") 
#     # marker_robot.robot_init("160")
#     # yield
#     print("start")
#     # marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':-1.57},1,625,1.57)
#     # yield
#     # marker_robot.robot_move('160',{'x':37.88,'y':48.94,'theta':3.14},1,625,1.57)
#     # yield
#     # marker_robot.robot_move('160',{'x':84.23,'y':48.23,'theta':3.14},1,625,1.57)
#     # # yield
#     # marker_robot.robot_move('160',{'x':93.15,'y':48.23,'theta':3.14},1,625,1.57)
#     # yield

#     # marker_robot.robot_move('160',{'x':40.38,'y':48.94,'theta':3.14},1,1425,0)
#     # yield
#     marker_robot.robot_external("160","PUT",0,{'x':40.38,'y':48.94,'theta':1.57},1425,0)
#     yield
#     # marker_robot.robot_setup('160','system::action','recovery')
#     # yield
#     # 行走到取货点
#     # marker_robot.robot_internal_inspect('160',1)
#     # yield
# marker_robot.robot_external_inspect("159",{'x':40.38,'y':48.94,'theta':-1.57},1425.0,0)
#     # yield
#     # marker_robot.robot_resume('160')
#     # yield
#     # marker_robot.robot_move('160',{'x':61.82,'y':87.18,'theta':0},1,800,0)
#     # yield
#     # #输送线取货
#     # marker_robot.robot_external("160","TAKE",0,{'x':40.38,'y':48.94,'theta':1.57},1425.0,0)
#     # yield
#     # marker_robot.robot_external("160","PUT",0,{'x':40.38,'y':48.94,'theta':1.57},1425.0,0)
#     # yield
#     # marker_robot.robot_pause('160','STOP_ACTION')
#     # yield
#     # marker_robot.robot_internal_tray('160',0,0)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,1)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,2)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,3)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,4)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,5)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,6)
#     # yield
#     # time.sleep(2)
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # marker_robot.robot_internal_tray('160',0,7)
#     # yield
#     # #最后一个料箱放在货叉内
#     # marker_robot.robot_external('160',"TAKE",0,{'x':61.82,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # #行走至放货点
#     # marker_robot.robot_move('160',{'x':63.62,'y':87.18,'theta':0},1,800,0)
#     # yield
#     # # # 将货叉内箱子放到输送线
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(5)
#     # #遍历箱子内部取货并放到输送线
#     # marker_robot.robot_internal_fork('160',0,7)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,6)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,5)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,4)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,3)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,2)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,1)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield
#     # time.sleep(3)
#     # marker_robot.robot_internal_fork('160',0,0)
#     # yield
#     # marker_robot.robot_external('160',"PUT",0,{'x':63.62,'y':87.18,'theta':-1.57},800.0,10)
#     # yield

# consumer = KafkaConsumer('ss', bootstrap_servers=['172.23.200.160:9092'])

# flag = 1
# print('please start all node！！！')
# # while True:
#     # f = open('take_put_loop_80.txt','a')
#     # f.write(str(flag)+"th test!!!!!\n")
# for num in range(1):
#     print(str(flag)+"th test")
#     t1 = task()
#     next(t1)
#     # f.close()
#     for msg in consumer:
#         if msg:
#             value = msg.value.decode(encoding='UTF-8',errors='strict')   #解码就是str了
#             # print(type(value))
#             recv = json.loads(value) #转成字典
#             if recv['robotId'] == '160':
#                 print(recv)
#                 if recv['executionResult'] == 0:
#                     # print(recv['binId'])
#                     try:
#                         next(t1)
#                     except:
#                         flag+=1
#                         break
#                 else:
#                     print("have error")
#                     # f = open('take_put_loop_80.txt','a')
#                     # f.write(str(recv)+"have error\n")
#                     # f.close()
#                     break
#             else:
#                 continue
