


class URLs:

    def __init__(self, version='', info='', ip='', port='', proto='https'):
        self.version = version
        self.info = info
        self.ip = ip
        self.port = port
        self.proto = proto

    def Check_version(self):
        if self.version == str("v1"):
            return URLs().URLs_v1(self.info, self.ip, self.port)
        elif self.version == str("v3"):
            return URLs().URLs_v3(self.info, self.ip, self.port, self.proto)
        elif self.version == str("wise_v1"):
            return URLs().wisefi_v1(self.info, self.ip, self.port)

    def URLs_v1(self ,info='', ip='', port=''):
        self.info = info
        self.ip = ip
        self.port = port

        URL = {

            'login': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/login',
            'clients': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wireless/1/clients',
            'version': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/device',
            'noise': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wireless/1/survey',
            'statusWireless': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wireless/1/status',
            'statusSystem': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/device/status',
            'HasUpdate': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/apply/status',
            'WanInfo': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wan',
            'throughputEth0': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/service/statistics/wlan0',
            'throughputWlan0': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/service/statistics/wlan0'

        }

        return URL[self.info]

    def URLs_v3(self, info='', ip='', port='', proto='' ):
        self.info = info
        self.ip = ip
        self.port = port
        self.proto = proto
        URL = {

            'login': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/login',
            'clients': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/status',
            'version': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/device',
            'noise2Ghz': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/radio0/survey',
            'noise5Ghz': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/radio1/survey',
            'statusSystem': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/device/status',
            'HasUpdate': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/apply/status',
            'WanInfo': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wan',
            'throughputEth0': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/service/statistics/eth0',
            'throughputWlan0': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/service/statistics/wlan0',
            'clientsmac2Ghz': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/wifi0/clients',
            'clientsmac5Ghz': self.proto+'://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/wifi1/clients'


        }
        print(URL[self.info])
        return URL[self.info]
    def wisefi_v1(self, info='', ip='', port=''):

        self.info = info
        self.ip = ip
        self.port = port

        URL = {
            'login' : 'http://' + self.ip + ':' + self.port + '/',
            'clients': 'http://'+ self.ip + ':' + self.port + '/dashboard/clientCount/',
            'aphealth': 'http://'+ self.ip + ':' + self.port + '/dashboard/apHealth/'








        }
        return URL[self.info]
