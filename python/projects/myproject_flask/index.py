from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_script import Manager
# 程序初始化
app = Flask(__name__)
# 命令行使用
manager = Manager(app)

# 创建程序实例时初始化
bootstrap = Bootstrap(app)

# 设置路由与视图函数
@app.route('/')
def index():
    return render_template('index.html')
# 设置用户页面
@app.route('/user')
def User_index():
    return render_template('user.html')
# 设置一个动态路由，欢迎加名字
@ app.route('/user/<name>')
def Hello_name(name):
    return render_template('user_name.html', name=name)

# 设置资源数据
@ app.route('/resource')
def resource():
    return render_template('resource.html')

# 返回404错误
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
# 返回500错误
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# 运行程序
if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)
