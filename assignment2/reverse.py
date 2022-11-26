input_string = input("")[1:-1]

if input_string == "":
    print ("[]")
else:  
    list  = input_string.split(', ')  
    for i in range(len(list)):
        list[i]=int(list[i])
    print(list[::-1])
