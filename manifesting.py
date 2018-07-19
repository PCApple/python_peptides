# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:09:41 2018

@author: jcase
"""

f =open(r'C:/Users/jcase/Downloads/ex3/data_mutations_extended.txt', 'r')
x = f.readline()
b =0
mandata = []
data = []
while x!= '':
    print(str(b))
    b=b+1
    splited = x.split('\t')
    if splited[16] not in data:
        print('appending')
        data.append(splited[16])
    x = f.readline()
f2 = open('C:/Users/jcase/Downloads/ex3/MANIFEST.txt', 'w')
for i in data:
    f2.write(i)
    f2.write('\n')
f2.close()
