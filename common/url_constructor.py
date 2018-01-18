


class URLs:

    def __init__(self, version='', info='', ip='', port=''):
        self.version = version
        self.info = info
        self.ip = ip
        self.port = port

    def Check_version(self):

        if self.version == str("v1"):
            return URLs().URLs_v1(self.info, self.ip, self.port)
        elif self.version == str("v3"):
            return URLs().URLs_v3(self.info, self.ip, self.port)

    def URLs_v1(self ,info='', ip='', port=''):
        self.info = info
        self.ip = ip
        self.port = port

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

    def URLs_v3(self, info='', ip='', port=''):
        self.info = info
        self.ip = ip
        self.port = port
        URL = {

            'login': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/login',
            'clients': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/status',
            'version': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/device',
            'noise': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/1/survey',
            'statusWireless': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wireless/1/status',
            'statusSystem': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/device/status',
            'HasUpdate': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/system/apply/status',
            'WanInfo': 'https://' + self.ip + ':' + self.port + '/cgi-bin/api/v3/interface/wan'

        }
        return URL[self.info]