__author__ = 'ritaotao'

# import urllib.request
# import urllib.parse
# # import lib2to3
# import http.cookiejar
# import re

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read())

# request = urllib.request.Request("http://www.baidu.com")
# response = urllib.request.urlopen(request)
# print(response.read())

# post
# values = {"username":"1016903103@qq.com","passowrd":"XXXX"}
# data = urllib.parse.urlencode(values)
## data = data.encode('utf-8')
# url = "https://passport.csdn.net/account.login?from=http://my.csdn.net/my/mycsdn"
# request = urllib.request.Request(url,data)
# response = urllib.request.urlopen(request)
# print(response.read())

# get
# values = {}
# values['username'] = "1016903103@qq.com"
# values['password'] = "XXXX"
# data = urllib.parse.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request = urllib.request.Request(geturl)
# response = urllib.request.urlopen(request)
# print(response.read())

# header
# url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username': 'cqc', 'password':'XXXX'}
# headers = {'User-Agent': user_agent}
# data = urllib.parse.urlencode(values)
# request = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(request)
# page = response.read()
# headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 'Referer':'http://www.zhihu.com/articles'}

# proxy
# enable_proxy = True
# proxy_handler = urllib.request.ProxyHandler({"http": 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib.request.ProxyHandler({})
# if enable_proxy:
#     opener = urllib.request.build_opened(proxy_handler)
# else:
#     opener = urllib.request.build_opener(null_proxy_handler)
# urllib.request.install_opener(opener)

# put, delete
# request = urllib.request.Request(url, data=data)
# request.get_method = lambda: 'PUT' # or 'DELETE'
# response = urllib.request.urlopen(request)

# debugLog
# httpHandler = urllib.request.HTTPHandler(debuglevel=1)
# httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
# opener = urllib.request.build_opener(httpHandler, httpsHandler)
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen('http://www.baidu.com')

# HttpError
# request = urllib.request.Request('http://www.xaxxxx.com')
# try:
#     urllib.request.urlopen(request)
# except urllib.request.URLError as e:
#     print(e.reason)

# HttpError, code/reason
# req = urllib.request.Request('http://blog.csdn.net/cqcre')
# try:
#     urllib.request.urlopen(req)
# except urllib.request.HTTPError as e:
#     print(e.code)
#     print(e.reason)

# req = urllib.request.Request('http://blog.csdn.net/cqcre')
# try:
#     urllib.request.urlopen(req)
# except urllib.request.HTTPError as e:
#     print(e.code)
# except urllib.request.URLError as e:
#     print(e.reason)
# else:
#     print("OK")

# req = urllib.request.Request('http://blog.csdn.net/cqcre')
# try:
#     urllib.request.urlopen(req)
# except urllib.request.URLError as e:
#     if hasattr(e,"code"):
#         print(e.code)
#     if hasattr(e,"reason"):
#         print(e.reason)
# else:
#     print("OK")

# save cookies to variable
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print('Name = '+item.name)
#     print('Value = '+item.value)

# save cookie to file
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

# load cookie from file
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# req = urllib.request.Request("http://www.baidu.com")
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print(response.read())

# simulate login using cookie
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# postdata = urllib.parse.urlencode({
#     "stuid": "201200131012",
#     "pwd": "23342321"
# })
# postdata = postdata.encode('utf-8')
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# result = opener.open(loginUrl, postdata)
# cookie.save(ignore_discard=True, ignore_expires=True)
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# try:
#     result = opener.open(gradeUrl)
#     print(result.read())
# except urllib.request.URLError as e:
#     print(e.reason)

# regular expression
# -*- coding: utf-8 -*-

#导入re模块
#
# # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
# pattern = re.compile(r'hello')
#
# # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
# result1 = re.match(pattern,'hello')
# result2 = re.match(pattern,'helloo CQC!')
# result3 = re.match(pattern,'helo CQC!')
# result4 = re.match(pattern,'hello CQC!')
#
# #如果1匹配成功
# if result1:
#     # 使用Match获得分组信息
#     print(result1.group())
# else:
#     print('1匹配失败！')
#
#
# #如果2匹配成功
# if result2:
#     # 使用Match获得分组信息
#     print(result2.group())
# else:
#     print('2匹配失败！')
#
#
# #如果3匹配成功
# if result3:
#     # 使用Match获得分组信息
#     print(result3.group())
# else:
#     print('3匹配失败！')
#
# #如果4匹配成功
# if result4:
#     # 使用Match获得分组信息
#     print(result4.group())
# else:
#     print('4匹配失败！')
#
# 匹配如下内容：单词+空格+单词+任意字符
# (not suitable for py 3.4.1
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#
# print("m.string:", m.string)
# print("m.re:", m.re)
# print("m.pos:", m.pos)
# print("m.endpos:", m.endpos)
# print("m.lastindex:", m.lastindex)
# print("m.lastgroup:", m.lastgroup)
# print("m.group():", m.group())
# print("m.group(1,2):", m.group(1, 2))
# print("m.groups():", m.groups())
# print("m.groupdict():", m.groupdict())
# print("m.start(2):", m.start(2))
# print("m.end(2):", m.end(2))
# print("m.span(2):", m.span(2))
# print(r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3'))

# pattern = re.compile(r'world')
# match = re.search(pattern,'hello world!')
# if match:
#     print(match.group())

# pattern = re.compile(r'\d+')
# print(re.split(pattern,'one1two2three3four4'))

# pattern = re.compile(r'\d+')
# print(re.findall(pattern,'one1two2three3four4'))

# pattern = re.compile(r'\d+')
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print(m.group())

# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# print(re.sub(pattern,r'\2 \1', s))
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
# print(re.sub(pattern,func,s))
#
# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# print(re.subn(pattern,r'\2 \1', s))
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
# print(re.subn(pattern,func, s))

 # match(string[, pos[, endpos]]) | re.match(pattern, string[, flags])
 # search(string[, pos[, endpos]]) | re.search(pattern, string[, flags])
 # split(string[, maxsplit]) | re.split(pattern, string[, maxsplit])
 # findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])
 # finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags])
 # sub(repl, string[, count]) | re.sub(pattern, repl, string[, count])
 # subn(repl, string[, count]) |re.sub(pattern, repl, string[, count])


# switch to python2.7
