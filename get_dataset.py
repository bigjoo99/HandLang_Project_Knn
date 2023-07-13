def get_dataSet(angle):
    
    f = open('getData.txt', 'a')  # 텍스트 파일을 이어서 쓰기 모드 
    for i in angle:
        i = round(i, 6)
        f.write(str(i))
        f.write(',')
    f.write("9.000000") # 라벨링을 위한 정답label
    f.write('\n')
    print("next")
    f.close();

def get_testData(angle):
    
    f = open('testData.txt', 'a')  # 텍스트 파일을 이어서 쓰기 모드 
    for i in angle:
        i = round(i, 6)
        f.write(str(i))
        f.write(',')
    f.write("14.000000") # 라벨링을 위한 정답label
    f.write('\n')
    print("next")
    f.close();
