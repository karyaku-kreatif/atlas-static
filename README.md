# Atlas Cuaca dan Musim Dunia (versi statis untuk GitHub Pages)

Tanpa server. Browser pengunjung yang menghitung jam lokal, musim, serta matahari terbit dan terbenam,
dan mengambil cuaca langsung dari Open-Meteo. Data kota (sekitar 50 ribu) berasal dari GeoNames.

## Tayangkan di GitHub Pages
1. Buat repositori baru di GitHub dan unggah semua isi folder ini (termasuk folder `.github`). Cabang utamanya harus bernama `main`.
2. Buka **Settings → Pages**, lalu pada **Source** pilih **GitHub Actions**.
3. Buka tab **Actions**, jalankan alur **Tayangkan ke GitHub Pages** (atau cukup lakukan satu commit).
   Alur ini mengunduh GeoNames, membuat `public/data/cities.json`, lalu menayangkan situs.
4. Alamat situs: `https://NAMA-AKUN.github.io/NAMA-REPO/`.

## Uji di komputer sendiri
```bash
python build_data.py cities5000
python -m http.server -d public 8000
```
Buka http://localhost:8000

## Catatan
- `public/data/cities.json` di repositori hanya contoh kecil; alur GitHub menggantinya dengan data lengkap saat build.
- Batas gratis Open-Meteo dihitung per alamat IP pengunjung dan hanya untuk penggunaan non-komersial.
- Pakai `cities15000` untuk data lebih ringan (sekitar 25 ribu kota).
- Atribusi GeoNames dan Open-Meteo sudah ada di footer; jangan dihapus.
