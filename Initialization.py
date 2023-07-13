import cv2
import mediapipe as mp
import time


class Initialize:
    def __init__(self):
        self.max_num_hands = 1  # 인식할 손의 최대 개수
        self.mp_hands = mp.solutions.hands  # MediaPipe의 손 인식 모듈을 가져옴
        self.mp_drawing = mp.solutions.drawing_utils  # 손 관련 랜드마크를 그리기 위한 drawing_utils 모듈을 가져옴
        self.hands = self.mp_hands.Hands(
            max_num_hands=self.max_num_hands,
            min_detection_confidence= 0.5,  # 무슨 뜻인지 알아보자
            min_tracking_confidence= 0.5)  # 손 인식 모델을 초기화


        self.cap = cv2.VideoCapture(0)  # 비디오 캡처 객체를

        self.startTime = time.time()  # 현재 시간을 startTime 변수에 저장  초기 셋팅
        self.prev_index = 0

        self.recognizeDelay = 1  # 제스처 인식 간의 딜레이 시간
