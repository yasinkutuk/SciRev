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


sitelinks=pd.read_csv(datapath+'01.DisciplineLinks.csv',sep=';')['Journal link']


site='https://scirev.org/disciplines'


a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
a9=[]
a10=[]
a21=[]
a22=[]
a23=[]
a24=[]
a25=[]
a26=[]
a27=[]
a28=[]

bar = Bar('Processing', max=(len(sitelinks)))
for i in range(len(sitelinks)):
	br=mec.Browser()
	page=br.open(sitelinks[i])
	tree = html.parse(page)
	get1 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[1]/text()')
	get2 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[2]/text()')
	get3 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[3]/text()')
	get4 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[4]/text()')
	get5 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[5]/text()')
	get6 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[6]/text()')
	get7 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[7]/text()')
	get8 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[8]/text()')
	get9 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[9]/text()')
	get10 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[10]/text()')
	try:
		get21=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[0]
		get22=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[1]
		get23=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[2]
		get24=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[3]
		get25=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[4]
		get26=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[5]
		get27=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[6]
		get28=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[7]
	except:
		get21 = []
		get22 = []
		get23 = []
		get24 = []
		get25 = []
		get26 = []
		get27 = []
		get28 = []
		continue
	a1.append(get1)
	a2.append(get2)
	a3.append(get3)
	a4.append(get4)
	a5.append(get5)
	a6.append(get6)
	a7.append(get7)
	a8.append(get8)
	a9.append(get9)
	a10.append(get10)
	a21.append(get21)
	a22.append(get22)
	a23.append(get23)
	a24.append(get24)
	a25.append(get25)
	a26.append(get26)
	a27.append(get27)
	a28.append(get28)
	bar.next()
bar.finish()

#br = mec.Browser()
#page = br.open(sitelinks[100])
#tree = html.parse(page)
#get1 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[1]/text()')
#get2 = tree.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/dl/dd[2]/text()')
#get21=tree.xpath('/html/body/div[2]/div[3]/div[2]/div[1]//tr/td[1]/text()')[0]

data = {'Issues per year': a1, 'Articles published last year': a2, 'Manuscripts received last year': a3,
        '% accepted last year': a4, '% immediately rejected last year': a5, 'Open access status' : a6,
	'Manuscript handling fee?' : a7, 'Kind of complaint procedure' : a8, 'Two-year impact factor' : a9,
	'Five-year impact factor' : a10, 'Duration first review ' :  a21, 'Total handling time accepted manuscripts' : a22,
	'Decision time immediate rejection' : a23, 'Average number of review reports' : a24,  
	'Average number of review rounds' : a25, 'Quality of review reports' : a26,
	 'Difficulty of reviewer comments' : a27, 'Overall rating manuscript handlingOverall rating manuscript handling' : a28}
data = pd.DataFrame(data)
data.to_csv(datapath + '02.Reviews.csv', sep=';')


print "Tüm işlem tamam Hocam!"


