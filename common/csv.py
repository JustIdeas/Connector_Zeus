import csv
import sys
import ast
import time

class CSV:

    def __init__(self, info=''):
        self.info = info


    def construct(self):

        #print("info hostID:", row[0], "info itemID:", row[1], "info value:", row[2], "info Clock:", row[3])
        listI = self.info
        #print (listI)
        LHostId = []
        LItemId = []
        LOwner = []
        LValue = []
        LClock = []




        for item in listI:
           #print (item[2])

           if item[2] != "0" and item[2].find("Traceback") == -1:
                DictI = ast.literal_eval("{" + item[2] + "}")
                for value, key in DictI.items():
                    print("Owner:", value, "Value", key)

                    LHostId.append(item[0])
                    LItemId.append(item[1])
                    LOwner.append(value)
                    LValue.append(key)
                    LClock.append(time.strftime("%D %H:%M", time.localtime(int(item[3]))))


        zipList = zip(LHostId, LItemId, LOwner , LValue, LClock)
        try:
            with open('names.csv', 'w') as csvfile:

                writer = csv.writer(csvfile, delimiter=';', lineterminator='\n')

                for row in zipList:
                    #print(Lowner, LValue)
                    writer.writerow(row)
                # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
                # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

        except:
            print('error', sys.exc_info()[0], sys.exc_info()[1])