# Sorting_Python

# Bubble Sort

Algoritma bubble sort cukup populer dan sederhana. Proses pada bubble sort dilakukan dengan penukaran data disebelahnya secara terus menerus hingga dalam suatu iterasi tertentu tidak ada lagi perubahan atau pertukaran. Algoritma bubble sort termasuk ke dalam kategori algoritma comparison sort, karena menggunakan perbandingan pada operasi antar elemenya.
Analogi algoritma bubble sort :
1. Bandingkan nilai pada data ke satu dengan data ke dua
2. Apabila nilai data ke satu lebih besar dari data ke dua maka tukar posisinya
3. Kemudian data yang lebih besar tersebut dibandingkan lagi dengan data ketuga
4. Apabila data ke tiga lebih kecil dari data ke dua maka tukar posisinya
5. Dan begitu seterusnya hingga semua data yang ada menjadi terurut

# Selection Sort

Algoritma selection sort merupakan pengurutan dengan konsep memilih elemen dengan nilai paling rendah dan menukar elemen tersebut dengan elemen ke –i. Nilai dari i dimulai dari 1 ke n, yang dimana n merupakan jumlah total elemen dikurangi satu.
Analogi algoritma selection sort :
1. Memulai pengecekan data dari data ke 1 hingga data ke n.
2. Menentukan bilangan dengan index terkecil dari data pada bilangan tersebut.
3. Menukar bilangan index terkecil dengan bilangan pertama.
4. Begitu seterusnya hingga data berhasil diurutkan semuanya.

# Insertion Sort

Algoritma insertion sort merupakan suatu metode pengurutan data dengan melakukan penempatan setiap elemen data pada pisisina dengan membandingkan dengan data-data yang telah ada. Prinsip dari insertion sort adalah dengan membagi data yang akan diurutkan menjadi dua kelompok, satu kelompok yang belum diurutkan dan yang satunya lagi sudah diurutkan, Elemen yang pertama diambil dari kelompok list yang belum diurutkan dan kemudian ditempatkan sesuai posisinya pada bagian lain yang belum diurutkan.
Analogi Algoritma insertion sort
1. Membandingkan data kedua dengan data kesatu
2. Apabila data ke dua lebih kecil maka tukar posisinya
3. Data ketiga dibandingkan dengan data kesatu dan kedua
4. Apabila data ketiga lebih kecil tukar lagi posisinya
5. Data keempat dibandingkan dengan data ketiga hingga kesatu
6. Apabila data keempat lebih kecil dari ketigana maka letakkan data keempat ke posisi paling depan
7. Begitu seterusnya hingga tidak ada lagi data yang dapat dipindahkan.

# Quick Sort

Algoritma quick sort ini cara kerjanya berprinsip pada penekatan divide and conquer yakni dengan memilih satu elemen sebagai elemen pivot dan mempartisi array sehingga sisi kiri pada pivot mempunyai semua elemen dengan nilai yang lebih kecil dibandingkan dengan elmen pivot dan pada sisi kanan mempunyai semua elemen dengan nilai yang lebih besar dibandingkan dengan nilai elemen pivot.
Analogi algoritma quick sort :
1. Mempunyai data A yang memiliki N elemen, pilih sembarang elemen dari data tersebut biasanya elemen pertama misalkan elemen x
2. Kemudian semua elemen tersebut disusun dengan menempatkan x pada posisi j sedemikian rupa sehingga elemen ke satu sampai pada j-1 dan memiliki nilai yang lebih besar dari x
3. Begitu seterusnya setiap sub data

# Merge Sort

Algoritma merge sort merupakan salah satu pengurutan dengan metode memecah data kemudian mengolah untuk diselesaikan pada setiap bagian dan menggabungkan kembali sehingga data tersebut berhasil tersusun. Merge sort dalam menyelesaikan pengurutan membutuhkan fungsi rekursif.
Analogi algoritma merge sort :
1. Data dipecah menjadi dua kelompok dimana kelompok pertama adalah setengah apabila data genap atau setengah kurang satu apabila data ganjil dari seluruh data.
2. Kemudian dilakukan pemecahan kembali pada masing-masing kelompok hingga hanya terdapat satu data pada satu kelompok.
3. Setelah digabungkan kembali dengan membandingkan pada blok yang sama apakah data pertama lebih besar dari pada data ketengah ditambah satu, jika iya maka data ketengah ditambah satu dipindah menjadi data pertama.
4.Kemudian data pertama tadi hngga data ketengah dipindah menjadi data kedua sampai data ketengah ditambah satu.
5. Begitu seterusnya sehingga membentuk sebuah data yang tersusun dalam satu kelompok yang utuh.

# Referensi :

https://www.pythonindo.com/insertion-sort-di-python/

http://codinginpro.blogspot.com/2018/06/macam-macam-sorting-pada-python.html

https://blogbugabagi.blogspot.com/2019/12/algoritma-sorting-bubble-sort-seletion.html

