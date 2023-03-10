import redis
from typing import Dict, List
import json
import time
from kafka import KafkaProducer
from kafka import KafkaConsumer, TopicPartition


class KuboInfo(object):
    """
    get robot info class,example:
    class test_class(KuboInfo):
        def test_fun(self,robot_id):
            print(self.batteryInfo(robot_id))
    re = test_class("172.23.101.28")
    re.test_fun()
    """

    def __init__(self, host_ip: str):
        """
        1 required argument,the redis host ip,redis port is 6379,if the port is not 6379,you should rewrite parent class init and gave a value to port,example:
        def __init__(self,host_ip:str,port:int):
            host_ip = host_ip
            port = port
            self.r = redis.StrictRedis(host=host_ip, port=port, db=0)
        """
        host_ip = host_ip
        port = 6379
        self.r = redis.StrictRedis(host=host_ip, port=port, db=0)

    def get_info(self, robot_id: str) -> Dict:
        """
        get the robot info for gaved id 
        """
        robot_id = "kubot_" + robot_id
        robot_data = self.r.get(robot_id)
        print(type(robot_data))
        robot_json = json.loads(robot_data)
        return robot_json

    def batteryInfo(self, robot_id: str) -> Dict:
        """
        return the robot batteryinfo,dict contain powerlevel,state and voltage,powerlevel A number in [0, 100], 0 for no power, 100 for full.state NORMAL = 0,CHARGING = 1
        voltage in mV. Voltage of the battery,example:{'powerLevel': 61, 'state': 0, 'voltage': 48681.00390625}
        """
        robot_json = self.get_info(robot_id)
        return robot_json["batteryInfo"]

    def errorState(self, robot_id: str) -> List:
        """
        return the robot errorstate,if have many error,this list have many value,example:[{'info': 'No image data!', 'node': 'fork_camera2', 'type': 2147484416}]
        """
        robot_json = self.get_info(robot_id)
        return robot_json["errorState"]

    def forkFinger(self, robot_id: str) -> List[Dict]:
        """
        return the robot forkfinger info,contain the right finger and the left finger,status -1: open, 1: close,example:[{'id': 0, 'status': -1.0}, {'id': 1, 'status': -1.0}]
        """
        robot_json = self.get_info(robot_id)
        return robot_json["forkFinger"]

    def forkRotate(self, robot_id: str) -> Dict:
        """
        return the robot forkrotate info,contain position and speed,the position is double in [-1.7,1.7],speed is double,unit is mm/s,example:{'position': 0.0, 'speed': 0.0}
        """
        robot_json = self.get_info(robot_id)
        return robot_json["forkRotate"]

    def forkStretch(self, robot_id: str) -> Dict:
        """
        return the robot forkstretch info,contain position and speed,the position is double in mm,Stretched distance of the fork,speed is double in mm/s,example:
        {'position': -0.0, 'speed': -0.0}
        """
        robot_json = self.get_info(robot_id)
        return robot_json["forkStretch"]

    def lastUpdate(self, robot_id: str) -> str:
        """
        return the time for lastest recv data,example:2020-11-16 19:47:56
        """
        robot_json = self.get_info(robot_id)
        lasttime = robot_json["lastUpdate"]
        timeArray = time.localtime(float(lasttime / 1000))
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return datetime

    def lift(self, robot_id: str) -> Dict:
        """
        return the lift info,contain height and speed,Height of the fork,height is double in mm,speed is double in mm/s,example:{'height': -0.0, 'speed': -0.0}
        """
        robot_json = self.get_info(robot_id)
        return robot_json["lift"]

    def mapPosition(self, robot_id: str) -> Dict:
        """
        return the robot_id Current position info,Dict contain x,y and theta,example:{'theta': 0.0, 'x': 0.0, 'y': 0.0}
        """
        robot_json = self.get_info(robot_id)
        return robot_json["mapPosition"]

    def obstacles(self, robot_id: str) -> List:
        """
        return the robot_id obstacles info,the area is direction,1 is rear,0 is front,the distance is distance of robot and obstacle,example:[{'area': 1, 'distance': 800.0}]
        """
        robot_json = self.get_info(robot_id)
        return self.robot_json["obstacles"]

    def robotState(self, robot_id: str) -> int:
        """
        return the robot_id state,
        ROBOT_READY_TO_INIT = 0,
        ROBOT_IDLE = 1,
        ROBOT_RUNNING = 2,
        ROBOT_ABNORMAL = 3,
        ROBOT_RECOVERY = 4,
        ROBOT_PAUSED = 5,

        """
        robot_json = self.get_info(robot_id)
        return robot_json["robotState"]

    def seqNum(self, robot_id: str) -> int:
        """
        the last order seqnum
        """
        robot_json = self.get_info(robot_id)
        return robot_json["seqNum"]

    def trays(self, robot_id: str) -> List:
        """
        the robot_id trays info,contain id,type,state,binID,the type: FORK = 0,TRAY = 1,state:FULL = 0,EMPTY = 1,ERROR = 2

        """
        robot_json = self.get_info(robot_id)
        return robot_json["trays"]

    def motionSpeed(self, robot_id: str) -> Dict:
        """
        the robot_id Current speed info
        """
        robot_json = self.get_info(robot_id)
        return robot_json["motionSpeed"]


class KuboOrder(object):

    def __init__(self, host_ip: str, port: str, binmodel: str):
        """
        bintype:DM_MARKED=0,MARKERLESS=10
        binmodel:STANDARD0 or CUSTOM0-SIZE0.3x0.3x0.3
        """
        self.binmodel = binmodel
        self.host_ip = host_ip
        self.port = port
        self.bootstrap_servers = self.host_ip + ":" + self.port
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def robot_init(self, robot_id: str):
        """
        robot boot the state is 0 ,init robot,the state will  become 2 ,example:
        markerless_robot = KuboOrder("172.23.101.100","9092","STANDARD")
        markerless_robot.robot_init("39")
        """
        msg_dict = {
            "msgType": 0,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def get_info(self, robot_id: str) -> Dict:
        """
        get the robot info for gaved id
        """
        host_ip = self.host_ip
        port = 6379
        self.r = redis.StrictRedis(host=host_ip, port=port, db=0)
        robot_id = "kubot_" + str(robot_id)
        robot_data = self.r.get(robot_id)
        robot_json = json.loads(robot_data)
        return robot_json

    def robot_move(self, robot_id: str, tag_position: dict, zonetype: int, lift_position: float, fork_position: float):
        """
        control the robot move to targetposition,and same time the lift and fork move to the limit position,example:
        zonetype:
        MAIN_PATH = 0, // 主干道
        RACK_STORAGE = 1, // 巷道区
        OPERATING_STATION = 2, // 工作站
        CHARGING_STATION = 3, // 充电站
        101//交汇道，通过会有语音提醒
        102--110//自定义
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        markerless_robot.robotmove('39',{'x':28.49,'y':31.78,'theta':0},1,1500,0)
        """
        msg_dict = {
            "msgType": 1,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "targetPosition": tag_position,
            "spaceSituation": {"zoneType": zonetype},
            # 移动过程中
            #    "limits" :{
            #        "liftPositionMax" : lift_position, # in mm.
            #        "liftPositionMin" : lift_position,  # in mm
            #        "forkRotationPositionMax": fork_position,  # in radian. [-1.7, 1.7]
            #        "forkRotationPositionMin": fork_position#in radian. [-1.7, 1.7]
            #     #    "fingerPosition": finger_position                    
            #        }
            # 前置条件
            "preconditions": {
                "liftPositionMax": lift_position,  # in mm.
                "liftPositionMin": lift_position,  # in mm
                "forkRotationPositionMax": fork_position,  # in radian. [-1.7, 1.7]
                "forkRotationPositionMin": fork_position  # in radian. [-1.7, 1.7]
                #    "fingerPosition": finger_position                    
            }
            # 前置条件
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_move_chassis(self, robot_id: str, tag_position: dict, zonetype: int):
        """
        control the robot move to targetposition,the lift and fork not move,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        markerless_robot.robot_move_chassis('39',{'x':28.49,'y':31.78,'theta':0},0)
        """
        msg_dict = {
            "msgType": 1,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "targetPosition": tag_position,
            "spaceSituation": {"zoneType": zonetype}
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_move_lift(self, robot_id: str, tag_position: dict, zonetype: int, lift_position: float,
                        fork_position: float):
        """
        control the robot move to targetposition,first move the lift and fork ,then move robot,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        markerless_robot.robot_move_lift('39',{'x':28.49,'y':31.78,'theta':0},1,1500,0)
        
        """
        msg_dict = {
            "msgType": 1,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "targetPosition": tag_position,
            "spaceSituation": {"zoneType": zonetype},
            "preconditions": {
                "liftPositionMax": lift_position,
                "liftPositionMin": lift_position,
                "forkRotationPositionMax": fork_position,
                "forkRotationPositionMin": fork_position
            }
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_external(self, robot_id: str, op_type: str, bintype: int, tag_position: dict, tag_height: float,
                       locationtype: int, **kw):
        """
        control robot PUT or TAKE goods from external,targetHeight is goods hight,binType is robot type(DM_MARKED=0,MARKERLESS=10),
        binModel is box type(STANDARD or CUSTOM0-SIZE0.3x0.3x0.3),localtionType is shelf type(STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10),
        example:
        markerless_robot = KuboOrder("172.23.101.100","9092","STANDARD")
        markerless_robot.robot_external("39","PUT",0,{'x':28.49,'y':31.78,'theta':-1.53},1200.0,0,locationSize=1)
        """
        if op_type == "PUT":
            optype = 0
        elif op_type == "TAKE":
            optype = 2
        else:
            print("the op_type must is 'PUT' or 'TAKE'")
        if "locationsize" in kw.keys():
            msg_dict = {
                "msgType": 2,
                "seqNum": int(time.time() * 1000),
                "robotId": robot_id,
                "opType": optype,  # Of type BinOpType,PUT=0 or TAKE=2
                "binId": "external " + op_type + " goods",  # any string
                "targetPosition": tag_position,
                "targetHeight": tag_height,  # goods height
                "binType": bintype,  # robot type,DM_MARKED=0,MARKERLESS=10
                "binModel": self.binmodel,
                # goods STANDARD<model number> or CUSTOM<model number>-SIZE<length>x<width>x<height>
                "locationType": locationtype,  # STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
                "locationSize": kw["locationsize"]
            }
        else:
            msg_dict = {
                "msgType": 2,
                "seqNum": int(time.time() * 1000),
                "robotId": robot_id,
                "opType": optype,  # Of type BinOpType,PUT=0 or TAKE=2
                "binId": "external " + op_type + " goods",  # any string
                "targetPosition": tag_position,
                "targetHeight": tag_height,  # goods height
                "binType": bintype,  # robot type,DM_MARKED=0,MARKERLESS=10
                "binModel": self.binmodel,
                # goods STANDARD<model number> or CUSTOM<model number>-SIZE<length>x<width>x<height>
                "locationType": locationtype  # STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
            }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_external_kiva(self, robot_id: str, op_type: str, en_position: dict, tag_position: dict, tag_height: float,
                            bintype: int, locationtype: int):
        if op_type == "PUT":
            optype = 0
            x = "entrancePosition"
            y = [{"step": "ENTER_LOCATION", "when": "after",
                  "type": "REPORT_ONLY"}]  # 放货指令，机器人离开entrancePostion到达库位点后，上报状态并继续执行

        elif op_type == "TAKE":
            optype = 2
            x = "exportPosition"
            y = [{"step": "LEAVE_LOCATION", "when": "before",
                  "type": "REPORT_AND_PAUSE"}]  # 取货指令，机器人顶升货物后，离开库位点进入exportPostion之前，暂停执行并上报状态
        else:
            print("the op_type must is 'PUT' or 'TAKE'")
        msg_dict = {
            "msgType": 2,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": optype,  # Of type BinOpType,PUT=0 or TAKE=2
            "binId": "external " + op_type + " goods",  # any string
            "targetPosition": tag_position,
            x: en_position,
            "targetHeight": tag_height,  # goods height
            "binType": bintype,  # robot type,DM_MARKED=0,MARKERLESS=10
            "binModel": self.binmodel,
            # goods STANDARD<model number> or CUSTOM<model number>-SIZE<length>x<width>x<height>
            "locationType": locationtype,  # STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
            "stepControl": y
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_external_inspect(self, robot_id: str, tag_position: dict, tag_height: float, locationtype: int):  # 检查库位料箱
        """
        locationtype:STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
        inspect the box on shelf,robot return from kafka,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD")
        markerless_robot.robot_external("39",{'x':28.49,'y':31.78,'theta':-1.53},1200.0)
        """
        msg_dict = {
            "msgType": 2,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": 4,  # Of type BinOpType,INSPECT=4
            "targetPosition": tag_position,
            "targetHeight": tag_height,  # goods height
            "locationType": locationtype  # STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_internal_fork(self, robot_id: str, bintype: int, tray_id: int):  # 内部从托盘转移货物到fork
        """
        internal transfer goods from tray to fork,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        markerless_robot.robot_internal_fork("39",1)
        """
        msg_dict = {
            "msgType": 3,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": 3,
            "binId": "internal transfer goods from " + str(tray_id) + "tray to fork",  # any string
            "binType": bintype,  # robot type,DM_MARKED=0,MARKERLESS=10
            "binModel": self.binmodel,
            # goods STANDARD<model number> or CUSTOM<model number>-SIZE<length>x<width>x<height>
            "srcTray": {
                "id": tray_id,  # 托盘id，第一个为0，第二个为1
                "type": 1
            },
            "dstTray": {
                "id": 0,
                "type": 0  # Of type TrayType.
            }
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_internal_tray(self, robot_id: str, bintype, tray_id: int):  # 内部从货叉转移货物到托盘
        """
        internal transfer goods from fork to tray,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        markerless_robot.robot_internal_tray("39",1)
        """
        msg_dict = {
            "msgType": 3,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": 3,
            "binId": "internal transfer goods from fork to " + str(tray_id) + "tray",
            "binType": bintype,  # robot type,DM_MARKED=0,MARKERLESS=10
            "binModel": self.binmodel,
            # goods STANDARD<model number> or CUSTOM<model number>-SIZE<length>x<width>x<height>
            "srcTray": {
                "id": 0,
                "type": 0
            },
            "dstTray": {
                "id": tray_id,  # 背篓id，第一个为0，第二个为1
                "type": 1
            }
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_internal_inspect(self, robot_id: str, tray_id: int):  # 内部托盘货物检查
        """
        internal inspect,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        markerless_robot.robot_internal_inspect("39",2)
        """
        msg_dict = {
            "msgType": 3,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": 4,
            "targetTray": {
                "id": tray_id,  # tray id
                "type": 1
            }
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_pause(self, robot_id: str, stoptype: str):  # pause robot
        """
        pause robot,STOP_ACTION=1 or STOP_COMMAND=0,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD0",0)
        markerless_robot.robot_pause("39","STOP_ACTION")
        """
        if stoptype == "STOP_COMMAND":
            stoptype_int = 0
        else:
            stoptype_int = 1
        msg_dict = {
            "msgType": 4,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "stopType": stoptype_int  # STOP_ACTION=1 or STOP_COMMAND=0
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    # def robot_resume(self,robot_id:str):#resume robot
    #     """
    #     resume robot,example:
    #     markerless_robot = KuboOrder("172.23.101.100","9092","STANDARD0")
    #     markerless_robot.robot_resume("39")
    #     """
    #     msg_dict = {
    #         "msgType" : 5, 
    #         "seqNum" : int(time.time()*1000),
    #         "robotId": robot_id,
    #         "stepControl":[
    #             {"seqNum" : 1669694069229,"step": "LEAVE_LOCATION","when": "before","type": "REPORT_AND_PAUSE"}
    #         ]

    #         }
    #     msg = json.dumps(msg_dict).encode()
    #     self.producer.send('ll', msg)

    def robot_resume(self, robot_id: str):  # resume robot
        """
        resume robot,example:
        markerless_robot = KuboOrder("172.23.101.100","9092","STANDARD0")
        markerless_robot.robot_resume("39")
        """
        msg_dict = {
            "msgType": 5,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_resurt(self, robot_id: str):
        """
        return last command executionresult
        """
        topic = "ss"
        consumer = KafkaConsumer(bootstrap_servers=[self.bootstrap_servers])
        ps = [TopicPartition(topic, p) for p in consumer.partitions_for_topic(topic)]
        consumer.assign(ps)
        for p in ps:
            last_offset = consumer.position(p)

        while last_offset > 0:
            consumer.seek(p, offset=last_offset - 1)
            for msg in consumer:
                lastmsg = json.loads(msg.value)
                break
            if lastmsg["robotId"] == robot_id:
                break
            else:
                last_offset = last_offset - 1

        return (lastmsg)

    def robot_setup(self, robot_id: str, node: str, value: list):
        """
        setup robot
        node: system::action,map::mapping
        value:
        restart---reboot robot
        recovery--recovery robot
        mapping--[{"code" : "1029233562","mapping" : {"x":29.23,"y":35.62}}]
        """
        msg_dict = {
            "msgType": 6,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "settings": [
                {"node": node,
                 "value": value}
            ]
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_external_inventory(self, robot_id: str, tag_position: dict, tag_height: float, locationtype: int,
                                 inspectType: str):  # 检查库位料箱
        """
        locationtype:STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
        inspect the box on shelf,robot return from kafka,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD")
        markerless_robot.robot_external_inventory("39",{'x':28.49,'y':31.78,'theta':-1.53},1200.0,1)
        """
        msg_dict = {
            "msgType": 2,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": 4,  # Of type BinOpType,INSPECT=4
            "targetPosition": tag_position,
            "targetHeight": tag_height,  # goods height
            "locationType": locationtype,  # STORAGE_SHELF=0,STORAGE_SHELF_DEEP1 = 1 or  CONVEYOR = 10
            "inspectType": inspectType
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)

    def robot_internal_inventory(self, robot_id: str, tray_id: int, inspectType: str):  # 内部托盘货物检查
        """
        internal inspect,example:
        markerless_robot = KuboOrder("172.23.101.100","9092",10,"STANDARD",0)
        inspect ####markerless_robot.robot_internal_inventory("39",2,0)
        inventory ####markerless_robot.robot_internal_inventory("39",2,1)
        """
        msg_dict = {
            "msgType": 3,
            "seqNum": int(time.time() * 1000),
            "robotId": robot_id,
            "opType": 4,
            "targetTray": {
                "id": tray_id,  # tray id
                "type": 1
            },
            "inspectType": inspectType
        }
        msg = json.dumps(msg_dict).encode()
        self.producer.send('ll', msg)
