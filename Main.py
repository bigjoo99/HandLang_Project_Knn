import cv2
import mediapipe as mp
import numpy as np
import keyboard
import time
from Initialization import Initialize
from Input import Input,setting
from calculate_vector import calculate_vector

model = Input()
key = None


while True:
    frame, img = setting.cap.read()  # 비디오 프레임 읽기 ( frame = 프레임 판독여부 bool, img = 이미지 프레임)
    if not frame: # 프레임을 못가져왔다면 패스
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 이미지를 RGB 색상 공간으로 변환
    result = setting.hands.process(imgRGB)  # 손 인식 모델을 사용하여 손 관련 정보를 추출

    if result.multi_hand_landmarks is not None:  # 손이 감지된 경우에만 실행
        for line in result.multi_hand_landmarks:
            joint = np.zeros((21, 3))  # 손 관절 좌표를 저장할 배열을 생성
            setting.mp_drawing.draw_landmarks(img, line, setting.mp_hands.HAND_CONNECTIONS)  # 손 랜드마크와 연결선을 이미지에 그림.
            for x, landmark in enumerate(line.landmark):
                joint[x] = [landmark.x, landmark.y, landmark.z]  # 손 관절 좌표를 배열에 저장
            angle = calculate_vector(joint)     # 관절 벡터 계산+ 함수 호출(calculate_vector)
        model.predict(np.array([angle], dtype=np.float32)) # 관절 벡터 예측하기
        
        # 화면에 분류된 제스처의 문자를 표시합니다.
        cv2.putText(img, model.gesture[model.index].upper(), (int(line.landmark[0].x * img.shape[1] - 10), int(line.landmark[0].y * img.shape[0] + 40)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    # 문장을 화면에 표시
    cv2.putText(img, model.sentence, (20, 440), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

    cv2.imshow('HandTracking', img)
    HandLang_img = cv2.imread('handLang.jpg')
    cv2.imshow('HandLang_img', HandLang_img)
    cv2.waitKey(1)  
    if keyboard.is_pressed('b'):  # 'b' 키가 눌리면 종료
        cv2.destroyAllWindows()
        break


