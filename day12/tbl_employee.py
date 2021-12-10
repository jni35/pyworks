import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")    #mydb.db가 없으면
    return conn

def select_emp():
    conn = getconn()  #db 연결 객체 생성
    cur = conn.cursor()     #db 작업(삽입,추가,변경,삭제) 객체
    sql = "SELECT * FROM employee ORDER BY emp_id"  # db검색, 오름차순(asc 생략됨)
    cur.execute(sql)        # 검색 실행
    rs = cur.fetchall()     # 모든 자료 가져오기(result set)

    # print(rs)
    for i in rs:
        print(i)
    conn.close()            # db 연결 종료 - 필수

def insert_emp():   #자료추가
    conn = getconn()  # db 연결 객체 생성
    cur = conn.cursor()  # db 작업 객체
    # 입력방법 1 - 칼럼값을 직접 입력
    # sql = "INSERT INTO employee VALUES ('e1001','추신수',40,40000)"    # data추가
    # 입력방법2 - ?기호 사용, 동적입력
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"    # data추가
    cur.execute(sql, ('e1004', '박인비', 33, 30000))
    conn.execute(sql)
    conn.commit()       # 커밋 실행 - 필수(데이터에 변경이 생겼을때 반드시 평가)
    conn.close()

def select_one():   #자료선택
    conn = getconn()
    cur = conn.cursor()
    sql = 'SELECT emp_id, name FROM employee WHERE emp_id=?'
    cur.execute(sql, (50000, ))     # 튜플 자료구조는 1개를 명시할때 (,)를  찍어야 한다.
    rs=cur.fetchall()   # 1명의 자료 반환
    print(rs)
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age=? WHERE emp_id=?"
    cur.execute(sql, (33, 'e1004'))
    conn.commit()
    conn.close()

def delete_emp():   #자료삭제
    conn = getconn()
    cur = conn.cursor()
    sql = 'DELETE FROM employee WHERE name=?'
    cur.execute(sql, ('안산',))
    conn.commit()
    conn.close()

if __name__=="__name__":
    # insert_emp()
    # select_one()
    update_emp()
    # delete_emp()
    select_emp()    #호출