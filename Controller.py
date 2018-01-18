import urllib3
import sys
import argparse

from common import http_post

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
    results = parser.parse_args(args)
    return (results.mode,
            results.ip,
            results.port,
            results.username,
            results.password,
            results.channel,
            results.version
            )


def main():
    m, ip, p, user, pas, ch, ver  = check_arg(sys.argv[1:])

    #print('mode:', m,'ip:', ip, 'port:', p, 'username:', user, 'password:', pas, 'channel:', ch, ver)
    if m == 'clients':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetClients()
        if response['data']['clients'] == []:
            print(0)
        else:
            print(len(response['data']['clients']))

    if m == 'version':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetVersion()
        if response["data"]["version"] == []:
            print(0)
        else:
            print(response["data"]["version"])

    if m == 'noise':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetNoise()
        print(response)

    if m == 'surveycount':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetNoise_channelCount()
        print(response)

    if m == 'noise_channel':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetNoise_byChannel()
        print(response)

    if m == 'noise_ownchannel':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetNoise_ownChannel()
        print(response)

    if m == 'channel':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).Getchannel()
        print(response)

    if m == 'uptime':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetUptime()
        print(response)

    if m == 'model':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetModel()
        print(response)

    if m == 'alias':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetAlias()
        print(response)

    if m == 'hasupdate':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetHasUpdate()
        print(response)

    if m == 'opmode':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch, ver).login()
        response = http_post.POST(0,ip, p, user, pas, ch, ver).GetOpMode()
        print(response)
main()





