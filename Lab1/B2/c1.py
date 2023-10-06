"""1. Tính:
a) (a + b), 
b) a/b, 
c) a^b"""

def Tong(a,b):
    return a+b
def Thuong(a,b):
    return a/b
def LuyThua(a,b):
    return a**b

a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
print("a+b=",Tong(a,b))
print("a/b=",Thuong(a,b))
print("a^b=",LuyThua(a,b))