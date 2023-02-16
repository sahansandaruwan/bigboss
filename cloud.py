from flask import Flask
from threading import Thread
from flask import render_template

app = Flask('')

@app.route('/')
def home():
   return render_template('index.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def alive():
    t = Thread(target=run)
    t.start()
    
    

   
