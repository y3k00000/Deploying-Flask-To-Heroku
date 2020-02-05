from flask import *
from pypinyin import pinyin, lazy_pinyin, Style
import urllib.parse

app = Flask(__name__)

@app.route('/pinyin')
def index():
    strToConvert = request.args.get("str")
    strToConvert = urllib.parse.unquote_plus(strToConvert)
    print(strToConvert)
    strToConvert = pinyin(strToConvert,style=Style.BOPOMOFO)
    strToConvert = "".join(str,strToConvert)
    print(strToConvert)
    return strToConvert


if __name__ == '__main__':
    app.run(debug=True)
