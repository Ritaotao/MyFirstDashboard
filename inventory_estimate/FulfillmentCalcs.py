__author__ = 'ritaotao'

from math import ceil
import requests
import re
import pandas as pd
from dateutil.relativedelta import relativedelta
from dateutil import parser
import warnings
warnings.filterwarnings("ignore") # to disable warnings from pandas

class FulfillmentCalcs(object):
    def __init__(self):
        self.new_member = 10
        self.new_gift_member = 0
        self.avg_additional_churn = 0.075
        self.buffer = 100
        self.r2w1_percent = 0.6
        self.r1w2_percent = 1 - self.r2w1_percent
        print 'The initial parameters are set to be...\n' \
              'New Members per Day: %i\n' \
              'New Gift Members per Day: %i\n' \
              'Avg Additional Churn: %.3f\n' \
              'Buffer: %i\n' \
              'Percentage of Variety Packs containing 2 Reds: %.2f\n' \
              'Percentage of Variety Packs containing 2 Whites: %.2f'\
              % (self.new_member,self.new_gift_member,self.avg_additional_churn,
                 self.buffer,self.r2w1_percent,self.r1w2_percent)

    # Update basic assumptions
    def param_update(self):
        print 'Starting to update basic assumptions...'
        self.new_member = raw_input('New Members per Day: ')
        self.new_gift_member = raw_input('New Gift Members per Day: ')
        self.avg_additional_churn = raw_input("Avg Additional Churn as percentage (From 28th to Date of Charge): ")
        self.buffer = raw_input('Buffer: ')
        self.r2w1_percent = raw_input('Percentage of Variety Packs containing 2 Reds: ')
        try:
            self.new_member = int(self.new_member)
            self.new_gift_member = int(self.new_gift_member)
            self.avg_additional_churn = float(self.avg_additional_churn)
            self.buffer = int(self.buffer)
            self.r2w1_percent = float(self.r2w1_percent)
            self.r1w2_percent = 1 - self.r2w1_percent
        except ValueError:
            print "One of the values fails to be int or float!"
            self.param_update()
        print 'The updated parameters are...\n' \
              'New Members per Day: %i\n' \
              'New Gift Members per Day: %i\n' \
              'Avg Additional Churn: %.3f\n' \
              'Buffer: %i\n' \
              'Percentage of Variety Packs containing 2 Reds: %.2f\n' \
              'Percentage of Variety Packs containing 2 Whites: %.2f'\
              % (self.new_member,self.new_gift_member,self.avg_additional_churn,
                 self.buffer,self.r2w1_percent,self.r1w2_percent)

    # download the report using Subscribepro API
    df = pd.DataFrame()
    def sp_collect(self):
        print 'Starting to download Complete Subscription Report...'
        # get access_token via SSH
        params_access = {
            "grant_type": "client_credentials",
            "client_id": "1247_2cxqsrmdt3y8w0gs888kkocskw8s8w4gkws00kk8oskwgkccko",
            "client_secret": "3dk8v8i4px4w004cg8wg0cgskc4g0ccs0go4wwgkwsk0gg4g40"
        }

        url_access = "https://api.subscribepro.com/oauth/v2/token"
        r_access = requests.get(url_access, params=params_access)
        print "Token request status code:",r_access.status_code

        # split out access_token and use api to pull complete subscription report
        pattern = re.compile(r'\"')
        access_token = re.split(pattern, r_access.content)[3]
        url_api = "http://api.subscribepro.com/services/v2/reports/complete_subscriptions?access_token=%s"%access_token
        r_api = requests.get(url_api)
        out_api = r_api.content[:]

        # cleaning raw report and transfer to pandas data frame object
        out1 = str(out_api).replace('ID','entry_id').replace('\'','')\
            .replace('\",\"',';').replace('\"','').split("\r\n")
        out2 = [x.split(";") for x in out1]
        self.df = pd.DataFrame(out2[1:], columns=out2[0])
        try:
            r_access.status_code = 200
            print "Successfully downloaded."
        except:
            print "Connection failed."

    # print out the basic stats from the downloaded report
    days = 0
    overall_churn = 0
    wa = 0
    perc_red = 0
    perc_white = 0
    est_total_pack = 0
    def print_stats(self):
        print "Starting to print stats..."
        # type in the date to be estimated
        # warning: current date should always before day 27th.
        date = raw_input('Enter the start date (yyyy-mm-dd) of interest (you can only enter a future date): ')
        dt = parser.parse(date)
        start = dt.strftime('%Y-%m-%d')
        left = dt.strftime('%Y-%m')+"-27"
        right = dt.strftime('%Y-%m')+"-28"
        end = (parser.parse(left) + relativedelta(months=+1)).strftime('%Y-%m-%d')
        self.days = (parser.parse(right)-parser.parse(start)).days

        # estimate overall churn based on last two-month subscriptions
        create_left = (parser.parse(dt.strftime('%Y-%m')+"-01") + relativedelta(months=-2)).strftime('%Y-%m-%d')
        create_right = (parser.parse(dt.strftime('%Y-%m')+"-30") + relativedelta(months=-1)).strftime('%Y-%m-%d')
        df_oc = self.df[(self.df.Created >= create_left) & (self.df.Created <= create_right)
                        & (self.df['Exp Date'] == "")]
        bottom = len(df_oc.index)
        df_oc_top = df_oc[(df_oc['Lst Ord Date'] == "") & ((df_oc.Status == "cancelled") | (df_oc.Status == 'failed'))]
        top = len(df_oc_top.index)
        self.overall_churn = top/float(bottom)
        print "From %s to %s, # of subscriptions created: %d, # of fm churn: %d.\n" \
              "Estimated Overall Churn, incl. Failed: %.2f\n" % (create_left,create_right,bottom,top,self.overall_churn)

        # non-gift customers
        df_1 = self.df[(self.df.Status == "active") & (self.df.Interval == "Every Month")
                       & (self.df['Nxt Ord Date'] >= start) & (self.df['Nxt Ord Date'] <= left)]
        df_2 = self.df[(self.df.Status == "active")
                       & (self.df['Nxt Ord Date'] >= right) & (self.df['Nxt Ord Date'] <= end)]

        df1 = df_1[(df_1['Exp Date'] == "")]
        red3_1 = len(df1[df1['SKU'].str.contains("red-3")].index)
        white3_1 = len(df1[df1['SKU'].str.contains("white-3")].index)
        variety3_1 = len(df1[df1['SKU'].str.contains("variety-3|variety3")].index)
        red6_1 = len(df1[df1['SKU'].str.contains("red-6")].index)
        white6_1 = len(df1[df1['SKU'].str.contains("white-6")].index)
        variety6_1 = len(df1[df1['SKU'].str.contains("variety-6")].index)
        df2 = df_2[(df_2['Exp Date'] == "")]
        red3_2 = len(df2[df2['SKU'].str.contains("red-3")].index)
        white3_2 = len(df2[df2['SKU'].str.contains("white-3")].index)
        variety3_2 = len(df2[df2['SKU'].str.contains("variety-3|variety3")].index)
        red6_2 = len(df2[df2['SKU'].str.contains("red-6")].index)
        white6_2 = len(df2[df2['SKU'].str.contains("white-6")].index)
        variety6_2 = len(df2[df2['SKU'].str.contains("variety-6")].index)
        print "Non-gift Customer Stats..."
        print "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i, " \
              "# of red 6: %i, # of white 6: %i, # of variety 6: %i;"\
              % (start, left, red3_1, white3_1,variety3_1, red6_1, white6_1, variety6_1)
        print "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i, " \
              "# of red 6: %i, # of white 6: %i, # of variety 6: %i;"\
              % (right, end, red3_2, white3_2, variety3_2, red6_2, white6_2, variety6_2)
        # gift customers
        df3 = df_1[(df_1['Exp Date'] != "") & ((df_1['Exp Date'] < start) | (df_1['Exp Date'] > left))]
        red3_3 = len(df3[df3['SKU'].str.contains("(red-3)|(gift-pre.*red)")].index)
        white3_3 = len(df3[df3['SKU'].str.contains("(white-3)|(gift-pre.*white)")].index)
        variety3_3 = len(df3[df3['SKU'].str.contains("(variety-3)|(gift-pre.*variety)")].index)
        variety6_3 = len(df3[df3['SKU'].str.contains("variety-6")].index)
        df4 = df_2[(df_2['Exp Date'] != "")]
        red3_4 = len(df4[df4['SKU'].str.contains("(red-3)|(gift-pre.*red)")].index)
        white3_4 = len(df4[df4['SKU'].str.contains("(white-3)|(gift-pre.*white)")].index)
        variety3_4 = len(df4[df4['SKU'].str.contains("(variety-3)|(gift-pre.*variety)")].index)
        variety6_4 = len(df4[df4['SKU'].str.contains("variety-6")].index)
        print "Gift Customer Stats..."
        print "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i, # of variety 6: %i;"\
              % (start, left, red3_3, white3_3,variety3_3, variety6_3)
        print "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i, # of variety 6: %i.\n"\
              % (right, end, red3_4, white3_4, variety3_4, variety6_4)

        # overall stats
        # population count (non-gift and gift)
        pop_ng = red3_1+white3_1+variety3_1+red6_1+white6_1+variety6_1+\
                 red3_2+white3_2+variety3_2+red6_2+white6_2+variety6_2
        pop_gi = red3_3+white3_3+variety3_3+variety6_3+\
                 red3_4+white3_4+variety3_4+variety6_4
        pop_total = pop_ng+pop_gi
        print "We have %d active members with a valid next order date in total." % pop_total
        print "%d non-gift customers, and %d gift customers." % (pop_ng, pop_gi)
        # estimate weighted avg bottles per pack
        pack3 = red3_1+red3_2+red3_3+red3_4+\
                white3_1+white3_2+white3_3+white3_4+\
                variety3_1+variety3_2+variety3_3+variety3_4
        pack6 = red6_1+red6_2+white6_1+white6_2+\
                variety6_1+variety6_2+variety6_3+variety6_4
        self.wa = 3*pack3/float(pack3+pack6) + 6*pack6/float(pack3+pack6)
        print "%d 3-bottle packs, and %d 6-bottle packs;\n" \
              "Estimated weighted avg per pack is %.3f." % (pack3,pack6,self.wa)
        # red:white ratio count
        num_of_red = ceil(3*(red3_1+red3_2+red3_3+red3_4+variety6_1+variety6_2)+6*(red6_1+red6_2)
                          +self.r2w1_percent*2*(variety3_1+variety3_2+variety3_3+variety3_4))
        num_of_white = ceil(3*(white3_1+white3_2+white3_3+white3_4+variety6_1+variety6_2)+6*(white6_1+white6_2)
                          +self.r1w2_percent*2*(variety3_1+variety3_2+variety3_3+variety3_4))
        self.perc_red = num_of_red/float(num_of_red+num_of_white)
        self.perc_white = 1 - self.perc_red
        print "The red:white ratio is %.2f:%.2f."%(self.perc_red, self.perc_white)
        self.est_total_pack = ceil((pop_total+self.new_member*self.days*(1-self.overall_churn))\
                                   *(1-self.avg_additional_churn)+pop_gi+self.new_gift_member*self.days+self.buffer)
        print "Total # of package we should order for: %i" % self.est_total_pack

    # Break-down into number of bottles per type of wine
    def wine_order_breakdown(self):
        print 'Starting to compute each number of bottles needed...'
        total_bottles = ceil(self.est_total_pack*self.wa)
        red_bottles = ceil(total_bottles*self.perc_red)
        white_bottles = total_bottles - red_bottles
        print "Total Wines needed (in bottles): %i; Red needed is %i, White needed is %i."\
              % (total_bottles,red_bottles,white_bottles)
        cases = [ceil(total_bottles/12.0), ceil(red_bottles/12.0), ceil(white_bottles/12.0)]
        print "Total Cases needed: %i; Red needed is %i, White needed is %i." % (cases[0],cases[1],cases[2])
        num_each = [ceil(cases[1]/3.0),ceil(cases[2]/3.0)]
        print "Number of each red needed is %i; Number of each white needed is %i." % (num_each[0],num_each[1])


# the main function to call each of the steps
def doit():
    run = FulfillmentCalcs()
    print '------'
    ask = raw_input('Do you want to update these assumptions?(y/n)').lower()
    if ask == 'y':
        run.param_update()
        print '------'
    elif ask == 'n':
        print 'Keep using the same assumptions...'
    else:
        print 'The input could only be y or n.'
    run.sp_collect()
    print '------'
    run.print_stats()
    print '------'
    run.wine_order_breakdown()
    print 'End of Estimation'

# call the function
doit()






