# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:22:12 2020

@author: Jay Patel
"""

def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
        
        mergesort(Left)
        mergesort(Right)
        
        j = k = l = 0
        while j<len(Left) and k < len(Right) :
            if Left[j] < Right[k]:
                arr[l] = Left[j]
                j+=1
            else:
                arr[l] = Right[k]
                k+=1
            l+=1
        while j < len(Left):
            arr[l] = Left[j]
            j+=1
            l+=1
        while k < len(Right) :
            arr[l] = Right[k]
            k+=1
            l+=1
        
if __name__ == '__main__':
    print("How many nubers you would like to enter: ", end="\n")
    n = int(input())
    arr = []
    for i in range (0,n):
        d=input()
        arr.append(d)
    mergesort(arr)
    
    print("Sorted array: ")
    for i in range(len(arr)):
        print(arr[i], end= " ")