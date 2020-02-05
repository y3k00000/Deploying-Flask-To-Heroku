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
    print(strToConvert)
    converted = [item[0] for item in strToConvert]
    converted = " ".join(converted)
    print(converted)
    return converted

if __name__ == '__main__':
    app.run(debug=True)
