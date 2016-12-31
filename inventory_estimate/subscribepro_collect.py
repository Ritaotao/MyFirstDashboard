__author__ = 'ritaotao'


import requests
import re
import pandas as pd
import csv
import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser

# first get access_token via SSH
params_access = {
    "grant_type": "client_credentials",
    "client_id": "1247_2cxqsrmdt3y8w0gs888kkocskw8s8w4gkws00kk8oskwgkccko",
    "client_secret": "3dk8v8i4px4w004cg8wg0cgskc4g0ccs0go4wwgkwsk0gg4g40"
}

url_access = "https://api.subscribepro.com/oauth/v2/token"
r_access = requests.get(url_access, params=params_access)
print "Token request status code:",r_access.status_code

# split out access_token and use subscribepro api to pull complete subscription report
pattern = re.compile(r'\"')
access_token = re.split(pattern, r_access.content)[3]
url_api = "http://api.subscribepro.com/services/v2/reports/complete_subscriptions?access_token=%s"%access_token
r_api = requests.get(url_api)
out_api = r_api.content[:]

# cleaning raw data and transfer to pandas dataframe object
out1 = str(out_api).replace('ID','entry_id').replace('\'','').replace('\",\"',';').replace('\"','').split("\r\n")
out2 = [x.split(";") for x in out1]
df = pd.DataFrame(out2[1:], columns=out2[0])


## write complete_subscription_report into a csv file
# with open('test.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for item in out1:
#         writer.writerow(item.split(";"))

# df = pd.read_csv('/Users/ritaotao/Documents/WineAwesomeness/WA_Py/inventory_estimate/test.csv', sep=";")
# print df.head()

# warning: current_date should always before day 27th.
i = datetime.datetime.now()
start = i.strftime('%Y-%m-%d')
left = i.strftime('%Y-%m')+"-27"
right = i.strftime('%Y-%m')+"-28"
end = (parser.parse(left) + relativedelta(months=+1)).strftime('%Y-%m-%d')
print start, left, right, end
# subset the records from now() to 27th day of current month
df_1 = df[(df.Status == "active") & (df.Interval == "Every Month")
                  & (df['Nxt Ord Date'] >= start) & (df['Nxt Ord Date'] <= left)]
df_2 = df[(df.Status == "active") & (df['Nxt Ord Date'] >= right) & (df['Nxt Ord Date'] <= end)]
df1 = df_1[(df_1['Exp Date'] == "")]
df2 = df_2[(df_2['Exp Date'] == "")]
df3 = df_1[(df['Exp Date'] != "") & ((df_1['Exp Date'] < start)|(df['Exp Date'] > left))]
df4 = df_2[(df['Exp Date'] != "")]
print df3[df3['SKU'].str.contains("(white-3)|(gift-pre.*white)")]['SKU']
# all_red1 = len(df1[df1['Prod Name'].str.contains("All Red")].index)
# all_white1 = len(df1[df1['Prod Name'].str.contains("All White")].index)
# variety1 = len(df1[df1['Prod Name'].str.contains("Variety")].index)
# df2 = df[(df.Status == "active") & (df.Interval == "Every Month") & (df['Nxt Ord Date'] >= '%s'%right) & (df['Nxt Ord Date'] <= '%s'%end)]
# all_red2 = len(df2[df2['Prod Name'].str.contains("All Red")].index)
# all_white2 = len(df2[df2['Prod Name'].str.contains("All White")].index)
# variety2 = len(df2[df2['Prod Name'].str.contains("Variety")].index)
# print all_red1, all_white1, variety1, all_red2, all_white2, variety2