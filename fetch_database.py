import os
import pymysql.cursors

def fetch_data(context, event):
    try:
       connection = pymysql.connect(host=os.environ["LOCALHOST"],
                                 database=os.environ["DATABASE"],
                                 user=os.environ["USER"],
                                 password=os.environ["PASSWORD"],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
       query = "select * from {}".format(os.environ["TABLE"])
       cursor = connection .cursor()
       cursor.execute(query)
       records = cursor.fetchall()
       print(records)

    except Error as e :
        print ("Error while connecting to Database", e)
    finally:
        connection.close()
