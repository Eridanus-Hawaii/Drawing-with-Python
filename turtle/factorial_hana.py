# 階乗
# 4! = 4 * 3 * 2 * 1
# factorial

def fact(n):
    result = 1
    for i in range(n):
        print(i + 1) # for debug
        result *= (i + 1)
    return result

def fact0(n):
    if n == 1:
        return 1
    return n * fact0(n-1)

# fact(1) = 1
# fact(2) = 2 * fact(2-1) = 2 * fact(1)
# fact(3) = 3 * fact(3-1) = 3 * fact(2)
# fact(4) = 4 * fact(4-1) = 4 * fact(3) 
# 4 * 3 * 2 * 1
# 4 * ( 3 * 2 * 1 )
# 4 * fact(3)
# 
# N! = N * (N-1) * (N-2) .........3 * 2 * 1
# N! = N * (N-1)!

res = fact0(100)
print(res)

# res = fact(4)
# print(res)

