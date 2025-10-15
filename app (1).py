from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# function baca data dri file JSON-------------------------------
def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

# function tulis data ke file JSON-----------------------------
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


# Route tampilkan data--------------------------------------------
@app.route('/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)

# Route tambah data----------------------------------------------
@app.route('/tambah', methods=['POST'])
def add_user():
    data = load_data()
    #ambil dari form-data
    id = request.form.get('id')
    name = request.form.get('nama')
    age = request.form.get('umur')

    new_user = {
        'id': id,
        'nama': name,
        'umur': age
    }

    data.append(new_user)
    save_data(data)
    return 'Data berhasil disimpan' 


if __name__ == '__main__':
    app.run(debug=True)