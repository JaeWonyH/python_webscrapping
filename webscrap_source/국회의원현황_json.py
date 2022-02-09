# json 파일로 저장
import json

from webscrap_source.국회의원현황 import member_detail_list

with open('data/member.json','w') as file:
    json.dump(member_detail_list,file)
