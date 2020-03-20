# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:49:33 2020

@author: ilucas
"""

token = 'https://bdif.amf-france.org/technique/multimedia?docId=a539d3ea-7eaa-428d-bdb5-af3f325011a4&famille=BDIF&bdifId='
def get_pages(token, nb):
    pages = []
    for i in range(1,nb+1):
        j = token + str(i)
        pages.append(j)
    return pages
pages = get_pages(token,295)

5080C022_220C0805


219C0044

import urllib.request


def add_zero(x):
    x = str(x)
    x = "0"*(4-len(x)) + x
    return x


for i in [220]:
    for j in range(7,806):
        tmp = str(i)+"C"+add_zero(j)
        tmp = tmp[::-1] + "_" + tmp
        url = 'https://bdif.amf-france.org/technique/multimedia?docId=a539d3ea-7eaa-428d-bdb5-af3f325011a4&famille=BDIF&bdifId='+tmp
        print(url)
        urllib.request.urlretrieve(url,"C:/Users/ilucas/Documents/Seuil/"+tmp+".pdf")


https://bdif.amf-france.org/technique/multimedia?docId=a539d3ea-7eaa-428d-bdb5-af3f325011a4&famille=BDIF&bdifId=7000C022_220C0007
https://bdif.amf-france.org/technique/multimedia?docId=a91ba88d-7676-4ee3-9730-570a7fe90a7e&famille=BDIF&bdifId=7000C022_220C0007