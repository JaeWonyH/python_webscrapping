### 국회의원 현황정보 수집/분석/시각화/저장
# 국회의원의 이름, id추출
# 각 국회의원의 상세페이지 정보 추출 by id -> json 파일로 저장
# 상세정보들을 DataFrame으로 변환
# 시각화(막대그래프, 히스토그램, 파이차트, 히트맵)
# 테이블로 저장

import requests
from bs4 import BeautifulSoup
import re

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

