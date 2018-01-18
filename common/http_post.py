import requests
import json
import datetime

from common import url_constructor
headers = {}
class POST:
    def __init__(self, params='', ip='', port='',
                 user='', passw='', channel='', version=''):
        self.params = params
        self.ip = ip
        self.user = user
        self.passw = passw
        self.channel = channel
        self.port = port
        self.version = version

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
        return response

    def GetVersion(self):

        post = requests.get(str(url_constructor.URLs(self.version, 'version', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
        return response

    def GetNoise(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
        size = len(response["data"])
        sum=0
        for i in range(size):
            signal = response["data"][i]["signal"]
            sum = sum - signal

        average = sum/size
        return round(average,2)

    def GetNoise_channelCount(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
        size = len(response["data"])
        return size

    def Getchannel(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'statusWireless', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
        return int(response['data']['channel'])

    def GetNoise_ownChannel(self):
        Own_Channel = POST.Getchannel(self)
        post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
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



    def GetNoise_byChannel(self):
        post = requests.get(str(url_constructor.URLs(self.version, 'noise', self.ip, self.port).Check_version()), verify=False, headers=headers)
        response = json.loads(post.content.decode('utf-8'))
        size = len(response["data"])
        sum = 0
        count=0
        average=0
        for i in range(size):
            get = response["data"][i]["signal"], response["data"][i]["channel"] == int(self.channel)
            if (get[1] == True):
                #print(get[0])
                signal = get[0]
                count = count + int(1)
                sum = sum - signal
        if count >=1:
            average = sum / count
        return round(average,2)


    def GetUptime(self):
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            time = str(datetime.timedelta(seconds=(response["data"]["uptime"])))
            return time

    def GetModel(self):
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            model = str(response["data"]["model"])
            return model

    def GetAlias(self):
            post = requests.get(str(url_constructor.URLs(self.version, 'statusSystem', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = str(response["data"]["alias"])
            return Alias

    def GetHasUpdate(self):
            post = requests.get(str(url_constructor.URLs(self.version, 'HasUpdate', self.ip, self.port).Check_version()), verify=False, headers=headers)
            response = json.loads(post.content.decode('utf-8'))
            Alias = bool(response["data"]["has_update"])
            #print(Alias)
            if Alias == False:
                Alias = "Produto na ultima versão de firmware"
            else:
                Alias = "Possui uma nova firmware para atualização"
            return Alias

    def GetOpMode(self):
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





