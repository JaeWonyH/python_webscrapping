# 상세정보들을 DataFrame으로 변환

import pandas as pd

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
print(member_df.loc[0:3,['당선횟수','당선횟수2']])



