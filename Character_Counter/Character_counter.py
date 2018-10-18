#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

cList = []
nList = []


def percentage(part, whole):
    return 100 * part/whole

def summation(nList):
    summation = 0
    for i in range(len(nList)):
        summation = summation + nList[i]
    return summation


def main():
    if len(sys.argv) < 2:
        print("Plese give a file as a parameter.")
        return
    with open(sys.argv[1]) as f:
        while True:
            find = False
            c = f.read(1)
            c = c.lower()
            if not c: break # Wut?
            if c == '\n' or c == ' ': continue
        
            for i in range(len(cList)):
                if c == cList[i]:
                    nList[i] = nList[i]+1
                    find = True
                    break
                
            if find == False:
                nList.append(1)
                cList.append(c)
                
    for i in range(len(cList)):
        for j in range(len(cList)):
            if cList[i] < cList[j]:
                temp = cList[i]
                cList[i] = cList[j]
                cList[j] = temp
                
                temp = nList[i]
                nList[i] = nList[j]
                nList[j] = temp

    summ = summation(nList)

    print("----------------------")
    print ("Char    Freq    Percentage")
    print("----------------------")
    for i in range(len(cList)): 
        per = percentage(nList[i], summ)
        print("%s\t%d\t%1.1f " % (cList[i], nList[i], per))
        
if __name__ == '__main__':
    main()


                
                

