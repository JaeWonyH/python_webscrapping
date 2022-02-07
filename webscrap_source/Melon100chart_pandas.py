# song_detail_list 읽어서 dataframe 객체 생성

import pandas as pd
from webscrap_source.Melon100chart import song_detail_list

song_df2 = pd.DataFrame(columns=['곡명','가수','앨범','좋아요','가사'])

# 1개의 row = Series 객체 , 1개의 column = Series  객체
for song_detail in song_detail_list:
    # dict <=> Series
    series_obj = pd.Series(song_detail)
    # list <=> DataFrame
    song_df2 = song_df2.append(series_obj, ignore_index=True)
print(song_df2.head())

