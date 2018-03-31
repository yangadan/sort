from random import *
from time import *
#冒泡排序
def Bubble(list):
    assert len(list)>1,"the length of list lower than 1"
    t=len(list)-1
    i=0
    while t>0:
        while i<t:
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
            i+=1
        t-=1
        i=0
#选择排序
def Select(list):
    assert len(list)>1,"the length of list lower than 1"
    t=len(list)-1
    i=j=0
    while i<t:
        k=j
        j+=1
        while j<=t:
            if list[j]<list[k]:
                k=j
            j+=1
        temp=list[k]
        list[k]=list[i]
        list[i]=temp
        i+=1
        j=i
#插入排序
def Insertion(list):
    #assert len(list)>1,"the length of list lower than 1"
    for index in range(1,len(list)):
        i=index-1
        temp=list[index]
        while i>=0:
            if list[i]>temp:
                list[i+1]=list[i]
                list[i]=temp
            else:
                break
            i-=1
    return
#希尔排序
def Shell(list):
    assert len(list)>1,"the length of list lower than 1"
    t=len(list)
    gap=1
    while gap<t/3:
        gap=3*gap+1

    while gap>=1:
        i = gap
        while i<t:
            j=i-gap
            temp=list[i]
            while j>=0:
                if  list[j]>temp:
                    list[j+gap]=list[j]
                    list[j]=temp
                else:
                    break
                j-=gap
            i+=1
        gap=int((gap-1)/3)
    return
#归并排序
def reunion(list1,list2,t1,t2):#归并排序的合并函数
        #t2=len(list2)
        #t1=len(list1)
        i=j=0
        list=[]
        while i<t1 and j<t2:
           if list1[i]>=list2[j]:
                list.append(list2[j])
                j+=1
           else:
               list.append(list1[i])
               i+=1
        if j<t2:
           return list+list2[j:]
        else:
            return list+list1[i:]

def Merge(list):
    t = len(list)
    if t<=5:
        Insertion(list)
        return list
    mid=int(t/2)
    list1=Merge(list[:mid])
    list2=Merge(list[mid:])
    return reunion(list1,list2,mid,t-mid)
#快速排序
def Quick_sort(list,left,right):
    #t=len(list)
    if left>=right:
        #Insertion(list[left:right+1])
        return
    j=right
    i=left
    temp=list[left]
    while i<j:
        while j>i and list[j]>temp :
            j-=1
        if j> i:
            list[i]=list[j]
            i+=1
        while i<j and list[i]<=temp :
            i+=1
        if i<j:
            list[j]=list[i]
            j-=1
    list[i]=temp
    Quick_sort(list,left,i-1)
    Quick_sort(list,i+1,right)
    #list1.append(temp)
    return
def Quicksort(list):
    t=len(list)
    Quick_sort(list,0,t-1)
    return
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        if left<right:
            lists[left] = lists[right]
            left+=1
        while left < right and lists[left] <= key:
            left += 1
        if left<right:
            lists[right] = lists[left]
            right-=1
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return
def quicksort(list):
    t=len(list)
    quick_sort(list,0,t-1)
    return
#堆排序
def heavy(list,i,t):
    max=i
    lchild=2*i+1
    rchild=2*i+2
    if lchild<t and list[lchild]>list[max]:
        max=lchild
    if rchild<t and list[rchild]>list[max]:
        max=rchild
    if max!=i:
        list[max], list[i] = list[i], list[max]
        heavy(list,max,t)
    return

def bulidmaxheap(list,t):
    #assert len(list) > 1, "the length of list lower than 1"
    for i in range(int(t/2))[::-1]:
        heavy(list,i,t)
    return
def Heapsort(list):
    #assert len(list) > 1, "the length of list lower than 1"
    t=len(list)
    bulidmaxheap(list,t)
    for i in range(1,t)[::-1]:
        list[0],list[i]=list[i],list[0]
        #templist=list[i:]
        heavy(list,0,i)
    return
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

# 创建堆
def build_heap(lists, size):
    for i in range(0, (int(size/2)))[::-1]:
        adjust_heap(lists, i, size)

# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists


def sort_test():
    list=[]
    #for j in range(10):
    for i in range(5):
        list.append(randint(0,1000))
    print(list)
    Quicksort(list)
    print(list)
#sort_test()
def main():
    sum=0
    funlist=(Bubble,Select,Insertion,Shell,Merge,Quicksort,Heapsort)
    avgtime=[0,0,0,0,0,0,0]
    list = []
    for j in range(5):
        for k in range(10000):
            list.append(randint(0, 1000))
        for i,fun in enumerate(funlist):
            temp=list.copy()
            t=time()
            fun(temp)
            t=time()-t
            avgtime[i]+=t
    print(avgtime)
if __name__=="__main__":
    main()
    #sort_test()
























