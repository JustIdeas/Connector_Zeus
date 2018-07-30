
class db_cons():

    def __init__(self, ta='', Hid='1', Iid='1'):

        self.ta = ta
        self.Hid = Hid
        self.Iid = Iid




    def run(self):

        db = {
            'history_text': 'SELECT `hosts`.`hostid`, `'+self.ta+'`.`itemid`, `'+self.ta+'`.`value`, `'+self.ta+'`.`clock`, FROM_UNIXTIME(clock) FROM `hosts`, `'+self.ta+'` WHERE ((`hosts`.`hostid` = "'+self.Hid+'") AND (`'+self.ta+'`.`itemid` = "'+self.Iid+'"))',

        }
        return db[self.ta]