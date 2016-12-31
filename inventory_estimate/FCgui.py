__author__ = 'ritaotao'

from Tkinter import *
from math import ceil
import requests
import re
import pandas as pd
from dateutil.relativedelta import relativedelta
from dateutil import parser
from PIL import ImageTk,Image
from StringIO import StringIO
import warnings
warnings.filterwarnings("ignore") # to disable warnings from pandas

class Application(Frame):
    """ A GUI application for FulfillmentCalcs """

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()

        # self.create_widgets()
        self.new_member = 10
        self.new_gift_member = 0
        self.avg_additional_churn = 0.075
        self.buffer = 100
        self.r2w1_percent = 0.6
        self.r1w2_percent = 1 - self.r2w1_percent
        # create log widget
        self.text = Text(self, width = 60, height = 20, wrap = WORD)
        self.text.configure(background='Deep Sky Blue')
        self.text.grid(row=0,column=1,columnspan=2, rowspan=14)
        message = 'The initial parameters are set to be...\n' \
              'New Members per Day: %i\n' \
              'New Gift Members per Day: %i\n' \
              'Avg Additional Churn: %.3f\n' \
              'Buffer: %i\n' \
              'Percentage of Variety Packs containing 2 Reds: %.2f\n' \
              'Percentage of Variety Packs containing 2 Whites: %.2f\n' \
              'Please enter a start date or update assumptions...'\
              % (self.new_member,self.new_gift_member,self.avg_additional_churn,
                 self.buffer,self.r2w1_percent,self.r1w2_percent)
        self.text.insert(0.0, message)

        """Create button, text and entry widgets"""
        pm1 = Label(self, text = "New Members per Day: ")\
            .grid(row = 2, column = 0, sticky = W)
        pm2 = Label(self, text = "New Gift Members per Day: ")\
            .grid(row = 4, column = 0, columnspan = 2, sticky = W)
        pm3 = Label(self, text = "Avg Additional Churn as percentage (From 28th to Date of Charge): ")\
            .grid(row = 6, column = 0, sticky = W)
        pm4 = Label(self, text = "Buffer: ")\
            .grid(row = 8, column = 0, sticky = W)
        pm5 = Label(self, text = "Percentage of Variety Packs containing 2 Reds: ")\
            .grid(row = 10, column = 0, sticky = W)
        pm6 = Label(self, text = "Enter the start date (yyyy-mm-dd) of interest "
                                      "(you can only enter a future date): ")\
            .grid(row = 0, column = 0, sticky = W)

        frame1 = Frame(self)
        self.custom1 = Entry(frame1, width = 10)
        self.custom1.pack(side="left", fill=None, expand=False)
        update_cm1 = Button(frame1, text = "Change", command = self.update_1)
        update_cm1.pack(side="left", fill=None, expand=False)
        frame1.grid(row=3, column=0, sticky="w")
        frame2 = Frame(self)
        self.custom2 = Entry(frame2, width = 10)
        self.custom2.pack(side="left", fill=None, expand=False)
        update_cm2 = Button(frame2, text = "Change", command = self.update_2)
        update_cm2.pack(side="left", fill=None, expand=False)
        frame2.grid(row=5, column=0, sticky="w")
        frame3 = Frame(self)
        self.custom3 = Entry(frame3, width = 10)
        self.custom3.pack(side="left", fill=None, expand=False)
        update_cm3 = Button(frame3, text = "Change", command = self.update_3)
        update_cm3.pack(side="left", fill=None, expand=False)
        frame3.grid(row=7, column=0, sticky="w")
        frame4 = Frame(self)
        self.custom4 = Entry(frame4, width = 10)
        self.custom4.pack(side="left", fill=None, expand=False)
        update_cm4 = Button(frame4, text = "Change", command = self.update_4)
        update_cm4.pack(side="left", fill=None, expand=False)
        frame4.grid(row=9, column=0, sticky="w")
        frame5 = Frame(self)
        self.custom5 = Entry(frame5, width = 10)
        self.custom5.pack(side="left", fill=None, expand=False)
        update_cm5 = Button(frame5, text = "Change", command = self.update_5)
        update_cm5.pack(side="left", fill=None, expand=False)
        frame5.grid(row=11, column=0, sticky="w")
        frame6 = Frame(self)
        self.custom6 = Entry(frame6, width = 10)
        self.custom6.pack(side="left", fill=None, expand=False)
        update_cm6 = Button(frame6, text = "Change", command = self.update_6)
        update_cm6.pack(side="left", fill=None, expand=False)
        frame6.grid(row=1, column=0, columnspan=2, sticky="w")
        frame_d = Frame(self)
        download = Button(frame_d, text = "Download Report (only need to download once)", command = self.sp_collect)
        download.pack(side="left", fill=None, expand=False)
        frame_d.grid(row=12, column=0, sticky="w")
        frame_all = Frame(self)
        stats = Button(frame_all, text = "Print Stats", command = self.print_stats)
        stats.pack(side="left", fill=None, expand=False)
        break_down = Button(frame_all, text = "Break Down into Red and White", command = self.wine_order_breakdown)
        break_down.pack(side="left", fill=None, expand=False)
        frame_all.grid(row=13, column=0, sticky="w")
        f1 = Frame(self)
        lb1 = Label(f1, text = "# of Packages to Order for: ")
        lb1.pack(side="left", fill=None, expand=False)
        self.result1 = Text(f1, width = 5, height=1, wrap =WORD)
        self.result1.pack(side="left", fill=None, expand=False)
        f1.grid(row=14, column=0, sticky="w")
        f2 = Frame(self)
        lb2 = Label(f2, text = "# of Bottles Each Red to Order for: ")
        lb2.pack(side="left", fill=None, expand=False)
        self.result2 = Text(f2, width = 5, height=1, wrap =WORD)
        self.result2.pack(side="left", fill=None, expand=False)
        f2.grid(row=15, column=0, sticky="w")
        f3 = Frame(self)
        lb3 = Label(f3, text = "# of Bottles Each White to Order for: ")
        lb3.pack(side="left", fill=None, expand=False)
        self.result3 = Text(f3, width = 5, height=1, wrap =WORD)
        self.result3.pack(side="left", fill=None, expand=False)
        f3.grid(row=16, column=0, sticky="w")

        path = 'http://thebacklabel.com/wp-content/uploads/2013/09/WA-Logo-1050x538.jpg'
        r = requests.get(path)
        image = Image.open(StringIO(r.content))
        image = image.resize((600, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.image = photo # keep a reference!
        label.grid(row=17, column=0, columnspan=2, sticky="w")

    # Update basic assumptions
    def update_1(self):
        self.new_member = self.custom1.get()
        try:
            self.new_member = int(self.new_member)
        except ValueError:
            message = "Not an integer!\n"
            self.text.insert(0.0, message)
        message = 'New Members per Day is set to be: %i\n' % self.new_member
        self.text.insert(0.0, message)

    def update_2(self):
        self.new_gift_member = self.custom2.get()
        try:
            self.new_gift_member = int(self.new_gift_member)
        except ValueError:
            message = "Not an integer!\n"
            self.text.insert(0.0, message)
        message = 'New Gift Members per Day is set to be: %i\n' % self.new_gift_member
        self.text.insert(0.0, message)

    def update_3(self):
        self.avg_additional_churn = self.custom3.get()
        try:
            self.avg_additional_churn = float(self.avg_additional_churn)
        except ValueError:
            message = "Not a decimal!\n"
            self.text.insert(0.0, message)
        message = 'Avg Additional Churn is set to be: %.3f\n' % self.avg_additional_churn
        self.text.insert(0.0, message)

    def update_4(self):
        self.buffer = self.custom4.get()
        try:
            self.buffer = int(self.buffer)
        except ValueError:
            message = "Not an integer!\n"
            self.text.insert(0.0, message)
        message = 'Buffer is set to be: %i\n' % self.buffer
        self.text.insert(0.0, message)

    def update_5(self):
        self.r2w1_percent = self.custom5.get()
        try:
            self.r2w1_percent = float(self.r2w1_percent)
            self.r1w2_percent = 1 - self.r2w1_percent
        except ValueError:
            message = "Not a decimal!\n"
            self.text.insert(0.0, message)
        message = 'Percentage of Variety Packs containing 2 Whites is set to be: %.2f\n' \
                  'Percentage of Variety Packs containing 2 Reds is set to be: %.2f\n' \
                  % (self.r1w2_percent, self.r2w1_percent)
        self.text.insert(0.0, message)

    dt = ''
    def update_6(self):
        # warning: current date should always before day 27th.
        self.dt = parser.parse(self.custom6.get())
        message = "The date of interest is set to be: %s\n" % self.dt
        self.text.insert(0.0, message)

        # download the report using Subscribepro API
    df = pd.DataFrame()
    def sp_collect(self):
        message1 = 'Starting to download Complete Subscription Report...\n'

        # get access_token via SSH
        params_access = {
            "grant_type": "client_credentials",
            "client_id": "1247_2cxqsrmdt3y8w0gs888kkocskw8s8w4gkws00kk8oskwgkccko",
            "client_secret": "3dk8v8i4px4w004cg8wg0cgskc4g0ccs0go4wwgkwsk0gg4g40"
        }

        url_access = "https://api.subscribepro.com/oauth/v2/token"
        r_access = requests.get(url_access, params=params_access)
        message2= "Token request status code:"+str(r_access.status_code)+"\n"

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
            message3 = "Successfully downloaded.\n"
        except:
            message3 = "Connection failed.\n"
        # print logs
        breaker = "------------\n"
        self.text.insert(0.0, breaker)
        self.text.insert(0.0, message3)
        self.text.insert(0.0, message2)
        self.text.insert(0.0, message1)
        self.text.insert(0.0, breaker)

    # print out the basic stats from the downloaded report
    days = 0
    overall_churn = 0
    wa = 0
    perc_red = 0
    perc_white = 0
    est_total_pack = 0
    def print_stats(self):
        self.result1.delete(1.0, END)
        # define the criterion dates to be evaluated
        start = self.dt.strftime('%Y-%m-%d')
        left = self.dt.strftime('%Y-%m')+"-27"
        right = self.dt.strftime('%Y-%m')+"-28"
        end = (parser.parse(left) + relativedelta(months=+1)).strftime('%Y-%m-%d')
        self.days = (parser.parse(right)-parser.parse(start)).days

        # estimate overall churn based on last two-month subscriptions
        create_left = (parser.parse(self.dt.strftime('%Y-%m')+"-01") + relativedelta(months=-2)).strftime('%Y-%m-%d')
        create_right = (parser.parse(self.dt.strftime('%Y-%m')+"-30") + relativedelta(months=-1)).strftime('%Y-%m-%d')

        message1 = "Starting to print stats...\n"
        df_oc = self.df[(self.df.Created >= create_left) & (self.df.Created <= create_right)
                        & (self.df['Exp Date'] == "")]
        bottom = len(df_oc.index)
        df_oc_top = df_oc[(df_oc['Lst Ord Date'] == "") & ((df_oc.Status == "cancelled") | (df_oc.Status == 'failed'))]
        top = len(df_oc_top.index)
        self.overall_churn = top/float(bottom)
        message2 = "From %s to %s, # of subscriptions created: %d, # of fm churn: %d.\n" \
                   "Estimated Overall Churn, incl. Failed: %.2f\n" \
                   % (create_left,create_right,bottom,top,self.overall_churn)

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
        message3 = "Non-gift Customer Stats...\n" \
                   "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i,\n" \
                   "# of red 6: %i, # of white 6: %i, # of variety 6: %i;\n" \
                   "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i,\n" \
                   "# of red 6: %i, # of white 6: %i, # of variety 6: %i;\n"\
                   % (start, left, red3_1, white3_1,variety3_1, red6_1, white6_1, variety6_1,
                      right, end, red3_2, white3_2, variety3_2, red6_2, white6_2, variety6_2)
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
        message4 = "Gift Customer Stats...\n" \
                   "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i, # of variety 6: %i;\n"\
                   "From %s to %s,\n# of red 3: %i, # of white 3: %i, # of variety 3: %i, # of variety 6: %i.\n"\
                   % (start, left, red3_3, white3_3,variety3_3, variety6_3,
                      right, end, red3_4, white3_4, variety3_4, variety6_4)

        # overall stats
        # population count (non-gift and gift)
        pop_ng = red3_1+white3_1+variety3_1+red6_1+white6_1+variety6_1+\
                 red3_2+white3_2+variety3_2+red6_2+white6_2+variety6_2
        pop_gi = red3_3+white3_3+variety3_3+variety6_3+\
                 red3_4+white3_4+variety3_4+variety6_4
        pop_total = pop_ng+pop_gi
        message5 = "We have %d active members with a valid next order date in total.\n" \
                   "%d non-gift customers, and %d gift customers.\n" % (pop_total, pop_ng, pop_gi)
        # estimate weighted avg bottles per pack
        pack3 = red3_1+red3_2+red3_3+red3_4+\
                white3_1+white3_2+white3_3+white3_4+\
                variety3_1+variety3_2+variety3_3+variety3_4
        pack6 = red6_1+red6_2+white6_1+white6_2+\
                variety6_1+variety6_2+variety6_3+variety6_4
        self.wa = 3*pack3/float(pack3+pack6) + 6*pack6/float(pack3+pack6)
        message6 = "%d 3-bottle packs, and %d 6-bottle packs;\n" \
                   "Estimated weighted avg per pack is %.3f.\n" % (pack3,pack6,self.wa)

        # red:white ratio count
        num_of_red = ceil(3*(red3_1+red3_2+red3_3+red3_4+variety6_1+variety6_2)+6*(red6_1+red6_2)
                          +self.r2w1_percent*2*(variety3_1+variety3_2+variety3_3+variety3_4))
        num_of_white = ceil(3*(white3_1+white3_2+white3_3+white3_4+variety6_1+variety6_2)+6*(white6_1+white6_2)
                          +self.r1w2_percent*2*(variety3_1+variety3_2+variety3_3+variety3_4))
        self.perc_red = num_of_red/float(num_of_red+num_of_white)
        self.perc_white = 1 - self.perc_red
        message7 = "The red:white ratio is %.2f:%.2f.\n" % (self.perc_red, self.perc_white)
        self.est_total_pack = int(ceil((pop_total+self.new_member*self.days*(1-self.overall_churn))\
                                   *(1-self.avg_additional_churn)+pop_gi+self.new_gift_member*self.days+self.buffer))
        message8 = "Total # of package we should order for: %i\n" % self.est_total_pack
        # print logs
        breaker = "------------\n"
        self.text.insert(0.0, breaker)
        self.text.insert(0.0, message8)
        self.text.insert(0.0, message7)
        self.text.insert(0.0, message6)
        self.text.insert(0.0, message5)
        self.text.insert(0.0, message4)
        self.text.insert(0.0, message3)
        self.text.insert(0.0, message2)
        self.text.insert(0.0, message1)
        self.text.insert(0.0, breaker)
        self.result1.insert(0.0, self.est_total_pack)

    # Break-down into number of bottles per type of wine
    def wine_order_breakdown(self):
        message1 = 'Starting to compute each number of bottles needed...\n'
        self.result2.delete(1.0, END)
        self.result3.delete(1.0, END)
        total_bottles = ceil(self.est_total_pack*self.wa)
        red_bottles = ceil(total_bottles*self.perc_red)
        white_bottles = total_bottles - red_bottles
        message2 = "Total Wines needed (in bottles): %i; Red needed is %i, White needed is %i.\n"\
                   % (total_bottles,red_bottles,white_bottles)
        cases = [ceil(total_bottles/12.0), ceil(red_bottles/12.0), ceil(white_bottles/12.0)]
        num_each = [int(ceil(cases[1]/3.0)),int(ceil(cases[2]/3.0))]
        message3 = "Total Cases needed: %i; Red needed is %i, White needed is %i.\n" \
                   "Number of each red needed is %i; Number of each white needed is %i.\n" \
                   % (cases[0],cases[1],cases[2], num_each[0],num_each[1])
        # print logs
        breaker = "------------\n"
        self.text.insert(0.0, breaker)
        self.text.insert(0.0, message3)
        self.text.insert(0.0, message2)
        self.text.insert(0.0, message1)
        self.text.insert(0.0, breaker)
        self.result2.insert(0.0, num_each[0])
        self.result3.insert(0.0, num_each[1])

if __name__==  "__main__":
    root = Tk()
    root.title("FulfillmentCalcs")
    root.geometry("1020x680")
    app = Application(root)
    # type ESC to terminate
    root.bind("<Escape>", lambda e: root.quit())
    root.mainloop()
