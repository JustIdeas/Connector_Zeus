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
    results = parser.parse_args(args)
    return (results.mode,
            results.ip,
            results.port,
            results.username,
            results.password,
            results.channel
            )


def main():
    m, ip, p, user, pas, ch  = check_arg(sys.argv[1:])

    #print('mode:', m,'ip:', ip, 'port:', p, 'username:', user, 'password:', pas, 'channel:', ch)
    if m == 'clients':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetClients()
        if response['data']['clients'] == []:
            print(0)
        else:
            print(len(response['data']['clients']))

    if m == 'version':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetVersion()
        if response["data"]["version"] == []:
            print(0)
        else:
            print(response["data"]["version"])

    if m == 'noise':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetNoise()
        print(response)

    if m == 'surveycount':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetNoise_channelCount()
        print(response)

    if m == 'noise_channel':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetNoise_byChannel()
        print(response)

    if m == 'noise_ownchannel':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetNoise_ownChannel()
        print(response)

    if m == 'channel':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).Getchannel()
        print(response)

    if m == 'uptime':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetUptime()
        print(response)

    if m == 'model':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetModel()
        print(response)

    if m == 'alias':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetAlias()
        print(response)

    if m == 'hasupdate':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetHasUpdate()
        print(response)

    if m == 'opmode':
        http_post.POST({'data': {'username': user, 'password': str(pas)}}, ip, p, user, pas, ch).login()
        response = http_post.POST(0,ip, p, user, pas, ch).GetOpMode()
        print(response)
main()





