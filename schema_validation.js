use panti_asuhan

db.createCollection("anak_asuh", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["id", "nama", "umur", "jenis_kelamin", "asal", "pendidikan"],
      properties: {
        id: {
          bsonType: "int",
          description: "id anak harus berupa angka dan wajib diisi"
        },
        nama: {
          bsonType: "string",
          description: "nama anak harus berupa teks dan wajib diisi"
        },
        umur: {
          bsonType: "int",
          minimum: 1,
          description: "umur anak minimal 1 tahun dan wajib diisi"
        },
        jenis_kelamin: {
          enum: ["perempuan", "laki-laki"],
          description: "jenis kelamin harus 'perempuan' atau 'laki-laki'"
        },
        asal: {
          bsonType: "string",
          description: "asal daerah anak wajib diisi"
        },
        pendidikan: {
          bsonType: "string",
          description: "jenjang pendidikan anak wajib diisi"
        },
        nilai: {
          bsonType: ["int", "null"],
          minimum: 0,
          maximum: 100,
          description: "nilai harus antara 0-100 jika diisi"
        }
      }
    }
  }
})

db.anak_asuh.insertMany([
  {
    id: 143411,
    nama: "Amel",
    umur: 16,
    jenis_kelamin: "perempuan",
    asal: "Ketapang Banyuwangi",
    pendidikan: "SMK",
    nilai: 70
  },
  {
    id: 143412,
    nama: "Siva",
    umur: 16,
    jenis_kelamin: "perempuan",
    asal: "Sumenep Madura",
    pendidikan: "SMK",
    nilai: 76
  },
  {
    id: 143413,
    nama: "Aini",
    umur: 8,
    jenis_kelamin: "perempuan",
    asal: "Kabat Banyuwangi",
    pendidikan: "MI",
    nilai: 69
  },
  {
    id: 143414,
    nama: "Intan",
    umur: 7,
    jenis_kelamin: "perempuan",
    asal: "Kabat Banyuwangi",
    pendidikan: "MI",
    nilai: 60
  },
  {
    id: 143415,
    nama: "Mira",
    umur: 7,
    jenis_kelamin: "perempuan",
    asal: "Bali",
    pendidikan: "MI",
    nilai: 70
  },
  {
    id: 143416,
    nama: "Tiara",
    umur: 3,
    jenis_kelamin: "perempuan",
    asal: "Kalipuro Banyuwangi",
    pendidikan: "Belum Sekolah",
    nilai: 0
  },
  {
    id: 143417,
    nama: "Manda",
    umur: 2,
    jenis_kelamin: "perempuan",
    asal: "Srono Banyuwangi",
    pendidikan: "Belum Sekolah",
    nilai: 0
  }
])

db.anak_asuh.insertMany([
  {
    id: 143411,
    nama: "Amel",
    umur: 16,
    jenis_kelamin: "perempuan",
    asal: "Ketapang Banyuwangi",
    pendidikan: "SMK",
    nilai: 70
  },
  {
    id: 143412,
    nama: "Siva",
    umur: 16,
    jenis_kelamin: "perempuan",
    asal: "Sumenep Madura",
    pendidikan: "SMK",
    nilai: 76
  },
  {
    id: 143413,
    nama: "Aini",
    umur: 8,
    jenis_kelamin: "perempuan",
    asal: "Kabat Banyuwangi",
    pendidikan: "MI",
    nilai: 69
  },
  {
    id: 143414,
    nama: "Intan",
    umur: 7,
    jenis_kelamin: "perempuan",
    asal: "Kabat Banyuwangi",
    pendidikan: "MI",
    nilai: 60
  },
  {
    id: 143415,
    nama: "Mira",
    umur: 7,
    jenis_kelamin: "perempuan",
    asal: "Bali",
    pendidikan: "MI",
    nilai: 70
  },
  {
    id: 143416,
    nama: "Tiara",
    umur: 3,
    jenis_kelamin: "perempuan",
    asal: "Kalipuro Banyuwangi",
    pendidikan: "Belum Sekolah",
    nilai: null
  },
  {
    id: 143417,
    nama: "Manda",
    umur: 2,
    jenis_kelamin: "perempuan",
    asal: "Srono Banyuwangi",
    pendidikan: "Belum Sekolah",
    nilai: null
  }
])

db.anak_asuh.find()

db.anak_asuh.find({ pendidikan: { $ne: "Belum Sekolah" } })
