from common import http_post

class _2Ghz:
    
    def __init__(self,  mode='', ip='', port='', user='', pas='', channel='', version='', interface=''):
        self.mode = mode
        self.ip = ip
        self.port = port
        self.user = user
        self.pas = pas
        self.channel = channel
        self.version = version
        self.interface = interface

    def check(self):
        
        if self.mode == 'clients':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetClients()
            if self.version == 'v1':
                if response['data']['clients'] == []:
                    print(0)
                else:
                    print(len(response['data']['clients']))
            elif self.version == 'v3':
                if response['data']['wireless']['radios'][0]['connected_clients'] == 0:
                    print(0)
                else:
                    print(response['data']['wireless']['radios'][0]['connected_clients'])

        if self.mode == 'version':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetVersion()
            if response["data"]["version"] == []:
                print(0)
            else:
                print(response["data"]["version"])

        if self.mode == 'noise':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetNoise()
            print(response)

        if self.mode == 'surveycount':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetNoise_channelCount()
            print(response)

        if self.mode == 'noise_channel':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetNoise_byChannel()
            print(response)

        if self.mode == 'noise_ownchannel':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetNoise_ownChannel()
            print(response)

        if self.mode == 'channel':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).Getchannel()
            print(response)

        if self.mode == 'uptime':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetUptime()
            print(response)

        if self.mode == 'model':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetModel()
            print(response)

        if self.mode == 'alias':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetAlias()
            print(response)

        if self.mode == 'hasupdate':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetHasUpdate()
            print(response)

        if self.mode == 'opmode':
            http_post.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user, self.pas, self.channel, self.version).login()
            response = http_post.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version).GetOpMode()
            print(response)