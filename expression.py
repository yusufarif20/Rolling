# Daftar ekspresi dan kategorinya
positive_emotions = ["senang", "bahagia", "gembira", "tersenyum"]
neutral_emotions = ["biasa saja", "netral", "diam"]
negative_emotions = ["sedih", "marah", "takut", "kesal", "cemberut"]

def klasifikasi_emosi(ekspresi):
    ekspresi = ekspresi.lower()

    if ekspresi in positive_emotions:
        return "Positif"
    elif ekspresi in neutral_emotions:
        return "Netral"
    elif ekspresi in negative_emotions:
        return "Negatif"
    else:
        return "Tidak dikenali"

# Program utama
while True:
    ekspresi = input("Masukkan ekspresi wajah (contoh: senang, sedih, netral): ")

    if ekspresi.lower() == "keluar":
        print("Program dihentikan.")
        break

    kelas = klasifikasi_emosi(ekspresi)
    print(f"Ekspresi '{ekspresi}' diklasifikasikan sebagai emosi: {kelas}\n")
