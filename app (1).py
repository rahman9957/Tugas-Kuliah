from flask import Flask, jsonify, request

app = Flask(__name__)

data_panti = [
    {"nomor_induk_panti": 1, "nama": "Rahman", "donasi": "Beras"},
    {"nomor_induk_panti": 2, "nama": "Irham", "donasi": "Baju"},
    {"nomor_induk_panti": 3, "nama": "Ibnu", "donasi": "Uang"},
]

@app.route('/data', methods=['GET'])
def tampil_data():
    return jsonify(data_panti)

@app.route('/tambah', methods=['POST'])
def tambah_data():
    data_baru = request.get_json()
    data_panti.append(data_baru)
    return jsonify(data_panti)

@app.route('/hapus/<nomor_induk_panti>', methods=['DELETE'])
def hapus_data(nomor_induk_panti):
    for d in data_panti:
        if d["nomor_induk_panti"] == int(nomor_induk_panti):
            data_panti.remove(d)
            break
    return jsonify(data_panti)

if __name__ == '__main__':
    app.run(debug=True)
