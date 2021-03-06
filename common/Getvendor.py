import urllib.request as urllib3
import json
import codecs

url = "http://macvendors.co/api/"
class Vendor:
    def __init__(self, Macs='00:00:00:00:00:00'):

        self.mac = Macs

    def run (self):

        request = urllib3.Request(url+self.mac, headers={'User-Agent' : "API Browser"})
        response = urllib3.urlopen( request )
        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))
        return str(obj['result']['company']).replace(',', '.')