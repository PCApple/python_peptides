# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 09:10:00 2018

@author: jcase
"""
#exec(open(r'parsing.py').read())
f=open(r'D:/parsed.txt', "r")

mrnas={}
sequence={}
rawdata=[]

for i in f:
    rawdata.append([j.strip() for j in i.split("\t")[:-1]])



for i in rawdata:
    x = 1
    #print("hello"0
    try:
        if i[0] not in mrnas:
            #print("hello False")
            mrnas[i[0]]=[i[1:5]]
            mrnas[i[0]].append([i[5:-1]])
            sequence[i[6]]=i[-1]
            x = x+1
        else:
            #print("hello")
            mrnas[i[0]][1].append(i[5:-1])
            sequence[i[6]]=i[-1]
    except:
        pass