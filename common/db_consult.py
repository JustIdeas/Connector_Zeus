import pymysql

from common import db_constructor

class dbConsult():
        def __init__(self, ip='', port='', user='', passw='', db='zabbix', Hid='1', Iid='1', ta=''):

                self.ip = ip
                self.user = user
                self.passw = passw
                self.db = db
                self.port = port
                self.Hid = Hid
                self.Iid = Iid
                self.ta = ta

        def consult(self):
                db = pymysql.connect(host=self.ip, user=self.user, passwd=self.passw, db=self.db, port=int(self.port), connect_timeout=10)
                consult = db.cursor()
                consult.execute(db_constructor.db_cons(self.ta, self.Hid, self.Iid).run())
                lista = list(consult)
                consult.close()
                return lista