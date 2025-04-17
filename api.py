from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import base64
from PIL import Image
import json
import os


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


filename = 'massiv/mas.json'


def read_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def write_json(data2, filename):     
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data2, f, ensure_ascii=False, indent=4)

data = read_json(filename)


@app.route('/', methods=['GET'])
def main():
    return "200"


@app.route('/api/get', methods=['GET'])
def getKatalog():
    return json.dumps(data)

@app.route('/api/admin/get', methods=['GET'])
def getKatalogAdmin():
    data = read_json(filename)
    return json.dumps(data)


@app.route('/api/login', methods=['GET'])
def login():
    login = request.args.get('login')
    password = request.args.get('password')
    print(login)
    if login == "aboba" and password == "aboba":
        return jsonify({"response": "adminEdit.html"}), 200
    
    return jsonify({"response": 400}), 400


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    img = data.get('img')
    text = data.get('text')
    
    if not img or not text:
        return jsonify({"error": "не заполнены поля"}), 400
    
    data = read_json(filename)
    
    tmp = 1
    for key in data.keys():
        if int(key) >= tmp:
            tmp = int(key) + 1
    
    data[str(tmp)]={"img":img,"text":text}
    
    write_json(data,filename)
    
    data = read_json(filename)
    
    
    return jsonify({"message": "успех"}), 200


@app.route('/api/admin/delete', methods=['POST'])
def delete():
    request2 = request.get_json()
    img = request2.get('img')
    text = request2.get('text')
    
    for key,value in data.items():
        if(value["img"]==img and value["text"]==text):
            data.pop(key)
            write_json(data,filename)
            return jsonify({"message": "удалено успешно"}), 200
        
    return jsonify({"message": "внутренняя ошибка"}), 500

#POST-------------------------------------------------------------------------------------------------------------------

#curl -X POST -d "14|2004-23-11|заголовок|текст" http://127.0.0.1:5000/postPost


if __name__ == "__main__":
    app.run(debug=True)