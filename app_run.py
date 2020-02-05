from flask import *
from pypinyin import pinyin, lazy_pinyin, Style

app = Flask(__name__)

@app.route('/pinyin')
def index(any):
    str = request.args.get("str")
    return "result = "+pinyin(str,style=Style.BOPOMOFO)


if __name__ == '__main__':
    app.run(debug=True)
