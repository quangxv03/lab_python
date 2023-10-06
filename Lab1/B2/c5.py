"""5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)"""

def DeQuy(n:int):
    return 1 if n == 1 or n == 2 else DeQuy(n-1) + DeQuy(n-2)

def KDeQuy(n):
    f0 = 0
    f1 = 1
    fn = 1
 
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
n = int(input("Nhập n: "))
print(DeQuy(n))
print(KDeQuy(n))