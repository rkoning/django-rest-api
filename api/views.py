import requests

from django.core import serializers
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Advertisement, Account, Campaign
from .serializers import AccountSerializer, CampaignSerializer, AdvertisementSerializer
from oauth2_provider.decorators import protected_resource

@api_view(['GET', 'POST'])
def account_collection(request):
    """
    get:
    Returns a list of all accounts

    post:
    Creates a new account
    """
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def account_element(request, pk):
    """
    get:
    retrieves the account by its primary key
    delete:
    deletes the account by its primary key
    put:
    Updates the account by its primary key
    """
    try:
        account = Account.objects.get(pk = pk)
    except Account.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        account.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def account_campaigns(request, pk):
    """
    get:
    Returns a list of all campaigns in this account
    """
    if request.method == 'GET':
        try:
            account = Account.objects.get(pk = pk)
            response = serializers.serialize("json", account.campaign_set.all())
            return HttpResponse(response, content_type = "application/json")
        except Account.DoesNotExist:
            return HttpResponse(status = 404)

@api_view(['GET', 'POST'])
def campaign_collection(request):
    """
    get:
    Returns a list of all campaigns

    post:
    Creates a new campaign
    """
    if request.method == 'GET':
        limit = int(request.GET.get('limit', 100))
        if limit > 100:
            limit = 100
        elif limit < 1:
            limit = 1
        offset = int(request.GET.get('offset', 0))
        campaigns = Campaign.objects.all()[offset:offset + limit]
        # serializer = CampaignSerializer(campaigns, many = True)
        # return Response(serializer.data)
        response = serializers.serialize("json", campaigns)
        return JsonResponse(response, content_type = "application/json")
    elif request.method == 'POST':
        serializer = CampaignSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def campaign_element(request, pk):
    """
    get:
    retrieves the campaign by its primary key
    delete:
    deletes the campaign by its primary key
    put:
    Updates the campaign by its primary key
    """
    try:
        campaign = Campaign.objects.get(pk = pk)
    except Campaign.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        campaign.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def campaign_advertisements(request, pk):
    """
    get:
    Returns a list of all advertisements in this campaign
    """
    if request.method == 'GET':
        try:
            campaign = Campaign.objects.get(pk = pk)
            response = serializers.serialize("json", Advertisement.handle_params(request, campaign.advertisement_set), fields=(request.GET.get('fields', None)))
            return HttpResponse(response, content_type = "application/json")
        except Campaign.DoesNotExist:
            return HttpResponse(status = 404)

@api_view(['GET', 'POST'])
def advertisement_collection(request):
    """
    get:
    Returns a list of all advertisements filtered by query parameters

    post:
    Creates a new advertisement
    """
    if request.method == 'GET':
        response = serializers.serialize("json", Advertisement.handle_params(request, Advertisement.objects.all()), fields=(request.GET.get('fields', None)))
        return HttpResponse(response, content_type = "application/json")
    if request.method == 'POST':
        serializer = AdvertisementSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def advertisement_element(request, pk):
    """
    get:
    retrieves the advertisement by its primary key
    delete:
    deletes the advertisement by its primary key
    put:
    Updates the advertisement by its primary key
    """
    try:
        ad = Advertisement.objects.get(pk = pk)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    print(request.method)
    serializer = AdvertisementSerializer(ad)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AdvertisementSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        ad.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
