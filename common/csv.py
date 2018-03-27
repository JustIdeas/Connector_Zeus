import csv
import sys
class CSV:

    def __init__(self, info=''):
        self.info = info


    def construct(self):

        #print("info hostID:", row[0], "info itemID:", row[1], "info value:", row[2], "info Clock:", row[3])
        listI = self.info
        LHostId = []
        LItemId = []
        LValue = []
        LClock = []
        translateList = listI[2]
        print("LISTA: ",translateList)
        #for key, value in translateList.items():
            #LValue.append(value)
        for i in listI:
           # print(i[0], i[1], i[2], i[3])

            LHostId.append(i[0])
            LItemId.append(i[1])
            LClock.append(i[3])


            zipList = zip(LHostId, LItemId, LValue, LClock)
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