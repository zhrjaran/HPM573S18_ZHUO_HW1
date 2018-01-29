# Problem 3
# Iterative
def summation(n):
    result=0
    for n in range(1,n+1):
        result+=n
    return result
print(summation(100))
# Recursive
def summation_r(n):
    if n==1:
        return n
    else:
        return n+ summation(n-1)
print(summation_r(100))
