from flask import Flask
app = Flask(__name__)

#@app.route("/")
#def hello():
 #   return "Hello World!"
@app.route("/")
def root():
    return app.send_static_file('index.html')
if __name__ == "__main__":
    app.run()