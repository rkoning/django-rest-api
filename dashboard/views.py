from django.shortcuts import render
from api.models import Account

# Create your views here.
def index(request):
    account = Account.objects.all()[0]
    campaigns = account.campaign_set.all()
    return render(request, 'index.html', context = { 'account' : account, 'account_campaigns' : campaigns })
