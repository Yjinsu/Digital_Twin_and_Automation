# Tutorial - Manipulator INDY-10

<br/>


## 로봇 연결

1. 컨트롤박스를 콘센트에 연결한뒤, 전원 버튼을 누릅니다. 2~5분이면 로봇이 완전히 작동하게 됩니다.
2. 컨트롤 박스 뒷면에 **랜선을 공유기에 연결**합니다. (**컴퓨터와 같은 wifi로 연결**되어야지만 ROS 코드를 사용한 제어가 가능합니다.)
3. 태블릿을 컨트롤 박스 뒷면 USB포트로 연결합니다.
4. 태블릿의 **Conty 앱**에 들어가 **USB연결**을 눌러 로봇이 잘 연결되는지 확인합니다.
  - 1. 만약 연결이 되지 않을 경우 **Emergency 버튼**을 확인해보세요. 눌러져 Lock되어 있을 경우, **돌려서 빼면 됩니다. **
  - 2. 우측 상단에 붉은 메세지가 떠있을 경우, 우측 상단에 있는 **리셋을 눌러 초기화**하면 됩니다.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174025653-e7f15dab-b155-416a-9d0f-18fe4ac11d66.png" width="80%" height="80%" alt="text" width="number" />
  </p>

<br/>

1. 로봇의 IP를 확인하기 위해 환경설정, **애플리케이션 정보**를 들어가 **IP**를 확인합니다. (**ROS로 로봇과 연결 시 **IP를 알아야합니다.)

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174025744-6447f5e6-fb89-4aea-bc10-2f583a1f22ca.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174025924-35c1c6a4-9c34-4d1b-9e6b-2c6279d56283.png" width="80%" height="80%" alt="text" width="number" />
  </p>


2. 이제 USB 연결을 해제하고 **확인한 IP로 WIFI모드로 연결**합니다. (*이때 태블릿 또한 같은 공유기 WIFI로 연결 되어 있어야 합니다)

3. **프로그램 > 새로만들기 > 시간기준 > 조인트이동 편집 > 직접 교시**로 들어가 직접 손으로 로봇 조인트들을 움직일 수 있습니다. 이를 통해 좌표 취득이 가능합니다.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174025946-5bd469b4-8b6b-4df9-9daf-9c27333318f9.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174025960-72cb5cf1-9268-4bb8-8bd8-f64d6ebf535f.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174026549-a2dfce42-37e2-4542-ad43-9be98db1931c.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174026695-a63a6dcd-e8cd-4cbd-a99d-28fa0a61b2a8.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174026748-8da295e7-8f57-46bc-a6bd-5d8cde75dfe2.png" width="80%" height="80%" alt="text" width="number" />
  </p>

   또한 이동 > 홈 위치 or 영위치를 누르는 것으로 조인트 별로 이상이 없는지 간단히 체크 할 수 있습니다.

실험 도중 로봇이 멈추거나, 오류가 생길 경우 **태블릿의 Reset 버튼**을 누르면 로봇 상태가 초기화 되며 오류가 고쳐집니다.

<br/><br/>

## Hardware - Vaccum Gripper

<br/>

### VGC10 (OnRobot)

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174002364-8460045f-b7f7-45d6-a4ee-385e9dd5e8f0.png" width="80%" height="80%" alt="text" width="number" />
  </p>

<br/>

### Specification

- 3개 종류의 Vacuum cup을 장착할 수 있습니다.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174015696-bb7289b4-9aa9-4ae0-83c8-d07c7b29d90b.png" width="50%" height="50%" alt="text" width="number" />
  </p>
- 들어올리고자 하는 물체 타입에 따라 적절한 Vaccum cup 선정이 요구됩니다.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174016249-b521bf76-bde7-4f5c-997c-e37bae04d3f3.png" width="50%" height="50%" alt="text" width="number" />
  </p>
- 최대 15kg 까지 들어올릴 수 있습니다.
- Customize된 **Adapter Plate**를 활용함으로서 보다 폭넓게 사용할 수 있습니다.
- **24V 전력공급**이 요구됩니다.
- **Open, close 두개의 입력선**으로 그리퍼를 제어합니다. **열고, 닫기 제어**

세부 사항은 [DataSheet](https://onrobot.com/sites/default/files/documents/Datasheet_VGC10_v1.2_EN.pdf?_gl=1*19vnqsf*_ga*MjA1MDE5NDAwOS4xNjU1MzU5MjUy*_up*MQ..)를 통해 확인할 수 있습니다.

<br/>

### 연결 - Adapter Plate, 그리퍼

아래의 이미지 예시처럼 Adapter Plate와 그리퍼를 연결할 수 있습니다.
<p align="center">
<img src="https://user-images.githubusercontent.com/84503980/174017208-65be0dbe-a845-4329-8b7b-69a8c9fdbda4.png" width="50%" height="50%" alt="text" width="number" />
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/84503980/174017252-206a2c08-6d7e-4e6b-89ef-8ed72f3f366b.png" width="50%" height="50%" alt="text" width="number" />
</p>

1. 4개의 나사를 4Nm 토크로 조여서 설치할 수 있습니다.
2. 설치 방향에 따라, Vaccum 채널(1, 2)를 효율적으로 사용할 수 있습니다.

<br/>

### 연결 - OnRobot Compute Box & IndyCB(컨트롤 박스)

1. OnRobot Compute Box
   <p align="center">
   <img src="https://user-images.githubusercontent.com/84503980/174020481-bea9a20e-2a60-440f-aa67-c902bf6edfc9.png" width="50%" height="50%" alt="text" width="number" />
   </p>
   <p align="center">
   <img src="https://user-images.githubusercontent.com/84503980/174021019-ecc4e287-f176-4a6a-9aec-b09b4397231b.png" width="60%" height="60%" alt="text" width="number" />
   </p>

   **OnRobot Compute Box** 단자와 컨트롤 박스를 연결합니다.
   **OnRobot Compute Box** 에 대한 자세한 설명읜 [Link](https://onrobot.com/sites/default/files/documents/User_Manual_for_HANWHA_v1.02_EN.pdf)의 19p 에서 확인 가능합니다.

<br/>

2. 컨트롤 박스 후면을 보면 아래의 이미지와 같이 Digital I/O, Analog I/O가 있습니다.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174018890-f552edc4-0270-4ccf-9c63-de833f231b20.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174027832-0ea4f497-39c7-4008-b599-9a4696a4ca56.png" width="80%" height="80%" alt="text" width="number" />
  </p>

   컨트롤 박스 포트에 대한 세부 설명은 [IndyCB](http://docs.neuromeka.com/2.3.0/kr/CB/section1/)에서 확인할 수 있습니다.
   
   전선을 포트에 넣어 연결하려면은 **작은 일자 드라이버**가 필요합니다. 각 번호의 포트 **구멍 옆의 주황색 부분**을 일자 드라이버로 꾸욱 누르면 포트 구멍이 열려 쉽게 넣고 뺄 수 있습니다. **하지만 너무 깊게 넣을 시 빼기 힘들 수 있으니 잘 잡힐 정도로만 넣으면 됩니다.**

<br/>

3. 컨트롤 박스의 I/O보드, 그리퍼 VGC10에 전력을 공급하기 위해 위의 아래의 이미지 처럼 포트를 연결합니다.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174030598-bc8b8d5f-a768-4424-a7c1-a27fcd88017a.png" width="80%" height="80%" alt="text" width="number" />
  <img src="https://user-images.githubusercontent.com/84503980/174030632-a7acb567-e90a-4fa5-93a4-24fe7fe4c993.png" width="80%" height="80%" alt="text" width="number" />
  </p>
  
   - **1-10포트의 9,10번째 포트(IndyCB)를 서로 연결**하고, **31-40포트와 41-50포트를 OnRobot Compute Box와 연결**합니다
   - **31-40 의 9,10번째 포트(IndyCB)**는 OnRobot Compute Box의 **24V, GND**에 연결됩니다
   - **41-50의 3,4번째 포트(IndyCB)**는 OnRobot Compute Box의 **DI1, DI2**에 연결됩니다
   - 그리퍼의 **Close(파랑선)을 41-50의 2번 포트에, Open(빨강)을 1번에 연결**합니다
   - 그리퍼 EGP-C-64을 사용하고 싶을 경우, **41-50의 10번 포트에 Vcc(빨강, 파랑 패턴선), 9번에 GND(회색 갈색 패턴선)을 추가로 연결**하면 됩니다.
   

<br/><br/>

### 제어 - 태블릿

1. Conty 앱을 실행하여 로봇과 연결합니다.

<br/>

2. 로봇 설정에 들어가면 아래의 이미지 처럼 화면에 바로 6개의 조인트 및 **Smart DI/O** 들이 보입니다.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/84503980/174032054-e28a36da-9fa6-426d-92ec-daef6cbdf19d.png" width="80%" height="80%" alt="text" width="number" />
  </p>

<br/>

3. Smart D I/O에서 **10 번과 11번**의 출력에 따라 VGC10과 연결된 **Close(blue), Open(red) 선에 0,1의 디지털 값**이 입력됩니다. 그리퍼 EGP-C-64를 연결한 경우, Smart D I/O에서 **8 번과 9번**의 출력에 따라 그리퍼와 연결된 **Close(blue), Open(red) 선에 0,1의 디지털 값**이 입력됩니다.

<br/>

4. 태블릿에서 **10번을 눌러 On (초록색) , 11번을 off(회색)**을 하면 VGC10이 **물체를 빨아들입니다**., 반대로 **10번을 다시 눌러 off, 11번을 눌러 on**하면 VGC10의 **흡입 동작이 정지**합니다

<br/>

5. VGC10의 경우 **Open과 Close가 { 1 ,0 } 또는 {0 , 1} 으로 입력**이 되어야 지만 열고 닫는 작용을 하게 됩니다.
