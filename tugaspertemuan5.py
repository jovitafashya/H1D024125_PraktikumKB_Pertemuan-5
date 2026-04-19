# Nama : Jovita Fashya Islami
# Nim : H1D024125
# Shift Lama : G
# Shift Baru : F

GEJALA = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}

KNOWLEDGE_BASE = {
    "Tonsilitis": {"G37","G12","G5","G27","G6","G21"},
    "Sinusitis Maksilaris": {"G37","G12","G27","G17","G33","G36","G29"},
    "Sinusitis Frontalis": {"G37","G12","G27","G17","G33","G36","G21","G26"},
    "Sinusitis Edmoidalis": {"G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"},
    "Sinusitis Sfenoidalis": {"G37","G12","G27","G17","G33","G36","G29","G7"},
    "Abses Peritonsiler": {"G37","G12","G6","G15","G2","G29","G10"},
    "Faringitis": {"G37","G5","G6","G7","G15"},
    "Kanker Laring": {"G5","G27","G6","G15","G2","G19","G1"},
    "Deviasi Septum": {"G37","G17","G20","G8","G18","G25"},
    "Laringitis": {"G37","G5","G15","G16","G32"},
    "Kanker Leher & Kepala": {"G5","G22","G8","G28","G3","G11"},
    "Otitis Media Akut": {"G37","G20","G35","G31"},
    "Contact Ulcers": {"G5","G2"},
    "Abses Parafaringeal": {"G5","G16"},
    "Barotitis Media": {"G12","G20"},
    "Kanker Nasofaring": {"G17","G8"},
    "Kanker Tonsil": {"G6","G29"},
    "Neuronitis Vestibularis": {"G35","G24"},
    "Meniere": {"G20","G35","G14","G4"},
    "Tumor Syaraf Pendengaran": {"G12","G34","G23"},
    "Kanker Leher Metastatik": {"G29"},
    "Osteosklerosis": {"G34","G9"},
    "Vertigo Postural": {"G24"}
}

SEPARATOR = "=" * 60
THIN = "-" * 60

def header():
    print(SEPARATOR)
    print("   SISTEM PAKAR DIAGNOSA PENYAKIT THT")
    print("   Metode: Forward Chaining")
    print(SEPARATOR)

def menu():
    print("\nDAFTAR GEJALA:")
    print(THIN)
    for k, v in GEJALA.items():
        print(f"[{k}] {v}")
    print(THIN)

def input_gejala():
    data = input("\nMasukkan kode gejala (pisahkan koma): ").upper()
    return set(data.replace(" ", "").split(","))

def inferensi(user):
    hasil = []
    for penyakit, gejala in KNOWLEDGE_BASE.items():
        cocok = user & gejala
        if cocok:
            skor = len(cocok) / len(gejala) * 100
            hasil.append((penyakit, skor))
    return sorted(hasil, key=lambda x: x[1], reverse=True)

def level(s):
    if s >= 75:
        return "SANGAT TINGGI"
    elif s >= 50:
        return "TINGGI"
    elif s >= 25:
        return "SEDANG"
    else:
        return "RENDAH"

def hasil_out(h):
    print("\nHasil Diagnosa:")
    if not h:
        print("Tidak ditemukan penyakit.")
        return
    for i, (p, s) in enumerate(h, 1):
        print(f"{i}. {p} ({s:.1f}%) {level(s)}")  

def main():
    while True:
        header()
        menu()
        g = input_gejala()
        h = inferensi(g)
        hasil_out(h)
        if input("\nUlangi? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()


