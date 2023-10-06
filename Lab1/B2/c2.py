"""2. Tính diện tích hình chữ nhật khi biết bán kính"""

def SHCN(a,b):
    return a*b

while True:
    a=float(input("Nhap chieu dai: "))
    b=float(input("Nhap chieu rong: "))
    
    if a>0 and b>0:
        print("Dien tich HCN:",SHCN(a,b))
        break
    else:
        print("Nhap lai!")