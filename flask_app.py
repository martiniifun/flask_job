
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '안녕하세요? 신명진입니다. 만나서 반갑습니다.'

