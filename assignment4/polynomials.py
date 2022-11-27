from SingleLinkedList import *

def add(F1,F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = max(size1,size2)
    finalList = SingleLinkedList()
    p1 = F1.head
    p2 = F2.head
    if size1 >= size2:
        for i in range(size2):
            finalList.add_last(int(p1.data) + int(p2.data))
            p1 = p1.next
            p2 = p2.next
        
        for i in range(size2, size1):
            finalList.add_last(int(p1.data))
            p1 = p1.next

    else:
        for i in range(size1):
            finalList.add_last(int(p1.data) + int(p2.data))
            p1 = p1.next
            p2 = p2.next
        
        for i in range(size1, size2):
            finalList.add_last(int(p2.data)) 
            p2 = p2.next      
    return finalList

def sub(F1,F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = max(size1,size2)
    finalList = SingleLinkedList()
    p1 = F1.head
    p2 = F2.head
    if size1 >= size2:
        for i in range(size2):
            finalList.add_last(int(p1.data) - int(p2.data))
            p1 = p1.next
            p2 = p2.next
        
        for i in range(size2, size1):
            finalList.add_last(int(p1.data))
            p1 = p1.next

    else:
        for i in range(size1):
            finalList.add_last(int(p1.data) - int(p2.data))
            p1 = p1.next
            p2 = p2.next
        
        for i in range(size1, size2):
            finalList.add_last(-int(p2.data)) 
            p2 = p2.next      
    return finalList

def mul(F1, F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = size1+size2-1
    finalList = SingleLinkedList()
    finalList.initialize("["+"0, "*(finalSize-1)+"0]")
    for i in range(size1):
        for j in range(size2):
            finalList.set_element(int(finalList.get_element(i+j))+int(F1.get_element(i))*int(F2.get_element(j)),i+j)

    return finalList

def clear(F1):
    F1.clear()

p1 = SingleLinkedList()
p1.initialize("[32, 41, 67]")

p2 = SingleLinkedList()
p2.initialize("[2, 3, 1]")

sum = mul(p1, p2)
sum.list_print()
clear(p1)
p1.list_print()