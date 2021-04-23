import requests
import jsonpath

# url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=12&time=7&ts=1&ys=1&cs=1&lb=1&sb=0&pb=4&mr=1&regions='
url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=7&ts=1&ys=1&cs=1&lb=1&sb=0&pb=4&mr=1&regions='
data = requests.get(url).json()
print(data)
ip = jsonpath.jsonpath(data, '$..ip')[0]
port = jsonpath.jsonpath(data, '$..port')[0]
print(ip)
print(port)

target_url = 'https://taobao.com'

proxyHost = ip
proxyPort = port

proxyMeta = 'http://%(host)s:%(port)s' % {
	'host':proxyHost,
	'port':proxyPort
}

proxies = {
	'http': proxyMeta,
	'https':proxyMeta
}

print(proxies)

resp = requests.get(target_url, proxies=proxies)
print(resp.status_code)
print(resp.json())