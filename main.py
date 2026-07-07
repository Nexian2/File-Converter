import os
import json
import urllib.request
from pathlib import Path
import gradio as gr
from pdf2docx import Converter
from docx2pdf import convert

def pdf_to_docx(pdf_file_path, output_file_path):
    cv = Converter(str(pdf_file_path))
    cv.convert(str(output_file_path))
    cv.close()
    return output_file_path

def docx_to_pdf(docx_file_path, output_file_path):
    convert(str(docx_file_path), str(output_file_path))
    return output_file_path

def upload_to_cloud(file_path):
    file_path = Path(file_path)
    try:
        server_req = urllib.request.Request("https://api.gofile.io/servers", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(server_req) as response:
            server_data = json.loads(response.read().decode('utf-8'))
            if server_data["status"] == "ok":
                server_name = server_data["data"]["servers"][0]["name"]
            else:
                raise Exception("Gagal mendapatkan server GoFile")

        upload_url = f"https://{server_name}.gofile.io/contents/uploadfile"
        boundary = "----WebKitFormBoundaryGofileUpload"
        
        with open(file_path, "rb") as f:
            file_data = f.read()
            
        parts = [
            b'--' + boundary.encode('utf-8'),
            b'Content-Disposition: form-data; name="file"; filename="' + file_path.name.encode('utf-8') + b'"',
            b'Content-Type: application/octet-stream',
            b'',
            file_data,
            b'--' + boundary.encode('utf-8') + b'--',
            b''
        ]
        
        body = b'\r\n'.join(parts)
        req = urllib.request.Request(upload_url, data=body)
        req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
        req.add_header('User-Agent', 'Mozilla/5.0')
        
        with urllib.request.urlopen(req) as response:
            upload_data = json.loads(response.read().decode('utf-8'))
            if upload_data["status"] == "ok":
                return upload_data["data"]["downloadPage"]
            else:
                raise Exception(upload_data.get("status", "Gagal upload"))
    except Exception as e:
        raise Exception(f"Gagal upload ke GoFile: {str(e)}")

def process_file(mode, file_obj):
    if file_obj is None:
        return "Silakan masukkan filenya terlebih dahulu", None

    input_path = Path(file_obj.name)
    
    if mode == "PDF ke DOCX":
        output_path = input_path.with_suffix(".docx")
        try:
            pdf_to_docx(input_path, output_path)
        except Exception as e:
            return f"Gagal Konversi: {str(e)}", None
    else:
        output_path = input_path.with_suffix(".pdf")
        try:
            docx_to_pdf(input_path, output_path)
        except Exception as e:
            return f"Gagal Konversi: {str(e)}", None

    try:
        cloud_url = upload_to_cloud(output_path)
        status_msg = f"Oke File berhasil dikonversi\n\n Link Cloud (GoFile):\n{cloud_url}"
    except Exception as e:
        status_msg = f"Gagal upload ke cloud: {str(e)}"

    return status_msg, str(output_path)

with gr.Blocks(title="Converter PDF ⇄ DOCX") as demo:
    gr.Markdown("# Converter PDF ⇄ DOCX")
    gr.Markdown("System Converter aman dari pengambilan data dari file anda, karena lokal jalannya")
    
    mode_input = gr.Radio(
        choices=["PDF ke DOCX", "DOCX ke PDF"], 
        value="PDF ke DOCX", 
        label="Pilih Mode Konversi"
    )
    
    file_input = gr.File(label="Seret atau pilih file Anda di sini")
    
    status_output = gr.Textbox(label="Status & Link Cloud", interactive=False)
    file_output = gr.File(label="Unduh Hasil Konversinya")
    
    file_input.change(
        fn=process_file, 
        inputs=[mode_input, file_input], 
        outputs=[status_output, file_output]
    )

if __name__ == "__main__":
    demo.launch()