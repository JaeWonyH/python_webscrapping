import pandas as pd
import pymysql
import sqlalchemy

pymysql.install_as_MySQLdb()  #pymysql과 sqlAlchemy 연동
from sqlalchemy import create_engine

try:
    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+pymysql://python:python@localhost:3306/python_db',encoding='utf-8')
    conn = engine.connect()

    #song_df(DataFrame객체)를 songs100 테이블로 저장 : to_sql() 함수사용
    songs100_df = pd.read_sql_table('songs100',conn)
    print(songs100_df.shape)
finally:
    conn.close()
    engine.dispose()

def search_album(keyword):
    import pandas as pd
    import pymysql
    import sqlalchemy

    pymysql.install_as_MySQLdb()  # pymysql과 sqlAlchemy 연동
    from sqlalchemy import create_engine

    sql = """select * from songs100 where album like %s;"""

    try:
        # dialect+driver://username:password@host:port/database
        engine = create_engine('mysql+pymysql://python:python@localhost:3306/python_db', encoding='utf-8')
        conn = engine.connect()

        album_df = pd.read_sql_query(sql, con=conn, params=('%' + keyword + '%',))
        print(album_df.shape)
        return album_df
    finally:
        conn.close()
        engine.dispose()


print(search_album('ost'))





