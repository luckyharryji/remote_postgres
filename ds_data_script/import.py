import os
import csv
import psycopg2
from settings import db_settings as settings

with open('data_import.csv','rb') as f_in:
    reader = csv.reader(f_in)
    data = list(reader)
try:
    conn = psycopg2.connect(**settings)
    cursor=conn.cursor()
    for data_set in data:
        year=data_set[0]
        filed=data_set[1]
        total=data_set[2]
        civilian=data_set[3]
        military=data_set[4]
        not_reported=data_set[5]
        denied=data_set[6]
        insert_data=(year,filed,total,civilian,military,not_reported,denied)
        cursor.execute('INSERT INTO proposal (year,Field,Total,Civilian,Military,Not_reported,Denied) VALUES (%s, %s, %s,%s, %s, %s,%s)',insert_data)
        conn.commit()
except:
    print 'connect error'
# row_count=0
# for row in cursor:
#     row_count+=1
#     print "row:%s %s\n" % (row_count,row)
