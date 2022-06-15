# Digital Twin & Automation

# 우편 분류 공정 (Pick and Place - Using QR Code)



## Introduction

이 Repository는 한동대학교 2021년 2학기에 진행된 기전융합프로젝트, 스마트 팩토리의 분류 자동화를 위한 산업로봇 시뮬레이터 환경 구축 (Developing Simulation Environment of Industrial robot (Indy) for Defect Inspection)을 기반으로, 

한동대학교 2022년 1학기에 진행된 Digital Twin & Automation 수업의 Project#2: **Robot Maipulator를 활용한 자동화 공정**에 대한 **설치 및 튜토리얼**이 포함되어 있습니다.
딥러닝을 활용하여 **산업로봇의 제어 코드를 작성**하고, 실제 로봇에 적용하는 것을 목적으로 합니다.

**Project 공정은 QR 코드를 활용한 우편 분류 공정**입니다
매니퓰레이터 모델은 **INDY-10 (Neuromeka)**로, **IndyDCP (인디 전용통신; Indy Dedicated Communication Protocol)** 을 사용해 공정을 구현하였습니다.

**IndyDCP**는 Neuromeka의 Indy 로봇을 제어하기 위한 전용 통신 프로토콜로서, 로봇의 기본적인 설정, 제어, 데이터 수신 등을 지원합니다.  Python, C++, MATLAB, Labview 클라이언트를 지원하는데, 본 프로젝트에서는 딥러닝을 활용하기 위해 [**Python IndyDCP 클라이언트 **](http://docs.neuromeka.com/2.3.0/kr/Python/section1/)를 사용했습니다.

로봇뿐만 아니라, 사용한 **그리퍼 EGP-64** 에 대한 연결 및 사용법 또한 Repository에 포함되어 있습니다.

**이 프로젝트는 한동대학교 김영근 교수님의 지도아래 진행되었습니다.**



## Requirements

**WIFI 연결**이 가능한 노트북 or 데스크탑이여야 하며, 이 프로젝트에서 사용한 노트북의 사양은 CPU - Intel(R) Core(TM) i7-9750H, RAM - 16GB, Graphic Card - NVIDIA GeForce RTX 2060 입니다.

**INDY-10 전용 태블릿**은 로봇 연결 및 상태 확인, 모드 변경을 통한 좌표 추출 등 프로젝트 수행 시 매우 유용한 도구입니다.

Deep Learning 모델의 Input Data 취득을 위해 **WebCam**이 필요합니다. 본 프로젝트에서는 QR 코드를 읽기 위해 노트북 외장 웹캠을 사용했습니다.

    

## Contents

* ### Tutorial Indy Hardware (Setting & Demo)

  * [Reference Link](https://github.com/chaochao77/ROS_neuromeka_tutorial/blob/main/md_fIles/Tutorial%20-%20Manipulator%20INDY-10.md)



* ### Tutorial Indy Sorting (Demo)

  * [Reference Link]()
