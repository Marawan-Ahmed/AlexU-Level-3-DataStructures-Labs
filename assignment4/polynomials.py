from SingleLinkedList import *


def add(F1, F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = max(size1, size2)
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


def sub(F1, F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = max(size1, size2)
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
    finalSize = size1 + size2 - 1
    finalList = SingleLinkedList()
    finalList.initialize("[" + "0, " * (finalSize - 1) + "0]")
    for i in range(size1):
        for j in range(size2):
            finalList.set_element(int(finalList.get_element(i + j)) + int(F1.get_element(i)) * int(F2.get_element(j)),
                                  i + j)

    return finalList


def clear(F1):
    F1.clear()


def eval(F1, x):
    result = 0
    size = F1.size
    for i in range(size):
        result = x * result + int(F1.get_element(i))
    return result


def print_equation(F1):
    temp = []
    size = F1.size
    for power in range(size - 1, -1, -1):
        coeff = int(F1.get_element(size - power - 1))
        if coeff == 0:
            continue
        temp.append(coeff_format(coeff))
        temp.append(power_format(power))
    temp[0] = temp[0].lstrip("+")
    return ''.join(temp)


def coeff_format(coeff):
    return str(coeff) if coeff < 0 else "+{0}".format(coeff)


def power_format(power):
    if power == 0:
        return ''
    elif power == 1:
        return 'x'.format(power)
    else:
        return 'x^{0}'.format(power)

def return_var(input):
    if input == "A" or "a":
        return A
    if input == "B" or "b":
        return B
    if input == "C" or "c":
        return C
    if input == "R" or "r":
        return R


if __name__ == "__main__":

    command = input()
    R = SingleLinkedList()
    try:
        if command == "set":
            sym = input()
            if sym not in ["A", "a", "B", "b", "C", "c", "R", "r"]:
                raise TypeError("")
            if sym == "A" or "a":
                Aa = input()
                A = SingleLinkedList()
                A.initialize(Aa)
            elif sym == "B" or "b":
                Bb = input()
                B = SingleLinkedList()
                B.initialize(Bb)
            elif sym == "C" or "c":
                Cc = input()
                C = SingleLinkedList()
                C.initialize(Cc)
            else:
                raise TypeError("")

        if command == "print":
            letter_print = input()
            if letter_print not in ["A", "a", "B", "b", "C", "c", "R", "r"]:
                raise TypeError("")
            if letter_print == "A" or "a":
                print(print_equation(A))
            if letter_print == "B" or "b":
                print(print_equation(B))
            if letter_print == "C" or "c":
                print(print_equation(C))
            if letter_print == "R" or "r":
                print(print_equation(R))

        if command == "eval":
            eval_letter = input()
            value = input()
            if eval_letter == "A" or "a":
                print(eval(A, value))
            if eval_letter == "B" or "b":
                print(eval(B, value))
            if eval_letter == "C" or "c":
                print(eval(C, value))

        if command == "add":
            operand1 = return_var(input())
            operand2 = return_var(input())
            print(print_equation(add(operand1, operand2)))
        if command == "sub":
            operand1 = return_var(input())
            operand2 = return_var(input())
            print(print_equation(sub(operand1, operand2)))
        if command == "mult":
            operand1 = return_var(input())
            operand2 = return_var(input())
            print(print_equation(mul(operand1, operand2)))
        if command == "clear":
            clear_letter = return_var(input())
            print(clear(clear_letter))
        else:
            print("Error")
    except TypeError:
        print("Error")





#p1 = SingleLinkedList()
#p1.initialize("[32, 41, 67]")

#p2 = SingleLinkedList()
#p2.initialize("[2, 3, 1]")

#sum = mul(p1, p2)
#sum.list_print()
#print(eval(p2, 2))
#p1.list_print()
#print(print_equation(p1))
