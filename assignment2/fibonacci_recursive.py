def fib(index):
  if(index == 0):
    return 0
  elif(index==1):
    return 1
  else:
    return (fib(index - 1) + fib(index - 2))  

input_value = int(input(""))
print(fib(input_value))