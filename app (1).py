#request -> perintah http -> GET, POST, PUT, DELETE
from flask import Flask, jsonify, request
import json

#membuat instance / object bernama app
app = Flask(__name__)

#perintah baca data
def ambil_data():
    with open('ppanti.json', 'r') as file:
        daftar_anak = json.load(file)
    return daftar_anak

#perintah simpan data
def simpan_data(data):
    with open('ppanti.json', 'w') as file:
        json.dump(data, file, indent=4)

#------------------------------------ROUTES--------------------------------------
@app.route('/') #rute homepage
def home(): #function 
    return '<H1>Selamat Datang Di Panti Asuhan Mutiara Insan</H1>'

#Routes baca data-------------------------------------------------
@app.route('/baca_data', methods=['GET'])
def get_data():
    daftar_anak = ambil_data()
    return jsonify(daftar_anak)

#Routes simpan data baru-----------------------------------------
@app.route('/tambah_data', methods=['POST'])
def penambahan_daftar_anak():
    data = ambil_data()
    nomor_induk_panti = request.form.get('nomor_induk_panti')
    nama = request.form.get('nama')
    jenis_kelamin = request.form.get('jenis_kelamin')

    yambah_anak = {
        'nomor_induk_ktp' : nomor_induk_panti,
        'nama' : nama,
        'jenis_kelamin' : jenis_kelamin 
    }

    data.append(tambah_anak)
    simpan_data(data)
    return jsonify(data)

#Routes Udah data / Edit-----------------------------------------
@app.route('/edit/<nomor_induk_panti, methods=['POST'])
def edit_dafar_anak(nomor_induk_panti):
    data = ambil_data()
    for pend in data:
        if pend['nomor_induk_panti] == nomor_induk_panti: #cari data daftar anak dengan nomor_induk_panti sesuai variabel nomor_induk_panti 
            pend['nama'] = request.form.get('nama')
            pend['gender'] = request.form.get('jenis_kelamin)
            simpan_data(data)
            return 'Data berhasil diubah'
    return 'Data tidak ditemukan'
    

#Routes Hapus data ----------------------------------------------
@app.route('/hapus/<nomor_induk_panti>', methods=['DELETE'])
def delete_data(nomor_induk_panti):
    data = ambil_data()
    for pend in data:
        if pend['nomor_induk_panti] == nomor_induk_panti:
            data.remove(pend)
            break

    simpan_data(data)
    return 'Data berhasil dihapus'

#menjalankan file app.py
if __name__ == '__main__':
    app.run(debug=True)
