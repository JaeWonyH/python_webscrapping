# melon 100 chart
# 100곡의 노래의 제목과 songID 추출해서 list에 저장하기
# 100곡의 노래의 상세정보를 추출해서 list와 dict에 저장해서 json 파일로 저장하기
# json 파일을 load하여 Pandas의 DataFrame에 저장하기
# DataFrame 객체를 DB의 Table에 저장하기

import requests
from bs4 import BeautifulSoup
import re

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
            #print(song_id, song_title, song_detail_url)
            print(song_dict)
            song_list.append(song_dict)
    print(len(song_list))


