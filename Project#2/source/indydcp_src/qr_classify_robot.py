from indy_utils import indydcp_client as client
from indy_utils.indy_program_maker import JsonProgramComponent

import json
import threading
from time import sleep
import numpy as np

import pyzbar.pyzbar as pyzbar
import cv2

import subprocess
import sys

robot_ip = "192.168.0.6"    # Robot (Indy) IP
robot_name = "NRMK-Indy10"  # Robot name (Indy7)indy

# Create class object
indy = client.IndyDCPClient(robot_ip, robot_name)

# 기계를 연결해준다.
indy.connect()

# 기계 세팅을 해준다.
indy.set_collision_level(5)
indy.set_joint_vel_level(4)
indy.set_task_vel_level(4)
indy.set_joint_blend_radius(20)
indy.set_task_blend_radius(0.2)

# 기계 세팅을 확인한다.
print(indy.get_collision_level())
print(indy.get_joint_vel_level())
print(indy.get_task_vel_level())
print(indy.get_joint_blend_radius())
print(indy.get_task_blend_radius())

# 관절 공간에서의 각도(j_pos)와 작업 공간에서의 위치 및 방향(t_pos)을 선언한다.
j_pos = indy.get_joint_pos()
t_pos = indy.get_task_pos()

# j_pos와 t_pos를 출력한다.
print(j_pos)
print(t_pos)

# 기계의 상태를 key에 저장한다.
key = []
status = indy.get_robot_status()
for value in status.keys():
    key.append(value)

# 기계의 상태가 저장된 key를 출력한다.
print(key)
print(type(status))

# 프로그램 실행 시 먼저 home 위치로 가게 한다.
indy.go_home()

# 기계가 동작한 후에는 꼭 이 구문을 넣어준다.
while True:
    status = indy.get_robot_status()
    sleep(0.2)
    if status[key[5]]==1 :
        break
print('done : go home process')

power_on = 1   # 기계의 작동이 필요한 경우: 1, 기계의 작동이 필요없는 경우: 0

while(1):
    
    # QR data를 'qr_code_reader.py'파일에서 읽어온다.
    out = subprocess.check_output(['python', 'qr_code_reader.py'] )
    location = out.decode('utf-8')          # 읽어온 데이터를 해독한 뒤에 location에 저장한다.
    location = location[:len(location)-2]   # 마지막 2개를 제외한 데이터를 최종적으로 location에 저장한다.
  
    # location에 저장된 값을 출력한다.
    print('Data : ', location, '\n')

    # location에 저장된 값에 따라 해당되는 위치의 좌표를 반환한다.
    if location == "Creation hall":
        locate_pos1 = [ 0.37860,  -0.53128,  0.70879,   169.93,   7.69,   71.93]         # 1번 위치 (위) 
        locate_pos2 = [ 0.39087,  -0.54838,  0.63746,   175.45,   3.60,   72.48]         # 1번 위치 (아래)
    elif location == "Newton hall":
        locate_pos1 = [ 0.25786,  -0.51737,  0.71442,   170.46,  13.09,   72.51]         # 2번 위치 (위)
        locate_pos2 = [ 0.26991,  -0.54060,  0.64523,   175.37,   8.12,   73.43]         # 2번 위치 (아래)
    elif location == "Rodem hall":
        locate_pos1 = [ 0.16076,  -0.49830,  0.73360,   170.77,  23.20,   71.19]         # 3번 위치 (위)
        locate_pos2 = [ 0.17026,  -0.52394,  0.64216,   178.11,  14.25,   73.32]         # 3번 위치 (아래)
    elif location == "Grace hall":
        locate_pos1 = [ 0.05757,  -0.54360,  0.72850,  -178.98,  14.83,   71.69]         # 4번 위치 (위)
        locate_pos2 = [ 0.06028,  -0.56183,  0.64116,  -176.20,   9.61,   72.75]         # 4번 위치 (아래)
    elif location == "Oseok hall":
        locate_pos1 = [-0.05459,  -0.57265,  0.71999,  -172.90,  10.95,   73.03]         # 5번 위치 (위)
        locate_pos2 = [-0.05496,  -0.59075,  0.63478,  -170.88,   3.16,   73.49]         # 5번 위치 (아래)
    elif location == "Hyundong hall":
        locate_pos1 = [-0.15900,  -0.57540,  0.73355,  -170.59,  12.66,   72.96]         # 6번 위치 (위)
        locate_pos2 = [-0.17164,  -0.59050,  0.63448,  -169.83,   5.84,   72.95]         # 6번 위치 (아래)
    elif location == 'quit':
        power_on = 0                                                                     # 기계 종료 Flag

    if power_on == 1:
        # 1단계: 우편이 놓여진 고정된 위치로 간다.
        t_pos = [0.51681, -0.14784, 0.50296, 179.93, 16.92, 163.91]             # 고정된 위치 (위)
        indy.task_move_to(t_pos) # move to 절대좌표, move by 상대좌표

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move1 process')
        
        # 2단계: z축 방향으로 내려가서 우편을 집을 준비를 마친다.
        t_pos = [0.55074, -0.15743, 0.39992, 179.95, 6.32, 163.92]             # 고정된 위치 (아래)
        indy.task_move_to(t_pos)

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move2 process')

        # 3단계: Vaccum head를 통해 우편을 집는다.
        indy.set_do(10, 1)
        indy.set_do(11, 0)       
               
        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move3 process')
        
        # 4단계: 우편을 집은 뒤에 home 위치로 간다.
        indy.go_home()      
        
        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move4(go home) process')

        # 5단계: location에 해당되는 위치로 간다.
        t_pos = locate_pos1
        indy.task_move_to(t_pos)

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move5 process')        

        # 6단계: z축 방향으로 내려가서 우편을 놓을 준비를 마친다.
        t_pos = locate_pos2
        indy.task_move_to(t_pos)

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move6 process')

        # 7단계: Vaccum head를 통해 우편을 놓는다.
        indy.set_do(10, 0)
        indy.set_do(11, 1)
        
        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move7 process')

        # 8단계: 우편을 놓은 뒤 Vaccum head를 올린다.
        t_pos = locate_pos1
        indy.task_move_to(t_pos)

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move8 process')  

        # 9단계: home 위치로 돌아가서 대기한다.
        indy.go_home()

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : move9(go home) process')

    if power_on == 0:
        # 추가적인 기계 작동이 없는 것으로 판단하고 zero 위치로 돌아간다.
        indy.go_zero()

        while True:
            status = indy.get_robot_status()
            sleep(0.2)
            if status[key[5]]==1 :
                break
        print('done : zero process')

        # 기계 연결을 해제한다.
        indy.disconnect()

        # 프로그램을 종료한다.
        sys.exit()