import cv2
import numpy as np


class Learn:
    def __init__(self):
        self.index = None
        self.dist = None
        self.neighbours = None
        self.results = None
        self.frame = None
        self.knn = None
        self.file = np.genfromtxt('getData.txt', delimiter=',') # 데이터셋 파일을 로드  
        self.angleFile = self.file[:, :-1]  # 각도 데이터
        self.labelFile = self.file[:, -1]  # 레이블 데이터
        self.angle = self.angleFile.astype(np.float32)  # 데이터를 float32 형식으로 변환
        self.label = self.labelFile.astype(np.float32)


    def train(self):
        self.knn = cv2.ml.KNearest_create()  # K-최근접 이웃 분류기를 생성
        self.knn.train(self.angle, cv2.ml.ROW_SAMPLE, self.label)  # KNN 모델을 학습


    def find(self, data):
        self.frame, self.results, self.neighbours, self.dist = self.knn.findNearest(data,3)  # KNN 모델을 사용하여 제스처를 분류
        self.index = int(self.results[0][0])  # 분류된 제스처의 인덱스
        return self.index