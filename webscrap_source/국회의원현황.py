### 국회의원 현황정보 수집/분석/시각화/저장
# 국회의원의 이름, id추출
# 각 국회의원의 상세페이지 정보 추출 by id -> json 파일로 저장
# 상세정보들을 DataFrame으로 변환
# 시각화(막대그래프, 히스토그램, 파이차트, 히트맵)
# 테이블로 저장

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=500"