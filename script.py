#!/usr/bin/python
import numpy as np
import re
#with open("./data/pt0101.htm") as f:
    #c=f.readlines()
    #print c,"\n"

#304 805

mh=210

tora=[]




for i in range(1,2):

    #filename='./data/pt'+str('%02d' % i)+'.htm'
    filename='torah.txt'
    lines=[line.rstrip('\n') for line in open(filename)]
    print lines
    L=len(lines)

    for j in range(L): 
        aa=[]
        #lines[j]=re.sub('<B>.*</B>','',lines[j])
        lines[j]=re.sub('{.}','',lines[j])
        lines[j]=re.sub('span.*span','',lines[j])
        #lines[j]=re.sub('\s*','',lines[j])
        x=list(lines[j])
        for i in range(len(x)):
            y=ord(x[i])
            #if y>mh and y!= 237 and y!=243:
            if y>mh:
                aa.append(x[i])
        l=len(aa)
        if l>0:
            #print l
            tora.append(aa)
            #a=np.sort(np.unique(aa))
            #print a.e,a
        
Tora=[]
Tora2=[]        
for s in tora:
    for c in s:
        Tora.append(c)


print ''.join(Tora)
U=np.unique(Tora)
a=0
for i in U:
    print i
    #xx=Tora2.count(i)
    #if xx<700:
        #a+=xx
#print a


print len(Tora)