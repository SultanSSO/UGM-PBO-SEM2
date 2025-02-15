niu = int(input("Masukkan NIU (6 digit): "))

# Meminta input nilai tugas dan laporan
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_laporan = float(input("Masukkan nilai laporan: "))

# Menghitung rata-rata nilai tugas dan laporan
rata_rata = (nilai_tugas + nilai_laporan) / 2

# Jika rata-rata kurang dari 40, siswa mendapat nilai K dan program berhenti
if rata_rata < 40:
    print(f"NIU: {niu}")
    print("Nilai Huruf: K")
else:
    # Meminta input nilai ujian
    nilai_ujian = float(input("Masukkan nilai ujian: "))
    
    # Menghitung nilai akhir dengan bobot: tugas 25%, laporan 25%, ujian 50%
    nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.50)
    
    # Menentukan nilai huruf berdasarkan nilai akhir
    if 80 <= nilai_akhir <= 100:
        nilai_huruf = "A"
    elif 70 <= nilai_akhir < 80:
        nilai_huruf = "B"
    elif 60 <= nilai_akhir < 70:
        nilai_huruf = "C"
    elif 50 <= nilai_akhir < 60:
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"
    
    # Menampilkan hasil
    print(f"NIU: {niu}")
    print(f"Nilai Akhir: {nilai_akhir:.2f}")
    print(f"Nilai Huruf: {nilai_huruf}")
