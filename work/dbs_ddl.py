#!/usr/bin/python

import psycopg2

def create_dbs():
    
    conn=psycopg2.connect("host=postgres port=5432 dbname=demo user=postgres password=postgres1234")
    conn.autocommit = True
    cur=conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS source")
    cur.execute("CREATE DATABASE source")
    cur.execute("DROP DATABASE IF EXISTS target")
    cur.execute("CREATE DATABASE target")
    conn.close()

create_dbs()
