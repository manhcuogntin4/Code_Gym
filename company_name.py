#!/bin/python3

import math
import os
import random
import re
import sys

def sort_dic(dic):
    sorted_dic_value = sorted(dic.items(), key=lambda kv: kv[1],  reverse=True)
    return sorted_dic_value
def sort_dic_key(sorted_dic_value):
    list_key_value=[]
    for k,v in sorted_dic_value:
        list_key_value.append((k,v))
    return list_key_value
def sort_list(list_key_value):
    l=list_key_value.copy()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if (l[i][1]==l[j][1]) and(l[i][0]>l[j][0]):
                t=l[i]
                l[i]=l[j]
                l[j]=t
    return l 

if __name__ == '__main__':
    s = input()
    d={}
    for i in s.strip():
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    sorted_dic_value=sort_dic(d)
    list_key_value=sort_dic_key(sorted_dic_value)
    list_key_value=sort_list(list_key_value)
    l=len(list_key_value)-1
    for i in range(0,3):
        print(list_key_value[i][0],list_key_value[i][1])