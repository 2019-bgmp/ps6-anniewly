#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:34:55 2019

@author: annie
"""

kcnt = []
kcov = []
KSIZE = 49

def convert_len_physical(kcount):
    return kcount + KSIZE -1
file = '/Users/annie/Documents/BGMP/hw_Bio_621/Shell/contigs.fa'

#file = '/Users/annie/Documents/BGMP/hw_Bio_621/ps6-anniewly/Unit_test.fa'
with open(file,"r") as fh:
    index = 0
    for line in fh:
        if ">" in line:
            a = line.split('_')
            kcnt.append(int(convert_len_physical(int(a[3]))))
            kcov.append(float(a[5]))
    print("The number of contigs is " + str(len(kcnt)))
    print("The maximum contig length is " + str(max(kcnt)))
    print("The mean contig length is " + str(sum(kcnt)/len(kcnt)))
    print("The total length of the genome assembly across the contigs is " +str(sum(kcnt)))
    print("The mean depth of coverage for the contigs is " +str(sum(kcov)/len(kcov)))
#%%
summation = 0
kcnt.sort(reverse = True)
for i in range(len(kcnt)):
    summation +=kcnt[i]
    if summation>=sum(kcnt)/2:
        print("The N50 values is "+ str(kcnt[i]))
#        print(i)
        break
#re.findall((?<=length_)[0-9]+(?!_cov),'NODE_11_length_3717_cov_19.315845')
#%%
lencontig={}
kcnt.sort()
n=1
count = 0
i = 0
for i in range(max(kcnt)//100+1):
    lencontig.update({i*100:0})
for i in range(len(kcnt)):
    lencontig[kcnt[i]//100*100]+=1
print("#Contig length \t Number of contigs in this category")
for keys,values in lencontig.items():
    print(str(keys) + '\t' + str(values))
#    lencontig.update({})
#    if kcnt[i]//100*100 in lencontig.keys():
#        lencontig[kcnt[i]//100*100]+=1
#    else:
#        lencontig.update({kcnt[i]//100*100:1})
 
#    if kcnt[i]//:
#        count+=1
#        i+=1
##        print(i)
#        
#    else:
#        list.append(count)
#        n+=1
#        count = 0
##        print(i)
##        if i >=len(kcnt):
##            break
        
            



