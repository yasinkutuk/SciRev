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

df=[]
dflist=[]
def concatenator(infile=datapath, outfile=datapath+'03.Concatenated.csv'):
    os.chdir(datapath)
    filelist=glob.glob(filetype)
    dflist=[]
    colnames=['No','% accepted last year','% immediately rejected last year','Articles published last year','Average number of review reports',
              'Average number of review rounds','Decision time immediate rejection','Difficulty of reviewer comments',
              'Duration first review','Five-year impact factor','Issues per year','Journal link','Kind of complaint procedure',
              'Manuscript handling fee?','Manuscripts received last year','Open access status','Overall rating manuscript handlingOverall rating manuscript handling',
              'Quality of review reports','Total handling time accepted manuscripts','Two-year impact factor']
    filelist=filelist[1:]
    for filename in filelist:
        if '02.Rev' in filename:
            print filename+' birleştiriliyor...'
            df=pandas.read_csv(filename,header=None,sep=';')
            dflist.append(df.iloc[1:,:])
    concatdf=pandas.concat(dflist,axis=0)
    concatdf.columns=colnames
    concatdf.to_csv(outfile,index=None,sep=';')


concatenator()
