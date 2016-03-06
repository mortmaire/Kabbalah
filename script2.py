#!/usr/bin/python
from __future__ import generators
import numpy as np
import re
#with open("./data/pt0101.htm") as f:
    #c=f.readlines()
    #print c,"\n"

#304 805

mh=210

tora=[]


def KMP(text, pattern):

    pattern = list(pattern)
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos




#for i in range(1,2):

    #filename='./data/pt'+str('%02d' % i)+'.htm'
filename='torah.txt'
tora = [x for x in open(filename)]
tora = tora[0]
#print len(tora)
Tora=[]
a=0
for x in tora:
    if x==' ':continue
    Tora.append(int(ord(x)-223))

#U=np.unique(Tora)

#for x in U:
    #xx=Tora.count(x)
    #print x,xx



string="halflafe"
seq=[]
seq2=[]
for i in string:
    seq.append(ord(i)-ord('a')+1)


#for i in string:
    #seq2.append(ord(i)-ord('a')+1)

seq.append(3)
#print seq2


print seq

#Tora=np.append(Tora,np.zeros(m-n).astype(int))
#Tora=np.array([Tora])
#Tora=Tora.reshape((50,-1))

Torra=[]

n=304805
N=50
d=0
N0=1290


for k in np.arange(N0,n):
    m=n+k-n%k
    Torra=np.append(Tora,np.zeros(m-n).astype(int)).reshape((-1,k)).T
    #print Torra
    flag=0
    for i in np.arange(k):
        for j in KMP(Torra[i],seq):
            print "HL3 CONFIRMED:",k,i,j
            flag=1
        #for j in KMP(Torra[i],seq2):
            #print "HL3 CONFIRMED:",k,i,j
            #flag=1
    print k
    if flag:exit(0)

#print Tora.shape
#Tora=np.reshape(Tora,(-1,5))





#lat=['a','b','g','d','h','u','z','kh','t','y','kh','kh','l','m','m','n','n','s','e','f','f','ts','ts','k','r','sh','s']

