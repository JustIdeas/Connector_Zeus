import urllib3
import sys
import argparse


from common import decide_func


urllib3.disable_warnings()

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Basic Functions')
    parser.add_argument('-m', '--mode',
                        help='Get act',
                        required='True',
                        default='version')
    parser.add_argument('-ip', '--ip',
                        help='ip address',
                        default='127.0.0.1')
    parser.add_argument('-p', '--port',
                        help='https port',
                        default='443')
    parser.add_argument('-user', '--username',
                        help='login username',
                        default='something')
    parser.add_argument('-pas', '--password',
                        help='login password',
                        default='something')
    parser.add_argument('-ch', '--channel',
                        help='login password',
                        default='something')
    parser.add_argument('-ver', '--version',
                        help='API Version',
                        default='v1')
    parser.add_argument('-int', '--interface',
                        help='Interface 2Ghz or 5Ghz, if 5Ghz, use bouth interfaces',
                        default='2Ghz')
    parser.add_argument('-soc', '--socket',
                        help='socket test port',
                        default='socket')
    parser.add_argument('-db', '--database',
                        help='name of yout database',
                        default='zabbix')
    parser.add_argument('-Hid', '--hostid',
                        help='Host ID',
                        default='')
    parser.add_argument('-Iid', '--itemid',
                        help='Item ID',
                        default='1')
    parser.add_argument('-ta', '--table',
                        help='Table Name',
                        default='1')
    parser.add_argument('-ssid', '--ssid',
                        help='ssid name',
                        default='1')
    parser.add_argument('-netw', '--network',
                        help='network name',
                        default='1')
    results = parser.parse_args(args)
    return (results.mode,
            results.ip,
            results.port,
            results.username,
            results.password,
            results.channel,
            results.version,
            results.interface,
            results.socket,
            results.database,
            results.hostid,
            results.itemid,
            results.table,
            results.network,
            results.ssid
            )


def main():
    m, ip, p, user, pas, ch, ver, int, soc, db, Hid, Iid, ta, ssid, netw = check_arg(sys.argv[1:])
    #print('mode:', m, 'ip:', ip, 'port:', p, 'username:', user, 'password:', pas, 'channel:', ch, ver, int, soc, db, Hid, Iid)

    decide_func.Decide(m, ip, p, user, pas, ch, ver, int, soc, db, Hid, Iid, ta, netw, ssid).check()



main()

