### 국회의원 현황정보 수집/분석/시각화/저장
# 국회의원의 이름, id추출
# 각 국회의원의 상세페이지 정보 추출 by id -> json 파일로 저장
# 상세정보들을 DataFrame으로 변환
# 시각화(막대그래프, 히스토그램, 파이차트, 히트맵)
# 테이블로 저장

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

url = "https://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do"
req_param_dict ={
    'currentPage':1,
    'rowPerPage':500
}
res = requests.get(url,params=req_param_dict)

if res.ok :
    soup = BeautifulSoup(res.text, 'html.parser') #페이지 소스보기
    atag_list = soup.select('div.memberna_list dl dt a')
    member_id_list = [] #국회의원 id 번호 list
    for atag in atag_list:
        href = atag['href']
        matched = re.search(r'(\d+)',href) #국회의원 id 추출
        if matched:
            member_id = matched.group(1)
        member_id_list.append(member_id) #국회의원 id append

member_detail_list = []
for idx, mem_id in enumerate(member_id_list[:5],1):
    detail_url = f'https://www.assembly.go.kr/assm/memPop/memPopup.do?dept_cd={mem_id}' #상세정보 url
    res = requests.get(detail_url)
    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')

        #1명의 정보를 저장할 dict 선언
        member_detail_dict = {}

        dt_list = [dt_tag.text for dt_tag in soup.select('dl.pro_detail dt')]
        dd_list = []
        for dd_tag in soup.select('dl.pro_detail dd'):
            pattern = re.compile(f'[\n\r\t]') #특수문자 패턴
            dd_text = pattern.sub('',dd_tag.text.strip()).replace(' ','') #dd_tag의 특수문자 empty string으로변환
            dd_list.append(dd_text)
        print(dd_list)




