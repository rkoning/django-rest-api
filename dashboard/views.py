from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advertisement, Account, Campaign
from .serializers import AccountSerializer, CampaignSerializer, AdvertisementSerializer
# Create your views here.

def index(request):
    recent_ads = Advertisement.objects.order_by('-date')
    context = { 'recent_ads' : recent_ads }
    output = ', '.join([str(ad) for ad in recent_ads])
    return render(request, 'dashboard/index.html', context)
#
# def detail(request, advertisement_id):
#     return HttpResponse("You're looking at: %s" % advertisement_id)
#
# def results(request, advertisement_id):
#     response = "You're looking at the results of %s."
#     return HttpResponse(response % advertisement_id)

@api_view(['GET'])
def account_collection(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def account_element(request, pk):
    try:
        account = Account.objects.get(pk = pk)
    except Account.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

@api_view(['GET'])
def campaign_collection(request):
    if request.method == 'GET':
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def campaign_element(request, pk):
    try:
        campaign = Campaign.objects.get(pk = pk)
    except Campaign.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

@api_view(['GET'])
def campaign_advertisements(request, pk):
    try:
        campaign = Campaign.objects.get(pk = pk)
        return Response(AdvertisementSerializer.handle_params(request, campaign.advertisement_set))
    except Campaign.DoesNotExist:
        return HttpResponse(status=404)


@api_view(['GET'])
def advertisement_collection(request):
    if request.method == 'GET':
        return Response(AdvertisementSerializer.handle_params(request, Advertisement.objects))

@api_view(['GET'])
def advertisement_element(request):
    try:
        ad = Advertisement.objects.get(pk = pk)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)
