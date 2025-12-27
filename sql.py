import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
sql_connection = sqlite3.connect("C:\\Users\\vishalappu\\Desktop\\db\\main.db")
# conn = sqlite3.connect(r"C:\\Users\\vishalappu\\Desktop\\db\\main.db")
''' The r"..." ensures Windows backslashes are handled correctly'''
table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", sql_connection)
print(table)
df = pd.read_sql_query("select * from students_info;",sql_connection)
print(df.columns)
print(df['District'].unique())
def district():
    user_need = input("Enter district name: ").upper()
    query = f"select distinct College_Name from students_info where District = '{user_need}'"
    district_wise = pd.read_sql_query(query,sql_connection)
    pd.set_option('display.max_colwidth', None)
    return district_wise
print(district())
def college_branch_summary():
    user_college_need = input("Enter College name: ").upper()
    query = "SELECT Branch, COUNT(*) AS student_count FROM students_info WHERE UPPER(College_Name) = ? GROUP BY Branch"
    branch_summary = pd.read_sql_query(query, sql_connection, params=(user_college_need,))
    plt.figure(figsize=(8,5))
    plt.bar(branch_summary['Branch'], branch_summary['student_count'], 
        color='violet', label='Student Count')
    plt.title(f"Branch-wise Student Count in {user_college_need}")
    plt.xlabel('Branch')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()
    return branch_summary
print(college_branch_summary())