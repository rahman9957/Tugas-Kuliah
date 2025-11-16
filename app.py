from flask import Flask, jsonify, request
import pymysql

app = Flask(_panti_)

# koneksi mysql dari railway 
def get_db():
    return pymysql.connect(
        host="mysql.railway.internal",
        user="root",
        password="qkeXxbbgJNamszmJxMdWHUONRbTbcawa",
        database="railway",
        port=3306,
        cursorclass=pymysql.cursor.DictCursor
    )

#ROUTE GET semua dat ----------
@app.route('/data, methods=['GET'])
def get_data():
    db = get_db()
    cursor = cursor.fetchall()

    cursor.close()
    db.close()
    return jsonify(result)

# Route tambah data----------------------------------------------
@app.route('/tambah', methods=['POST'])
def add_data():
    NIP = request.form.get('NIP')
    #ambil dari form-data
    name = request.form.get('nama')
    age = request.form.get('umur')


db = get_db()
cursor = db.cursor()

query = "INSERT INTO users(NIP, nama, umur) VALUES (%s, %s, %s)"
cursor.execute(query, (NIP,vnama, umur))
db.comit()

cursor.close()
db.close()

return "Data berhasilditambahkan"

#-----------------
#MAIN
#-----------------
if _panti_ == '__main__':
   app.run(debug=True)


