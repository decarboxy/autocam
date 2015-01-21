from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/record')
def add_data():
    pass

@app.route('/status')
def get_status():
    return

if __name__ == '__main__':
    app.run()