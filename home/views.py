from django.shortcuts import render
import requests
from django.http import JsonResponse
import datetime

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

def coinPrice(request):
    try:
        data = requests.get(URL).json()
        return render(request, "home/price_table.html", {"data": data})
    except ValueError:
        print("Your network is dis' contected")


def time(request):
    now = datetime.datetime.now()
    return JsonResponse({'current_datetime': now.strftime('%Y-%m-%d %H:%M:%S')})
