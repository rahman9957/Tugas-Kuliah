from flask import Flask, jsonify, request
import pymysql

app = Flask(_panti_)

# koneksi mysql dari railway 
def get_db():
    return pymysql.connect(host="mysql.railway.internal",user="root",


data--------------------------------------------
@app.route('/data', methods=['GET'])
def get_data()
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
