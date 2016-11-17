from flask import Flask
app = Flask(__name__)

#@app.route("/")
#def hello():
 #   return "Hello World!"
@app.route("/")
def root():
    return app.send_static_file('index.html')
	
@app.route('/name')
def fname():
	return 'Your name is'

@app.route('/name/<name>')
def finame(name):
	return 'Your name is ' + name	
	
if __name__ == "__main__":
    app.run()