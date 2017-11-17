import unittest
from common import configDB
import readConfig as readConfig
import pymysql
import os

localReadConfig = readConfig.ReadConfig()
local_db = configDB.MyDB()
# romwe抽奖活动相关操作


class TestDB(unittest.TestCase):

    def setUp(self):
        self.select_member = None
        self.select_list = {}
        self.cursor = None
        host = localReadConfig.get_db("host")
        username = localReadConfig.get_db("username")
        password = localReadConfig.get_db("password")
        port = localReadConfig.get_db("port")
        database = localReadConfig.get_db("database")
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database
        }
        # execute jmeter case
        result = os.popen(r'E:\JMeter\apache-jmeter-3.0\apache-jmeter-3.0\bin\jmeter.bat -n -t F:\JMeterworkspace\romwe抽奖活动.jmx -l f:\result.jtl')
        print(result.read())
        # connect to DB
        self.db = pymysql.connect(**config)
        # create cursor
        self.cursor = self.db.cursor()
        if self.cursor:
            print("Connect DB successfully!")

    def testDB(self):
        mysql1 = """SELECT COUNT(activity_type) FROM rs_member_winner WHERE email='wangke@dotfashion.cn'"""
        mysql2 = """SELECT activity_type, COUNT(*) FROM rs_member_winner WHERE email='wangke@dotfashion.cn' GROUP BY activity_type"""
        file = "F:/result-app.txt"

        self.cursor.execute(mysql1)
        count_num = self.cursor.fetchall()
        for n in count_num:
            with open(file, "a") as f:
                f.write("****************RWM-APP****************\n抽奖总数：%d \n" % n[0])

        self.cursor.execute(mysql2)
        list = self.cursor.fetchall()
        self.num = 0
        # get result list
        for i in list:
            if i[0] < 6:
                self.num += i[1]
            with open(file, "a") as f:
                f.write("奖项：%d  出现次数：%d \n" % (i[0], i[1]))

        sumget = """SELECT COUNT(*) FROM rs_member_point_record WHERE member_id IN (SELECT member_id FROM rs_member WHERE email='wangke@dotfashion.cn')"""
        self.cursor.execute(sumget)
        a = self.cursor.fetchall()
        for i in a:
            print("查询到%d条积分中奖记录。" % i[0])
            print("计算到%d条积分中奖记录。" % self.num)
        coupon_num = """SELECT COUNT(*) FROM rs_coupon_email WHERE email = 'wangke@dotfashion.cn'"""
        self.cursor.execute(coupon_num)
        b = self.cursor.fetchall()
        for n in b:
            print("优惠券绑定记录%d条" % n[0])

    def tearDown(self):
        delsql = """DELETE FROM rs_member_winner WHERE email='wangke@dotfashion.cn'"""
        delsql2 = """DELETE FROM rs_member_point_record WHERE member_id IN (SELECT member_id FROM rs_member WHERE email='wangke@dotfashion.cn') AND last_update_time > '2017-11-07 00:00:00'"""
        delsql3 = """DELETE FROM rs_coupon_email WHERE email = 'wangke@dotfashion.cn'"""
        self.cursor.execute(delsql)
        self.db.commit()
        self.cursor.execute(delsql2)
        self.db.commit()
        self.cursor.execute(delsql3)
        self.db.commit()

        # close database
        self.db.close()
