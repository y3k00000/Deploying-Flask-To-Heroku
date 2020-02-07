# Heroku-Pinyin

Forked from [Deploying-Flask-To-Heroku](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)

Deploying a small api on Heroku for Chinese text to Chu-In transformation, utilizing [pypinyin](http://pypinyin.mozillazg.com/)

Example : 
request:
GET https://test-pypinyin.herokuapp.com/pinyin?str=愛麗絲夢遊仙境
response:
ㄞˋ ㄌㄧˋ ㄙ ㄇㄥˋ ㄧㄡˊ ㄒㄧㄢ ㄐㄧㄥˋ

for fuzzy comparation of chinese speeches.
