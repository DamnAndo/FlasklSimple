# Final Project - Fase 1: Aplikasi Flask Sederhana

Aplikasi web sederhana menggunakan Flask untuk form input data nama dan alamat yang disimpan ke file JSON.

## Deskripsi

Aplikasi ini merupakan bagian dari Final Project Cloud Full-Stack Deployment pada Fase 1. Aplikasi memiliki fitur:
- Form input untuk nama dan alamat
- Penyimpanan data ke file JSON (`data_peserta.json`)
- Menampilkan semua data yang tersimpan di bawah form
- Desain responsif dengan CSS inline

## Cara Menjalankan di Lokal

### Opsi 1: Running Langsung (Python)

#### Prasyarat
- Python 3.7+ terinstall
- pip (Python package manager)

#### Instalasi
1. Clone atau download repository ini
2. Buka terminal/command prompt di folder project
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Menjalankan Aplikasi
```bash
python app.py
```
Aplikasi akan berjalan di: `http://127.0.0.1:5001`

### Opsi 2: Docker (Recommended untuk Deployment)

#### Prasyarat
- Docker dan Docker Compose terinstall

#### Menjalankan dengan Docker Compose
```bash
# Build dan jalankan container
docker-compose up --build

# Atau jalankan di background
docker-compose up -d --build
```

Aplikasi akan berjalan di: `http://localhost:5001`

#### Menghentikan Container
```bash
docker-compose down
```

#### Melihat Logs
```bash
docker-compose logs -f
```

## Cara Penggunaan

1. Buka browser dan akses `http://127.0.0.1:5001` (atau `http://localhost:5001` untuk Docker)
2. Isi form dengan nama dan alamat
3. Klik tombol "Simpan Data"
4. Data akan otomatis tersimpan di file `data_peserta.json`
5. Data yang tersimpan akan ditampilkan di bawah form

## Struktur File

```
FlasklSimple/
├── app.py                 # File utama aplikasi Flask
├── requirements.txt       # Dependencies Python
├── Dockerfile            # Konfigurasi Docker container
├── docker-compose.yml    # Konfigurasi Docker Compose
├── README.md             # Dokumentasi project
├── data/                 # Folder data (untuk Docker volume)
└── data_peserta.json     # File database (auto-generated)
```

## Fitur Teknis

- **Framework**: Flask 2.3.3
- **Storage**: File JSON
- **Template**: HTML dengan CSS inline (single-file approach)
- **Port**: 5001
- **Host**: 0.0.0.0 (accessible dari network)
- **Containerization**: Docker support

## 🌍 Live Deployment

**Aplikasi Live:** https://flask-simple-app-224617852311.us-central1.run.app

## 🔄 CI/CD Pipeline Setup

### Google Cloud Build Configuration (Recommended)

Project ini menggunakan **Google Cloud Build** untuk CI/CD - lebih native ke GCP dan tidak perlu service account keys!

### 📋 Langkah Setup Cloud Build CI/CD

**1. Push ke GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit with Cloud Build CI/CD"
   git branch -M main
   git remote add origin https://github.com/USERNAME/flask-simple-app.git
   git push -u origin main
   ```

**2. Setup Cloud Build Trigger (via GCP Console):**
- Buka **Cloud Build** → **Triggers**
- Klik **Create Trigger**
- Pilih **GitHub** → Connect repository Anda
- Event: **Push to branch**
- Branch: `^main$`
- Configuration: **Cloud Build configuration file (YAML)**
- Cloud Build configuration file location: `cloudbuild.yaml`
- Klik **Create**

**3. Automatic Deployment:**
Setiap push ke branch `main` akan otomatis:
- Build Docker image dengan Cloud Build
- Push ke Artifact Registry
- Deploy ke Cloud Run
- **Tanpa perlu manage secrets!**

### 📁 File CI/CD
- **`cloudbuild.yaml`** - Konfigurasi Cloud Build
- **`.github/workflows/deploy.yml`** - GitHub Actions (backup)

### 🔧 GitHub Actions (Alternative)
Jika prefer GitHub Actions, setup Workload Identity Federation atau gunakan service account key.

## Persiapan Fase Selanjutnya

Project ini siap untuk:
- ✅ Fase 2: Containerization dengan Docker (SELESAI)
- ✅ Fase 3: Cloud deployment ke GCP Cloud Run (SELESAI)
- ✅ Fase 4: CI/CD Pipeline setup (SELESAI)
- Fase 5: Monitoring & Security (Optional)

## Catatan

- File `data_peserta.json` akan otomatis dibuat saat pertama kali data diinput
- Aplikasi berjalan dalam mode debug untuk development
- Tidak ada database eksternal yang diperlukan
