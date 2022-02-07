# 행정구역 정보를 읽고, 분석하기
# read_csv() 함수로 csv file 읽어오기
# 특정행과 열을 선택하기
# 컬럼명변경
# 상관관계 분석(인구수와 면적간의 상관관계)
# 시각화

import pandas as pd

data = pd.read_csv('data/data_draw_korea.csv')
print(type(data))
print(data.head())