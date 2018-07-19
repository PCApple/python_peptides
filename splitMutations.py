# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:28:50 2018

@author: pcase
"""
path = 'C:/Users/jcase/Downloads/ex3/'
mutName = 'data_mutations_extended.txt'
manifestName = 'MANIFEST.txt'
f =open(r'' +path+mutName,'r')

data= {}
x = f.readline()
while x != '':
    split = x.split('\t')
    if split[16] not in data:
        print('adding')
        data[split[16]] = x
    else:
        #print('appending')
        data[split[16]] = data[split[16]] + x
    x = f.readline()
for i in data:
    m = open(r'' + path + manifestName, 'r')
    j = m.readline()
    name =""
    while j !='':
        #print('looking')
        if j.split('\n')[0] in i:
            print('found')
            name = j.split('\n')[0]
        j = m.readline()
    w = open(path + name + '.txt', 'w')
    print('print')
    w.write(data[name])
    w.write('\n')
    w.close()
    