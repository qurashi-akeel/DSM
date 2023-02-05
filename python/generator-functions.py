# range(1, 10) is generator function

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b


print(fib(10))  # <generator object fib at 0x100c49030>

# way to get data from the generator functions
for i in fib(10):
    print(i)

print(True or False and True)
