## Phone & Social Media Lookup Tool 🔍📱

*command-line tool* berbasis Python yang dirancang untuk melakukan investigasi informasi awal (*reconnaissance*) secara cepat terhadap nomor telepon atau WhatsApp. Tool ini membantu analis keamanan, investigator OSINT, dan developer untuk mengidentifikasi validitas nomor serta melacak jejak digital (digital footprint) terkait di platform media sosial seperti **Instagram** dan **Facebook**.

---

## 🚀 Fitur Utama

*   **WhatsApp Validator:** Memeriksa apakah nomor target terdaftar secara aktif di WhatsApp menggunakan validasi API publik tanpa perlu login.
*   **Phone Enrichment:** Integrasi modul *reverse lookup* untuk mengidentifikasi data negara, provider (carrier), lokasi geografis, dan deteksi kebocoran informasi awal.
*   **Automated Social Media Hunter:** Memanfaatkan teknik *Google Dorking* yang dioptimalkan secara otomatis untuk mencari indeks profil publik **Instagram** dan **Facebook** berdasarkan nama/username target.
*   **Interactive CLI Interface:** Tampilan antarmuka terminal yang bersih, intuitif, dan *user-friendly* dengan pewarnaan otomatis menggunakan `colorama`.

---

## Instalasi & Persiapan
​1. Kloning Repositori
​Langkah pertama, klon repositori ini ke direktori lokal Anda :
```
git clone https://github.com/123tool/Social-Media-Lookup-Tool.git
cd Social-Media-Lookup-Tool
```
## 2. Install Dependency
​Pastikan Anda sudah menginstal Python 3.8 ke atas. Pasang pustaka pendukung menggunakan perintah berikut :
```
pip install -r requirements.txt
```
## 3. Konfigurasi API (Opsional)
​Buka file config.py jika Anda ingin mengaktifkan fitur pencarian lokasi dari Numverify. Masukkan API Key Anda pada variabel berikut :
```
NUMVERIFY_API_KEY = "MASUKKAN_API_KEY_ANDA_DI_SINI"
```
## 4. Cara Penggunaan
​Jalankan skrip utama melalui terminal atau command prompt Anda :
```
python main.py
```

## Alur Kerja Tool :

- ​Masukkan Nomor Telepon: Input nomor target dengan format kode negara (contoh: 6281234567xxx).
- Cek Status WA : Sistem akan memvalidasi apakah nomor tersebut aktif di WhatsApp beserta tautan langsungnya.
- ​Enrichment Data : Informasi seputar operator seluler dan wilayah nomor akan ditampilkan.
- ​Social Hunting : Masukkan nama lengkap atau nama panggung target (bisa didapatkan dari GetContact/Truecaller) untuk melacak otomatis profil Instagram dan Facebook mereka yang terindeks di publik.

## ​🛑 Catatan Keamanan & Disclaimer

​*Tool ini dibuat murni untuk tujuan edukasi, analisis keamanan digital, investigasi forensik legal, dan riset OSINT (Open Source Intelligence). Penulis tidak bertanggung jawab atas segala bentuk penyalahgunaan tool ini yang melanggar hukum privasi atau ketentuan layanan (Terms of Service) dari platform pihak ketiga terkait. Gunakan dengan bijak dan bertanggung jawab.*
