from django.contrib import admin

# Register your models here.
from .models import CompleteSubscription, Update, Result, NODSplit

class CompleteSubscriptionAdmin(admin.ModelAdmin):
    list_display=('entry_id','status','lst_ord_date','nxt_ord_date','interval','exp_date','cust_id','mage_cust_id',
                  'first','last','email','prod_id','prod_name','sku','price','discount','qty','ship_method',
                  'mage_bill_addy','mage_ship_addy','payment_token','coupon','created','updated')
    list_filter = ['created']
    search_fields = ['email', 'mage_cust_id']

class UpdateAdmin(admin.ModelAdmin):
    list_display=('id', 'timestamp','start_date','new_member','new_gift_member','buffer','r2w1_percent')
    list_filter = ['timestamp']
    search_fields = ['id']

class ResultAdmin(admin.ModelAdmin):
    list_display=(
            'update','start','end','fm_churn','nfm_churn','pop_ng','pop_gi','pop_tot','pop_3pack','pop_6pack','wa',
            'bot_red','bot_white','red_perc','white_perc','tot_pack','tot_bottles','red_bottles','white_bottles',
            'tot_cases','red_cases','white_cases','reds_each','whites_each')
    search_fields = ['update']

class NODSplitAdmin(admin.ModelAdmin):
    list_display=(
        'update','start','left','ng_red3_l','ng_white3_l','ng_variety3_l','ng_red6_l','ng_white6_l','ng_variety6_l',
        'g_red3_l','g_white3_l','g_variety3_l','right','end','ng_red3_r','ng_white3_r','ng_variety3_r','ng_red6_r',
        'ng_white6_r','ng_variety6_r','g_red3_r','g_white3_r','g_variety3_r', 'red3_perc', 'white3_perc', 'red6_perc', 'white6_perc', 'variety3_perc', 'variety6_perc'
    )
    search_fields = ['update']

admin.site.register(CompleteSubscription, CompleteSubscriptionAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(NODSplit, NODSplitAdmin)