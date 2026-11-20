"""Membuat public/data/cities.json dari GeoNames.
Pakai:  python build_data.py cities5000   (sekitar 50 ribu kota)
        python build_data.py cities15000  (sekitar 25 ribu kota)
        python build_data.py berkas.txt   (berkas GeoNames lokal)"""
import csv, io, json, os, sys, urllib.request, zipfile

src = sys.argv[1] if len(sys.argv) > 1 else "cities5000"
if os.path.isfile(src):
    text = open(src, encoding="utf-8").read()
else:
    url = f"https://download.geonames.org/export/dump/{src}.zip"
    print("Mengunduh", url)
    z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=300).read()))
    text = z.read(f"{src}.txt").decode("utf-8")

rows = []
for r in csv.reader(io.StringIO(text), delimiter="\t", quoting=csv.QUOTE_NONE):
    if len(r) < 18 or not r[17]:
        continue
    # kolom GeoNames: 0 id, 1 nama, 2 ascii, 4 lat, 5 lon, 8 negara, 14 penduduk, 16 elevasi (DEM), 17 zona waktu
    rows.append((int(r[0]), r[1], r[2], r[8], round(float(r[4]), 3), round(float(r[5]), 3), int(r[14] or 0), int(r[16] or 0), r[17]))
rows.sort(key=lambda x: -x[6])  # terbesar dulu; peta memakai urutan ini

tz = sorted({r[8] for r in rows})
ti = {t: i for i, t in enumerate(tz)}
out = {"tz": tz, "c": [[r[0], r[1], r[3], r[4], r[5], r[6], ti[r[8]], r[7]] + ([r[2]] if r[2] != r[1] else []) for r in rows]}
os.makedirs("public/data", exist_ok=True)
with open("public/data/cities.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print(f"Selesai: {len(rows)} kota, {os.path.getsize('public/data/cities.json') // 1024} KB")
