from datetime import datetime
from datetime import date

class SinhVien:
    #biến của lớp, chung cho tất cả đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"

    #hàm khởi tạo, hàm tạo lập: khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo #thuộc tính private
        self.__hoTen = hoTen #thuộc tính private
        self.__ngaySinh = ngaySinh #thuộc tính private

    #cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self.__maSo

    #cho phép thay đổi giá trị thuốc tính maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten):
        self.__hoTen = hoten

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh
    
    #phương thức tĩnh: các phương thức không truy xuất gì đến thuộc tính, hành vi của lớp
    #những phương thức này không cần truyền tham số mặc định self
    #đây không phải là một hành vi (phương thức) của 1 đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    #phương thức của lớp, chỉ truy xuất tới các biến thành viên của lớp
    #không truy xuất được các thuộc tính riêng của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    #tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    #hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)

    #tìm sinh viên theo mssv, nếu có trả về sinh viên
    def timSvTheoMssv(self, mssv: int):
        return [ sv for sv in self.dssv if sv.maSo == mssv]

    #tìm sinh viên theo mssv, nếu có trả về vị trí của sinh viên trong danh sách
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    
    #xóa sinh viên có mã số mssv, thông báo xóa được hoặc không
    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    #tìm sinh viên tên "Nam"
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.rsplit(' ', 1)[-1] == ten]

    #tìm những sinh viên sinh trước 15/6/2000
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

sv1 = SinhVien(2115239, "Trần Văn Nam",
               date(2003,6,5))
sv2 = SinhVien(2115287, "Hoàng Vũ Minh Trung",
                date(2003,7,3)) 
sv3 = SinhVien(2115258, "Võ Xuân Quang",
               date(2003,11,1))
sv4 = SinhVien(211817, "Trương Tấn Diệm",
               date(2003,12,5))
sv5 = SinhVien(2113014, "Phạm Anh Quân",
               date(2003,9,9))


# sv.xuat()
ds = DanhSachSv()
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.themSinhVien(sv5)
ds.xuat()

while(True):
    msTim = int(input("Nhập vào mã số muốn tìm: "))
    kq = ds.timSvTheoMssv(msTim)
    if kq != None and len(kq) > 0:
        print("Đã tìm thấy sinh viên có mã số: ", msTim)
        for sv in kq:
            sv.xuat()
            print("Vị trí:",ds.timVTSvTheoMssv(msTim))
        break
    else:
        print(f"Không tìm thấy sinh viên có mã {msTim}")

# tim ten sinh viên
while(True):
    ten = input("Nhập vào tên sinh viên muốn tìm: ")
    kq = ds.timSvTheoTen(ten)
    if kq != None and len(kq) > 0:
        print("Đã tìm thấy sinh viên có tên: ", ten)
        for sv in kq:
            sv.xuat()
        break
    else:
        print(f"Không tìm thấy sinh viên có tên {ten}")

ngay = date(2006, 6, 15)
kqNgay = ds.timSvSinhTruocNgay(ngay)
if kq != None and len(kq) > 0:
    print(f"Đã tìm thấy sinh viên sinh trước thời gian {ngay}")
    for sv in kqNgay:
        sv.xuat()
else:
    print(f"Không thấy sinh viên sinh trước thời gian {ngay}")

maSo = int(input("Nhập vào mã số muốn xóa: "))
ds.xoaSvTheoMssv(maSo)
ds.xuat()