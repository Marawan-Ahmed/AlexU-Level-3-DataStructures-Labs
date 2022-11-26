input_string = input("")[1:-1]

if input_string == "":
    print ([0,0])
else:  
    list  = input_string.split(', ')
    evenSum = 0
    oddSum = 0
    for i in range(len(list)):
        list[i]=int(list[i])
        if (list[i]%2==0):
            evenSum+=list[i]
        else:
            oddSum+=list[i]    
    print([evenSum, oddSum])
