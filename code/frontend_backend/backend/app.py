from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 普通GET请求
@app.route('/msg/', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)


# 带有查询字符串的GET请求
@app.route('/login/')
def info():
    name = None
    if request.args.get('name', None):
        name = request.args.get('name', None)
    response = {
        'msg': 'login {}'.format(name)
    }

    return jsonify(response)


# 要给 URL 添加变量部分，你可以把这些特殊的字段标记为 <variable_name> ，
# 这个部分将会作为命名参数传递到你的函数。规则可以用 <converter:variable_name> 指定一个可选的转换器。

# POST请求
@app.route('/welcome/', methods=['POST'])
def post():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    response = {
        'msg': 'welcome {}'.format(name)
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8023, debug=True)