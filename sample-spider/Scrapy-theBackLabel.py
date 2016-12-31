__author__ = 'ritaotao'

# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class tbl:

    def __init__(self, baseUrl):
        self.baseURL = baseUrl
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent': self.user_agent}
        self.stories = []

    def getPage(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8','ignore')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print "Fail to connect to theBackLabel, Error reason", e.reason
                return None

    def getContents(self):
        pageCode = self.getPage()
        pattern = re.compile('<img src=(.*?).*?/>',re.S)
        items = re.findall(pattern,pageCode)
        for item in items:
            print item[0]

baseURL = 'http://thebacklabel.com/all-articles-2/#.Vgmv2xNVikq'
stbl = tbl(baseURL)
stbl.getContents()