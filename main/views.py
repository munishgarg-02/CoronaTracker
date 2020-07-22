from django.shortcuts import render
import requests
import json
# Create your views here.

def Main(request):
    url = 'https://api.covid19api.com/summary'
    res = requests.get(url)
    dic = json.loads(res.text)
    info = dic['Countries']
    globalInfo = dic['Global']
    x = sorted(info, key = lambda i: i['TotalConfirmed'], reverse=True)
    context = {
        'x':x,
        'globalInfo':globalInfo
    }
    return render(request,'index.html',context)


def Detail(request,slug):
    url = 'https://api.covid19api.com/summary'
    res = requests.get(url)
    dic = json.loads(res.text)
    info = dic['Countries']
    globalInfo = dic['Global']
    for x in info:
        if slug == x['Slug']:
            if slug == 'india':
                url='https://covid-19india-api.herokuapp.com/v2.0/state_data'
                res = requests.get(url)
                lis = json.loads(res.text)
                y = lis[1]['state_data']
                dic = sorted(y,key=lambda i:i['confirmed'],reverse=True)
                context={
                    'x':x,
                    'globalInfo':globalInfo,
                    'dic':dic
                }
                break
            else:    
                context = {
                    'x':x,
                    'globalInfo':globalInfo,
                }
                break
    return render(request,'detail.html',context)


def About(request):
    return render(request,'about.html')
