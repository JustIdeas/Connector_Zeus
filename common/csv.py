import csv
import sys
class CSV:

    def __init__(self, info=''):
        self.info = info


    def construct(self):
        list = {'Samsung Electronics Co.,Ltd': 14, 'Apple, Inc.': 10, 'Motorola Mobility LLC, a Lenovo Company': 4, 'LG Electronics (Mobile Communications)': 3, 'LG Electronics': 2, 'ASUSTek COMPUTER INC.': 1, 'Microsoft Corporation': 1, 'T&A Mobile Phones': 1}
        Lowner = []
        LValue = []
        for key, value in list.items():
            print(key, value)
            Lowner.append(key)
            LValue.append(value)

            zipList = zip(Lowner, LValue)
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