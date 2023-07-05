def fib(num):
  a = 0
  b = 1
  sum = 0
  for _ in range(0,num):
    sum = a+b
    a = b
    b = sum
  return sum

def fibonacci(num):
  return num if num < 2 else fib(num-1) + fib(num-2)


print(fib(5))
print(fibonacci(5))