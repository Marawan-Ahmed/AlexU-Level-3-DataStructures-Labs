input_value = int(input(""))
if (input_value == 1):
  print(0)
elif (input_value == 2):
  print(1)
else:
  fib1=0
  fib2=1
  fib3=1
  for i in range(input_value - 2):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
  print(fib3)