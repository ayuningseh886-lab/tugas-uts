# Tugas Python – Object-Oriented Programming (OOP)

Repository ini berisi rangkuman materi dan latihan Python berdasarkan file tugas yang dikumpulkan.

## Isi Repository

- `materi/Python_OOP.pptx` — materi presentasi asli tentang Class dan Object.
- `materi/Rangkuman_Materi.md` — ringkasan konsep Python OOP.
- `src/class_dan_object.py` — latihan coding Class dan Object, attributes, dan methods.
- `src/percakapan_di_mal.py` — program sederhana yang menampilkan dialog pertemuan di mal.
- `output/output.txt` — hasil output latihan Class dan Object.
- `output/README.txt` — catatan dari file latihan awal.

## Ringkasan Materi

### 1. Class dan Object
Class adalah blueprint atau template untuk membuat object. Object adalah instance atau hasil pembuatan dari sebuah class. Beberapa object dapat dibuat dari class yang sama dengan nilai data yang berbeda.

### 2. Attributes
Attribute adalah variabel yang menyimpan data pada object.

- **Instance attribute** dimiliki oleh object tertentu. Nilainya dapat berbeda antara satu object dan object lainnya.
- **Class attribute** didefinisikan di dalam class dan menjadi nilai bawaan yang dapat diakses oleh object dari class tersebut.

### 3. Methods
Method adalah function yang berada di dalam class dan dapat dipanggil melalui object.

### 4. Parameter `self`
`self` merujuk pada instance atau object yang sedang memanggil method. Dengan `self`, method dapat mengakses attribute milik object tersebut.

### 5. Method dengan Parameter
Method dapat menerima parameter tambahan selain `self`, seperti function pada umumnya.

### 6. Naming Conventions
- Nama class menggunakan **PascalCase**, misalnya `Mahasiswa` atau `MataPelajaran`.
- Nama method menggunakan **snake_case**, misalnya `perkenalan()` atau `jalankan()`.
- Nama attribute menggunakan **snake_case**, misalnya `nama_depan` atau `nama_belakang`.

## Cara Menjalankan Program

Pastikan Python sudah terpasang. Buka terminal pada folder repository, lalu jalankan:

```bash
python src/class_dan_object.py
```

Untuk menjalankan program percakapan di mal:

```bash
python src/percakapan_di_mal.py
```

## Catatan

Program menggunakan Python standar dan tidak memerlukan instalasi library tambahan.
