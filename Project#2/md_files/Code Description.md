# Code Description

Project#2 - 우편 분류 공정(Using QR Code)에 사용한 Main Code Algorithm은 다음과 같다.

<br/>
<p align="center">
      <img src="https://user-images.githubusercontent.com/84503980/173984351-4c86ff43-055b-493a-850d-456d8d736d36.png" width="100%" height="100%" alt="text" width="number" />
      </p>

<br/><br/>

## 1. 카메라를 통해 우편의 QR 코드를 인식 후 데이터를 해독하여 Main File인 qr_classify_robot.py로 보낸다.

   코드 구성은 다음과 같다.

   1. 해당 파일에 필요한 라이브러리를 불러온다.

   ```python
   import pyzbar.pyzbar as pyzbar
   import cv2
   ```

   2. 카메라에서 영상을 가져온다. (Window)

   ```python
   cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Window
   #cap = cv2.VideoCapture(0)                # Linux
   ```

   3. location을 선언해주며, 초기값은 '0'으로 설정한다.

   ```python
   location = str(0)   # Declare location
   ```

   4. while() 함수를 통해 카메라가 작동하는 동안 반복문이 실행되도록 하며, 카메라가 매 프레임을 읽도록 한다.

   ```python
   while(cap.isOpened()):
     ret, img = cap.read()	# Read image(frame) 
   
     if not ret:
       continue
   ```

   5. 읽어온 이미지를 gray scale로 변환시킨 뒤에 이미지 안에서 QR 코드를 찾아 해독한다.

   ```python
     # Convert image to gray scale
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
     # Decode QR code in image
     decoded = pyzbar.decode(gray)
   ```

   6. 검출한 QR 코드의 영역 및 타입을 추출하고, QR 코드의 데이터를 문자열로 해독한다. 또한, 해독한 데이터를 location에 저장한다.

   ```python
     for d in decoded:
       # Extract the area of the QR code.
       x, y, w, h = d.rect
   
       # Read decoded data & type
       barcode_data = d.data.decode("utf-8")
       barcode_type = d.type
       # Store decoded QR data to location
       location = barcode_data
   ```

   7. 이미지 내 QR 코드 영역에 사각형 테두리를 그린 뒤, text에 QR 코드의 타입 및 데이터를 저장하여 이미지에 포함시킨다.

   ```python
   	# Draw rectangular at the area of the QR code  
       cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
   
       # Store QR data & type in the text, and put in image
       text = '%s (%s)' % (barcode_data, barcode_type)
       cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
   ```

   8. 카메라로 읽고 있는 이미지를 'img' 윈도우로 보여준다.

   ```python
     # Show image in 'img' window
     cv2.imshow('img', img)
   ```

   9. location에 QR data가 저장되면 반복문에서 나간다.

   ```python
     # Exit the while loop when QR data is store in the location
     if location != str(0):
         break
   ```

   10. 'q'를 누르면 location에 종료 구문이 저장된 채로 반복문에서 나간다.

   ```python
     # When 'q' is pressed, the ending phrase is stored in the location and leaves the loop.
     key = cv2.waitKey(1)
     if key == ord('q'):
       location = 'quit'
       break
   ```

   11. location에 저장된 QR data를 출력해준 뒤, 설정해놓은 카메라와 윈도우를 해제한다.

   ```python
   # Print the location (Allows the location to be read from qr_classify_robot.py)
   print(location)
   
   # Turn off the set camera and window
   cap.release()
   cv2.destroyAllWindows()
   ```

   

## 2. qr_classify_robot.py [Main File]

   Sub File인 qr_code_reader.py에서 받은 우편의 QR 데이터를 바탕으로 로봇을 작동시켜 해당되는 지점으로 우편을 옮긴다.

   코드 구성은 다음과 같다.

   1. 해당 파일에 필요한 라이브러리를 불러온다. 

   ```python
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
   ```

   2. 로봇의 IP와 name을 입력해 주며, 해당 데이터를 통해 indy라는 클라스를 만들어준다.

   ```python
   robot_ip = "192.168.0.6"  	# Robot IP
   robot_name = "NRMK-Indy10"  # Robot name
   
   indy = client.IndyDCPClient(robot_ip, robot_name)	# Robot Class
   ```

   3. 주어진 IP  환경에서 해당 로봇에 연결시킨다.

   ```python
   indy.connect()	# Robot Connect 
   ```

   4. 로봇의 환경을 설정해준 뒤에 출력해서 확인해본다.

   ```python
   # Robot Setting
   indy.set_collision_level(5)
   indy.set_joint_vel_level(3)
   indy.set_task_vel_level(3)
   indy.set_joint_blend_radius(20)
   indy.set_task_blend_radius(0.2)
   
   # Check Robot Setting
   print(indy.get_collision_level())
   print(indy.get_joint_vel_level())
   print(indy.get_task_vel_level())
   print(indy.get_joint_blend_radius())
   print(indy.get_task_blend_radius())
   ```

   5. 로봇의 관절 공간에서의 각도(j_pos), 작업 공간에서의 위치 및 방향(t_pos)을 선언한 뒤에 출력해서 확인해본다.

   ```python
   # Angle in joint space(j_pos), Location and orientation in the workspace(t_pos)
   j_pos = indy.get_joint_pos()
   t_pos = indy.get_task_pos()
   
   # Check j_pos & t_pos
   print(j_pos)
   print(t_pos)
   ```

   6. 로봇의 상태를 key에 저장한 뒤에 출력해서 확인해본다.

   ```python
   # Store the status of the robot in the key.
   key = []
   status = indy.get_robot_status()
   for value in status.keys():
       key.append(value)
   
   # Check key & type of status
   print(key)
   print(type(status))
   ```

   7. 로봇을 home 위치로 보내 대기 상태로 만든다.

   ```python
   # Home Position
   indy.go_home()
   ```

   8. 로봇을 동작한 경우에는 Safety Function을 넣어주어 로봇이 동작하는 중에는 추가 입력을 받지 않게 만들며, 동작이 끝난 뒤에는 종료 구문을 출력한다.

   ```python
   # Store the status of the robot in the key.
   key = []
   status = indy.get_robot_status()
   for value in status.keys():
       key.append(value)
   
   # Check key & type of status
   print(key)
   print(type(status))
   ```

   9. 로봇 작동 플래그로 power_on을 선언해주며, 초기값은 1로 설정한다.

   ```python
   # Robot Operation Flag
   power_on = 1   # Robot operation needed: 1, Robot operation not needed: 0
   ```

   10. while() 함수를 통해 무한 루프를 만든 뒤, qr_code_reader.py 파일에서 읽은 QR 코드 데이터를 읽어와서 문자열로 해독한다. 그리고 필요한 부분만 location에 최종적으로 저장한 다음에 출력하여 확인해본다.

   ```python
   while(1):
       # Read QR code from 'qr_code_reader.py'
       out = subprocess.check_output(['python', 'qr_code_reader.py'] )
       location = out.decode('utf-8')          # Decode QR code and store data in location
       location = location[:len(location)-2]   # Store data excluding the last two in the location.
     
       # Check location
       print('Data : ', location, '\n')
   ```

   11. location에 저장된 데이터에 해당되는 좌표1(위), 좌표2(아래)를 반환해준다. 만약 location에 quit이라는 데이터가 저장되어 있다면, power_on 플래그를 1에서 0으로 변환시킨다.

   ```python
       # Returns the coordinates of the corresponding location (six location)
       if location == "Creation hall":
           locate_pos1 = [ 0.37860,  -0.53128,  0.70879,   169.93,   7.69,   71.93]    # UP
           locate_pos2 = [ 0.39087,  -0.54838,  0.63746,   175.45,   3.60,   72.48]    # Down
       elif location == "Newton hall":
           locate_pos1 = [ 0.25786,  -0.51737,  0.71442,   170.46,  13.09,   72.51]    # UP
           locate_pos2 = [ 0.26991,  -0.54060,  0.64523,   175.37,   8.12,   73.43]    # Down
       elif location == "Rodem hall":
           locate_pos1 = [ 0.16076,  -0.49830,  0.73360,   170.77,  23.20,   71.19]    # UP
           locate_pos2 = [ 0.17026,  -0.52394,  0.64216,   178.11,  14.25,   73.32]    # Down
       elif location == "Grace hall":
           locate_pos1 = [ 0.05757,  -0.54360,  0.72850,  -178.98,  14.83,   71.69]    # UP
           locate_pos2 = [ 0.06028,  -0.56183,  0.64116,  -176.20,   9.61,   72.75]    # Down
       elif location == "Oseok hall":
           locate_pos1 = [-0.05459,  -0.57265,  0.71999,  -172.90,  10.95,   73.03]    # UP
           locate_pos2 = [-0.05496,  -0.59075,  0.63478,  -170.88,   3.16,   73.49]    # Down
       elif location == "Hyundong hall":
           locate_pos1 = [-0.15900,  -0.57540,  0.73355,  -170.59,  12.66,   72.96]    # UP
           locate_pos2 = [-0.17164,  -0.59050,  0.63448,  -169.83,   5.84,   72.95]    # Down
       elif location == 'quit':
           power_on = 0	# Robot Operation Flag(0)
   ```

   12. location 데이터에 따른 좌표가 할당되고, power_on 플래그가 1인 상태라면, 우편 분류 공정이 실행된다.

       우편 분류 공정의 순서는 다음과 같다.

       - 1단계: 우편이 놓여진 고정된 좌표로 간다.
       - 2단계: z축 방향으로 내려가서 우편을 집을 준비를 마친다.
       - 3단계: Vaccum head를 통해 우편을 집는다.
       - 4단계: 우편을 집은 뒤에 home 위치로 간다.
       - 5단계: 우편 분류함 중 location에 해당되는 위치로 간다.
       - 6단계: z축 방향으로 내려가서 우편을 놓을 준비를 마친다.
       - 7단계: Vaccum head를 통해 우편을 놓는다.
       - 8단계: Vaccum head를 우편 분류함 위로 올린다. 
       - 9단계: home 위치로 돌아가서 대기한다.

   ```python
   if power_on == 1:
           # Step 1: Go to the stationary location where the mail is placed
           t_pos = [0.51681, -0.14784, 0.50296, 179.93, 16.92, 163.91]		# Stationary location(Up)
           indy.task_move_to(t_pos) # move to -> Absolute coordinates, move by -> Relative coordinates
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move1 process')
           
           # Step 2: Go down the z-axis and get ready to pick up the mail
           t_pos = [0.55074, -0.15743, 0.39992, 179.95, 6.32, 163.92]		# Stationary location(Down)
           indy.task_move_to(t_pos)
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move2 process')
   
           # Step 3: Pick up mail through Vaccum head
           indy.set_do(8, 0)
           indy.set_do(9, 1)       
                  
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move3 process')
           
           # Step 4: Pick up the mail and go to the home location
           indy.go_home()      
           
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move4(go home) process')
   
           # Step 5: Go to the location corresponding to the location
           t_pos = locate_pos1
           indy.task_move_to(t_pos)
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move5 process')        
   
           # Step 6: Go down the z-axis and get ready to put the mail
           t_pos = locate_pos2
           indy.task_move_to(t_pos)
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move6 process')
   
           # Step 7: Mail is placed through Vaccum head
           indy.set_do(9, 0)
           indy.set_do(8, 1)
           
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move7 process')
           
           # Step 8: Post the mail and raise the Vaccum head.
           t_pos = locate_pos1
           indy.task_move_to(t_pos)
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move8 process')  
           
           # Step 9: Return to the home position and stand by
           indy.go_home()
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : move9(go home) process')
   ```

   13. location에 quit이라는 데이터가 저장되어 power_on 플래그가 1에서 0으로 바뀐 경우에는 추가적인 로봇 작동이 없는 거라 판단하여 로봇을 zero 위치로 복귀시킨 뒤 프로그램을 종료한다.

   ```python
       if power_on == 0:
           # Zero position
           indy.go_zero()
   
           while True:
               status = indy.get_robot_status()
               sleep(0.2)
               if status[key[5]]==1 :
                   break
           print('done : zero process')
   
           # Disconnect the robot
           indy.disconnect()
   
           # Exit the program
           sys.exit()
   ```

   
