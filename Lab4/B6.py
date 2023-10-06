# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *
from tkinter import ttk
import re
from openpyxl import Workbook
from tkinter import messagebox

#kiem tra dieu kien ma so sinh vien
def validate_numbers_input(event):
    numbers = numbers_field.get()
    if not numbers.isdigit() or len(numbers) !=7:
        messagebox.showerror("Lỗi","MSSV phải chứa đứng 7 số")
        numbers_field.delete(0,"end") #xoa noi dung nhap sai
#kiem tra email nhap vao
def validate_email_input():
    email = email_field.get()
    pattern = r'^\w+@\w+\.\w+$'
    if not re.match(pattern, email):
        messagebox.showerror("Lỗi", "Email không hợp lệ.")
        email_field.delete(0, "end")
# kiểm tra số điện thoại nhập vào
def validate_phone_input(event):
    phone = phone_field.get()
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Lỗi", "Số điện thoại phải chứa đúng 10 số.")
        phone_field.delete(0, "end")
# kiểm tra học kỳ nhập vào đúng hay chưa
def validate_semester_input(event):
    semester = semester_field.get()
    if semester not in ["1", "2", "3"]:
        messagebox.showerror("Lỗi", "Học kỳ phải là 1, 2 hoặc 3.")
        semester_field.delete(0,"end")
# kiểm tra định dạng ngày sinh nhập vào
def validate_birth_input():
    birth = birth_field.get()
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if not re.match(pattern, birth):
        messagebox.showerror("Lỗi", "Ngày sinh không đúng định dạng dd/mm/yyyy.")
        birth_field.delete(0, "end")
# nút gửi
def submit():
    numbers = numbers_field.get()
    name = name_field.get()
    birth = birth_field.get()
    email = email_field.get()
    phone = phone_field.get()
    semester = semester_field.get()
    year = year_field.get()

    # Kiểm tra xem có chọn ít nhất một môn học hay không
    if not var1.get() and not var2.get() and not var3.get() and not var4.get():
        messagebox.showerror("Lỗi", "Vui lòng chọn ít nhất một môn học.")
        return

    # Kiểm tra điều kiện về mã số sinh viên, email, số điện thoại, học kỳ, và ngày sinh
    if (
        not numbers or len(numbers) != 7 or not numbers.isdigit() or
        not re.match(r'^\w+@\w+\.\w+$', email) or
        not phone.isdigit() or len(phone) != 10 or
        semester not in ["1", "2", "3"] or
        not re.match(r'^\d{2}/\d{2}/\d{4}$', birth)
    ):
        messagebox.showerror("Lỗi", "Vui lòng kiểm tra lại thông tin.")
        return

    # Tạo một Workbook mới và lựa chọn một sheet (hoặc tạo một sheet mới)
    wb = Workbook()
    sheet = wb.active

    # Thêm thông tin vào các cột
    sheet.append(["Mã số sinh viên", "Họ tên", "Ngày sinh", "Email", "Số điện thoại", "Học kỳ", "Năm học", "Môn học"])

    # Điền thông tin của sinh viên
    selected_courses = []
    if var1.get():
        selected_courses.append("Lập trình Python")
    if var2.get():
        selected_courses.append("Lập trình Java")
    if var3.get():
        selected_courses.append("Công nghệ phần mềm")
    if var4.get():
        selected_courses.append("Phát triển ứng dụng web")

    sheet.append([numbers, name, birth, email, phone, semester, year, ", ".join(selected_courses)])

    # Lưu tập tin Excel
    wb.save(r'C:\Users\ADMIN\Documents\Book1.xlsx')

    messagebox.showinfo("Thông báo", "Đăng ký thành công.")
if __name__ =="__main__":
    root = Tk()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
# create a GUI window
    root.configure(background='light green')
    root.title("Đăng ký học phần")
    root.geometry("450x300")

    heading = Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", bg="light green", fg="red", font=100).place(x=120, y=5)
    numbers = Label(root, text="Mã số sinh viên", bg="light green").place(x=10, y=30)
    name = Label(root, text="Họ tên", bg="light green").place(x=10, y=50)
    birth = Label(root, text="Ngày sinh", bg="light green").place(x=10, y=70)
    email = Label(root, text="Email", bg="light green").place(x=10, y=90)
    phone = Label(root, text="Số điện thoại", bg="light green").place(x=10, y=110)
    semester = Label(root, text="Học kỳ", bg="light green").place(x=10, y=130)
    year = Label(root, text="Năm học", bg="light green").place(x=10, y=150)
    subject = Label(root, text="Chọn môn học", bg="light green").place(x=10, y=170)
    cb1 = Checkbutton(root, text="Lập trình Python", bg="light green", variable=var1).place(x=120, y=170)
    cb2 = Checkbutton(root, text="Công nghệ phần mềm", bg="light green", variable=var2).place(x=290, y=170)
    cb3 = Checkbutton(root, text="Lập trình Java", bg="light green", variable=var3).place(x=120, y=190)
    cb4 = Checkbutton(root, text="Phát triển úng dụng web", bg="light green", variable=var4).place(x=290, y=190)
    register = Button(root, text="Đăng ký",width=8 ,bg="purple", fg="white", command=submit).place(x=125, y=230)
    close = Button(root, text="Thoát", width=8, bg="purple", fg="white", command=exit).place(x=295, y=230)

# create a text entry box
# for typing the information
    numbers_field = Entry(root, width=42)
    numbers_field.place(x=125, y=30)
    name_field = Entry(root, width=42)
    name_field.place(x=125, y=50)
    birth_field = Entry(root, width=42)
    birth_field.place(x=125, y=70)
    email_field = Entry(root, width=42)
    email_field.place(x=125, y=90)
    phone_field = Entry(root, width=42)
    phone_field.place(x=125, y=110)
    semester_field = Entry(root, width=42)
    semester_field.place(x=125, y=130)
    year_field = ttk.Combobox(root, width=39)
    year_field.place(x=125, y=150)
    year_field["value"] = ("2022 - 2023", "2023 - 2024", "2024 - 2025")

    # kiểm tra xem nhập đúng mã số sinh viên, email, số điện thoại, học kỳ, ngày sinh thông qua các hàm đã tạo trước đó
    numbers_field.bind("<FocusOut>", validate_numbers_input)
    email_field.bind("<FocusOut>", lambda e: validate_email_input())
    phone_field.bind("<FocusOut>", validate_phone_input)
    semester_field.bind("<FocusOut>", validate_semester_input)
    birth_field.bind("<FocusOut>", lambda e: validate_birth_input())

    # start the GUI
    root.mainloop()
