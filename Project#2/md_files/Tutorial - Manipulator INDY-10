## Tutorial - Manipulator INDY-10

##### 로봇 연결

1. 컨트롤박스를 콘센트에 연결한뒤, 전원 버튼을 누릅니다. 2~5분이면 로봇이 완전히 작동하게 됩니다.
2. 컨트롤 박스 뒷면에 **랜선을 공유기에 연결**합니다. (**컴퓨터와 같은 wifi로 연결**되어야지만 ROS 코드를 사용한 제어가 가능합니다.)
3. 태블릿을 컨트롤 박스 뒷면 USB포트로 연결합니다.
4. 태블릿의 **Conty 앱**에 들어가 **USB연결**을 눌러 로봇이 잘 연결되는지 확인합니다.

4-1. 만약 연결이 되지 않을 경우 **Emergency 버튼**을 확인해보세요. 눌러져 Lock되어 있을 경우, **돌려서 빼면 됩니다. **

4-2. 우측 상단에 붉은 메세지가 떠있을 경우, 우측 상단에 있는 **리셋을 눌러 초기화**하면 됩니다.

[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/11.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/11.jpg)

1. 로봇의 IP를 확인하기 위해 환경설정, **애플리케이션 정보**를 들어가 **IP**를 확인합니다. (**ROS로 로봇과 연결 시 **IP를 알아야합니다.)

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/12.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/12.jpg)[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/13.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/13.jpg)

2. 이제 USB 연결을 해제하고 **확인한 IP로 WIFI모드로 연결**합니다. (*이때 태블릿 또한 같은 공유기 WIFI로 연결되어 있어야합니다)

3. 로봇이 작동이 잘되는지 간단히 테스트 하고싶으시다면 아래와 같이 **프로그램 > 새로만들기 > 시간기준 > 조인트이동 편집 > 직접 교시**로 들어가 직접 손으로 로봇 조인트들을 움직일 수 있습니다.

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/17.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/17.jpg)[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/14.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/14.jpg)

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/15.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/15.jpg)[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/19.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/19.jpg)

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/16.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/16.jpg)

   또한 이동 > 홈 위치 or 영위치를 누르는 것으로 조인트 별로 이상이 없는지 간단히 체크 할 수 있습니다.

실험 도중 로봇이 멈추거나, 오류가 생길 경우 **태블릿의 Reset 버튼**을 누르면 로봇 상태가 초기화 되며 오류가 고쳐집니다.



##### 실제 로봇 연결

1. INDY-10을 작동시키고, **컨트롤박스에 연결된 공유기와 동일한 WIFI로 컴퓨터와 연결**합니다.

2. 태블릿으로 확인한 로봇의 IP로 터미널 창에서 아래의 명령어의 xxx부분에 **IP주소를 추가하여 실행**합니다.

   `roslaunch indy10_moveit_config moveit_planning_execution.launch robot_ip:=xxx.xxx.xxx.xxx`

3. 태블릿으로 로봇을 조작하여 움직이면 Rviz에서도 실시간으로 로봇이 움직이는 것을 확인 할 수 있습니다.

4. 종료하시고 싶으시다면 명령을 실행한 터미널로 가서 `ctrl+c` 를 눌러 실행한 `roslaunch`가 종료되면서 Rviz가 꺼지고 로봇과의 연결이 끊깁니다.



## Hardware - Gripper

##### EGP-C-64 (SCHUNK)

[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/140.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/140.jpg)

###### Specification

- 20mm의 스트로크
- 230N의 힘 (50%, 100% 조절 가능)
- **24V 전력공급** 필요
- **Open, close 두개의 입력선**으로 그리퍼 **열고, 닫기 제어**
- LED light, 스트로크 위치 감지 센서 등 출력 센서

###### 연결 - 플랜지, 그리퍼

그리퍼를 로봇에 장착 할 때, 로봇의 엔드툴과 그리퍼의 장착부를 호환시켜주는 부품을 플랜지라 합니다. 아래의 이미지 예시처럼 플랜지를 먼저 장착한 뒤, 그리퍼를 장착하면 됩니다.

[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/150.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/150.jpg)

1. 플랜지를 M4나사 6개와 로봇의 엔드툴 부분과 연결합니다.
2. 그 후 위치에 맞게 그리퍼를 끼운 후, M4 육각렌치로 4개의 나사를 돌려 장착합니다.

###### 연결 - 컨트롤 박스

1. 컨트롤 박스 후면을 보면 아래의 이미지와 같이 Digital I/O, Analog I/O가 있습니다.

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/112.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/112.jpg)[![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/111.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/image/111.jpg)

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/114.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/114.jpg)

   전선을 포트에 넣어 연결하려면은 **일자 드라이버 작은게 **필요합니다. 각 번호의 포트 **구멍 옆의 주황색 부분**을 일자 드라이버로 꾸욱 누르면 포트 구멍이 열려 쉽게 넣고 뺄 수 있습니다. **하지만 너무 깊게 넣을 시 빼기 힘들 수 있으니 잘 잡힐 정도로만 넣으면 됩니다.**

2. 컨트롤 박스의 I/O보드들에 전력을 공급하기 위해 위의 오른쪽 이미지 처럼 **1-10포트의 9,10번째를 서로 연결**하고, **11-20포트의 9,10번째를 서로 연결**합니다

   - 1-10 의 9,10번째 포트는 **GND**, 1-20의 9,10번째 포트는 **24[V] VCC**로 **컨트롤 박스 내부에서 자체적으로 I/O보드에 24[V]전력이 공급**되게 해줍니다.

3. 이제 그리퍼 EGP-C-64에 전력 공급을 위해 **41-50의 10번 포트에 Vcc(빨강, 파랑 패턴선), 9번에 GND(회색 갈색 패턴선)을 연결**합니다.

4. 그리퍼의 **Close(파랑선)을 41-50의 2번 포트에, Open(빨강)을 1번에 연결**합니다. 아래의 이미지처럼 연결되었다면 그리퍼를 사용할 준비가 완료 된겁니다.

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/113.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/113.jpg)

###### 제어 - 태블릿

1. Conty 앱을 실행하여 로봇과 연결합니다.

2. 로봇 설정에 들어가면 아래의 이미지 처럼 화면에 바로 6개의 조인트 및 **Smart DI/O** 들이 보입니다.

   [![img](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/141.jpg)](https://github.com/chaochao77/ROS_neuromeka_tutorial/raw/main/image/141.jpg)

3. Smart D I/O에서 **8 번과 9번**의 출력에 따라 그리퍼와 연결된 **Close(blue), Open(red) 선에 0,1의 디지털 값**이 입력됩니다.

4. 태블릿에서 **8번을 눌러 On (초록색) , 9번을 off(회색)**을 하면 그리퍼 **열기**, 반대로 **8번을 다시 눌러 off, 9번을 눌러 on**하면 그리퍼 **닫기** 작용을 하게 됩니다.

5. EGP-C-64의 경우 **Open과 Close가 { 1 ,0 } 또는 {0 , 1} 으로 입력**이 되어야 지만 열고 닫는 작용을 하게 됩니다.
