import pymysql

class dbConsult():
        def __init__(self, ip='', port='', user='', passw='', db='zabbix', Hid='1', Iid='1'):

                self.ip = ip
                self.user = user
                self.passw = passw
                self.db = db
                self.port = port
                self.Hid = Hid
                self.Iid = Iid

        def consult(self):

                #db = pymysql.connect(host='192.100.206.188', user='root', passwd='lockinet', db='zabbix', port=9699, connect_timeout=10)
                db = pymysql.connect(host=self.ip, user=self.user, passwd=self.passw, db=self.db, port=int(self.port), connect_timeout=10)
                consult = db.cursor()
                #print("SELECT `hosts`.`hostid`, `history_text`.`itemid`, `history_text`.`value`, `history_text`.`clock`  FROM `hosts`, `history_text` WHERE ((`hosts`.`hostid` = "+ str(self.Hid)+ ") AND (`history_text`.`itemid` = "+str(self.Iid)+"))")
                consult.execute("SELECT `hosts`.`hostid`, `history_text`.`itemid`, `history_text`.`value`, `history_text`.`clock`  FROM `hosts`, `history_text` WHERE ((`hosts`.`hostid` = "+self.Hid+") AND (`history_text`.`itemid` = "+self.Iid+"))")
                lista = list(consult)

                #for row in lista:
                consult.close()
                #print("db_consult retorno banco:", )
                return lista



