from flask import Flask,request, render_template
from datetime import datetime

import subprocess
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', conteudo="testando alo alo")

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 80, debug = True)
