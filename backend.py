import mysql.connector
import pandas as pd
import test2
import classifier

def add_to_database(results,base_url):

    sql_list=[]

    for r in results:
        sql_list.append((r["name"],r['startDate'],r['endDate'],r['classification'],r['url'],))

    print(sql_list)

    print(sql_list[0])
    def new_list(id):
        new1_list=[]
        for x in sql_list:
            m=list(x)
            m.append(id)
            new1_list.append(tuple(m))
        print(new1_list[0])
        return new1_list

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Srsscthr#1",
        database="events"
    )


    cursor = mydb.cursor()

    #q1="create table interesting_urls (id int PRIMARY KEY AUTO_INCREMENT,url_name varchar(100))"
    #q2 ="create Table scraped (name varchar(100),startDate varchar(100), endDate varchar(100),classification varchar(5000),url varchar(2000),url_id int,FOREIGN KEY(url_id) REFERENCES interesting_urls(id))"





    website=[(base_url)]
    q3 =" insert into interesting_urls (url_name) values (%s)"
    cursor.execute(q3,website)
    last_id = cursor.lastrowid

    new1_list=new_list(last_id)

    q5 ="insert into scraped (name ,startDate , endDate ,classification ,url,url_id ) values (%s,%s,%s,%s,%s,%s)"
    cursor.executemany(q5,new1_list)

    mydb.commit()