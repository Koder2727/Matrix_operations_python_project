# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:23:45 2021

@author: kunal
"""

""" This file is for handling of the database related operations"""

import sqlite3

conn = sqlite3.connect('tracker_data.db')
c = conn.cursor()

#create the tables in the database
if __name__ == '__main__':
    c.execute(''' Create table data 
                  ([generated_id] INTEGER PRIMARY KEY , [college_study] INTEGER , 
                   [Coding] INTEGER , [Gaming] INTEGER , [Reading] INTEGER ,
                   [Innovation] INTEGER )''')    
    conn.commit()


def Update_values(l):
    conn.execute('''Insert into data (college_study , Coding , Gaming , Reading , Innovation)
                     VALUES (? , ? , ? , ? , ?)''' , (int(l[0]) , int(l[1]) , int(l[2]) , int(l[3]) , int(l[4])))

    conn.commit()

def Get_last_7_values():
    cursor = c.execute(''' select * from data order by generated_id desc limit 7''')
    rows = cursor.fetchall()
    print(rows)
    return rows


