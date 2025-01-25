# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jelaskan latar belakang bisnis dari perushaan tersebut.

Jaya Jaya Maju adalah perusahaan multinasional yang didirikan pada tahun 2000 dan kini mempekerjakan lebih dari 1000 orang yang tersebar di berbagai wilayah di seluruh negeri.

### Permasalahan Bisnis

Meskipun telah berkembang menjadi perusahaan besar, Jaya Jaya Maju masih menghadapi tantangan dalam mengelola karyawan. Akibatnya, tingkat attrition rate, persentase karyawan yang keluar dibandingkan total karyawan—mencapai lebih dari 10%.

### Cakupan Proyek

- Membuat business dashboard tentang faktor faktor penyebab attrition
- Mengeksplorasi data dan insight karyawan perusahaan lewat EDA
- Membangun model klasifikasi untuk prediksi kemungkinan attrition
- Menyiapkan enviroment dan mengirim dataset ke database
- Menjawab question tentang faktor faktor apa saja yang berpengaruh dengan attrition

### Persiapan

Sumber data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) (./dataset)

Setup environment:

```
pip install -r requirements.txt
```

Buka notebook lewat jupyter notebook/google colab atau jalankan attrition API dengan `py prediction.py` lalu test model dengan menjalakan `sh test.sh`

## Business Dashboard

Business dashboard yang dibuat menampilkan berbagai faktor yang mempengaruhi attrition (tingkat keluar karyawan) di perusahaan **Jaya Jaya Maju**. Dashboard ini berisi beberapa visualisasi data yang membantu manajer HR dalam memahami pola yang berkontribusi terhadap tingginya attrition rate.  

1. **Attrition Distribution**  
   - Menampilkan distribusi karyawan yang keluar dan bertahan.  
2. **Total Working Years Distribution Group by Attrition**  
   - Menggambarkan hubungan antara jumlah tahun bekerja dengan attrition.  
3. **Monthly Income Distribution Group by Attrition**  
   - Menganalisis dampak gaji bulanan terhadap kemungkinan karyawan keluar.  
4. **Distance from Home Distribution Group by Attrition**  
   - Mengukur apakah jarak rumah ke kantor berpengaruh terhadap tingkat keluar karyawan.  
5. **Marital Status Distribution Group by Attrition**  
   - Memeriksa pengaruh status pernikahan terhadap keputusan untuk keluar.  
6. **Overtime Distribution Group by Attrition**  
   - Menunjukkan apakah karyawan yang sering lembur lebih cenderung keluar.  
7. **Job Level Distribution Group by Attrition**  
   - Membandingkan level pekerjaan dengan tingkat keluar karyawan.  
8. **Business Travel Distribution Group by Attrition**  
   - Menilai apakah frekuensi perjalanan bisnis memengaruhi keputusan keluar.  

Dashboard ini memungkinkan HR untuk mengidentifikasi faktor utama yang berkontribusi pada attrition dan mengambil langkah strategis untuk mengurangi tingkat turnover karyawan.

[lihat realtime dashboard](http://146.190.111.51:3000/public/dashboard/1f694ca9-c6c3-411e-bf8d-c652d4ef3844)

## Conclusion

Proyek yang dikerjakan mengatasi problem attrition rate yang tinggi pada perusahaan. Membangun model machine learning untuk memprediksi kecenderungan attrition untuk melakukan pencegahan. Mengetahui faktor faktor penting terjadinya attrition membuat tim HR memiliki pengetahuan dan insight dalam alasan mengapa seseorang melakukan attrition, dengan begini tim HR dapat membuat informed decision dalam kebijakan atau keputusan yang diambil.

### Rekomendasi Action Items (Optional)

Dari faktor faktor yang ada, berikut rekomendasi yang dapat dilakukan dalam membuat kebijakan:

- Memberikan berbagai insentif lebih apabila overtime memang harus dilakukan
- Evaluasi beban kerja karyawan dan terapkan batasan lembur
- Program retensi untuk karyawan baru dan level rendah, mis: mentorship/career development
- Kebijakan remote/hybrid working bagi karyawan yang tinggal jauh
- Subsidi transportasi atau akomodasi
- Mengapreasi dengan insentif bagi mereka yang sudah bekera lama
