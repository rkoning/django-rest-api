from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Advertisement
# Create your views here.

def index(request):
    recent_ads = Advertisement.objects.order_by('-date')[:5]
    context = { 'recent_ads' : recent_ads }
    output = ', '.join([str(ad) for ad in recent_ads])
    return render(request, 'dashboard/index.html', context)

def detail(request, advertisement_id):
    return HttpResponse("You're looking at: %s" % advertisement_id)

def results(request, advertisement_id):
    response = "You're looking at the results of %s."
    return HttpResponse(response % advertisement_id)
