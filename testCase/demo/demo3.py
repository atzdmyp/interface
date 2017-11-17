from common import common
import unittest
from common import configDB

local_db = configDB.MyDB()


class TestDB(unittest.TestCase):

    def setUp(self):
        self.select_member = None
        self.select_list = []
        self.cursor = None

    def testDB(self):
        mysql = "SELECT COUNT(activity_type) FROM `rs_member_winner` WHERE email='wangke@dotfashion.cn'"
        self.select_member = common.get_sql("newsitetest", "rs_member_wallet_bill", "select_member")
        self.cursor = local_db.executeSQL(self.select_member, '1933546')
        self.list = local_db.get_all(self.cursor)
        # get result list
        for l in self.list:
            self.select_list.append(l)
            print(l[2])
        print(self.select_list[4][8])

    def tearDown(self):
        # close database
        local_db.closeDB()
