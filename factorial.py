
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5)) # 120

n = 5

for i in range(0, n):
    print(i)