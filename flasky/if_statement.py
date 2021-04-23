# 输入http://127.0.0.1:5000/1/ 为登录状态，否则为未登录状态
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<is_login>/')
def index(is_login):
    if is_login == '1':
        user = {
            'username': u'啃书君',
            'age': 18
        }
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')