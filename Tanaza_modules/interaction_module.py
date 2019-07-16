import Tanaza_modules.ssh_module as ssh
import sys



countwlan = []

class interact():

    def __init__(self, ip="", username="", password="", interface="5Ghz"):
        self.ip = ip
        self.username = username
        self.password = password
        self.interface = interface

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

