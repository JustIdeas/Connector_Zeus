import requests
import json
import datetime

from common import url_constructor
headers = {}
class POST:
    def __init__(self, params='', ip='', port='',
                 user='', passw='', channel='', version='', interface=''):
        self.params = params
        self.ip = ip
        self.user = user
        self.passw = passw
        self.channel = channel
        self.port = port
        self.version = version
        self.interface = interface

    def login(self):
        payload = self.params
        post = requests.post(str(url_constructor.URLs(self.version, 'login', self.ip, self.port).Check_version()), data=json.dumps(payload), verify=False, headers=headers)

        if post.status_code == 200:
            token = json.loads(post.content.decode('utf-8'))['data']['Token']
            headers['Authorization'] = 'Bauer ' + token

        return True

    def GetClients(self):

        post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))

        if self.version == 'v1':
            if response['data']['clients'] == []:
                return(0)
            else:
                return(len(response['data']['clients']))
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

        post = requests.get(str(url_constructor.URLs(self.version, 'version', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
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
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0
        if self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise2Ghz', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0
        if self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise5Ghz', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            if response != None:
                size = len(response["data"])
                return size
            else:
                return 0

    def Getchannel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'statusWireless', self.ip, self.port).Check_version()),
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            return response['data']['channel']

        elif self.version == 'v3' and self.interface == '2Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            return response['data']['wireless']['radios'][0]['channel']

        elif self.version == 'v3' and self.interface == '5Ghz':
            post = requests.get(str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            return response['data']['wireless']['radios'][1]['channel']


    def GetNoise_ownChannel(self):
        Own_Channel = POST.Getchannel(self)
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
            post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
            post = requests.get(str(url_constructor.URLs(self.version, 'noise2Ghz', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
                headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            time = str(datetime.timedelta(seconds=(response["data"]["uptime"])))
            return time
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            time = str(datetime.timedelta(seconds=(response["data"]["device"]["uptime"])))
            return time

    def GetModel(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            model = str(response["data"]["model"])
            return model
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            model = str(response["data"]["device"]["model"])
            return model


    def GetAlias(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = str(response["data"]["alias"])
            return Alias
        if self.version == 'v3':
            post = requests.get(
                str(url_constructor.URLs(self.version, 'clients', self.ip, self.port).Check_version()),
                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = str(response["data"]["device"]["alias"])
            return Alias

    def GetHasUpdate(self):

        #all this function is not collecting the right data, instead of get the info
        #if the firmware is up to date, it's taking if the device has any configuration to be applied.
        #there is an way to do it, collecting data from cronos passing the URL from cronos. This will be done on next refactory.

        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'HasUpdate', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = bool(response["data"]["has_update"])
            #print(Alias)
            if Alias == False:
                Alias = "Produto na ultima versão de firmware"
            else:
                Alias = "Possui uma nova firmware para atualização"
            return Alias
        if self.version == 'v3':
            post = requests.get(str(url_constructor.URLs(self.version, 'HasUpdate', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = bool(response["data"]["has_update"])
            # print(Alias)
            if Alias == False:
                Alias = "Produto na ultima versão de firmware"
            else:
                Alias = "Possui uma nova firmware para atualização"
            return Alias


    def GetOpMode(self):
        if self.version == 'v1':
            post = requests.get(str(url_constructor.URLs(self.version, 'WanInfo', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
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
                                verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = str(response["data"]["device"]["network_mode"])
            if Alias == "router":
                Alias = "Roteador"
                return Alias
            elif Alias == "bridge":
                Alias = "Bridge"
                return Alias
            return Alias

    def GetThroughputEth0_Upload(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'throughputEth0', self.ip, self.port).Check_version()),
                            verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
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
                            verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
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
            verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
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
                            verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
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








