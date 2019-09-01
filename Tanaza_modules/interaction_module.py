import Tanaza_modules.ssh_module as ssh
import sys
import requests
import json
import urllib3
import datetime



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
countwlan = []

class interact():

    def __init__(self, ip="", username="", password="", interface="5Ghz", ssid="", network="", device=""):
        self.ip = ip
        self.username = username
        self.password = password
        self.interface = interface
        self.ssid = ssid
        self.network = network
        self.device = device

    def run(self):

        response = ssh.send("iw dev",
                          ip=self.ip,
                          username=self.username,
                          password=self.password).command_get()
        #print("return from:", response)

        for i in range(len(response)):
            if "wlan" in response[i]:
                countwlan.append(i)
        result = interact(ip=self.ip, username=self.username, password=self.password, interface=self.interface).by_interface(data=response)
        return result
    def by_interface(self, data):
        countclients = 0

        if self.interface == "5Ghz":
            for i in range(len(countwlan)):
                interface = str(data[countwlan[i]]).replace("Interface", "").strip()
                position = int(countwlan[i] + 6)
                if "center1: 5" in data[position]:
                    response = ssh.send("iw dev "+interface+" station dump | grep -c \"Station\"",
                                        ip=self.ip,
                                        username=self.username,
                                        password=self.password).command_get()
                    response = int(str(response[0]).replace('\n', '').strip())
                    countclients = countclients + response

        if self.interface == "2Ghz":
            countclients = 0
            for i in range(len(countwlan)):
                interface = str(data[countwlan[i]]).replace("Interface", "").strip()
                position = int(countwlan[i] + 6)
                if "center1: 2" in data[position]:
                    response = ssh.send("iw dev "+interface+" station dump | grep -c \"Station\"",
                                        ip=self.ip,
                                        username=self.username,
                                        password=self.password).command_get()
                    response = int(str(response[0]).replace('\n', '').strip())
                    countclients = countclients + response

        return countclients

    def API_get_clients(self):
        post = requests.get(
            "https://cloud.tanaza.com/apis/v3.0/"+self.username+"/"+self.password+"/status",
            verify=False,
            timeout=30)
        response = json.loads(post.content.decode('utf-8'))
        if self.device:
            for i in response["payload"]["account"]["networks"]:
                if i["label"] == self.network:
                    for b in i["devices"]:
                        if b["label"] == self.device:
                            for c in b["ssids"]:
                                if c["label"] == self.ssid:
                                    if c["clients"] == None:
                                        return 0
                                    else:
                                        return len(c["clients"])
                        else:
                            return 0
        for i in response["payload"]["account"]["networks"]:
            if i["label"]  == self.network:
                for b in i["devices"]:
                    for c in b["ssids"]:
                        if c["label"] == self.ssid:
                            if c["clients"] == None:
                                return 0
                            else:
                                return len(c["clients"])

    def API_get_uptime(self):
        post = requests.get(
            "https://cloud.tanaza.com/apis/v3.0/" + self.username + "/" + self.password + "/status",
            verify=False,
            timeout=30)
        response = json.loads(post.content.decode('utf-8'))
        if self.device:
            for i in response["payload"]["account"]["networks"]:
                if i["label"] == self.network:
                    for b in i["devices"]:
                        if b["label"] == self.device:
                           print(b["last_uptime"])
                           value = int(b["last_uptime"])
                           result = str(datetime.timedelta(seconds=value))
                           print(result)
                           return result
                        else:
                            return 0
