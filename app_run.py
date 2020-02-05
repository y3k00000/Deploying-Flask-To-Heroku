from flask import *
from pypinyin import pinyin, lazy_pinyin, Style

app = Flask(__name__)

@app.route('/<path:any>')
def index(any):
    str = request.args.get("str")
    return "Hello World!! "+str


if __name__ == '__main__':
    app.run(debug=True)
