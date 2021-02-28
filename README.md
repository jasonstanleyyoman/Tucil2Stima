### Tugas Kecil IF 2211 Strategi Algoritma

## Masalah
Diberikan sebuah list mata kuliah beserta requirementnya, program diminta untuk menentukan matkul apa yang bisa diambil di sebuah semester (semester 1 - 8). Sebuah matkul hanya bisa diambil jika mahasiswa sudah mengambil seluruh requirementnya

## Algoritma Decrease And Conquer
Problem ini sama dengan masalah topological sorting dan penyelesaiannya menggunakan pendekatan decrease and conquer. Pada algoritma ini, setiap masalah akan dikurangi kompleksitasnya dan akan melakukan pemanggilan algoritma lagi sampai masalah selesai. Cara mengurangi kompleksitasnya adalah dengan mencari node di graf yang memiliki derajat masuk sama dengan 0. Node yang didapatkan akan dihapus dari graf dan mungkin akan memunculkan node baru yang mungkin derajat masuknya 0.


## Requirement

Solusi program dibuat dengan bahasa ```python```. Anda bisa melakukan instalasi ```python``` di tautan berikut [Python3 Installation](https://www.python.org/downloads/)

Tidak ada requirement tambahan selain library-library yang sudah disediakan ```python``` pada saat instalasi

## Cara Penggunaan
Buka terminal di folder [src](/src). Namun sebelum itu, test file harus dimasukkan ke dalam folder [test](/test).
```sh
python 13519019.py {NAMA_FILE_TEST}
```
Misal Anda telah membuat file test baru bernama ```new.txt``` di folder test, maka command untuk menjalankan program adalah:
```sh
python 13519019.py new
```

## Author
[Jason Stanley Yoman](jasonstanleyyoman@gmail.com)

NIM : 13519019
