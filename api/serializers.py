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

    def handle_params(request, ad_set):
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        start = request.GET.get('start_date','1000-1-1')
        end = request.GET.get('end_date', now())
        order_by = request.GET.get('order_by', 'clicks')
        order = request.GET.get('order', 'asc')
        order = '-' if order == 'desc' else ''
        ads = ad_set.filter(date__range=[start, end]).order_by("%s%s" % ( order, order_by ) )[offset:limit]
        # ads = list(ads.values("clicks").annotate(Avg("impressions")))
        # print(ads)
        # if filter:
        #     ads = ads.values('cost')
        return ads
