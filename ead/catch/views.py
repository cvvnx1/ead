from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from catch.sales import sales
from catch.additem import additem

from time import time, localtime, strftime

# Create your views here.

def begin(request):
    begin = strftime("%Y-%m-%dT00:00:00.000Z", localtime(int(time())))
    now = strftime("%Y-%m-%dT%H:%M:%S.000Z", localtime(int(time())))
    return render_to_response('test.html', {"begin": begin, "now": now})


def list(request):
    appid = "Your appid"
    devid = "Your devid"
    certid = "Your certid"
    token = "Your token"

    list = sales(appid, devid, certid, token)
    list.auth()
    list.getOrder()

    return HttpResponse(simplejson.dumps(list.createList(), ensure_ascii=False))

def total(request):
    return render_to_response('total.html', {})

def sell(request):
    appid = "Your appid"
    devid = "Your devid"
    certid = "Your certid"
    token = "Your token"

    list = additem(appid, devid, certid, token)
    list.auth()
    list.add()

    return HttpResponse(simplejson.dumps(list.createList(), ensure_ascii=False))

