# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 18:47:52 2016

░█░░░░░░░░░░░░╔╗░░░░╔╗░░░╔╗░░░
░░░░░░░░░░░░░░║║░░░╔╝╚╗░░║║░░░
╔╗░╔╦══╦══╦╦═╗║║╔╦╗╠╗╔╬╗╔╣║╔╗░
║║░║║╔╗║══╬╣╔╗╣╚╝╣║║║║║║║║╚╝╝░
║╚═╝║╔╗╠══║║║║║╔╗╣╚╝║╚╣╚╝║╔╗╗░
╚═╗╔╩╝╚╩══╩╩╝╚╩╝╚╩══╩═╩══╩╝╚╝░
╔═╝╔╗░░░░░░░░░░░╔╗░░░░░░░░░░░░
╚═╔╝╚╗░░░░░░░░░░║║░░░░░░░░░░░░
╔═╩╗╔╝╔══╦╗╔╦══╦╣║░╔══╦══╦╗╔╗░
║╔╗║║░║╔╗║╚╝║╔╗╠╣║░║╔═╣╔╗║╚╝║░
║╔╗║╚╗║╚╝║║║║╔╗║║╚╦╣╚═╣╚╝║║║║░
╚╝╚╩═╝╚═╗╠╩╩╩╝╚╩╩═╩╩══╩══╩╩╩╝░
░░░░░░╔═╝║░░░░░░░░░░░░░░░░░░░░
░░░░░░╚══╝░░░░░░░░░░░░░░░░░░░░


@author: Yasin
"""
#Initial Setups
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#Importings
import mechanize as mec
import urllib2
import urllib
from urllib import urlencode
from lxml import html
from bs4 import BeautifulSoup as bs
from urllib2 import parse_http_list
from pandas import read_csv
import pandas as pd
import math
import json
import re
import platform
from os import listdir as ls
from progress.bar import Bar
import time
from lxml import etree
import numpy as np

#Path Specifier (Kodlarım Hem linux hemde Windows'da çalışsın)
if platform.system()=='Linux':
    crawlerpath= r'/media/DRIVE/Dropbox/_My_Research/SciRev/crawlers/'
    datapath= r'/media/DRIVE/Dropbox/_My_Research/SciRev/data/'
    print "Abi, Linux bu!"
else:
    crawlerpath=r'D://Dropbox//_My_Research//SciRev//crawlers//'
    datapath=r'D://Dropbox//_My_Research//SciRev//data//'
    print "Hocam Windows'dasın"


#Mimicing Browser
hdr = {"Host": "scirev.org",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
"Accept": "*/*",
"Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
"Content-Type":"text/html; charset=utf-8",
"Accept-Encoding": "identity",
"X-Requested-With": "XMLHttpRequest",
"Referer": "https://scirev.org/about/welcome/",
"Cookie": "__utma=45412152.1424915812.1465638666.1467996321.1468056341.11; \
__utmz=45412152.1465638666.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); \
__auc=75312a441553edf3e92f4d51d8c; __gfp_64b=tltrSz7UZyUj2wJ29_zcTNbDRlwxCDxRj5w13WFiRmD._7; facebooklike=fbmodalviewed;\
 s_nr=1467985988780-Repeat; OPTAW_gaCookie=GA1.2.1424915812.1465638666; ASPSESSIONIDSQTSCDTS=CKCAMKODJBLOCCGKGMHEIEEM; \
 __utmc=45412152; s_cc=true; s_ppv=-%2C100%2C100%2C947; s_sq=%5B%5BB%5D%5D; __asc=5edba925155cefa07b1b07e9797; __utmb=45412152.2.10.1468056341; __utmt=1",
"Connection": "keep-alive"}


site='https://scirev.org/disciplines'

br=mec.Browser()
page=br.open(site)
tree = html.parse(page)
get = tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]/ul//li/a/@href')
links=list(set(get))



codelist=[]
disciplinelist=[]
disciplinelink=[]
bar = Bar('Processing', max=(len(links)))
for j in range(len(links)):
    br=mec.Browser()
    page=br.open(links[j])
    tree = html.parse(page)
    code = tree.xpath('/html/body/div[2]/div[3]/div[2]/table/tbody//tr/td[1]/text()')
    discipline = tree.xpath('/html/body/div[2]/div[3]/div[2]/table/tbody//tr/td[2]/a/text()')
    disciplink = tree.xpath('/html/body/div[2]/div[3]/div[2]/table/tbody//tr/td[2]/a/@href')
    codelist.append(code)
    disciplinelist.append(discipline)
    disciplinelink.append(disciplink)
    bar.next()
bar.finish()

codelist = [item for sublist in codelist for item in sublist]
disciplinelist = [item for sublist in disciplinelist for item in sublist]
disciplinelink = [item for sublist in disciplinelink for item in sublist]
print "Kodların çekilme işlemi tamam Hocam!"




collectorlinks=[]
codes2=[]
disciplinelist2=[]
bar = Bar('Processing', max=(len(disciplinelink)))
for l in range(len(disciplinelink)):
    br = mec.Browser()
    page = br.open(disciplinelink[l])
    tree = html.parse(page)
    get = tree.xpath('/html/body/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul//li/a/@href')
    links = list(set(get))
    collectorlinks.append(links)
    codes2.append(list(np.repeat(codelist[l],len(links),axis=0)))
    disciplinelist2.append(list(np.repeat(disciplinelist[l], len(links), axis=0)))
    bar.next()
bar.finish()

codes2 = [item for sublist in codes2 for item in sublist]
collectorlinks = [item for sublist in collectorlinks for item in sublist]
disciplinelist2 = [item for sublist in disciplinelist2 for item in sublist]
print "Linklerin çekilme işlemi tamam Hocam!"








journals=[]
jourlinks=[]
codeslist=[]
discs2=[]
discs2link=[]
bar = Bar('Processing', max=(len(collectorlinks)))
for k in range(len(collectorlinks)):
    br=mec.Browser()
    page=br.open(collectorlinks[k])
    tree = html.parse(page)
    journal = tree.xpath('//table/tbody//tr/td[1]/a/text()')
    jourlink = tree.xpath('//table/tbody//tr/td[1]/a/@href')
    journals.append(journal)
    jourlinks.append(jourlink)
    codeslist.append(list(np.repeat(codes2[k],len(journal),axis=0)))
    discs2.append(list(np.repeat(collectorlinks[k],len(journal),axis=0)))
    discs2link.append(list(np.repeat(disciplinelist2[k], len(journal), axis=0)))
    bar.next()
bar.finish()

journals=[item for sublist in journals for item in sublist]
jourlinks=[item for sublist in jourlinks for item in sublist]
codeslist=[item for sublist in codeslist for item in sublist]
discs2=[item for sublist in discs2 for item in sublist]
discs2link=[item for sublist in discs2link for item in sublist]


data = {'Discipline Code': codeslist, 'Discipline': discs2, 'Discipline link': discs2link,
        'Journal title': journals, 'Journal link': jourlinks}
data = pd.DataFrame(data)
data.to_csv(datapath + '01.DisciplineLinks.csv', sep=';')


print "Tüm işlem tamam Hocam!"

