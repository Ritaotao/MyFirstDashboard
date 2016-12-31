#python first
#django second
#your apps
#local directory

from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.db.models import Q, F
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

from .models import CompleteSubscription, Update, Result, NODSplit
from .forms import UpdateForm

from math import ceil
import requests
import re
from dateutil.relativedelta import relativedelta
import warnings
warnings.filterwarnings("ignore") # to disable warnings from pandas

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    form = UpdateForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Parameters successfully updated!')
        return HttpResponseRedirect('/membership/')

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def download(request):
    # delete existing records
    CompleteSubscription.objects.all().delete()
    #get access_token via SSH
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
    def ifelse(self):
        if self == '':
            return None
        else:
            return self

    for row in out2:
        csreport = CompleteSubscription()
        csreport.entry_id = ifelse(row[0])
        csreport.status = row[1]
        csreport.lst_ord_date = ifelse(row[2])
        csreport.nxt_ord_date = ifelse(row[3])
        csreport.interval = row[4]
        csreport.exp_date = ifelse(row[5])
        csreport.cust_id = ifelse(row[6])
        csreport.mage_cust_id = ifelse(row[7])
        csreport.first = row[8]
        csreport.last = row[9]
        csreport.email = row[10]
        csreport.prod_id = ifelse(row[11])
        csreport.prod_name = row[12]
        csreport.sku = row[13]
        csreport.price = ifelse(row[14])
        csreport.discount = ifelse(row[15])
        csreport.qty = ifelse(row[16])
        csreport.ship_method = row[17]
        csreport.mage_bill_addy = ifelse(row[18])
        csreport.mage_ship_addy = ifelse(row[19])
        csreport.payment_token = row[20]
        csreport.coupon = row[21]
        csreport.created = ifelse(row[22])
        csreport.updated = ifelse(row[23])
        csreport.save()

    if r_access.status_code == 200:
        messages.success(request, 'Complete Subscription Report successfully downloaded.')
        return HttpResponseRedirect('/membership/')

@login_required(login_url='/login/')
def insight(request):
    param = Update.objects.order_by('-pk')[0]

    # get the date range of interest
    start = param.start_date
    left = start.replace(day=27)
    right = start.replace(day=28)
    end = left + relativedelta(months=+1)
    days = (right-start).days

    # churn analysis with two months historical non-gift
    create_right = start.replace(day=1)
    create_left = create_right + relativedelta(months=-2)
    df = CompleteSubscription.objects.filter(exp_date=None)\
        .filter(created__gte=create_left).filter(created__lte=create_right)
    denom = df.count() # number of subscriptions created within last two months
    df_oa = df.filter(Q(status='cancelled') | Q(status='failed'))
    df_fm = df_oa.filter(lst_ord_date=None)
    num_fm = df_fm.count() # number of fm churn
    num_nfm = df_oa.count() - num_fm
    fm_churn = num_fm/float(denom) # fm churn
    nfm_churn = num_nfm/float(denom) # nfm churn

    # prepare feeding data
    df_active = CompleteSubscription.objects.filter(status='active')
    df_1 = df_active.filter(interval='Every Month').filter(nxt_ord_date__gte=start).filter(nxt_ord_date__lte=left)
    df_2 = df_active.filter(nxt_ord_date__gte=right).filter(nxt_ord_date__lte=end)

    # non-gift customers
    df1 = df_1.filter(exp_date=None)
    df2 = df_2.filter(exp_date=None)

    red3_1 = df1.filter(sku__contains='red-3').count()
    white3_1 = df1.filter(sku__contains='white-3').count()
    variety3_1 = df1.filter(Q(sku__contains='variety-3') | Q(sku__contains='variety3')).count()
    red6_1 = df1.filter(sku__contains='red-6').count()
    white6_1 = df1.filter(sku__contains='white-6').count()
    variety6_1 = df1.filter(sku__contains='variety-6').count()

    red3_2 = df2.filter(sku__contains='red-3').count()
    white3_2 = df2.filter(sku__contains='white-3').count()
    variety3_2 = df2.filter(Q(sku__contains='variety-3') | Q(sku__contains='variety3')).count()
    red6_2 = df2.filter(sku__contains='red-6').count()
    white6_2 = df2.filter(sku__contains='white-6').count()
    variety6_2 = df2.filter(sku__contains='variety-6').count()

    # gift customers
    df3 = df_1.filter(exp_date__gt=F('nxt_ord_date')+relativedelta(months=+1))
    df4 = df_2.filter(exp_date__gt=F('nxt_ord_date'))

    red3_3 = df3.filter(Q(sku__contains='red-3')|Q(sku__regex=r'gift.*red.*')).count()
    white3_3 = df3.filter(Q(sku__contains='white-3')|Q(sku__regex=r'gift.*white.*')).count()
    variety3_3 = df3.filter(Q(sku__contains='variety-3')|Q(sku__regex=r'gift.*variety.*')).count()

    red3_4 = df4.filter(Q(sku__contains='red-3')|Q(sku__regex=r'gift.*red.*')).count()
    white3_4 = df4.filter(Q(sku__contains='white-3')|Q(sku__regex=r'gift.*white.*')).count()
    variety3_4 = df4.filter(Q(sku__contains='variety-3')|Q(sku__regex=r'gift.*variety.*')).count()

    # overall stats
    # population count (non-gift and gift)
    pop_ng = red3_1+white3_1+variety3_1+red6_1+white6_1+variety6_1+\
             red3_2+white3_2+variety3_2+red6_2+white6_2+variety6_2
    pop_gi = red3_3+white3_3+variety3_3+red3_4+white3_4+variety3_4
    pop_tot = pop_ng+pop_gi

    # red:white bottle ratio
    bot_red = int(ceil(3*(red3_1+red3_2+red3_3+red3_4+variety6_1+variety6_2)+6*(red6_1+red6_2)\
                 +2*param.r2w1_percent*(variety3_1+variety3_2+variety3_3+variety3_4)))
    r1w2_percent = 1 - param.r2w1_percent
    bot_white = int(ceil(3*(white3_1+white3_2+white3_3+white3_4+variety6_1+variety6_2)+6*(white6_1+white6_2)\
                   +r1w2_percent*2*(variety3_1+variety3_2+variety3_3+variety3_4)))
    red_perc = bot_red/float(bot_red+bot_white)
    white_perc = 1 - red_perc

    # weighted avg bottles per pack
    pop_3pack = red3_1+red3_2+red3_3+red3_4+\
            white3_1+white3_2+white3_3+white3_4+\
            variety3_1+variety3_2+variety3_3+variety3_4
    pop_6pack = red6_1+red6_2+white6_1+white6_2+variety6_1+variety6_2
    wa = 3*pop_3pack/float(pop_3pack+pop_6pack) + 6*pop_6pack/float(pop_3pack+pop_6pack)

    # estimated total pack to order
    tot_pack = int(ceil(pop_ng*(1-nfm_churn)+param.new_member*days*(1-fm_churn)\
                        +pop_gi+param.new_gift_member*days+param.buffer))
    tot_bottles = int(ceil(tot_pack*wa))
    red_bottles = int(ceil(tot_bottles*red_perc))
    white_bottles = tot_bottles - red_bottles
    red_cases = int(ceil(red_bottles/12.0))
    white_cases = int(ceil(white_bottles/12.0))
    tot_cases = red_cases+white_cases
    reds_each = int(ceil(red_cases/3.0))
    whites_each = int(ceil(white_cases/3.0))

    result = Result()
    nod = NODSplit()
    result.update = param
    result.start = start
    result.end = end
    result.fm_churn = fm_churn
    result.nfm_churn = nfm_churn
    result.pop_tot = pop_tot
    result.pop_ng = pop_ng
    result.pop_gi = pop_gi
    result.bot_red = bot_red
    result.bot_white = bot_white
    result.red_perc = red_perc
    result.white_perc = white_perc
    result.pop_3pack = pop_3pack
    result.pop_6pack = pop_6pack
    result.wa = wa
    result.tot_pack = tot_pack
    result.tot_bottles = tot_bottles
    result.red_bottles = red_bottles
    result.white_bottles = white_bottles
    result.tot_cases = tot_cases
    result.red_cases = red_cases
    result.white_cases = white_cases
    result.reds_each = reds_each
    result.whites_each = whites_each
    result.save()

    nod.update = param
    nod.start = start
    nod.left = left
    nod.ng_red3_l = red3_1
    nod.ng_white3_l = white3_1
    nod.ng_variety3_l = variety3_1
    nod.ng_red6_l = red6_1
    nod.ng_white6_l = white6_1
    nod.ng_variety6_l = variety6_1
    nod.g_red3_l = red3_3
    nod.g_white3_l = white3_3
    nod.g_variety3_l = variety3_3
    nod.right = right
    nod.end = end
    nod.ng_red3_r = red3_2
    nod.ng_white3_r = white3_2
    nod.ng_variety3_r = variety3_2
    nod.ng_red6_r = red6_2
    nod.ng_white6_r = white6_2
    nod.ng_variety6_r = variety6_2
    nod.g_red3_r = red3_4
    nod.g_white3_r = white3_4
    nod.g_variety3_r = variety3_4
    nod.save()
    if reds_each >= 0 & whites_each>=0:
        message1 = 'Quick View: Red Bottles: %i; White Bottles: %i. To see details, click <Details>.' %(reds_each, whites_each)
    else:
        message1 = 'There\'s something wrong.'
    messages.success(request, message1)
    return HttpResponseRedirect('/membership/')

@login_required(login_url='/login/')
def detail(request):
    param = Update.objects.order_by('-pk')[0]
    result = Result.objects.filter(update=param).order_by('-pk')[0]
    nod = NODSplit.objects.filter(update=param).order_by('-pk')[0]
    round_r2w1_percent = round(param.r2w1_percent*100, 2)
    round_fm_churn = round(result.fm_churn*100, 2)
    round_nfm_churn = round(result.nfm_churn*100, 2)
    round_red_perc = round(result.red_perc*100, 2)
    round_white_perc = round(result.white_perc*100, 2)
    real_red = result.reds_each*36
    real_white = result.whites_each*36
    real_tot = real_red+real_white
    context = {
        "start": result.start,
        "end": result.end,
        "r2w1_percent": round_r2w1_percent,
        "new_member": param.new_member,
        "new_gift_member": param.new_gift_member,
        "buffer": param.buffer,
        "fm_churn": round_fm_churn,
        "nfm_churn": round_nfm_churn,
        "pop_tot": result.pop_tot,
        "pop_ng": result.pop_ng,
        "pop_gi": result.pop_gi,
        "pop_3pack": result.pop_3pack,
        "pop_6pack": result.pop_6pack,
        "left": nod.left,
        "right": nod.right,
        "ng_red3_l": nod.ng_red3_l,
        "ng_white3_l": nod.ng_white3_l,
        "ng_variety3_l": nod.ng_variety3_l,
        "ng_red6_l": nod.ng_red6_l,
        "ng_white6_l": nod.ng_white6_l,
        "ng_variety6_l": nod.ng_variety6_l,
        "g_red3_l": nod.g_red3_l,
        "g_white3_l": nod.g_white3_l,
        "g_variety3_l": nod.g_variety3_l,
        "ng_red3_r": nod.ng_red3_r,
        "ng_white3_r": nod.ng_white3_r,
        "ng_variety3_r": nod.ng_variety3_r,
        "ng_red6_r": nod.ng_red6_r,
        "ng_white6_r": nod.ng_white6_r,
        "ng_variety6_r": nod.ng_variety6_r,
        "g_red3_r": nod.g_red3_r,
        "g_white3_r": nod.g_white3_r,
        "g_variety3_r": nod.g_variety3_r,
        "red_perc": round_red_perc,
        "white_perc": round_white_perc,
        "wa": result.wa,
        "tot_pack": result.tot_pack,
        "tot_bottles": result.tot_bottles,
        "red_bottles": result.red_bottles,
        "white_bottles": result.white_bottles,
        "tot_cases": result.tot_cases,
        "red_cases": result.red_cases,
        "real_red": real_red,
        "real_white": real_white,
        "real_tot": real_tot,
        "white_cases": result.white_cases,
        "reds_each": result.reds_each,
        "whites_each": result.whites_each
    }

    return render(request, 'detail.html', context)



