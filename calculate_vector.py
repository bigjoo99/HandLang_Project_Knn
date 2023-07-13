import numpy as np
import keyboard
from get_dataset import get_dataSet
from get_dataset import get_testData

def calculate_vector(arr):
    v1 = arr[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :]
    v2 = arr[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], :]
    v = v2 - v1  # 관절 벡터를 계산
    v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]  # 벡터의 정규화를 수행합.

    # 각도를 계산하기 위해 관절 벡터를 선택
    compare_V1 = v[[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17], :]
    compare_V2 = v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :]
    angle = np.arccos(np.einsum('nt,nt->n', compare_V1, compare_V2))  # 각도를 계산
    angle = np.degrees(angle)  # 각도를 도 단위로 변환
    
    if keyboard.is_pressed('a'):  # 'a' 키가 눌리면 get_dataSet함수를 호출하여 data셋 수집
        get_dataSet(angle)
    
    if keyboard.is_pressed('s'):
        get_testData(angle)    
    return angle
