from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Account(models.Model):
    account_id = models.BigIntegerField(primary_key = True)
    account_descriptive_name = models.CharField(max_length = 256)
    customer_descriptive_name = models.CharField(max_length = 256)

class Campaign(models.Model):
    campaign_id = models.BigIntegerField(primary_key = True)
    campaign_name = models.CharField(max_length = 256)
    campaign_status = models.CharField(max_length = 256)
    account = models.ForeignKey(Account, on_delete = models.CASCADE)

class Advertisement(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete = models.CASCADE)

    # These Ids should be foreign keys, but I don't have the data to make their tables useful
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
