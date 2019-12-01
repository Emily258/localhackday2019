from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/diet', methods=['GET'])
def diet():
    vegetarian = request.args.get('Vegetarian')
    vegan = request.args.get('Vegan')
    celiac = request.args.get('Celiac')

    if (vegetarian is not ''):
        return render_template('vegetarian.html')

if __name__ == '__main__':
    app.run()
