import requests


def IPConfig():
    r = str(requests.get('http://myip.ipip.net', timeout=6).text).split(" ")[1].split("：")[-1]
    return r


if __name__ == '__main__':
    print(IPConfig())
