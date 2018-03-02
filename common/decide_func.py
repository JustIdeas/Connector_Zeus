from common import get_func


class Decide:

    def __init__(self, mode='', ip='', port='', user='', pas='', channel='', version='', interface='', sock='9090'):
        self.mode = mode
        self.ip = ip
        self.port = port
        self.user = user
        self.pas = pas
        self.channel = channel
        self.version = version
        self.interface = interface
        self.socket = sock

    def check(self):

        if self.mode == 'clients':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetClients()
            print(response)

        if self.mode == 'version':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetVersion()
            print(response)

        if self.mode == 'noise':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetNoise()
            print(response)

        if self.mode == 'surveycount':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetNoise_channelCount()
            print(response)

        if self.mode == 'noise_channel':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetNoise_byChannel()
            print(response)

        if self.mode == 'noise_ownchannel':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetNoise_ownChannel()
            print(response)

        if self.mode == 'channel':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).Getchannel()
            print(response)

        if self.mode == 'uptime':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetUptime()
            print(response)

        if self.mode == 'model':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetModel()
            print(response)

        if self.mode == 'alias':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetAlias()
            print(response)

        if self.mode == 'hasupdate':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetHasUpdate()
            print(response)

        if self.mode == 'opmode':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetOpMode()
            print(response)

        if self.mode == 'uploadeth0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetThroughputEth0_Upload()
            print(response)

        if self.mode == 'downloadeth0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetThroughputEth0_Download()
            print(response)

        if self.mode == 'uploadwlan0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetThroughputWlan0_Upload()
            print(response)

        if self.mode == 'downloadwlan0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetThroughputWlan0_Download()
            print(response)

        if self.mode == 'socket':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, self.socket).SocketTest()
            print(response)

        if self.mode == 'deviceowner':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface).GetClientsMac()
            print(response)