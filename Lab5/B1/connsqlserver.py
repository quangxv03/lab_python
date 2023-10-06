import pyodbc
from prettytable import PrettyTable

def get_connection():
    connectionString = '''Driver={ODBC Driver 17 for SQL Server};
                        Server=LAPTOP-MEGOLFVS;
                        Database=QLSinhVien;
                        Trusted_Connection=yes;'''
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Lop')
        records = cursor.fetchall()

        print (f"Danh sách lớp là:")
        for row in records:
            print("*" * 50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra. Thông tin lỗi: ",error)

# get_all_class()

def get_all_sv():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """
        SELECT SinhVien.ID AS 'Mã số', SinhVien.HoTen AS 'Họ tên', 
               SinhVien.MaLop AS 'Mã lớp', Lop.TenLop AS 'Tên lớp'
        FROM SinhVien
        LEFT JOIN Lop ON SinhVien.MaLop = Lop.ID
        """
        
        cursor.execute(select_query)
        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["Mã số", "Họ tên", "Mã lớp", "Tên lớp"]
        print("Danh sách tất cả các sinh viên là: ")
        for row in records:
            table.add_row([row[0], row[1], row[2], row[3]])

        print(table)
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# get_all_sv()

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop WHERE id = ?"

        params = (class_id,)
        cursor.execute(select_query, params)

        records = cursor.fetchone()

        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", records[0])
        print("Tên lớp: ", records[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# get_class_by_id(1)

#hien thi thong tin sinh vien theo ma sinh vien
def get_student_by_id(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query="Select * from SinhVien where ID = ?"

        params =(student_id,)
        cursor.execute(select_query, params)

        records = cursor.fetchone()
        
        print(f"Thông tin sinh viên có mã số {student_id} là: ")
        print("Mã số: ", records[0])
        print("Họ tên: ", records[1])
        print("Mã lớp: ", records[2])
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
        
# get_student_by_id(3)

#hien thi danh sach sinh vien theo lop (khi biet ma lop/ten lop)
def get_student_by_idclass(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query ="Select * from SinhVien where MaLop = ?"

        params =(class_id,)
        cursor.execute(select_query,params)

        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["Mã số", "Họ tên", "Mã lớp"]

        print(f"Danh sách sinh viên có mã lớp {class_id} là: ")
        for row in records:
            table.add_row([row[0], row[1], row[2]])

        print(table)
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# get_student_by_idclass(3)

#tim kiem thong tin sinh vien theo ten va lop
def find_student(class_id, name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "SELECT * FROM SinhVien WHERE HoTen LIKE ? AND MaLop = ?"

        params = (f"%{name}%", class_id,)
        cursor.execute(select_query,params)   

        records = cursor.fetchall()  
        table = PrettyTable()
        table.field_names = ["Mã số", "Họ tên", "Mã lớp"]

        print(f"Sinh viên tên {name} có mã lớp {class_id} là: ")
        for row in records:
            table.add_row([row[0], row[1], row[2]])

        print(table)
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# find_student(3, "Trung")

# insert
def insert_class(class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "Insert into Lop(TenLop) values ( ? )"
        cursor.execute(select_query, (class_name))

        connection.commit()

        print("Đã thêm thành công!")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# insert_class("CTK45B")

