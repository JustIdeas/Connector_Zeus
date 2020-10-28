from common import get_func


class Decide:

    def __init__(self, mode='', ip='', port='',
                 user='', pas='', channel='',
                 version='', interface='', sock='9090',
                 db='zabbix', Hid='1', Iid='1',
                 ta='', ssid="", network="", proto="https"):
        self.mode = mode
        self.ip = ip
        self.port = port
        self.user = user
        self.pas = pas
        self.channel = channel
        self.version = version
        self.interface = interface
        self.socket = sock
        self.db = db
        self.Hid = Hid
        self.Iid = Iid
        self.ta = ta
        self.ssid = ssid
        self.network = network
        proto=self.proto = proto

    def check(self):
        if self.mode == 'clients':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetClients()
            print(response)

        if self.mode == 'dbcsv':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto, sock=self.socket, db=self.db, Hid=self.Hid, Iid=self.Iid,).dbCSV()
            print(response)

        if self.mode == 'version':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetVersion()
            print(response)

        if self.mode == 'noise':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetNoise()
            print(response)

        if self.mode == 'surveycount':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetNoise_channelCount()
            print(response)

        if self.mode == 'noise_channel':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetNoise_byChannel()
            print(response)

        if self.mode == 'noise_ownchannel':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetNoise_ownChannel()
            print(response)

        if self.mode == 'channel':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).Getchannel()
            print(response)

        if self.mode == 'uptime':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetUptime()
            print(response)

        if self.mode == 'model':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetModel()
            print(response)

        if self.mode == 'alias':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetAlias()
            print(response)

        if self.mode == 'hasupdate':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetHasUpdate()
            print(response)

        if self.mode == 'opmode':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetOpMode()
            print(response)

        if self.mode == 'uploadeth0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetThroughputEth0_Upload()
            print(response)

        if self.mode == 'downloadeth0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetThroughputEth0_Download()
            print(response)

        if self.mode == 'uploadwlan0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetThroughputWlan0_Upload()
            print(response)

        if self.mode == 'downloadwlan0':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetThroughputWlan0_Download()
            print(response)

        if self.mode == 'socket':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto,sock=self.socket).SocketTest()
            print(response)

        if self.mode == 'deviceowner':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetClientsMac()
            print(response)
        if self.mode == 'stasignal':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version, self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).Get_signal_sta()
            print(response)

        if self.mode == 'countdevowner':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetCountVendorsMac()
            print(response)

        if self.mode == 'ownermac':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).GetVendorAndMac()
            print(response)

        if self.mode == 'table':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, self.prot, self.socket, self.db, self.Hid, self.Iid, self.ta).ConsultDb()

            print(response)

        if self.mode == 'wisecorporate':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).Wisecorporate()
            print(response)

        if self.mode == 'wiseguests':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).Wiseguests()
            print(response)

        if self.mode == 'wiseaphealthok':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).WiseAphealthok()
            print(response)

        if self.mode == 'wiseaphealthnok':
            get_func.POST({'data': {'username': self.user, 'password': str(self.pas)}}, self.ip, self.port, self.user,
                          self.pas, self.channel, self.version,self.interface, proto=self.proto).login()
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).WiseAphealthnok()
            print(response)

        if self.mode == 'tanazaclients':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto).TanazaGetClients_byfrequency()
            print(response)

        if self.mode == 'tanazaclients_api':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto, ssid=self.ssid, network=self.network, device=self.Hid).TanazaGetClients_API()
            print(response)
        if self.mode == 'tanazauptime_api':
            response = get_func.POST(0, self.ip, self.port, self.user, self.pas, self.channel, self.version,
                                     self.interface, proto=self.proto, ssid=self.ssid, network=self.network,
                                     device=self.Hid).TanazaGetUptime_API()
            print(response)