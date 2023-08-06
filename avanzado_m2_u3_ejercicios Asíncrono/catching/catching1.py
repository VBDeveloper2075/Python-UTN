from functools import cache

@cache
def factorial(n):
    print(n)
    return n*factorial(n-1) if n else 1

print(factorial(10))
print("---"*23)
print(factorial(4))
print("---"*23)
print(factorial(12))
print("---"*23)