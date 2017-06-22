#coding:utf-8

import  urllib2

if __name__ == 'main':

    # 发送请求
    url = "http://www.maiziedu.com"
    request = urllib2.Request(url = url)
    response =   urllib2.urlopen(request)
    print  response.read()