from __future__ import unicode_literals
from django.db import models
import datetime
# Create your models here.
class CompleteSubscription(models.Model):
    entry_id = models.IntegerField(default=None)
    status = models.CharField(max_length=100, blank=True)
    lst_ord_date = models.DateTimeField(null=True, blank=True)
    nxt_ord_date = models.DateField(null=True, blank=True)
    interval = models.CharField(max_length=200, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    cust_id = models.IntegerField(null=True, blank=True)
    mage_cust_id = models.IntegerField(null=True, blank=True)
    first = models.CharField(max_length=200, blank=True)
    last = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    prod_id = models.IntegerField(null=True, blank=True)
    prod_name = models.CharField(max_length=200, blank=True)
    sku = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0, blank=True)
    discount = models.DecimalField(max_digits=12, decimal_places=4, default=0, blank=True)
    qty = models.IntegerField(default=0)
    ship_method = models.CharField(max_length=200, blank=True)
    mage_bill_addy = models.IntegerField(null=True, blank=True)
    mage_ship_addy = models.IntegerField(null=True, blank=True)
    payment_token = models.CharField(max_length=200, blank=True)
    coupon = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "%i, %s\n" % (self.entry_id, self.exp_date)

# query parameters
class Update(models.Model):
    start_date = models.DateField(default=datetime.date.today)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    new_member = models.IntegerField(default=10)
    new_gift_member = models.IntegerField(default=0)
    buffer = models.IntegerField(default=100)
    r2w1_percent = models.DecimalField(max_digits=6, decimal_places=4, default=0.6)

    def __unicode__(self):
        return "%i" % (self.id)

# fulfillment calculation result
class Result(models.Model):
    update = models.ForeignKey(Update, on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateField()
    end = models.DateField()
    fm_churn = models.DecimalField(max_digits=12, decimal_places=4)
    nfm_churn = models.DecimalField(max_digits=12, decimal_places=4)
    pop_ng = models.IntegerField()
    pop_gi = models.IntegerField()
    pop_tot = models.IntegerField()
    pop_3pack = models.IntegerField()
    pop_6pack = models.IntegerField()
    wa = models.DecimalField('weighted_average',max_digits=12, decimal_places=4)
    bot_red = models.IntegerField()
    bot_white = models.IntegerField()
    red_perc = models.DecimalField(max_digits=12, decimal_places=4)
    white_perc = models.DecimalField(max_digits=12, decimal_places=4)
    tot_pack = models.IntegerField()
    tot_bottles = models.IntegerField()
    red_bottles = models.IntegerField()
    white_bottles = models.IntegerField()
    tot_cases = models.IntegerField()
    red_cases = models.IntegerField()
    white_cases = models.IntegerField()
    reds_each = models.IntegerField()
    whites_each = models.IntegerField()


# valid next order date subscriptions split     
class NODSplit(models.Model):
    update = models.ForeignKey(Update, on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateField()
    left = models.DateField()
    ng_red3_l = models.IntegerField()
    ng_white3_l = models.IntegerField()
    ng_variety3_l = models.IntegerField()
    ng_red6_l = models.IntegerField()
    ng_white6_l = models.IntegerField()
    ng_variety6_l = models.IntegerField()
    g_red3_l = models.IntegerField()
    g_white3_l = models.IntegerField()
    g_variety3_l = models.IntegerField()
    right = models.DateField()
    end = models.DateField()
    ng_red3_r = models.IntegerField()
    ng_white3_r = models.IntegerField()
    ng_variety3_r = models.IntegerField()
    ng_red6_r = models.IntegerField()
    ng_white6_r = models.IntegerField()
    ng_variety6_r = models.IntegerField()
    g_red3_r = models.IntegerField()
    g_white3_r = models.IntegerField()
    g_variety3_r = models.IntegerField()
    red3_perc = models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
    white3_perc = models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
    red6_perc = models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
    white6_perc = models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
    variety3_perc = models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)
    variety6_perc = models.DecimalField(max_digits=12, decimal_places=4,null=True, blank=True)





