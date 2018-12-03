from rest_framework import serializers
from .models import Account, Campaign, Advertisement
import datetime

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'uuid', 'ext_account_id', 'account_descriptive_name', 'customer_descriptive_name')

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'uuid', 'ext_campaign_id', 'campaign_name', 'campaign_status', 'account')

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = (
            'id',
            'campaign',
            'city_criteria_id',
            'country_criteria_id',
            'metro_criteria_id',
            'most_specific_criteria_id',
            'region_criteria_id',
            'date',
            'device',
            'is_targeting_location',
            'location_type',
            'average_position',
            'clicks',
            'conversions',
            'conversion_value',
            'cost',
            'impressions',
            'interactions',
            'interaction_types',
            'video_views'
        )
