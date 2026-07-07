<p align="center">
  <img src="https://img.icons8.com/color/96/pdf.png" width="60" alt="PDF Logo">
  <img src="https://img.icons8.com/color/96/microsoft-word_2019.png" width="60" alt="Word Logo">
</p>

# Instant PDF DOCX Converter
Aplikasi web sederhana buat konversi file antara PDF dan DOCX secara instan lewat browser aplikasi dan langsung memproses konversi secara lokal dan akan otomatis mengunggah hasilnya ke GoFile untuk menghasilkan link unduhan yang siap didownload

Aplikasi ini dibangun menggunakan Gradio sebagai antarmuka web, serta library pdf2docx dan docx2pdf untuk menangani proses konversinya

## Fitur Utama

- Proses otomatis tanpa tombol submit, tinggal upload file dan tunggu hasilnya
- Dua mode konversi yang bisa dipilih langsung: PDF ke DOCX atau DOCX ke PDF
- Hasil konversi bisa diunduh langsung ke komputer atau dibagikan lewat link cloud GoFile

## Cara Kerja Sistem

1. Pengguna memilih mode konversi yang diinginkan pada halaman web
2. File dokumen dimasukkan ke dalam kolom unggahan yang tersedia
3. Aplikasi langsung membaca file tersebut untuk memicu fungsi konversi secara lokal
4. Setelah konversi selesai, aplikasi meminta server GoFile untuk menyiapkan slot penyimpanan
5. File hasil konversi diunggah ke cloud dan sistem mengembalikan link unduhan secara instan

## Persyaratan Sistem

Pastikan Python sudah terinstal di komputer Anda. Selain itu, aplikasi ini membutuhkan beberapa library tambahan yang bisa dipasang lewat pip

```bash
pip install -r requirements.txt
```

Dan habistuh tinggal masukin perintah

```bash
Python3 Main.py
```

Selesai, selamat mencoba!
