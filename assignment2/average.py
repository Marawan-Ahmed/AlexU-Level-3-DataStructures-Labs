input_string = input("")[1:-1]

if input_string == "":
    print (0.0)
else:  
    list  = input_string.split(', ')
    sum = 0
    for i in range(len(list)):
        list[i]=int(list[i])
        sum+=list[i]
    average = sum/len(list)    
    print(average)
