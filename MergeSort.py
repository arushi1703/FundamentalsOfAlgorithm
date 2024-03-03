from random import *

def mergeSort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
    
        mergeSort(left)
        mergeSort(right)

        print("left: ",left," right: ",right)

        i=0
        j=0
        k=0

        while(i<len(left) and j<len(right)):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
            else:
                l[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
            
l=[]
for i in range(10):
    x=randint(0,500)
    if x in l:
        continue
    else:
        l.append(x)

print("Original list: ",l)
mergeSort(l)
print("Sorted list: ",l)

