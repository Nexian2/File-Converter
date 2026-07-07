<p align="center">
  <img src="https://img.icons8.com/papercut/120/file.png" width="80" alt="File Logo">
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

==========================================================================================

# Instant PDF DOCX Converter 

A simple web app to convert files back and forth between PDF and DOCX instantly right from your browser. Once you drop the file, it processes the conversion locally and automatically uploads the result to GoFile to generate a ready-to-share download link

This app is built using Gradio for the web interface, along with the pdf2docx and docx2pdf libraries to handle the conversion under the hood

## Key Features

- Fully automated process with no submit button needed, just upload your file and wait for the result
- Two conversion modes you can switch instantly: PDF to DOCX or DOCX to PDF
- Converted files can be downloaded directly to your computer or shared via GoFile cloud link

## How It Works

1. Select the desired conversion mode on the web page
2. Drop or upload your document file into the available upload area
3. The app reads the file immediately to trigger the local conversion process
4. Once converted, the app requests the GoFile server to prepare a storage slot
5. The converted file is uploaded to the cloud and the system returns the download link instantly

## System Requirements

Make sure Python is already installed on your computer. Other than that, this app requires a few extra libraries that can be installed via pip

```bash
pip install -r requirements.txt
```

After installing requirements.txt

```bash
Python3 Main.py
```

And Finish, good luck Trying!
