import pymysql


db = pymysql.connect(host='IP', user='root', passwd='pass', db='zabbix', port='PORT', connect_timeout=50)

consult = db.cursor()

consult.execute("SELECT `hosts`.`hostid`, `history_text`.`itemid`  FROM `hosts`, `history_text` WHERE ((`hosts`.`hostid` = 10172) AND (`history_text`.`itemid` = 34510))")
lista = list(consult)

for row in lista:
        print(row[1])

consult.close()
