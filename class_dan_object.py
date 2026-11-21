# class_dan_object.py (versi yang sudah diubah)

# ===== 1. Class dan Object =====
class Kampus:
    pass


class Mahasiswa:
    pass


kampus1 = Kampus()
kampus2 = Kampus()
print(type(kampus1))
print(type(kampus2))

mhs1 = Mahasiswa()
mhs2 = Mahasiswa()
print(type(mhs1))
print(type(mhs2))

# ===== 2. Instance attribute =====
mhs1.nim = 111111
mhs1.nama = "Citra"
print(mhs1.nim)
print(mhs1.nama)

mhs2.nim = 111112
mhs2.nama = "Dimas"
print(mhs2.nim)
print(mhs2.nama)


# ===== 3. Class attribute =====
class Kampus:
    nama = "Universitas Contoh"
    alamat = "Jakarta"


kampus = Kampus()
print(kampus.nama)
print(kampus.alamat)


class Mahasiswa:
    nim = 0
    nama = ""
    jurusan = "Sistem Informasi"


mahasiswa = Mahasiswa()
print(mahasiswa.nim)
print(mahasiswa.nama)
print(mahasiswa.jurusan)


# ===== 4. Method =====
class Mahasiswa:
    nim = 0
    nama = ""
    jurusan = "Sistem Informasi"

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}, jurusan {self.jurusan}")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "Citra"
mahasiswa.perkenalan()
mahasiswa.hello("Dimas")
