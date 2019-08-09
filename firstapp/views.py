from django.shortcuts import render
import json
import requests
from .models import Beer_snack, Soju_snack, Whiskey_snack, Wine_snack, RiceWine_snack, Cocktail_snack

# Create your views here.
def index(request):
    r = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat=37.56667&lon=126.97806&appkey=a6101311-8fdc-403e-85c5-73d6f44b06eb")
    data = json.loads(r.text)
    weather = data["weather"]["summary"]
    cTime = weather[0]["timeRelease"]
    cPlace = weather[0]['grid']['city'] + ' ' + weather[0]['grid']['county'] + ' ' + weather[0]['grid']['village']
    cSky = weather[0]["today"]["sky"]["name"]
    cMax = weather[0]["today"]["temperature"]["tmax"]
    cMin = weather[0]["today"]["temperature"]["tmin"]
    ment=''
    if weather[0]["today"]["sky"]["name"]=='비':
        ment='비도 오는데 막걸리 한잔 어때요?'
    elif weather[0]["today"]["sky"]["name"]=='흐림':
        ment='꾸릿꾸릿한 날씨엔 맥주'
    elif weather[0]["today"]["sky"]["name"]=='맑음':
        ment='소주같이 맑은 날에는 소주'
    elif weather[0]["today"]["sky"]["name"]=='눈':
        ment='눈에는 눈 멘트 모르겠다 칵테일'

    return render(request, 'index.html', {'cSky': cSky, 'cPlace':cPlace, 'cTime':cTime, 'cMax':cMax, 'cMin':cMin,'ment':ment })

def snacks(request):
    r = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat=37.56667&lon=126.97806&appkey=a6101311-8fdc-403e-85c5-73d6f44b06eb")
    data = json.loads(r.text)
    weather = data["weather"]["summary"]
    cTime = weather[0]["timeRelease"]
    cPlace = weather[0]['grid']['city'] + ' ' + weather[0]['grid']['county'] + ' ' + weather[0]['grid']['village']
    cSky = weather[0]["today"]["sky"]["name"]
    cMax = weather[0]["today"]["temperature"]["tmax"]
    cMin = weather[0]["today"]["temperature"]["tmin"]
    ment=''
    beer_snack = Beer_snack.objects
    soju_snack = Soju_snack.objects
    whiskey_snack = Whiskey_snack.objects
    wine_snack = Wine_snack.objects
    riceWine_snack = RiceWine_snack.objects
    cocktail_snack = Cocktail_snack.objects
    if weather[0]["today"]["sky"]["name"]=='비':
        ment='비도 오는데 막걸리 한잔 어때요?'
    elif weather[0]["today"]["sky"]["name"]=='흐림':
        ment='꾸릿꾸릿한 날씨엔 맥주'
    elif weather[0]["today"]["sky"]["name"]=='맑음':
        ment='소주같이 맑은 날에는 소주'
    elif weather[0]["today"]["sky"]["name"]=='눈':
        ment='눈에는 눈 멘트 모르겠다 칵테일'
    return render(request, 'snacks.html', {'cSky': cSky, 'cPlace': cPlace, 'cTime': cTime, 'cMax': cMax, 'cMin': cMin,'ment': ment,'beer_snack': beer_snack, 'soju_snack': soju_snack, 'whiskey_snack': whiskey_snack,'riceWine_snack': riceWine_snack,'cocktail_snack': cocktail_snack,'wine_snack': wine_snack})

def area(request):
    r = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat=37.56667&lon=126.97806&appkey=a6101311-8fdc-403e-85c5-73d6f44b06eb")
    data = json.loads(r.text)
    weather = data["weather"]["summary"]
    cTime = weather[0]["timeRelease"]
    cPlace = weather[0]['grid']['city'] + ' ' + weather[0]['grid']['county'] + ' ' + weather[0]['grid']['village']
    cSky = weather[0]["today"]["sky"]["name"]
    cMax = weather[0]["today"]["temperature"]["tmax"]
    cMin = weather[0]["today"]["temperature"]["tmin"]
    ment=''
    if weather[0]["today"]["sky"]["name"]=='비':
        ment='비도 오는데 막걸리 한잔 어때요?'
    elif weather[0]["today"]["sky"]["name"]=='흐림':
        ment='꾸릿꾸릿한 날씨엔 맥주'
    elif weather[0]["today"]["sky"]["name"]=='맑음':
        ment='소주같이 맑은 날에는 소주'
    elif weather[0]["today"]["sky"]["name"]=='눈':
        ment='눈에는 눈 멘트 모르겠다 칵테일'
    return render(request, 'area.html', {'cSky': cSky, 'cPlace':cPlace, 'cTime':cTime, 'cMax':cMax, 'cMin':cMin,'ment':ment })
def recipe(request):
    r = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat=37.56667&lon=126.97806&appkey=a6101311-8fdc-403e-85c5-73d6f44b06eb")
    data = json.loads(r.text)
    weather = data["weather"]["summary"]
    cTime = weather[0]["timeRelease"]
    cPlace = weather[0]['grid']['city'] + ' ' + weather[0]['grid']['county'] + ' ' + weather[0]['grid']['village']
    cSky = weather[0]["today"]["sky"]["name"]
    cMax = weather[0]["today"]["temperature"]["tmax"]
    cMin = weather[0]["today"]["temperature"]["tmin"]
    ment=''
    if weather[0]["today"]["sky"]["name"]=='비':
        ment='비도 오는데 막걸리 한잔 어때요?'
    elif weather[0]["today"]["sky"]["name"]=='흐림':
        ment='꾸릿꾸릿한 날씨엔 맥주'
    elif weather[0]["today"]["sky"]["name"]=='맑음':
        ment='소주같이 맑은 날에는 소주'
    elif weather[0]["today"]["sky"]["name"]=='눈':
        ment='눈에는 눈 멘트 모르겠다 칵테일'
    return render(request, 'recipe.html', {'cSky': cSky, 'cPlace':cPlace, 'cTime':cTime, 'cMax':cMax, 'cMin':cMin,'ment':ment })

def pageon(request):
    r = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat=37.56667&lon=126.97806&appkey=a6101311-8fdc-403e-85c5-73d6f44b06eb")
    data = json.loads(r.text)
    weather = data["weather"]["summary"]
    cTime = weather[0]["timeRelease"]
    cPlace = weather[0]['grid']['city'] + ' ' + weather[0]['grid']['county'] + ' ' + weather[0]['grid']['village']
    cSky = weather[0]["today"]["sky"]["name"]
    cMax = weather[0]["today"]["temperature"]["tmax"]
    cMin = weather[0]["today"]["temperature"]["tmin"]
    ment=''
    if weather[0]["today"]["sky"]["name"]=='비':
        ment='비도 오는데 막걸리 한잔 어때요?'
    elif weather[0]["today"]["sky"]["name"]=='흐림':
        ment='꾸릿꾸릿한 날씨엔 맥주'
    elif weather[0]["today"]["sky"]["name"]=='맑음':
        ment='소주같이 맑은 날에는 소주'
    elif weather[0]["today"]["sky"]["name"]=='눈':
        ment='눈에는 눈 멘트 모르겠다 칵테일'
    return render(request, 'pageon.html', {'cSky': cSky, 'cPlace':cPlace, 'cTime':cTime, 'cMax':cMax, 'cMin':cMin,'ment':ment })

