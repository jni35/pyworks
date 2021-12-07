# book 테이블 만들기
import sqlite3

def getconn():
    con = sqlite3.connect('./output/book.db')
    return con

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE book(
        book_no INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        publisher TEXT NOT NULL,
        page INTEGER
        )
    """
    #AUTOINCREMENT - 자동 순번(sequence)
    cur.execute(sql)
    conn.commit()
    print("book테이블 생성")
    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES(?,?,?)"
    cur.execute(sql, ('웹표준의 정석', '고경희', 600))
    conn.commit()
    conn.close()

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()    #db연결
    cur = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"   #책 번호로 검색
    cur.execute(sql, (1, ))
    rs = cur.fetchall()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE book SET publisher page = ? WHERE book_no = ?"    #page 300->350으로 변경
    cur.execute(sql, ("김명석", 500, 4))
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM book"  #book_no = 1인 책 삭제
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__=="__main__":
    # create_table()
    insert_book()
    # update_book()
    # delete_book()
    select_book()
    # select_one()
