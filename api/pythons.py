from flask import Flask, request
import requests
app = Flask(__name__)

TELEGRAM_API = "https://apI.telegram.org"
@app.route('/bot<token>/<method>', methods=['GET', 'POST'])



def proxy(token, method):
    url = f"{TELEGRAM_API}/bot{token}/{method}"
  







  
    resps = requests.request( method=request.method, url=url, params=request.args,data=request.get_data(), headers={k: v for k, v in request.headers if k.lower() != 'host'})
    return (resps.content, resps.status_code, resps.headers.items())
@app.route('/')

def homes():
    return "Proxy"
