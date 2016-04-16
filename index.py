from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'huanglixing'


@app.route('/')
def hello_world():
    flash('Hlixing的第一个GIT-WEB项目')
    return render_template('gs_fddbr.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
