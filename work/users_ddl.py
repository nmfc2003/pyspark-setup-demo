#!/usr/bin/python

import psycopg2

def create_source_tables():
    conn=psycopg2.connect("host=postgres port=5432 dbname=source user=postgres password=postgres1234")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name varchar(100), address varchar(100), user_uid varchar(100), cre_datetime timestamp)")
    conn.commit()
    conn.close()
    
def create_target_tables():
    conn=psycopg2.connect("host=postgres port=5432 dbname=target user=postgres password=postgres1234")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name varchar(100), address varchar(100), user_uid varchar(100), cre_datetime timestamp)")
    conn.commit()
    conn.close()

create_source_tables()
create_target_tables()