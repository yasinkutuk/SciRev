# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:47:52 2017

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

import os,glob,pandas
filetype='*.csv'


#Path Specifier (Kodlarım Hem linux hemde Windows'da çalışsın)
if platform.system()=='Linux':
    crawlerpath= r'/media/DRIVE/Dropbox/_My_Research/SciRev/crawlers/'
    datapath= r'/media/DRIVE/Dropbox/_My_Research/SciRev/data/'
    print "Abi, Linux bu!"
else:
    crawlerpath=r'D://Dropbox//_My_Research//SciRev//crawlers//'
    datapath=r'D://Dropbox//_My_Research//SciRev//data//'
    print "Hocam Windows'dasın"

k=[]
os.chdir(datapath)
filelist=glob.glob(filetype)
for i in filelist:
    if ('01.Dis' in i) or ('03.Con' in i):
        k.append(i)



k0=pandas.read_csv(datapath+k[0],sep=';')
k1=pandas.read_csv(datapath+k[1],sep=';')
k=pd.merge(k0, k1, on='Journal link', how='left')
k=k.drop_duplicates()
k.to_csv(datapath+'04.Merged.csv',index=None,sep=';')