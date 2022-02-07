# 행정구역 정보를 읽고, 분석하기
# read_csv() 함수로 csv file 읽어오기
# 특정행과 열을 선택하기
# 컬럼명변경
# 상관관계 분석(인구수와 면적간의 상관관계)
# 시각화

import pandas as pd

data = pd.read_csv('data/data_draw_korea.csv')

# print(type(data))
# print(data.head())
# print(data.shape)
# print(data.index)
# print(data.columns)
# print(data.info())

# print(data.describe())
# print('인구수 최대',data['인구수'].max())
# print('인구수 표준편차',data['인구수'].std())

#unique한 광역시도명
# print(data['광역시도'].unique())

#광역시도 row counting
# print(data['광역시도'].value_counts())

#서욽특별시에 속한 구에 대한 정보 선택하기
print(data.loc[data['광역시도']=='서울특별시'])
print(data.loc[data['광역시도']=='서울특별시'].sort_values(by='인구수',ascending=False).reset_index(drop=True))

#서울특별시의 인구수의 평균과 표준편차
data_seoul =data.loc[data['광역시도']=='서울특별시']
print('표준편차',data_seoul['인구수'].std())
print('평균',data_seoul['인구수'].mean())