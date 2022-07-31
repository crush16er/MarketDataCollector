import requests
import datetime
import time
from forex_python.converter import CurrencyRates

url = 'https://steamcommunity.com/market/search?appid=730&q=broken+fang+case'
url2 = 'https://steamcommunity.com/market/search?appid=730&q=operation+riptide+case'
url3 = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=tag_weapon_ak47&category_730_Exterior%5B%5D=tag_WearCategory1&category_730_Quality%5B%5D=tag_strange&category_730_Quality%5B%5D=tag_unusual_strange&appid=730&q=asiimov'
url4 = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=tag_weapon_ak47&category_730_Exterior%5B%5D=tag_WearCategory2&category_730_Quality%5B%5D=tag_strange&category_730_Quality%5B%5D=tag_unusual_strange&appid=730&q=neon+rider'
url5 = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&appid=730&q=stockholm+2021+dust'
url6 = 'https://steamcommunity.com/market/search?q=revolver+case&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730'
url7 = 'https://steamcommunity.com/market/search?q=falchion+case&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730'
url8 = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730&q=shadow+case'


c = CurrencyRates()
usdtopln = c.convert('USD', 'PLN', 1)

while True:

    #Broken Fang Case
    r = requests.get(url)
    text = r.text
    quantity = text.split("data-qty=\"",1)[1]
    price = text.split("data-currency=\"1\">$",1)[1]
    qqq = quantity[0:6]
    ppp = price[0:4]
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln, usdtopln)
    print(x)
    print(pln)
    f = open("datasaved.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()


    #Operation Riptide Case
    r = requests.get(url2)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:5]
    ppp = price[0:4]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("operationriptidecase.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()


    #AK-47 Asiimov StatTrack Minimal Wear
    r = requests.get(url3)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:2]
    ppp = price[0:5]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("ak47asiimovminimalwearstattrack.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()


    # AK-47 Neon Rider StatTrack Field Tested
    r = requests.get(url4)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:2]
    ppp = price[0:5]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("ak47neonriderfieldtestedstattrack.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()


    #Stockholm Souvenir Dust2 Package
    r = requests.get(url5)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:5]
    ppp = price[0:4]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("stockholmsouvenirdustpackage.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()

    # Revolver Case
    r = requests.get(url6)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:5]
    ppp = price[0:4]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("revolvercase.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()

    # Falchion Case
    r = requests.get(url7)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:5]
    ppp = price[0:4]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("falchioncase.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()

    # Shadow Case
    r = requests.get(url8)
    text = r.text
    quantity = text.split("data-qty=\"", 1)[1]
    price = text.split("data-currency=\"1\">$", 1)[1]
    qqq = quantity[0:5]
    ppp = price[0:4]
    c = CurrencyRates()
    pln = usdtopln * float(ppp)
    pln = round(pln, 2)
    e = datetime.datetime.now()
    x = "%s %s %s %s %s %s %s %s" % (e.day, e.month, e.year, e.hour, e.minute, qqq, ppp, pln)
    print(x)
    print(pln)
    f = open("shadowcase.txt", "a")
    f.write(x)
    f.write("\n")
    f.close()

    time.sleep(20)