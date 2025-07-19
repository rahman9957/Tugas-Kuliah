db.anak_asuh.find().pretty()

use panti_asuhan

db.anak_asuh.insertMany([
  {
    _id: 143411,
    nama: "Amel",
    umur: 16,
    jenis_kelamin: "Perempuan",
    asal: "Ketapang, Banyuwangi",
    pendidikan: "SMK",
    nilai: 70
  },
  {
    _id: 143412,
    nama: "Siva",
    umur: 16,
    jenis_kelamin: "Perempuan",
    asal: "Sumenep, Madura",
    pendidikan: "SMK",
    nilai: 76
  },
  {
    _id: 143413,
    nama: "Aini",
    umur: 8,
    jenis_kelamin: "Perempuan",
    asal: "Kabat, Banyuwangi",
    pendidikan: "MI",
    nilai: 69
  },
  {
    _id: 143414,
    nama: "Intan",
    umur: 7,
    jenis_kelamin: "Perempuan",
    asal: "Kabat, Banyuwangi",
    pendidikan: "MI",
    nilai: 60
  },
  {
    _id: 143415,
    nama: "Mira",
    umur: 7,
    jenis_kelamin: "Perempuan",
    asal: "Bali",
    pendidikan: "MI",
    nilai: 70
  },
  {
    _id: 143416,
    nama: "Tiara",
    umur: 3,
    jenis_kelamin: "Perempuan",
    asal: "Kalipuro, Banyuwangi",
    pendidikan: "Belum Sekolah",
    nilai: 0
  },
  {
    _id: 143417,
    nama: "Manda",
    umur: 1.5,
    jenis_kelamin: "Perempuan",
    asal: "Srono, Banyuwangi",
    pendidikan: "Belum Sekolah",
    nilai: 0
  }
])

db.anak_asuh.aggregate([
  {
    $group: {
      _id: "$jenis_kelamin",
      jumlah: { $sum: 1 }
    }
  }
])

db.anak_asuh.aggregate([
  {
    $group: {
      _id: "$pendidikan",
      rata_rata_nilai: { $avg: "$nilai" }
    }
  }
])

db.anak_asuh.aggregate([
  {
    $group: {
      _id: "$asal",
      jumlah: { $sum: 1 }
    }
  }
])

db.anak_asuh.aggregate([
  {
    $group: {
      _id: "$pendidikan",
      nilai_tertinggi: { $max: "$nilai" }
    }
  }
])

db.anak_asuh.aggregate([
  {
    $group: {
      _id: "$pendidikan",
      nilai_terendah: { $min: "$nilai" }
    }
  }
])

db.anak_asuh.aggregate([
  {
    $match: { pendidikan: "Belum Sekolah" }
  },
  {
    $group: {
      _id: "$pendidikan",
      jumlah: { $sum: 1 }
    }
  }
])

db.anak_asuh.aggregate([
  {
    $sort: { nilai: -1 }
  },
  {
    $limit: 1
  }
])

db.anak_asuh.aggregate([
  {
    $group: {
      _id: "$pendidikan",
      jumlah_anak: { $sum: 1 }
    }
  }
])
