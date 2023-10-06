from math import gcd

class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"

    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq
    
    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq

a = PhanSo(7, 3)
b = PhanSo(3, 5)
print(f"Phan so a: {a}")
print(f"Phan so a: {b}")
print(f"a + b = {a} + {b} = {a + b}")
print(f"a - b = {a} - {b} = {a - b}")
print(f"a * b = {a} * {b} = {a * b}")
print(f"a * b = {a} / {b} = {a / b}")

class DanhSachPhanSo:
    def __init__(self):
        self.danh_sach_phan_so = []

    def them_phan_so(self, phan_so):
        self.danh_sach_phan_so.append(phan_so)

    def dem_so_phan_so_am(self):
        return sum(1 for phan_so in self.danh_sach_phan_so if phan_so.tu < 0)

    def tim_phan_so_duong_nho_nhat(self):
        phan_so_duong_nho_nhat = None
        for phan_so in self.danh_sach_phan_so:
            if phan_so.tu > 0:
                if phan_so_duong_nho_nhat is None or phan_so.tu / phan_so.mau < phan_so_duong_nho_nhat.tu / phan_so_duong_nho_nhat.mau:
                    phan_so_duong_nho_nhat = phan_so
        return phan_so_duong_nho_nhat

    def tim_vi_tri_cua_phan_so(self, phan_so_tim):
        vi_tri = []
        for i, phan_so in enumerate(self.danh_sach_phan_so):
            if phan_so.tu == phan_so_tim.tu and phan_so.mau == phan_so_tim.mau:
                vi_tri.append(i)
        return vi_tri

    def tong_cac_phan_so_am(self):
        return sum(phan_so.tu for phan_so in self.danh_sach_phan_so if phan_so.tu < 0)

    def xoa_phan_so(self, phan_so_xoa):
        self.danh_sach_phan_so = [phan_so for phan_so in self.danh_sach_phan_so if phan_so != phan_so_xoa]

    def xoa_tat_ca_phan_so_tu_x(self, x):
        self.danh_sach_phan_so = [phan_so for phan_so in self.danh_sach_phan_so if phan_so.tu != x]

    def sap_xep_tang_dan(self, theo_mau=False):
        self.danh_sach_phan_so.sort(key=lambda phan_so: (phan_so.tu / phan_so.mau if theo_mau else phan_so.tu, phan_so.mau))

    def sap_xep_giam_dan(self, theo_mau=False):
        self.danh_sach_phan_so.sort(key=lambda phan_so: (phan_so.tu / phan_so.mau if theo_mau else phan_so.tu, phan_so.mau), reverse=True)

# Sử dụng lớp DanhSachPhanSo và các chức năng
danh_sach = DanhSachPhanSo()
danh_sach.them_phan_so(PhanSo(1, 2))
danh_sach.them_phan_so(PhanSo(3, 4))
danh_sach.them_phan_so(PhanSo(-1, 3))
danh_sach.them_phan_so(PhanSo(2, 5))
danh_sach.them_phan_so(PhanSo(-2, 7))

print(f"Số phân số âm trong danh sách: {danh_sach.dem_so_phan_so_am()}")
phan_so_duong_nho_nhat = danh_sach.tim_phan_so_duong_nho_nhat()
print(f"Phân số dương nhỏ nhất trong danh sách: {phan_so_duong_nho_nhat}")
print(f"Vị trí của phân số (2/5) trong danh sách: {danh_sach.tim_vi_tri_cua_phan_so(PhanSo(2, 5))}")
print(f"Tổng các phân số âm trong danh sách: {danh_sach.tong_cac_phan_so_am()}")
danh_sach.xoa_phan_so(PhanSo(3, 4))
print("Danh sách sau khi xóa phân số (3/4):", [str(ps) for ps in danh_sach.danh_sach_phan_so])
danh_sach.xoa_tat_ca_phan_so_tu_x(-1)
print("Danh sách sau khi xóa tất cả phân số có tử là -1:", [str(ps) for ps in danh_sach.danh_sach_phan_so])

print("Danh sách ban đầu:", [str(ps) for ps in danh_sach.danh_sach_phan_so])
danh_sach.sap_xep_tang_dan()
print("Danh sách sau khi sắp xếp tăng dần theo tử số:", [str(ps) for ps in danh_sach.danh_sach_phan_so])
danh_sach.sap_xep_tang_dan(theo_mau=True)
print("Danh sách sau khi sắp xếp tăng dần theo mẫu số:", [str(ps) for ps in danh_sach.danh_sach_phan_so])
danh_sach.sap_xep_giam_dan()
print("Danh sách sau khi sắp xếp giảm dần theo tử số:", [str(ps) for ps in danh_sach.danh_sach_phan_so])
danh_sach.sap_xep_giam_dan(theo_mau=True)
print("Danh sách sau khi sắp xếp giảm dần theo mẫu số:", [str(ps) for ps in danh_sach.danh_sach_phan_so])
