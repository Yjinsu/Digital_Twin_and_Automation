import pyzbar.pyzbar as pyzbar
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Window에서 실행시킬 때
#cap = cv2.VideoCapture(0)                # Linux에서 실행시킬 때

location = str(0)   # location 위치 선언

while(cap.isOpened()):
  # 카메라로 매 프레임마다 이미지를 읽어드린다.
  ret, img = cap.read() 

  if not ret:
    continue
  
  # 이미지를 Gray scale로 변환시킨다.
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # Gray scale로 변환된 QR 이미지를 해독한다.
  decoded = pyzbar.decode(gray)

  for d in decoded:
    # QR 코드의 영역을 추출한다. 
    x, y, w, h = d.rect

    # QR 코드의 타입과 데이터를 읽는다.
    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    # QR 코드의 데이터를 location에 저장한다.
    location = barcode_data

    # QR 코드 부분에 사각형을 그린다.
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # QR 코드의 타입과 데이터를 text에 저장한 뒤에 화면에 나타낸다.
    text = '%s (%s)' % (barcode_data, barcode_type)
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

  # 카메라로 매 프레임마다 읽고 있는 이미지를 'img' 윈도우로 보여준다.
  cv2.imshow('img', img)

  # location에 QR 코드 데이터가 저장되면 반복문에서 나간다.
  if location != str(0):
      break
  
  # 'q'를 누르게 되면 location에 종료 구문이 저장된 채로 반복문에서 나간다.
  key = cv2.waitKey(1)
  if key == ord('q'):
    location = 'quit'
    break

# 저장된 location을 print하여 qr_classify_robot.py에서 location을 읽을 수 있도록 한다.
print(location)

# 설정해놓은 카메라와 윈도우를 해제한다.
cap.release()
cv2.destroyAllWindows()