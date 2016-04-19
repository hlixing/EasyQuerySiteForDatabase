from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, validators
app = Flask(__name__)
app.secret_key = 'huanglixing'


class LoginForm(Form):
    username = TextField("username", [validators.required()])
    address = TextField("address", [validators.required()])


@app.route('/', methods="GET", "POST")
def hello_world():
    myform = LoginForm(request.form)
    if request.methods == "POST":
        if myform.username.data == "jikexueyuan" and myform.address.data ==
            "123456" and myform.validator()
            return redirect("http://www.baidu.com")
        else:
            message = "用户名地址错误"
        return render_template("gs.fddbr.html", message=message, form=myform)
    return render_template("gs.fddbr.html", form=myform)


    flash('Hlixing的第一个GIT-WEB项目')
    return render_template('gs_fddbr.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
