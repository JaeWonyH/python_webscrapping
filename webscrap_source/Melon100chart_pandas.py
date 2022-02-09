# song_detail_list 읽어서 dataframe 객체 생성

import pandas as pd
from webscrap_source.Melon100chart import song_detail_list
import pymysql
import sqlalchemy

song_df2 = pd.DataFrame(columns=['곡명','가수','앨범','좋아요','가사'])

# 1개의 row = Series 객체 , 1개의 column = Series  객체
for song_detail in song_detail_list:
    # dict <=> Series
    series_obj = pd.Series(song_detail)
    # list <=> DataFrame
    song_df2 = song_df2.append(series_obj, ignore_index=True)
#print(song_df2.head())

#song_file을 읽어서 Dataframe 객체를 생성하는 방법
song_df = pd.read_json('data/songs.json')
#print(type(song_df))
#print(song_df.head()) #앞에 5 줄
#print(song_df.tail()) #끝에 5줄
# print('shape', song_df.shape)
# print('columns', song_df.columns)
# print('index', song_df.index)
# print('values', type(song_df.values)) #2차원배열

# 가수 컬럼 값별로 row counting
#print(song_df['가수'].value_counts())

# unique한(중복제거) 가수 컬럼의 값을 가져오기
#song_df['가수'].unique()

#indexing
#print(song_df.loc[song_df['가수'] == '임영웅'])

# 특정 행과 열을 선택하기
# loc[], iloc[] 사용한다.
# Slicing 을 사용해서 구간을 주어서 행과 열을 선택
# [ ]
# (list)를 사용해서 여러개의 행과 열을 선택
# 조건식을 만족하는 행과 열을 선택

# Slicing : 인덱스가 0부터 5까지의 행과 모든 열을 선택하기
#print(song_df.loc[0:5]) # song_df.loc[0:5,:])

# Slicing : 인덱스가 0부터 10까지의 행과 모든 열을 선택하기 , 1개의 행을 skip
#print(song_df.loc[0:10:2]) # song_df.loc[0:10:2,:]

### sqlAlchemy와 Pymysql을 사용하여 DataFrame객체를 DB에 저장하기
pymysql.install_as_MySQLdb()  #pymysql과 sqlAlchemy 연동
from sqlalchemy import create_engine

print(song_df.head())
try:
    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+pymysql://python:python@localhost:3306/python_db',encoding='utf-8')
    print(engine)
    conn = engine.connect()

    #song_df(DataFrame객체)를 songs 테이블로 저장 : to_sql() 함수사용
    song_df.to_sql(name = 'songs', con=engine, if_exists='replace', index=False)
finally:
    conn.close()
    engine.dispose()





