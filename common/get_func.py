import requests
import json
import datetime
import socket
import sys
import ast
import urllib3
from collections import defaultdict

from common import url_constructor
from common import Getvendor
from collections import Counter
from common import csv
from common import db_consult
from common import csv
from common import db_constructor

headers = {}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class POST:
    def __init__(self, params='', ip='', port='',
                 user='', passw='', channel='', version='', interface='', sock='9090', db='zabbix', Hid='1', Iid='1', ta=''):
        self.params = params
        self.ip = ip
        self.user = user
        self.passw = passw
        self.channel = channel
        self.port = port
        self.version = version
        self.interface = interface
        self.socket = sock
        self.db = db
        self.Hid = Hid
        self.Iid = Iid
        self.ta = ta

    def login(self):
        try:
            payload = self.params
            post = requests.post(str(url_constructor.URLs(self.version, 'login', self.ip, self.port).Check_version()), data=json.dumps(payload), verify=False, headers=headers, timeout=30)
            
            if post.status_code == 200:
                token = json.loads(post.content.decode('utf-8', errors='ignore'))['data']['Token']
                headers['Authorization'] = 'Bauer ' + token
            return True
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectTimeout) as e:
            return 0

    def GetClientsMac(self,sepVendor=0):
        self.sepVendor = sepVendor
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            vendorinfo = []
            MacsInfo = []
            if response['data']['clients'] == []:
                return (0)
            else:
                clients_count = (len(response['data']['clients']))
                for i in range(clients_count):
                    if self.sepVendor == 2:
                        if response['data']['clients'][i]['interface'] == 'wireless':
                            Macs = response['data']['clients'][i]['mac_address']
                            vendorinfo.append(Getvendor.Vendor(Macs).run())
                            MacsInfo.append(Macs)
                    else:
                        if response['data']['clients'][i]['interface'] == 'wireless':
                            Macs = response['data']['clients'][i]['mac_address']
                            vendorinfo.append(Getvendor.Vendor(Macs).run())
                if len(vendorinfo) == 0:
                    return 0
                if self.sepVendor == 1:
                    if len(vendorinfo) == 0:
                        return 0
                    return vendorinfo
                if self.sepVendor == 2:
                    if len(vendorinfo) == 0:
                        return 0
                    #print (vendorinfo, MacsInfo, "Befor ZIP")

                    resulting = zip(MacsInfo, vendorinfo)
                    return  str(dict(resulting)).strip('{').strip('}')

                result = Counter(vendorinfo)
                return str(result).strip('Counter').strip('(').strip(')').strip('{').strip('}')

        if self.version == 'v3':


            vendorinfo = []
            MacsInfo = []

            if self.interface == '2Ghz':
                post = requests.get(
                    str(url_constructor.URLs(self.version, 'clientsmac2Ghz', self.ip, self.port).Check_version()),
                    verify=False, headers=headers, timeout=60)
                response = json.loads(post.content.decode('utf-8', errors='ignore'))

                if response['data']['clients'] == 0:
                    return (0)
                else:
                    clients_count = (len(response['data']['clients']))

                    for i in range(clients_count):
                        if self.sepVendor == 2:
                            if response['data']['clients'][i]['interface'] == 'wireless':
                                Macs = response['data']['clients'][i]['mac_address']
                                vendorinfo.append(Getvendor.Vendor(Macs).run())
                                MacsInfo.append(Macs)
                        else:
                            if response['data']['clients'][i]['interface'] == 'wireless':
                                Macs = response['data']['clients'][i]['mac_address']
                                vendorinfo.append(Getvendor.Vendor(Macs).run())
                    if len(vendorinfo) == 0:
                        return 0
                    if self.sepVendor == 1:
                        if len(vendorinfo) == 0:
                            return 0
                        return vendorinfo
                    if self.sepVendor == 2:
                        if len(vendorinfo) == 0:
                            return 0
                        # print (vendorinfo, MacsInfo, "Befor ZIP")

                        resulting = zip(MacsInfo, vendorinfo)
                        return str(dict(resulting)).strip('{').strip('}')

                    result = Counter(vendorinfo)
                    return str(result).strip('Counter').strip('(').strip(')').strip('{').strip('}')
            if self.interface == '5Ghz':
                post = requests.get(str(url_constructor.URLs(self.version, 'clientsmac5Ghz', self.ip, self.port).Check_version()),
                        verify=False, headers=headers, timeout=30)

                response = json.loads(post.content.decode('utf-8', errors='ignore'))
                if response['data']['clients'] == 0:
                        return (0)
                else:
                    clients_count = (len(response['data']['clients']))
                    for i in range(clients_count):
                        if self.sepVendor == 2:
                            if response['data']['clients'][i]['interface'] == 'wireless':
                                Macs = response['data']['clients'][i]['mac_address']
                                vendorinfo.append(Getvendor.Vendor(Macs).run())
                                MacsInfo.append(Macs)
                        else:
                            if response['data']['clients'][i]['interface'] == 'wireless':
                                Macs = response['data']['clients'][i]['mac_address']
                                vendorinfo.append(Getvendor.Vendor(Macs).run())
                    if len(vendorinfo) == 0:
                        return 0
                    if self.sepVendor == 1:
                        if len(vendorinfo) == 0:
                            return 0
                        return vendorinfo
                    if self.sepVendor == 2:
                        if len(vendorinfo) == 0:
                            return 0
                        # print (vendorinfo, MacsInfo, "Befor ZIP")

                        resulting = zip(MacsInfo, vendorinfo)
                        return str(dict(resulting)).strip('{').strip('}')

                    result = Counter(vendorinfo)
                    return str(result).strip('Counter').strip('(').strip(')').strip('{').strip('}')


    def GetCountVendorsMac(self):
        count = POST.GetClientsMac(self, 1)
        if count == 0:
            return 0
        count = len(list(set(count)))
        return count

    def GetVendorAndMac(self):
        Return = POST.GetClientsMac(self, 2)
        if Return == 0:
            return 0
        return Return


    def GetClients(self):

        post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        count = 0
        if self.version == 'v1':
            if response['data']['clients'] == []:
                return(0)
            else:
                clients_count = (len(response['data']['clients']))
                for i in range(clients_count):
                    if response['data']['clients'][i]['interface'] == 'wireless':
                        count = count + 1

                return count
        elif self.version == 'v3' and self.interface == '2Ghz':
            if response['data']['wireless']['radios'][0]['connected_clients'] == 0:
                return 0
            else:
                return response['data']['wireless']['radios'][0]['connected_clients']
        elif self.version == 'v3' and self.interface == '5Ghz':
            if response['data']['wireless']['radios'][1]['connected_clients'] == 0:
                return(0)
            else:
                return(response['data']['wireless']['radios'][1]['connected_clients'])


    def GetVersion(self):

        post = requests.get(str(url_constructor.URLs(self.version, 'version', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        if self.version == 'v1':
            if response["data"]["version"] == []:
                return 0
            else:
                return response["data"]["version"]
        elif self.version == 'v3':
            if response["data"]["version"] == []:
                return 0
            else:
                return response["data"]["version"]


    def GetNoise(self):

        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])

                sum = 0
                for i in range(size):
                    signal = response["data"][i]["signal"]
                    sum = sum - signal

                average = sum / size
                return round(average, 2)
            else:
                return 0

        if self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise2Ghz', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])

                sum = 0
                for i in range(size):
                    signal = response["data"][i]["signal"]
                    sum = sum - signal

                average = sum / size
                return round(average, 2)
            else:
                return 0

        if self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise5Ghz', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])

                sum = 0
                for i in range(size):
                    signal = response["data"][i]["signal"]
                    sum = sum - signal

                average = sum / size
                return round(average, 2)
            else:
                return 0

    def GetNoise_channelCount(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0
        if self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise2Ghz', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0
        if self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise5Ghz', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0

    def Getchannel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'statusWireless', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            return response['data']['channel']

        elif self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            return response['data']['wireless']['radios'][1]['channel']

        elif self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            return response['data']['wireless']['radios'][0]['channel']


    def GetNoise_ownChannel(self):
        Own_Channel = POST.Getchannel(self)
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                sum = 0
                count = 0
                average = 0
                for i in range(size):
                    get = response["data"][i]["signal"], response["data"][i]["channel"] == Own_Channel
                    if (get[1] == True):
                        signal = get[0]
                        count = count + int(1)
                        sum = sum - signal
                if count >= 1:
                    average = sum / count
                return round(average,2)
            else:
                return 0

        elif self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise2Ghz', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                sum = 0
                count = 0
                average = 0
                for i in range(size):
                    get = response["data"][i]["signal"], response["data"][i]["channel"] == Own_Channel
                    if (get[1] == True):
                        signal = get[0]
                        count = count + int(1)
                        sum = sum - signal
                if count >= 1:
                    average = sum / count
                return round(average, 2)
            else:
                return 0

        elif self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'noise5Ghz', self.ip, self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                sum = 0
                count = 0
                average = 0
                for i in range(size):

                    get = response["data"][i]["signal"], response["data"][i]["channel"] == Own_Channel
                    if (get[1] == True):
                        signal = get[0]
                        count = count + int(1)
                        sum = sum - signal
                if count >= 1:
                    average = sum / count
                return round(average, 2)
            else:
                return 0





    def GetNoise_byChannel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                sum = 0
                count=0
                average=0
                for i in range(size):
                    get = response["data"][i]["signal"], response["data"][i]["channel"] == int(self.channel)
                    if (get[1] == True):
                        signal = get[0]
                        count = count + int(1)
                        sum = sum - signal
                if count >=1:
                    average = sum / count
                return round(average,2)
            else:
                return 0

        elif self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise2Ghz', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                sum = 0
                count=0
                average=0
                for i in range(size):
                    get = response["data"][i]["signal"], response["data"][i]["channel"] == int(self.channel)
                    if (get[1] == True):
                        signal = get[0]
                        count = count + int(1)
                        sum = sum - signal
                if count >=1:
                    average = sum / count
                return round(average,2)
            else:
                return 0
        elif self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'noise5Ghz', self.ip, self.port).Check_version()), verify=False,
                headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                sum = 0
                count = 0
                average = 0
                for i in range(size):
                    get = response["data"][i]["signal"], response["data"][i]["channel"] == int(self.channel)
                    if (get[1] == True):
                        signal = get[0]
                        count = count + int(1)
                        sum = sum - signal
                if count >= 1:
                    average = sum / count
                return round(average, 2)
            else:
                return 0


    def GetUptime(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            time = str(datetime.timedelta(seconds=(response["data"]["uptime"])))
            return time
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            time = str(datetime.timedelta(seconds=(response["data"]["device"]["uptime"])))
            return time

    def GetModel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            model = str(response["data"]["model"])
            return model
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            model = str(response["data"]["device"]["model"])
            return model

    def GetAlias(self):
        if self.version == 'v1':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = str(response["data"]["alias"])
            return Alias
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = str(response["data"]["device"]["alias"])

        return Alias

    def GetHasUpdate(self):

        #all this function is not collecting the right data, instead of get the info
        #if the firmware is up to date, it's taking if the device has any configuration to be applied.
        #there is an way to do it, collecting data from cronos passing the URL from cronos. This will be done on next refactory.

        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'HasUpdate', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = bool(response["data"]["has_update"])
            #print(Alias)
            if Alias == False:
                Alias = "Produto na ultima versão de firmware"
            else:
                Alias = "Possui uma nova firmware para atualização"
            return Alias
        if self.version == 'v3':
            post = requests.get(str(url_constructor.URLs(self.version, 'HasUpdate', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = bool(response["data"]["has_update"])
            # print(Alias)
            if Alias == False:
                Alias = "Produto na ultima versão de firmware"
            else:
                Alias = "Possui uma nova firmware para atualização"
            return Alias


    def GetOpMode(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'WanInfo', self.ip, self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = str(response["data"]["opmode"])
            if Alias == "router":
                Alias = "Roteador"
                return Alias
            elif Alias == "bridge":
                Alias = "Bridge"
                return Alias
            return Alias
        if self.version == 'v3':
            post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = str(response["data"]["wan"]["ipv4"]["opmode"])
            if Alias == "router":
                Alias = "Roteador"
                return Alias
            elif Alias == "bridge":
                Alias = "Bridge"
                return Alias
            return Alias

    def GetThroughputEth0_Upload(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'throughputEth0', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result=0
        if response != None:
            size = len(response["data"])
            for i in range(size):
                value = response["data"][i]["throughput"]["tx"]
                result = result + int(value)
            if result == 0:
                return 0
            else:
                result = round(result/size/1000/1000,3)
                return result

    def GetThroughputEth0_Download(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'throughputEth0', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result=0
        if response != None:
            size = len(response["data"])
            for i in range(size):
                value = response["data"][i]["throughput"]["rx"]
                result = result + int(value)
            if result == 0:
                return 0
            else:
                result = round(result/size/1000/1000,3)
                return result

    def GetThroughputWlan0_Upload(self):
        post = requests.get(
            str(url_constructor.URLs(self.version, 'throughputWlan0', self.ip, self.port).Check_version()),
            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = 0
        if response != None:
            size = len(response["data"])
            for i in range(size):
                value = response["data"][i]["throughput"]["tx"]
                result = result + int(value)
            if result == 0:
                return 0
            else:
                result = round(result / size / 1000 / 1000, 3)
                return result

    def GetThroughputWlan0_Download(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'throughputWlan0', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result=0
        if response != None:
            size = len(response["data"])
            for i in range(size):
                value = response["data"][i]["throughput"]["rx"]
                result = result + int(value)
            if result == 0:
                return 0
            else:
                result = round(result/size/1000/1000,3)
                return result

    def SocketTest(self):

        try:
            init = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            init.settimeout(5)
            init.connect((self.ip, int(self.socket)))
            # init.timeout(3)
            init.shutdown(2)
            return 1

        except socket.error as e:
            return 0
            #print("Something went wrong inside of Socket_test module:", sys.exc_info()[0], sys.exc_info()[1])

    def ConsultDb(self):
        infoDB = db_consult.dbConsult(self.ip, self.port, self.user, self.passw, self.db, self.Hid, self.Iid, self.ta).consult()
        result = csv.CSV(infoDB, self.ip).construct()

        return result

    def Wisecorporate(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["corporate"]
        return result

    def Wiseguests(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["guest"]
        return result

    def WiseAphealthok(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'aphealth', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["noProblem"]
        return result

    def WiseAphealthnok(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'aphealth', self.ip, self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["problem"]
        return result



