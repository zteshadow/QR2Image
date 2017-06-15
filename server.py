#!/user/bin/env python3
#-*- coding:utf8 -*-

from flask import Flask, render_template, request, make_response
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def wechat():
  data = request.args
  if len(data) == 0:
    return render_template('index.html')
  else:
    if request.method=='GET':
      token = 'qr2image'
      signature = data.get('signature','')
      timestamp = data.get('timestamp','')
      nonce = data.get('nonce','')
      echostr = data.get('echostr','')
      s = [timestamp,nonce,token]
      s.sort()
      s = ''.join(s)
      if(hashlib.sha1(s.encode('utf-8')).hexdigest() == signature):
        return make_response(echostr)
      else:
        return 'error'

@app.route("/pic")
def base():
  qr = request.values.get('qr')
  user = request.values.get('user')
  #check user
  #get image by qr from server
  return {'result':'ok', 'images':['http://1.jpg', 'http://2.jpg']}

if (__name__ == '__main__'):
    app.run(debug = True, host = '0.0.0.0', port = 8080)
