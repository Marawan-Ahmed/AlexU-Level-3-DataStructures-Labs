input_string = input("")[1:-1]
input_value = int(input(""))

if input_string == "":
    print ("[]")
else:
    list  = input_string.split(', ')
    for i in range(len(list)):
        list[i]=int(list[i])

    numOfOccur=0
    newList = list.copy()
    for i in range(len(list)):   
        if (list[i]==input_value):
            newList.pop(i-numOfOccur)  
            numOfOccur+=1

    newList += [input_value] * numOfOccur
    print(newList)

