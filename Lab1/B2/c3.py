"""3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước"""

import math
def KiemTraSoNguyenTo (num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True 
def LietKeSoNguyenTo(a,b):
    for i in range(a,b+1):
        if(KiemTraSoNguyenTo(i)):
            print(i, end=' ')

while True:
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("Nhập số cuối: "))
        
        if a < 0 or b <0:
            print("Vui lòng nhập số lớn hơn 0!")
        elif a > b:
            print("Số thứ nhất lớn hơn số cuối!")
        else:
            LietKeSoNguyenTo(a,b)
            break