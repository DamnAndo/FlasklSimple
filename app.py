import os
import json
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Tentukan nama file JSON untuk menyimpan data
DATA_FILE = 'data_peserta.json'

def load_data():
    """Fungsi untuk membaca data dari file JSON"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(new_entry):
    """Fungsi untuk menyimpan data baru ke file JSON"""
    data = load_data()
    data.append(new_entry)
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Template HTML yang digabung langsung di dalam file Python (Inline Template)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Final Project - Fase 1</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        h2, h3 {
            color: #2c3e50;
            margin-top: 0;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        hr {
            border: 0;
            height: 1px;
            background: #ddd;
            margin: 30px 0;
        }
        .data-list {
            list-style: none;
            padding: 0;
        }
        .data-item {
            background: #f9f9f9;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin-bottom: 10px;
            border-radius: 0 4px 4px 0;
        }
        .data-item strong {
            color: #2c3e50;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Form Input Data (Fase 1)</h2>
    <form action="/submit" method="POST">
        <div class="form-group">
            <label for="nama">Nama:</label>
            <input type="text" id="nama" name="nama" required placeholder="Masukkan nama kamu">
        </div>
        <div class="form-group">
            <label for="alamat">Alamat:</label>
            <textarea id="alamat" name="alamat" rows="3" required placeholder="Masukkan alamat kamu"></textarea>
        </div>
        <button type="submit">Simpan Data</button>
    </form>

    <hr>

    <h3>Data Terdaftar:</h3>
    <ul class="data-list">
        {% if semua_data %}
            {% for item in semua_data %}
                <li class="data-item">
                    <strong>Nama:</strong> {{ item.nama }} <br>
                    <strong>Alamat:</strong> {{ item.alamat }}
                </li>
            {% endfor %}
        {% else %}
            <p style="color: #7f8c8d; font-style: italic;">Belum ada data yang disimpan.</p>
        {% endif %}
    </ul>
</div>

</body>
</html>
"""

@app.route('/')
def index():
    # Ambil semua data dari file JSON untuk ditampilkan di bawah form
    semua_data = load_data()
    return render_template_string(HTML_TEMPLATE, semua_data=semua_data)

@app.route('/submit', methods=['POST'])
def submit():
    # Ambil data dari form
    nama = request.form.get('nama')
    alamat = request.form.get('alamat')
    
    if nama and alamat:
        # Simpan ke data format dict
        new_entry = {
            'nama': nama,
            'alamat': alamat
        }
        save_data(new_entry)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Aplikasi berjalan di mode debug pada port 5000
    app.run(debug=True, host='0.0.0.0', port=5001)
