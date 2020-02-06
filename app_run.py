from flask import *
from pypinyin import pinyin, lazy_pinyin, Style
import urllib.parse
# import json

app = Flask(__name__)

@app.route('/pinyin')
def index():
    strToConvert = request.args.get("str")
    strToConvert = urllib.parse.unquote_plus(strToConvert)
    converted = pinyin(strToConvert,style=Style.BOPOMOFO)
#     converted = json.dumps(converted)
    converted = [item[0] for item in converted]
    converted = " ".join(converted)
    return converted

if __name__ == '__main__':
    app.run(debug=True)
