__author__ = 'ritaotao'
import requests
import re

def download():
        # get access_token via SSH
        params_access = {
            "grant_type": "client_credentials",
            "client_id": "1247_2cxqsrmdt3y8w0gs888kkocskw8s8w4gkws00kk8oskwgkccko",
            "client_secret": "3dk8v8i4px4w004cg8wg0cgskc4g0ccs0go4wwgkwsk0gg4g40"
        }

        url_access = "https://api.subscribepro.com/oauth/v2/token"
        r_access = requests.get(url_access, params=params_access)

        # split out access_token and use api to pull complete subscription report
        pattern = re.compile(r'\"')
        access_token = re.split(pattern, r_access.content)[3]
        url_api = "http://api.subscribepro.com/services/v2/reports/complete_subscriptions?access_token=%s"%access_token
        r_api = requests.get(url_api)
        out_api = r_api.content[:]
        out1 = str(out_api).replace('ID','entry_id').replace('\'','')\
            .replace('\",\"',';').replace('\"','').split("\r\n")
        out2 = [x.split(";") for x in out1]
        out2 = out2[1:(-1)]
        print len(out2)
        print out2[-1]

download()