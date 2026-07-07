# Instant PDF DOCX Converter

Aplikasi web sederhana buat konversi bolak-balik antara PDF dan DOCX secara instan lewat browser. Begitu file ditaruh, aplikasi langsung memproses konversi secara lokal dan otomatis mengunggah hasilnya ke GoFile untuk menghasilkan link unduhan yang siap dibagikan

btw aplikasi ini dibangun menggunakan Gradio sebagai antarmuka web, serta library pdf2docx dan docx2pdf untuk menangani proses konversinya

## Fitur Utama

- Proses otomatis tanpa tombol submit, tinggal upload file dan tunggu hasilnya
- Dua mode konversi yang bisa dipilih langsung: PDF ke DOCX atau DOCX ke PDF
- Hasil konversi bisa diunduh langsung ke komputer atau dibagikan lewat link cloud GoFile

## Persyaratan Sistem

Pastikan Python sudah terinstal di komputer Anda. Selain itu, aplikasi ini membutuhkan beberapa library tambahan yang bisa dipasang lewat pip

```bash
pip install gradio pdf2docx docx2pdf

woi
