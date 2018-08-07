import csv
import sys
import ast
import time
import re


class CSV:

    def __init__(self, info='', ip=''):
        self.info = info
        self.ip = ip
    def construct(self):

        def macheck(value=''):
            if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", value.lower()):
                return True
            else:
                return False

        try:

            listI = self.info

            LHostId = []
            LItemId = []
            LOwner = []
            LCBrand = []
            LVBrand = []
            LCMac = []
            LVMac = []
            LCInter = []
            LVInter = []
            LCPhyM = []
            LVPhyM = []
            LValue = []
            LClock = []

            for item in listI:

               if item[2] != "0" and item[2].find("Traceback") == -1 and ("'"+":") in item[2] and item[2].find("InsecureRequestWarning") == -1:

                   if item[2].find("Brand"):
                        ListFor = ast.literal_eval(item[2])
                        for i in range(len(ListFor)):
                            Dict = dict(ListFor[i])
                            for value, key in Dict.items():
                                if value == 'Brand':
                                    LVBrand.append(key)
                                elif value == 'Mac':
                                    LVMac.append(key)
                                elif value == 'PhyMode':
                                    LVPhyM.append(key)
                                elif value == 'Interface':
                                    LVInter.append(key)
                                LHostId.append(item[0])
                                LItemId.append(item[1])
                                LClock.append(item[4])
                   else:
                       DictI = ast.literal_eval("{" + item[2] + "}")
                       for value, key in DictI.items():
                           if macheck(value) == True:
                                LHostId.append(item[0])
                                LItemId.append(item[1])
                                LOwner.append(key)
                                LValue.append(value)
                                LClock.append(time.strftime("%D %H"+"h"+" %M", time.localtime(int(item[3]))))
                           else:
                                LHostId.append(item[0])
                                LItemId.append(item[1])
                                LOwner.append(value)
                                LValue.append(key)
                                LClock.append(time.strftime("%D %H" + "h" + " %M", time.localtime(int(item[4]))))
            if not LVBrand:
                zipList = zip(LHostId, LItemId, LOwner , LClock, LValue)
                columns = ("HostID", "ItemID", "Fabricantes", "Qtd", "Data")
                if columns is None:
                    return "Empty Columns"
                with open(self.ip+'.result.csv', 'w') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', lineterminator='\n')
                    writer.writerow(columns)
                    for row in zipList:
                        writer.writerow(row)
                return 'Excel file created'
            else:
                zipList = zip(LHostId, LItemId, LVBrand, LVMac, LVInter, LVPhyM, LClock)
                columns = ("HostID", "ItemID", "Brand", "MAC", "Interface", "PhyMode", "Data")
                if columns is None:
                    return "Empty Columns"
                with open(self.ip + '.result.csv', 'w') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', lineterminator='\n')
                    writer.writerow(columns)
                    for row in zipList:
                        writer.writerow(row)
                return 'Excel file created'

        except:
             print('error', sys.exc_info()[0], sys.exc_info()[1])





