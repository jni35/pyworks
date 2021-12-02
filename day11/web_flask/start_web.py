# 웹 서버 만들기
from flask import Flask, render_template, request

app = Flask(__name__)   # flask 객체 app 생성

@app.route('/')
# @ - 에너테이션     # '/'는 루트 경로(시작)     #ip - 127.0.01 -> host:port
def index():
    return render_template('index.html')    # html파일을 index에 전송
    # 파일명 templates 정확히 입력!!
    # return "<h1>hello~ Flask!!<h1>"       # 문자열을 페이지에 전송

@app.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'POST':        # 'POST' 방식이라면
        id = request.form['id']         # name값 id를 가져옴
        pwd = request.form['password']  # name값 password를 가져옴
        name = request.form['name']
        return render_template('member_info.html', id=id, pwd=pwd, name=name)
    else:
        return render_template('register.html')     # GET 방식

@app.route('/loop_index')
def get_loopindex():
    items=['a', 'b', 'c', 'd']
    return render_template('loop_index.html', items=items)


app.run(debug=True)       # debug=True, 서비스하기전 개발 모드