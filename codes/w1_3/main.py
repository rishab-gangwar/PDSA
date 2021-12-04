from binarysearch import binarysearch
from sortingN_2 import selectionsort,insertionsort,Isort
from sortingNlogn import mergesort,quicksort
from Linkedlist import Node

lis=[1,5,7,18,29,36,38,55,78,85,91,97]
list_=[45,36,96,23,12,56,45,32,10,1,5,64,12,16]
print(binarysearch(lis,79))
print(selectionsort(list_))
print(insertionsort(list_))
print(Isort(list_))
print(mergesort(list_))
print(quicksort(list_,0,len(list_)-1))
