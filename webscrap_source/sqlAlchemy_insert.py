### Songs100 테이블에 insert 하기
# sqlalchemy를 사용하여 레코드 insert 하기
# id ( PK 컬럼) 속성을 auto_increment 로 설정하기

import pymysql
import sqlalchemy

pymysql.install_as_MySQLdb()  #pymysql과 sqlAlchemy 연동
from sqlalchemy import create_engine
from sqlalchemy.sql import text

try:
    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+pymysql://python:python@localhost:3306/python_db',encoding='utf-8')
    with engine.connect() as conn:
        # auto_increment
        auto_inc_sql = text('''alter table songs100 modify id int auto_increment;''')
        conn.execute(auto_inc_sql)

        #insert
        values_tuple = ({'title':'집가고싶어','singer':'황재원','album':'sweet_home','likes':10000,'lyric':'아 집에 가고싶다~'},)
        insert_sql = text('''
        insert into songs100 (title,singer,album,likes,lyric) 
        values(:title,:singer,:album,:likes,:lyric)
        ''')
        for value in values_tuple:
            conn.execute(insert_sql,**value)  #dictTYpe

finally:
    conn.close()
    engine.dispose()