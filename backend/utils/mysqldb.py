#coding=utf_8
import datetime
import pymysql.cursors
from Ultraman import settings
s=settings.DATABASES['default']

def update_task_status(test_result,_id):
    conn=pymysql.connect(s['HOST'],s['USER'],s["PASSWORD"],s["NAME"],cursorclass=pymysql.cursors.DictCursor)
    cur=conn.cursor()
    datetimenowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql="UPDATE crontab_cron SET test_result='%s',update_time='%s' WHERE id=%d"%(test_result,datetimenowTime,_id)
    try:
     cur.execute(sql)
     conn.commit()
     conn.close()
    except Exception as e:
     print (e)
     conn.close()
     conn.rollback()
def selectemail(pro_name):
    conn=pymysql.connect(s['HOST'],s['USER'],s["PASSWORD"],s["NAME"],cursorclass=pymysql.cursors.DictCursor)
    try:
        cur=conn.cursor()
        sql="select  * from project_project WHERE pro_name='%s'"%pro_name
        cur.execute(sql)
        results = cur.fetchall()

        conn.close()
        return results[0]
    except Exception as e:
        conn.close()
def selectprojectcount():
    conn=pymysql.connect(s['HOST'],s['USER'],s["PASSWORD"],s["NAME"],cursorclass=pymysql.cursors.DictCursor)
    try:
        cur=conn.cursor()
        sql="select * from project_project"
        cur.execute(sql)
        results = cur.fetchall()

        conn.close()
        return len(results)
    except Exception as e:
        conn.close()
def select_project():
    conn=pymysql.connect(s['HOST'],s['USER'],s["PASSWORD"],s["NAME"],cursorclass=pymysql.cursors.DictCursor)
    try:
        cur=conn.cursor()
        sql="select * from project_project"
        cur.execute(sql)
        results = cur.fetchall()
        l=[i['pro_name'] for i in results]
        conn.close()
        return l
    except Exception as e:
        conn.close()
def select_erp(sql):
    conn=pymysql.connect('10.185.240.86','3306_test','iS6CXpYqgZ8Mhjui','secooPisDB',cursorclass=pymysql.cursors.DictCursor)# 参数为ip，用户名，密码，数据库
    cur=conn.cursor()# 使用cursor()方法获取操作游标？什么叫游标
    cur.execute(sql)# 使用execute方法执行SQL语句
    data = cur.fetchall()#获取一条数据库。
    conn.close()
    return data

def upadate_erp(sql):
    conn=pymysql.connect('10.185.240.86','3306_test','iS6CXpYqgZ8Mhjui','secooPisDB',cursorclass=pymysql.cursors.DictCursor)# 参数为ip，用户名，密码，数据库
    cur=conn.cursor()# 使用cursor()方法获取操作游标？什么叫游标
    cur.execute(sql)# 使用execute方法执行SQL语句
    conn.commit()
    conn.close()

if __name__=="__main__":
    # update_task_status("pass",20)
    print(select_project())