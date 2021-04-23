from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'

@app.route('/comments')
def comment():
    comments = [
        {
            'user': '张三',
            'content': 'up加油'
        },
        {
            'user': '李四',
            'content': 'undo'
        }
    ]
    return render_template('index.html', comments=comments)
