import paramiko
import scp

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

class send:
    def __init__(self, info='', ip='', timeout=45, directory="/tmp", username="", password=""):
        self.info = info
        self.ip = ip
        self.timeout = timeout
        self.drectory = directory
        self.username = username
        self.password = password


    def file(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(AllowAnythingPolicy())
            client.connect(self.ip, username=self.username, password=self.password, port=22, timeout=self.timeout)

            with scp.SCPClient(client.get_transport()) as scps:
                scps.put(self.info, self.drectory)
            return True
        except:
            return False

    def command(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(AllowAnythingPolicy())
            client.connect(self.ip, username=self.username, password=self.password, port=22, timeout=self.timeout)
            out1 = client.exec_command(self.info, timeout=self.timeout)[1]
            client.close()
            return True
        except Exception as e:
            print(e)
            return False
    def command_get(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(AllowAnythingPolicy())
            client.connect(self.ip, username=self.username, password=self.password, port=22, timeout=self.timeout)
            stdin, stdout, stderr = client.exec_command(self.info, timeout=self.timeout)
            response = stdout.readlines()
            client.close()
            return response
        except Exception as e:
            print("exception: ", e)
            return False