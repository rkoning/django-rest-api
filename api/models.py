from django.db import models
from django.db.models import Avg
import uuid
from django.contrib.postgres.fields import ArrayField
from collections import defaultdict
# Create your models here.

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    ext_account_id = models.BigIntegerField(default = 0)
    account_descriptive_name = models.CharField(max_length = 256)
    customer_descriptive_name = models.CharField(max_length = 256)

class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    ext_campaign_id = models.BigIntegerField(default = 0)
    campaign_name = models.CharField(max_length = 256)
    campaign_status = models.CharField(max_length = 256)
    account = models.ForeignKey(Account, on_delete = models.CASCADE)

    def get_average_of_advertisements(attr):
        return self.advertisement_set.aggregate(Avg(attr)).values()[0]

    def get_sum_by_time(self):
        sums = defaultdict(int)
        for o in self.advertisement_set.order_by('date'):
            sums[o.date] += o.clicks
        return sums

class Advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    # reference to the campaign that this Ad is part of
    campaign = models.ForeignKey(Campaign, on_delete = models.CASCADE)
    # These ids should be foreign keys,
    # but I don't have the data to make their tables useful
    # so alas they will be BigInts
    city_criteria_id = models.BigIntegerField(null = True)
    country_criteria_id = models.BigIntegerField(null = True)
    metro_criteria_id = models.BigIntegerField(null = True)
    most_specific_criteria_id = models.BigIntegerField(null = True)
    region_criteria_id = models.BigIntegerField(null = True)

    date = models.DateField()
    device = models.CharField(max_length = 256)
    is_targeting_location = models.BooleanField(default = False)
    location_type = models.CharField(max_length = 256)
    average_position = models.FloatField(default = 0.0)
    clicks = models.IntegerField(default = 0)
    conversions = models.FloatField(default = 0.0)
    conversion_value = models.FloatField(default = 0.0)
    cost = models.FloatField(default = 0.0)
    impressions = models.IntegerField(default = 0)
    interactions = models.IntegerField(default = 0)
    interaction_types = ArrayField(models.CharField(max_length = 256), size = 8)
    video_views = models.IntegerField(default = 0)

    def __str__(self):
        return "%s %s %s" % (self.date, self.device, self.cost)
