from flask import Flask 
app = Flask(__name__)

@app.route('/vegetarian', methods=["GET"])
def vegetarian(): 
    return "Vegetarian"

@app.route('/vegan', methods=["GET"])
def vegan(): 
    return "Vegan"

@app.route('/celiac', methods=["GET"])
def celiac(): 
    return "Celiac"

if __name__ == '__main__':
    app.run()

    