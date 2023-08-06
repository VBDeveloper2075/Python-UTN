_cache={}
def factorial(n):
    try:
        if _cache[n]:
            return _cache[n]
    except:
        b=n
        print(n)
        a=b*factorial(b-1) if n else 1
        _cache[b]=a
        return a

print(factorial(10))
print("---"*23)
print(factorial(4))
print("---"*23)
print(factorial(12))
print("---"*23)