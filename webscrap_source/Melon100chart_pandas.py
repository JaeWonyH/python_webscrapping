# json 파일을 load하여 Pandas의 DataFrame에 저장하기
# DataFrame 객체를 DB의 Table에 저장하기

import json
import pandas as pd

with open('data/songs.json',encoding='utf-8') as file:
    songs_json =json.loads(file.read())

#print(songs_json)
song_df = pd.read_json('data/songs.json')
#print(song_df)
#print(song_df.tail())

# song_detail_list 읽어서 dataframe 객체 생성
song_df2 = pd.DataFrame(columns = ['곡명','가수','앨범','좋아요','가사'])

# 1개의 row = Series 객체 , 1개의 column = Series  객체
for song_detail in song_detail_list:
    print(song_detail)
    series_object = pd.Series(song_detail)
    song_df2 = song_df2.append(series_object, ignore_index=True)
song_df2

