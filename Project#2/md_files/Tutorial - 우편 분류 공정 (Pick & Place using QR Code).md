# Main Contents: Pick and Place using QR code

프로젝트 수행을 위해 구축한 우편 분류 공정에 대한 **Python IndyDCP** 코드는 아래의 순서에 따라 작동하게 됩니다.

<p align="center">
      <img src="https://user-images.githubusercontent.com/84503980/173833947-62c3d286-cb0f-4d5e-9e0e-6d73da0a5944.png" width="50%" height="50%" alt="text" width="number" />
      </p>
      
<br/><br/><br/>

## 1. External Envirionment Setting

<br/>

1. QR 코드 생성
   우편을 분류하기 위해, 먼저 QR 코드를 생성하는 과정이 필요합니다.
   QR 코드 생성에는, Python Module "qrcode" 를 활용했습니다.
   
   <img src="https://user-images.githubusercontent.com/84503980/173837441-2640bf07-6d1a-4ec9-96ed-9da41ddb0509.png" width="100%" height="100%" align = 'center'/>
   
   위와 같은 방법을 통해 QR코드 이미지를 만들고, 이를 인쇄한 뒤 편지 봉투에 붙였습니다.

<br/>

2. 좌표 고정
    편지 봉투를 쌓아 둘 곳과, 분류할 곳의 좌표를 설정해야 합니다.
    **INDY-10 전용 태블릿**을 활용, '직접 교시' 모드를 통해 좌표를 취득하였습니다.
    그 과정은 다음과 같습니다
    
    - INDY-10 전용 태블릿에서, 초보자 모드에서 직접교시 모드로 바꿔줍니다.

      <p align="center">
      <img src="https://user-images.githubusercontent.com/84503980/173838034-fa1d1820-6ee1-4cf3-b772-a164d9136ada.png" width="50%" height="50%" alt="text" width="number" />
      </p>
    
    - 로봇을 원하는 위치로 움직여 좌표를 땁니다.	

      <p align="center">
      <img src="https://user-images.githubusercontent.com/84503980/173838362-0cee0a60-e234-4209-8747-9bda393254cf.png" width="50%" height="50%" alt="text" width="number" />
      </p>
      
    여기서 취득한 좌표를 사용하는 부분에 대해서는, 추후 **3. Coding** 부분에서 다시 언급하겠습니다.

<br/><br/><br/>

## 2. Internal Environment Setting

1) **Install Visual Studio Code**

   - **Visual Studio Code** 란, 윈도우(Windows), 맥(Mac OS), 리눅스(Linux) 운영체제 모두에서 사용 가능한 소스 코드 편집기입니다.
   - 원활한 코드 수정/실행을 위해, VScode를 설치합니다.
   - 다음의 주소를 통해 VScode를 설치할 수 있습니다. [Install Link](https://code.visualstudio.com/Download)

2) **Install Anaconda**

    - "Anaconda" 란, 파이썬 가상 환경을 통해 라이브러리들을 쉽게 설치하고 관리할 수 있게 하는 도구입니다.
    - 파이썬은 기본적으로 패키지 관리 시스템 **pip** 만을 포함하며, 필요에 따라 추가적으로 툴/패키지를 수동으로 추가해야 합니다.
    - 패키지를 다운로드하는 과정이 반복될 경우, 프로젝트 수행에 필요 없는 패키지가 사전에 설치된 경우 필요 이상으로 공간을 차지하곤 합니다.
    - 이때 Anaconda 가상환경을 활용하면, 필요가 없어진 가상환경을 삭제하는 것 만으로 설치한 모든 패키지를 제거할 수 있습니다.
    - 다음의 주소를 통해 Anaconda를 설치할 수 있습니다. [Install Link](https://www.anaconda.com/products/distribution#Downloads)
    - Conda 가상 환경 사용 방법은 다음과 같습니다.

      * Open Anaconda Prompt(admin mode)
       <p align="center">
      <img src="https://user-images.githubusercontent.com/84503980/173847474-65566d79-b8ef-43ae-9b86-0e1c44687694.png" width="80%" height="80%" alt="text" width="number" />
      </p>

      * Update conda

       ```python
            conda update -n base -c default conda
       ```

      * Create Virtual Environment for Python (In this project, We used Python 3.9)

       ```python
            conda create -n py39 python = 3.9
       ```
3) **Install Python module**

    - QR 코드를 인식하는 딥러닝 모델을 사용하기 위해서는 아래의 파이썬 모듈 설치가 요구됩니다.

      * libzbar0
      * pyzbar
      * numpy
    
    - Anaconda 가상 환경에 파이썬 모듈을 설치하는 방법은 다음과 같습니다
    
      * Activate Virtual Environment
       
       ```python
            conda activate py39
       ```

      * Install pip module
       
       ```python
            # Approach 1
            !apt install libzbar0
            !pip install pyzbar
            pip install numpy
            
            # Approach 2
            conda install libzbar0
            conda install pyzbar
            conda install numpy
       ```

4) **Download IndyDCP Package & Demo Code **

    - 매니퓰레이터 모델 **INDY-10 (Neuromeka)** 을 구동시키기 위한 패키지와, Demo 수행을 위한 코드를 다운로드합니다.
    - [Download Link]()
    - [Algorithm of Main Code](https://github.com/Yjinsu/Digital_Twin_and_Automation/blob/main/Project%232/md_files/Code%20Description.md)
 
<br/><br/><br/>

## 3. Demo

튜토리얼을 모두 수행하였을 경우, 다음과 같이 로봇이 동작합니다.

1. [Demo Link]()





