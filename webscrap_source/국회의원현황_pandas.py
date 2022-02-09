# 상세정보들을 DataFrame으로 변환

import pandas as pd
from datetime import date

member_df = pd.read_json('data/member.json')
# print(member_df.shape) #행열 출력
# print(member_df['정당'].unique()) #정당 정보 출력
# print(member_df['정당'].value_counts()) #각 정당별 몇명있는지
# print(member_df['당선횟수'].value_counts()) #몇번 당선됬는지(몇대별로 구분됰)
# print(member_df['선거구'].value_counts())

#당선횟수2 컬럼을 새로 추가
#4선(17대,18대,19대,21대) -> 4선
#print(type(member_df['당선횟수'])) #pandas.core.series.Series
#print(type(member_df['당선횟수'].str)) #pandas.core.strings.accessor.StringMethods -> 슬라이싱, 인덱싱하기 위해서
temp_str= member_df['당선횟수'].str
member_df['당선횟수2'] = temp_str[:2] #2글자 슬라이싱 값을 당선횟수2라는 컬럼으로 저장
#print(member_df['당선횟수2'].value_counts())
#6선이 누군지
#print((member_df.loc[member_df['당선횟수2']=='6선']))

#선거구
temp_str2 = member_df['선거구'].str
member_df['선거구2'] = temp_str2[:2]
#print(member_df['선거구2'].value_counts(normalize=True)) #normalize는 퍼센트로 나타내기
#print((member_df.loc[member_df['선거구2']=='강원']))

#생년월일로 나이계산하기
#print(member_df['생년월일'].head(2))
#DatetimeIndex 객체를 사용해서 생년월일 컬럼의 값(str)을 year,month,day로 각각 추출한다.
#year,month,day 3개의 컬럼을 새로 추가한다.
print(pd.DatetimeIndex(member_df['생년월일']).year) #year값만 출력
member_df['year'] = pd.DatetimeIndex(member_df['생년월일']).year
member_df['month'] = pd.DatetimeIndex(member_df['생년월일']).month
member_df['day'] = pd.DatetimeIndex(member_df['생년월일']).day
print(member_df.loc[0:3,['year','month','day']])
#현재날짜를 통해 나이 계산
today = date.today()
print(today)
birth_1 = date(1960,1,3)
birth_2 = date(1960,3,4)
age = today.year - birth_1.year - ((today.month,today.day)<(birth_1.month,birth_1.day)) #False이므로 0으로 계산(생일 지남)
age2 = today.year - birth_2.year - ((today.month,today.day)<(birth_2.month,birth_2.day)) #Ture이므로 1로 계산(아직 생일 안지남)
print(age,age2)

#가장 나이가 어린 사람은 누구인지
print(member_df.loc[member_df['year']==member_df['year'].max(),['이름','정당']])
#국회의원 나이 계산 함수 정의하기
#인자로 받는 birth는 date객체
def calc_age(birth):
    #현재날짜
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

#나이 계산할 list 생성
age_list =[]
#row별로 년,월,일 컬럼의 값으로 나이를 계산하고 그 결과(나이)값을 list에 append
for idx,row in member_df.iterrows():
    age = calc_age(date(row['year'],row['month'],row['day']))
    age_list.append(age)

print(age_list)
member_df['나이'] = age_list
print(member_df.loc[0:3,['이름','나이']])




