#!/user/bin/env python3
#-*- coding:utf8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pic")
def base():
  qr = request.values.get('qr')
  user = request.values.get('user')
  #check user
  #get image by qr from server
  return {'result':'ok', 'images':['http://1.jpg', 'http://2.jpg']}

if (__name__ == '__main__'):
    app.run(debug = True, host = '0.0.0.0', port = 8080)
