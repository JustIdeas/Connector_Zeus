
class URLs:

    def __init__(self, version='', info=''):
        self.version = version
        self.info = info


    def Check_version(self):

        if self.version == 'v3':
            URLs().URLs_v3(self.info)
        elif self.version == 'v1':
            URLs().URLs_v1(self.info)

    def URLs_v1(self ,info=''):

        self.info = info
        URL = {

            'login': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/login',
            'clients': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wireless/1/clients',
            'version': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/device',
            'noise': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wireless/1/survey',
            'statusWireless': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wireless/1/status',
            'statusSystem': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/device/status',
            'HasUpdate': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/system/apply/status',
            'WanInfo': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v1/interface/wan'

        }
        return URL[self.info]

    def URLs_v3(self, info=''):
        self.info = info
        URL = {

            'login': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/login',
            'clients': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/1/clients',
            'version': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/device',
            'noise': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/1/survey',
            'statusWireless': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/1/status',
            'statusSystem': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/device/status',
            'HasUpdate': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/apply/status',
            'WanInfo': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wan'

        }
        return URL[self.info]