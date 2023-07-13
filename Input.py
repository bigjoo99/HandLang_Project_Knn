import keyboard
import time
from Learning import Learn
from Initialization import Initialize

knn = Learn()
knn.train()
setting = Initialize()


class Input:
    def __init__(self):
        self.sentence = ''
        self.index = None
        self.results = None
        self.gesture = {  # 제스처와 해당 제스처에 대응하는 문자를 매핑한 딕셔너리
            0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
            8: 'i', 9: 'j', 10: 'k', 11: '1', 12: 'm', 13: 'n', 14: 'o', 15: 'p',
            16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 
            23: 'x', 24: 'y', 25: 'z', 26: 'spacing', 27: 'clear', 28: 'delete'
        }
        
    def predict(self, data):
        self.index = knn.find(data)
        
        if self.index in self.gesture.keys():  # 분류된 제스처가 딕셔너리의 키에 있는 경우에만 실행
            if self.index != setting.prev_index:  # 이전 제스처와 현재 제스처가 다른 경우
                setting.startTime = time.time()  # startTime을 현재 시간으로 업데이트
                setting.prev_index = self.index  # 이전 제스처를 현재 제스처로 업데이트
            else:
                if time.time() - setting.startTime > setting.recognizeDelay:  # 인식 딜레이를 초과한 경우
                    
                    setting.startTime = time.time()  # 현재 시간으로 업데이트
                    if self.index == 26:  # 제스처가 'spacing'인 경우 공백추가
                        self.sentence += ' '

                    elif self.index == 27:  # 제스처가 'clear'인 경우 문장 초기화
                        self.sentence = ''

                    elif self.index == 28:  # self.index == 28:  하나 지우기
                        self.sentence = self.sentence[:-1]

                    else:
                        self.sentence += self.gesture[self.index]  # 제스처에 해당하는 문자를 문장에 추가
