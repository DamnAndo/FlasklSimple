# Gunakan Python image yang lebih kecil dan efisien
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Copy requirements file terlebih dahulu untuk memanfaatkan Docker layer cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file aplikasi ke container
COPY app.py .

# Buat directory untuk data jika belum ada
RUN mkdir -p /app/data

# Expose port (sesuai dengan yang diubah ke 5001)
EXPOSE 5001

# Environment variable untuk Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Command untuk menjalankan aplikasi
CMD ["python", "app.py"]
