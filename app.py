from flask import Flask
app = Flask(__name__)

@app.route("/show/info")
def index():
    return "Super restaurant"
if __name__ == '__main__':
    app.run()
    
    