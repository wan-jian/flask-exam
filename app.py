from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = '''
    <html>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    '''
    return html


@app.route('/index')
def index():
    return render_template('index.html', name='Tom')


@app.route('/p1')
def p1():
    scores = [{'课程': 'os', '姓名': '张三', '成绩': '85'},
              {'课程': 'db', '姓名': '张三', '成绩': '70'},
              {'课程': 'os', '姓名': '李四', '成绩': '60'},
              {'课程': 'db', '姓名': '李四', '成绩': '90'}]

    return render_template('p1.html', scores=scores)


@app.route('/p2')
def p2():
    return render_template('p2.html')


@app.route('/p3', methods=['POST', 'GET'])
def p3():
    if request.method == 'POST':
        cource = request.form['cource']
        name = request.form['name']
        score = request.form['score']
    else:
        cource = request.args['cource']
        name = request.args['name']
        score = request.args['score']

    return render_template('p3.html', cource=cource, name=name, score=score)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
