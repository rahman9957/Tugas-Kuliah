// --- PANTI PUTRI ---
db.panti_putri.insertMany([
  { nama: "Manda", usia: "15 Bulan", asal: "Kecamatan Srono", status_sekolah: "Belum Sekolah", status_anak: "Dhuafa" },
  { nama: "Mutiara", usia: "3 Tahun", asal: "Kecamatan Kabat", status_sekolah: "Belum Sekolah", status_anak: "Dhuafa" },
  { nama: "Amira", usia: "6 Tahun", asal: "Kecamatan Banyuwangi", status_sekolah: "TK", status_anak: "Dhuafa" },
  { nama: "Intan", usia: "7 Tahun", asal: "Kecamatan Kabat", status_sekolah: "MI", status_anak: "Dhuafa" },
  { nama: "Aini", usia: "8 Tahun", asal: "Kecamatan Kabat", status_sekolah: "MI", status_anak: "Dhuafa" },
  { nama: "Amel", usia: "14 Tahun", asal: "Kecamatan Kalipuro", status_sekolah: "SMK", status_anak: "Dhuafa" },
  { nama: "Siva", usia: "15 Tahun", asal: "Kabupaten Sumenep", status_sekolah: "SMK", status_anak: "Dhuafa" }
]);

// --- PANTI PUTRA ---
db.panti_putra.insertMany([
  { nama: "Arwi", usia: "10 Hari", asal: "Bali", status_sekolah: "Belum Sekolah", status_anak: "Dhuafa" },
  { nama: "Farhan", usia: "16 Bulan", asal: "Banyuwangi", status_sekolah: "Belum Sekolah", status_anak: "Dhuafa" },
  { nama: "Juna", usia: "3 Tahun", asal: "Banyuwangi", status_sekolah: "Belum Sekolah", status_anak: "Dhuafa" },
  { nama: "Biant", usia: "9 Tahun", asal: "Banyuwangi", status_sekolah: "SD", status_anak: "Dhuafa" },
  { nama: "Adit", usia: "11 Tahun", asal: "Banyuwangi", status_sekolah: "SD", status_anak: "Dhuafa" },
  { nama: "Rahul", usia: "14 Tahun", asal: "Banyuwangi", status_sekolah: "SMK", status_anak: "Piatu" },
  { nama: "Farihal", usia: "14 Tahun", asal: "Banyuwangi", status_sekolah: "SMK", status_anak: "Dhuafa" },
  { nama: "Anam", usia: "15 Tahun", asal: "Banyuwangi", status_sekolah: "SMK", status_anak: "Dhuafa" },
  { nama: "Riski", usia: "10 Tahun", asal: "Lombok", status_sekolah: "SD", status_anak: "Dhuafa" }
]);

// INSERT (sudah dilakukan di atas)

// READ / FIND
db.panti_putra.find({ status_sekolah: "SMK" });

// UPDATE
db.panti_putri.updateOne(
  { nama: "Siva" },
  { $set: { status_anak: "Yatim Piatu" } }
);

// DELETE
db.panti_putra.deleteOne({ nama: "Arwi" });

db.donatur.insertOne({
  nama: "Ibu Rina",
  kontak: {
    no_hp: "081234567890",
    alamat: "Surabaya"
  },
  donasi: {
    jumlah: 500000,
    metode: "Transfer",
    tanggal: "2025-06-01"
  }
});

// Data anak mengacu pada ID donatur
const idDonatur = ObjectId(); // contoh ID referensi

db.donatur.insertOne({
  _id: idDonatur,
  nama: "Pak Budi",
  no_hp: "089876543210",
  alamat: "Malang"
});

db.penerima_donasi.insertOne({
  nama_anak: "Amira",
  umur: "6 Tahun",
  donatur_id: idDonatur
});

// QUERY: cari anak usia SMK
db.panti_putri.find({ status_sekolah: "SMK" });

// AGGREGATION: hitung jumlah anak per status sekolah
db.panti_putra.aggregate([
  { $group: { _id: "$status_sekolah", total: { $sum: 1 } } }
]);