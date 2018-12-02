from django.shortcuts import render
import requests
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Advertisement, Account, Campaign
from .serializers import AccountSerializer, CampaignSerializer, AdvertisementSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def account_collection(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def account_element(request, pk):
    try:
        account = Account.objects.get(pk = pk)
    except Account.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def campaign_collection(request):
    if request.method == 'GET':
        limit = int(request.GET.get('limit', 100))
        offset = int(request.GET.get('offset', 0))
        campaigns = Campaign.objects.all()[offset:limit]
        # serializer = CampaignSerializer(campaigns, many = True)
        # return Response(serializer.data)
        response = serializers.serialize("json", campaigns)
        return JsonResponse(response, content_type = "application/json")
    elif request.method == 'POST':
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        response = serializers.serialize("json", AdvertisementSerializer.handle_params(request, campaign.advertisement_set))
        return HttpResponse(response, content_type = "application/json")
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
