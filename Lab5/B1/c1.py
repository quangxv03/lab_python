import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 17 for SQL Server};
                      Server=LAPTOP-MEGOLFVS;
                      Database=QLSinhVien;
                      Trusted_Connection=yes;''')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
db_version = cursor.fetchone()
conn.close()
print("SQl Server version:",db_version)

# import sqlite3

# def get_connection():
#     connection = sqlite3.connect('QLSinhVien.db')
#     return connection

# def close_connection(connection):
#     if connection:
#         connection.close()
        
# def read_database_version():
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         cursor.execute("Select sqlite_version();")
#         db_version = cursor.fetchone()
#         print("Ban dang su dung SQLite phien ban: ", db_version)
#         close_connection(connection)
#     except (Exception, sqlite3.Error) as error:
#         print("Da co loi xay ra. Thong tin loi: ",error)

# read_database_version()