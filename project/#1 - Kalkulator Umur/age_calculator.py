from datetime import datetime

tanggal_lahir = input ("Masukkan tanggal lahir anda (format: YYYY-MM-DD): ")
tgl_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
hari_ini = datetime.now()
umur = hari_ini - tgl_lahir

year_age = umur.days // 365
sisa_hari = umur.days % 365
umur_bulan = sisa_hari // 30
umur_hari = sisa_hari % 30  

print(f"\nUmur kamu sekarang : {year_age} tahun, {umur_bulan} bulan, {umur_hari} hari")
print(f"Kamu sudah hidup selama {umur.days} hari")