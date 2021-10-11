# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:25:25 2018

@author: home168
"""

import requests
from bs4 import BeautifulSoup
from random import choice

count = 0

filename = input("Enter file name to load:")
if '.txt' not in filename: filename+='.txt'

website = int(input("Enter Source Website\n 1) http://sentence.yourdictionary.com \n 2) https://sentencedict.com/ \nYour Choice:"))

with open(filename, "r") as f:
    lst = [line.strip().split('/') for line in f]
    
l = [item for sublist in lst for item in sublist]
tup1 = tuple(l)
print(tup1)


with open('sentences.dat', 'w', encoding='UTF-8') as f:
    for word in tup1:
        count += 1
        if website == 1:
            html = requests.get('http://sentence.yourdictionary.com/'+word)
            sp = BeautifulSoup(html.text, 'html.parser')
            lstToFind = sp.find_all("li", {"class": "sentences-list-item"})
        
            srtd = sorted(lstToFind[:len(lstToFind)//5], key=len)
            srtd.extend(srtd_[:len(srtd_)//2+1])
            srtd = sorted(srtd, key=len)
            sp = choice(srtd[:len(srtd)//5+1])
            
            sp = sp.find('div')
            sp = sp.find('div')
            sp = sp.find('div')
            sp = sp.find('span')
            sp = str(sp).replace('<mark>', '**')
            sp = str(sp).replace('</mark>', '**')
            spi = sp.find('>')
            sp = sp[spi+1:-1]
            spi = sp.find('<')
            #sp.replace('\\xa0', ' ')
            f.write(str(count)+' '+sp[0:spi]+'\n')
            
        elif website == 2:
            html = requests.get('https://sentencedict.com/'+word+'.html')
            sp = BeautifulSoup(html.text, 'html.parser')
            sp = sp.find_all('div', {"id":"all"})
            srtd = [i[i.find('>')+1:].rstrip('</div>]').lstrip(' 1234567890.,())') for i in str(sp).split('<div')][2:]
            
            srtd = sorted(srtd, key=len)
            sp = choice(srtd[:len(srtd)//5+1])
            
            sp = str(sp).replace('<em>', '**')
            sp = str(sp).replace('</em>', '**')
            f.write(str(count)+' '+sp+'\n')
            
        print(str(count)+'/'+str(len(tup1)))
    
