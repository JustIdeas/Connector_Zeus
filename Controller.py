import urllib3
import sys
import argparse

from common import http_post
from common import only_2ghz
from common import _2ghz_5ghz

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
    results = parser.parse_args(args)
    return (results.mode,
            results.ip,
            results.port,
            results.username,
            results.password,
            results.channel,
            results.version,
            results.interface
            )


def main():
    m, ip, p, user, pas, ch, ver, int  = check_arg(sys.argv[1:])

    if int == '2Ghz':
        print('entrou 2Ghz')
        only_2ghz._2Ghz(m, ip, p, user, pas, ch, ver).check()

    #print('mode:', m,'ip:', ip, 'port:', p, 'username:', user, 'password:', pas, 'channel:', ch, ver, int)

main()





