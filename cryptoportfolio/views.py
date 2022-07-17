from curses.ascii import HT
from operator import index
import re
from django.shortcuts import render
from django.http import HttpResponse
import ccxt
import datetime
import cryptoportfolio
from cryptoportfolio.forms import CryptoForm  
from cryptoportfolio.models import Crypto
from django.http import HttpResponseRedirect
from django.forms import Form
from datetime import datetime
def index(request):
  Cryptos=Crypto.objects.get(crypto_name='BTC')
  old_time=str(Cryptos.added_time.replace(second=0, microsecond=0))
  old_time=old_time[:19]
  ct =str(datetime.utcnow().replace(second=0, microsecond=0))
  exchange = ccxt.binance()
  stored_time = int(datetime.strptime(old_time, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
  current_time=int(datetime.strptime(ct, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
  price_current_time = exchange.fetch_ohlcv('BTC/USDT', '1m',current_time, 1)
  price_added_time = exchange.fetch_ohlcv('BTC/USDT', '1m', stored_time, 1)
  total=int(price_added_time[0][4])-int(price_current_time[0][4])
  x=price_added_time[0][4]
  y=price_current_time[0][4]
  context={'x':x, 'y':y, 'total':total}
  return render(request, 'cryptoportfolio/index.html', context)