# melon 100 chart
# 100곡의 노래의 제목과 songID 추출해서 list에 저장하기
# 100곡의 노래의 상세정보를 추출해서 list와 dict에 저장해서 json 파일로 저장하기
# json 파일을 load하여 Pandas의 DataFrame에 저장하기
# DataFrame 객체를 DB의 Table에 저장하기

import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://www.melon.com/chart/index.htm'
req_header_dict = {
    #요청헤더 : 브라우저 정보
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, headers=req_header_dict)
#요청헤더 응답코드
print(res.status_code)

if res.ok:
    html =res.text
    soup = BeautifulSoup(html, 'html.parser')
    # <div id ='tb_list'><tr><a>
    #song 몇개 있는지
    print(len(soup.select("div#tb_list tr a[href*='playSong']")))
    a_tags = soup.select("div#tb_list tr a[href*='playSong']")
    #print(a_tags)
    song_list = [] #100곡 담을 list

    #100곡의 노래의 제목과 songID 추출해서 list에 저장하기
    for idx,a_tag in enumerate(a_tags,1):
        song_dict = {} #song 정보 담을 dict
        #<a href = "">노래제목<a>
        song_title = a_tag.text
        song_dict['song_title'] = song_title
        #href 속성 값 추출
        href_value = a_tag['href']
        #print(href_value)
        #print(idx,song_title)
        matched = re.search(r'(\d+)\);',href_value)  #정규표현식을 써서 song_id 추출 , 정규표현식 연습 site: https://regexr.com/
        if matched:
            song_id =matched.group(1)
            song_dict['song_id'] =song_id
            song_detail_url = f'https://www.melon.com/song/detail.htm?songId={song_id}' #노래 상세정보 url
            song_dict['song_detail_url'] = song_detail_url
            #print(song_dict)
            song_list.append(song_dict)
    print(len(song_list))

# 100곡의 노래의 상세정보를 추출해서 list와 dict에 저장해서 json 파일로 저장하기
song_detail_list = []
for idx,song in enumerate(song_list,1):
    #print(song['song_detail_url'])
    #song 1곡의 상세정보를 저장할 dict
    song_detail_dict = {}
    song_detail_url = song['song_detail_url']
    res = requests.get(song_detail_url, headers=req_header_dict)
    #print(res.status_code)
    if res.ok:
        soup = BeautifulSoup(res.text , 'html.parser')
        song_detail_dict['곡명'] = song['song_title']
        if soup.select("a[href*='goArtistDetail'] span"):
            song_detail_dict['가수'] = soup.select("a[href*='goArtistDetail'] span")[0].text
        if soup.select("div.meta dd")[0] :
            song_detail_dict['앨범'] = soup.select("div.meta dd")[0].text
        #print(song_detail_dict)
        song_id  =song['song_id']
        #print(song_id)
        like_url = f'https://www.melon.com/commonlike/getSongLike.json?contsIds={song_id}'
        like_res = requests.get(like_url,headers=req_header_dict)
        #print(like_url)
        #print(like_res.status_code)
        #좋아요 건수 ajax 통신 함으로 json파일로 받음
        #print(like_res.json()['contsLike'][0]['SUMMCNT'])
        song_detail_dict['좋아요'] = like_res.json()['contsLike'][0]['SUMMCNT']

        lyric_div = soup.select("div#d_video_summary")
        if lyric_div:
            lyric_temp = lyric_div[0].text
            # 정규표현식을 이용하여 패턴 찾음.
            pattern = re.compile(r'[\r\n\t]]')
            #print(lyric)
            #패턴(특수문자) 찾아서 대체
            lyric= pattern.sub('',lyric_temp.strip())
        else:
            lyric = ''
        song_detail_dict['가사'] = lyric

        song_detail_list.append(song_detail_dict)
print(song_detail_list[:3]) #3개만 출력
print(len(song_detail_list)) #song_detail_list안의 곡수

#json 파일로 저장
with open('data/songs.json','w',encoding='utf-8') as file:
    json.dump(song_detail_list,file)


