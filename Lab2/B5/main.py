from datetime import datetime
from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSV

sv1 = SinhVienChinhQuy(1957698, "Trần Văn A", datetime.strptime("23/6/1999", "%d/%m/%Y"), 88)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 98)
sv3 = SinhVienPhiCQ(1957692, "Thái Thị Thu",datetime.strptime("15/8/1998", "%d/%m/%Y"), "Cao đẳng", 2)
sv4 = SinhVienPhiCQ(2098324, "Trần Thanh Tâm", datetime.strptime("27/8/2020", "%d/%m/%Y"), "Cao đẳng", 2)
sv5 = SinhVienPhiCQ(2004544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2000", "%d/%m/%Y"), "Trung cấp", 2.5)
sv6 = SinhVienChinhQuy(2884567, "Nguyễn Thành Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 68)
sv7 = SinhVienPhiCQ(2094545, "Nguyễn Thanh Thanh", datetime.strptime("29/10/1999", "%d/%m/%Y"), "Trung cấp", 2.5)
sv8 = SinhVienChinhQuy(2884679, "Võ Hoài Nam", datetime.strptime("4/1/2008", "%d/%m/%Y"), 70)

dssv = DanhSachSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.xuat()

vt = dssv.timSVTheoMS(2004544)
print(f"Sinh vien o vi tri thu {vt + 1} trong danh sach")

kq = dssv.timSVThemLoai("chinhquy")
print("Danh sach sinh vien theo loai:")
for sv in kq:
    print(sv)
    
print("Sinh vien co diem ren luyen >= 80:")
diem_ren_luyen_sv = dssv.timSVDiemRenLuyen(80)
for sv in diem_ren_luyen_sv:
    print(sv)
    
print("Sinh vien co trinh do cao dang sinh truoc 15/8/1999:")
ngay_gioi_han = datetime.strptime("15/8/1999", "%d/%m/%Y")
cao_dang_truoc_ngay_sv = dssv.timSVCaoDangSinhTruoc(ngay_gioi_han)
for sv in cao_dang_truoc_ngay_sv:
    print(sv)