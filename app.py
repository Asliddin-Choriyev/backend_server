from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

# Ma'lumotlar bazasi sifatida oddiy ro'yxat

# GET so'rovi
@app.route('/projects', methods=['GET'])
def get_items():
    return jsonify(data)

# POST so'rovi
@app.route('/projects', methods=['POST'])
def add_item():
    item = request.json
    data.append(item)
    return jsonify(item), 201

# API serverini ishga tushirish
if __name__ == '__main__':
    app.run(debug=True)

