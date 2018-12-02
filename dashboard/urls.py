from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name = 'home'),
    url(r'^api/v1/accounts/$', account_collection, name = 'account_collection'),
    url(r'^api/v1/accounts/(?P<pk>[0-9]+)$', account_element, name = 'account_element'),
    url(r'^api/v1/campaigns/$', campaign_collection, name = 'campaign_collection'),
    url(r'^api/v1/campaigns/(?P<pk>[0-9]+)/advertisements$', campaign_advertisements, name = 'campaign_element'),
    url(r'^api/v1/advertisements/$', advertisement_collection, name = 'advertisement_collection'),
    url(r'^api/v1/advertisements/(?P<pk>[0-9]+)$', advertisement_element, name = 'advertisement_element')
]
