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
            finalList.addLast(int(p1.data) + int(p2.data))
            p1 = p1.next
            p2 = p2.next
        
        for i in range(size2, size1):
            finalList.addLast(int(p1.data))
            p1 = p1.next

    else:
        for i in range(size1):
            finalList.addLast(int(p1.data) + int(p2.data))
            p1 = p1.next
            p2 = p2.next
        
        for i in range(size1, size2):
            finalList.addLast(int(p2.data)) 
            p2 = p2.next      
    return finalList

p1 = SingleLinkedList()
p1.initializeList("[1 , 2, 3, 4]")

p2 = SingleLinkedList()
p2.initializeList("[1 , 2, 3, 4, 5, 6]")

sum = add(p1, p2)
sum.listPrint()