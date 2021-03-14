# flaskを使用した簡単なwebサーバー
from flask import Flask, render_template, request, session,redirect,url_for
from controller import cache_controller
import datetime
app = Flask(__name__)

# session key
app.secret_key = 'hello\/.,mnbv'

@app.route('/')
def index():
    """
    トップ画面を表示
    """
    cache_controller.test()

    session['authentication'] = _now()

    name = "Yoshiko Tsushima"
    title = "index"
    return render_template("index.html",
        title=title, name=name)


@app.route('/search')
def search():
    """
    検索画面を表示
    """
    print("method type:", request.method, "---", session['authentication'])

    if request.method == "POST":
        return "TODO"

    else:
        title = "search"
        return render_template("search.html",title=title)


@app.route('/send/<string:message>')
def send(message):
    print('send message:', message)
    return redirect(url_for('index')) # url_forに設定値は関数名


def _now():
    """
    現在時刻（年月日時分秒ミリ秒）を返す
    """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return now




if __name__ == "__main__":
    app.run(debug=True)
