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
from Tanaza_modules import interaction_module as tanaza
headers = {}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class POST:
    def __init__(self, params='', ip='', port='',
                 user='', passw='', channel='',
                 version='', interface='', sock='9090',
                 db='zabbix', Hid='1', Iid='1',
                 ta='', ssid="", network="", device="", proto='https'):
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
        self.ssid = ssid
        self.network = network
        self.device = device
        self.proto = proto

    def login(self):
        try:
            payload = self.params
            post = requests.post(str(url_constructor.URLs(proto=self.proto,version=self.version, info='login', ip=self.ip, port=self.port).Check_version()), data=json.dumps(payload), verify=False, headers=headers, timeout=30)
            
            if post.status_code == 200:
                token = json.loads(post.content.decode('utf-8', errors='ignore'))['data']['Token']
                headers['Authorization'] = 'Bauer ' + token
            return True
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectTimeout) as e:
            return 0

    def GetClientsMac(self,sepVendor=0):
        self.sepVendor = sepVendor
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
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
            Phymode = []
            Combined2G = []
            Combined5G = []
            Combined = []

            if self.interface == '2Ghz':
                post = requests.get(
                    str(url_constructor.URLs(proto=self.proto,version=self.version, info='clientsmac2Ghz', ip=self.ip, port=self.port).Check_version()),
                    verify=False, headers=headers, timeout=60)
                response = json.loads(post.content.decode('utf-8', errors='ignore'))

                if response['data']['clients'] == 0:
                    return (0)
                else:
                    clients_count = (len(response['data']['clients']))
                    print("TOTAL CLIENTES 2GHZ",clients_count)
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
                post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clientsmac5Ghz', ip=self.ip, port=self.port).Check_version()),
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
            if self.interface == 'Both':
                post2ghz = requests.get(
                    str(url_constructor.URLs(proto=self.proto,version=self.version, info='clientsmac2Ghz', ip=self.ip, port=self.port).Check_version()),
                    verify=False, headers=headers, timeout=60)
                post5ghz = requests.get(
                    str(url_constructor.URLs(proto=self.proto,version=self.version, info='clientsmac5Ghz', ip=self.ip, port=self.port).Check_version()),
                    verify=False, headers=headers, timeout=60)

                response2g = json.loads(post2ghz.content.decode('utf-8', errors='ignore'))
                response5g = json.loads(post5ghz.content.decode('utf-8', errors='ignore'))

                if response2g['data']['clients'] == 0:
                    return (0)
                else:
                    clients_count = (len(response2g['data']['clients']))
                    for i in range(clients_count):
                        if self.sepVendor == 2:
                            if response2g['data']['clients'][i]['interface'] == 'wireless':
                                mode = response2g['data']['clients'][i]['phymode']
                                Macs = response2g['data']['clients'][i]['mac_address']
                                phyrate = {"Rx": response2g['data']['clients'][i]['rxrate']/1000, "Tx": response2g['data']['clients'][i]['txrate']/1000}
                                uptime = response2g['data']['clients'][i]['uptime']
                                Combined2G.extend([({'Brand': Getvendor.Vendor(Macs).run(), 'Mac': Macs, "TIme Connected": uptime, 'PhyMode': mode, 'Interface': '2ghz', "PhyRate": phyrate})])
                        else:
                            if response2g['data']['clients'][i]['interface'] == 'wireless':
                                Macs = response2g['data']['clients'][i]['mac_address']
                                vendorinfo.append(Getvendor.Vendor(Macs).run())
                    if self.sepVendor == 2:
                        if len(Combined2G) == 0:
                            return 0
                    if self.sepVendor == 1:
                        if len(vendorinfo) == 0:
                            return 0
                        return vendorinfo

                if response5g['data']['clients'] == 0:
                    return (0)
                else:
                    clients_count = (len(response5g['data']['clients']))
                    for i in range(clients_count):
                        if self.sepVendor == 2:
                            if response5g['data']['clients'][i]['interface'] == 'wireless':
                                mode = response5g['data']['clients'][i]['phymode']
                                Macs = response5g['data']['clients'][i]['mac_address']
                                phyrate = {"Rx": response5g['data']['clients'][i]['rxrate']/1000,
                                           "Tx": response5g['data']['clients'][i]['txrate']/1000}
                                uptime = response5g['data']['clients'][i]['uptime']
                                Combined5G.extend([({'Brand': Getvendor.Vendor(Macs).run(), 'Mac': Macs, "TIme Connected": uptime, 'PhyMode': mode, 'Interface': '5ghz', "PhyRate": phyrate})])

                        else:
                            if response5g['data']['clients'][i]['interface'] == 'wireless':
                                Macs = response5g['data']['clients'][i]['mac_address']
                                vendorinfo.append(Getvendor.Vendor(Macs).run())

                    if self.sepVendor == 1:
                        if len(vendorinfo) == 0:
                            return 0
                        return vendorinfo
                    if self.sepVendor == 2:
                        if not len(Combined2G) and len(Combined5G):
                            return 0
                        Combined.extend(Combined2G)
                        Combined.extend(Combined5G)
                        return Combined
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

        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),verify=False, headers=headers, timeout=30)
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
            if response['data']['wireless']['radios'][1]['connected_clients'] == 0:
                return 0
            else:
                return response['data']['wireless']['radios'][1]['connected_clients']
        elif self.version == 'v3' and self.interface == '5Ghz':
            if response['data']['wireless']['radios'][0]['connected_clients'] == 0:
                return(0)
            else:
                return(response['data']['wireless']['radios'][0]['connected_clients'])
        elif self.version == 'v3' and self.interface == 'Both':
            if response['data']['wireless']['radios'][0]['connected_clients'] and response['data']['wireless']['radios'][1]['connected_clients'] == 0:
                return(0)
            else:
                Combined = (int(response['data']['wireless']['radios'][0]['connected_clients']) + int(response['data']['wireless']['radios'][1]['connected_clients']))
                return(Combined)


    def GetVersion(self):

        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='version', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise2Ghz', ip=self.ip, port=self.port).Check_version()),
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise5Ghz', ip=self.ip, port=self.port).Check_version()),
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0
        if self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise2Ghz', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0
        if self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise5Ghz', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0

    def Getchannel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='statusWireless', ip=self.ip, port=self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            return response['data']['channel']

        elif self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            return response['data']['wireless']['radios'][1]['channel']

        elif self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            return response['data']['wireless']['radios'][0]['channel']


    def GetNoise_ownChannel(self):
        Own_Channel = POST.Getchannel(self)
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise2Ghz', ip=self.ip, port=self.port).Check_version()),
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
                str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise5Ghz', ip=self.ip, port=self.port).Check_version()),
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise2Ghz', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
                str(url_constructor.URLs(proto=self.proto,version=self.version, info='noise5Ghz', ip=self.ip, port=self.port).Check_version()), verify=False,
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='statusSystem', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            time = str(datetime.timedelta(seconds=(response["data"]["uptime"])))
            return time
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            time = str(datetime.timedelta(seconds=(response["data"]["device"]["uptime"])))
            return time

    def GetModel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='statusSystem', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            model = str(response["data"]["model"])
            return model
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            model = str(response["data"]["device"]["model"])
            return model

    def GetAlias(self):
        if self.version == 'v1':
            post = requests.get(
                str(url_constructor.URLs(proto=self.proto,version=self.version, info='statusSystem', ip=self.ip, port=self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = str(response["data"]["alias"])
            return Alias
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = str(response["data"]["device"]["alias"])

        return Alias

    def GetHasUpdate(self):

        #all this function is not collecting the right data, instead of get the info
        #if the firmware is up to date, it's taking if the device has any configuration to be applied.
        #there is an way to do it, collecting data from cronos passing the URL from cronos. This will be done on next refactory.

        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='HasUpdate', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
            response = json.loads(post.content.decode('utf-8', errors='ignore'))
            Alias = bool(response["data"]["has_update"])
            #print(Alias)
            if Alias == False:
                Alias = "Produto na ultima versão de firmware"
            else:
                Alias = "Possui uma nova firmware para atualização"
            return Alias
        if self.version == 'v3':
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='HasUpdate', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='WanInfo', ip=self.ip, port=self.port).Check_version()), verify=False, headers=headers, timeout=30)
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
            post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
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
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='throughputEth0', ip=self.ip, port=self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result=0
        if response != None:
            if "eth0" in response["data"]:
                value = response["data"]["eth0"]["throughput"]["tx"]
                result = int(value)
                if result == 0:
                    return 0
                else:
                    result = round(result/1000/1000,3)
                    return result
            elif "eth1" in response["data"]:
                value = response["data"]["eth1"]["throughput"]["tx"]
                result = int(value)
                if result == 0:
                    return 0
                else:
                    result = round(result/1000/1000,3)
                    return result

    def GetThroughputEth0_Download(self):
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='throughputEth0', ip=self.ip, port=self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result=0
        if response != None:
            if "eth0" in response["data"]:
                value = response["data"]["eth0"]["throughput"]["rx"]
                result = int(value)
                if result == 0:
                    return 0
                else:
                    result = round(result / 1000 / 1000, 3)
                    return result
            elif "eth1" in response["data"]:
                value = response["data"]["eth1"]["throughput"]["rx"]
                result = int(value)
                if result == 0:
                    return 0
                else:
                    result = round(result / 1000 / 1000, 3)
                    return result

    def GetThroughputWlan0_Upload(self):
        post = requests.get(
            str(url_constructor.URLs(proto=self.proto,version=self.version, info='throughputWlan0', ip=self.ip, port=self.port).Check_version()),
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
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='throughputWlan0', ip=self.ip, port=self.port).Check_version()),
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
    def Get_signal_sta(self):
        post = requests.get(str(url_constructor.URLs(proto=self.proto,
                                                     version=self.version,
                                                     info='signal_client_sta',
                                                     ip=self.ip,
                                                     port=self.port).Check_version()),
                                                    verify=False, headers=headers, timeout=30)

        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        if response != None:
            response = response['data']
            signal = -1*response['signal']
            return signal

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
        infoDB = db_consult.dbConsult(self.ip, port=self.port, user=self.user, passw=self.passw, db=self.db, Hid=self.Hid, Iid=self.Iid, ta=self.ta).consult()
        result = csv.CSV(infoDB, ip=self.ip).construct()

        return result

    def Wisecorporate(self):
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["corporate"]
        return result

    def Wiseguests(self):
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='clients', ip=self.ip, port=self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["guest"]
        return result

    def WiseAphealthok(self):
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='aphealth', ip=self.ip, port=self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["noProblem"]
        return result

    def WiseAphealthnok(self):
        post = requests.get(str(url_constructor.URLs(proto=self.proto,version=self.version, info='aphealth', ip=self.ip, port=self.port).Check_version()),
                            verify=False, headers=headers, timeout=30)
        response = json.loads(post.content.decode('utf-8', errors='ignore'))
        result = response["data"]["problem"]
        return result

    def TanazaGetClients_byfrequency(self):
        result = tanaza.interact(ip=self.ip, username=self.user, password=self.passw, interface=self.interface).run()
        return result

    def TanazaGetClients_API(self):
        result = tanaza.interact(username=self.user, password=self.passw, ssid=self.ssid, network=self.network, device=self.device).API_get_clients()
        return result

    def TanazaGetUptime_API(self):
        result = tanaza.interact(username=self.user, password=self.passw, ssid=self.ssid, network=self.network, device=self.device).API_get_uptime()
        return result



