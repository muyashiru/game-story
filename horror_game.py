#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Game Story Horor - Text-Based Adventure
Pilihan Anda menentukan nasib karakter dalam petualangan horor ini
"""

import time
import sys

def cetak_lambat(teks, delay=0.03):
    """Mencetak teks dengan efek ketikan"""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cetak_judul():
    """Menampilkan judul game"""
    print("\n" + "="*60)
    print("          MALAM DI HUTAN KELAM          ")
    print("       Text-Based Horror Adventure       ")
    print("="*60 + "\n")
    time.sleep(1)

def pilih(pilihan_list):
    """Menampilkan pilihan dan mengembalikan input pemain"""
    print("\nPilihan Anda:")
    for i, pilihan in enumerate(pilihan_list, 1):
        print(f"{i}. {pilihan}")
    
    while True:
        try:
            pilihan = int(input("\nMasukkan nomor pilihan (1-{}): ".format(len(pilihan_list))))
            if 1 <= pilihan <= len(pilihan_list):
                return pilihan
            else:
                print(f"Pilih nomor antara 1 dan {len(pilihan_list)}!")
        except ValueError:
            print("Masukkan nomor yang valid!")

def ending_selamat():
    """Ending 1 - Berhasil selamat"""
    cetak_lambat("\n🌅 === ENDING: SELAMAT ===")
    cetak_lambat("\nAnda berhasil melarikan diri dari hutan mengerikan itu.")
    cetak_lambat("Saat fajar menyingsing, Anda menemukan jalan raya dan mendapat pertolongan.")
    cetak_lambat("Pengalaman malam itu akan terus menghantui mimpi-mimpi Anda...")
    cetak_lambat("\nTERIMA KASIH TELAH BERMAIN!")
    print("\n" + "="*60 + "\n")

def ending_terjebak():
    """Ending 2 - Terjebak selamanya"""
    cetak_lambat("\n👻 === ENDING: TERJEBAK ===")
    cetak_lambat("\nAnda tidak pernah keluar dari rumah itu.")
    cetak_lambat("Suara Anda bergabung dengan bisikan-bisikan di dalam dinding...")
    cetak_lambat("Korban berikutnya akan mendengar namamu dipanggil dalam kegelapan.")
    cetak_lambat("\nGAME OVER")
    print("\n" + "="*60 + "\n")

def ending_mengerikan():
    """Ending 3 - Nasib mengerikan"""
    cetak_lambat("\n💀 === ENDING: KUTUKAN ===")
    cetak_lambat("\nAnda tidak seharusnya membuka pintu itu...")
    cetak_lambat("Sesuatu yang seharusnya tetap terkurung kini bebas.")
    cetak_lambat("Dan Anda menjadi bagian dari kutukannya untuk selamanya.")
    cetak_lambat("\nGAME OVER")
    print("\n" + "="*60 + "\n")

def ending_pengecut():
    """Ending 4 - Tetap di mobil"""
    cetak_lambat("\n🚗 === ENDING: PENANTIAN ===")
    cetak_lambat("\nAnda memilih tetap di dalam mobil dan menunggu hingga pagi.")
    cetak_lambat("Suara-suara mengerikan mengelilingi mobil sepanjang malam...")
    cetak_lambat("Saat matahari terbit, sebuah truk lewat dan membantu Anda.")
    cetak_lambat("Anda selamat, tapi tidak akan pernah lupa malam yang mengerikan itu.")
    cetak_lambat("\nTERIMA KASIH TELAH BERMAIN!")
    print("\n" + "="*60 + "\n")

def scene_basement():
    """Scene di basement"""
    cetak_lambat("\n--- RUANG BAWAH TANAH ---")
    cetak_lambat("\nAnda turun tangga yang berderit ke basement yang gelap.")
    cetak_lambat("Udara terasa lembab dan berbau busuk.")
    cetak_lambat("Di pojok ruangan, Anda melihat sebuah pintu logam dengan rantai berkarat.")
    cetak_lambat("Ada suara menggaruk dari balik pintu itu...")
    
    pilihan = pilih([
        "Buka pintu yang dirantai",
        "Cari jalan keluar lain",
        "Kembali ke atas"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda melepas rantai dengan susah payah...")
        cetak_lambat("Pintu terbuka perlahan...")
        time.sleep(2)
        cetak_lambat("KESALAHAN FATAL!")
        ending_mengerikan()
        return False
    elif pilihan == 2:
        cetak_lambat("\nAnda menemukan jendela kecil yang menuju ke belakang rumah!")
        cetak_lambat("Anda berhasil keluar dan lari menuju hutan...")
        return scene_hutan_escape()
    else:
        cetak_lambat("\nAnda berbalik dan naik tangga dengan cepat...")
        return scene_lantai_atas()

def scene_hutan_escape():
    """Scene melarikan diri ke hutan"""
    cetak_lambat("\n--- MELARIKAN DIRI ---")
    cetak_lambat("\nAnda berlari kencang di antara pepohonan gelap.")
    cetak_lambat("Di kejauhan Anda melihat cahaya...")
    cetak_lambat("Sesuatu mengejar Anda dari belakang!")
    
    pilihan = pilih([
        "Lari ke arah cahaya",
        "Bersembunyi di balik pohon besar",
        "Panjat pohon"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda berlari sekuat tenaga ke arah cahaya...")
        cetak_lambat("Itu adalah lentera seorang ranger hutan!")
        ending_selamat()
        return False
    elif pilihan == 2:
        cetak_lambat("\nAnda bersembunyi, tapi makhluk itu mencium bau Anda...")
        cetak_lambat("Ini adalah akhir dari petualangan Anda...")
        ending_mengerikan()
        return False
    else:
        cetak_lambat("\nAnda memanjat, tapi cabang patah...")
        cetak_lambat("Jatuh yang menyakitkan... dan sesuatu menunggu di bawah...")
        ending_mengerikan()
        return False

def scene_lantai_atas():
    """Scene di lantai atas"""
    cetak_lambat("\n--- LANTAI ATAS ---")
    cetak_lambat("\nAnda naik tangga menuju lantai atas.")
    cetak_lambat("Ada tiga pintu kamar yang terbuka sedikit.")
    cetak_lambat("Dari salah satu kamar terdengar lagu pengantar tidur...")
    
    pilihan = pilih([
        "Masuk ke kamar dengan lagu pengantar tidur",
        "Cari jendela untuk keluar",
        "Kembali ke lantai bawah"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda membuka pintu kamar...")
        cetak_lambat("Sebuah kotak musik tua berputar sendiri...")
        cetak_lambat("Mendadak pintu tertutup dan terkunci!")
        ending_terjebak()
        return False
    elif pilihan == 2:
        cetak_lambat("\nAnda menemukan jendela di ujung koridor!")
        cetak_lambat("Jendela itu menuju atap anjungan yang bisa Anda turun.")
        cetak_lambat("Anda berhasil keluar dan lari ke dalam hutan...")
        return scene_hutan_escape()
    else:
        cetak_lambat("\nAnda turun kembali ke lantai bawah...")
        return scene_dalam_rumah()

def scene_dalam_rumah():
    """Scene pertama di dalam rumah"""
    cetak_lambat("\n--- DI DALAM RUMAH TUA ---")
    cetak_lambat("\nAnda masuk ke dalam rumah tua yang gelap.")
    cetak_lambat("Udara berbau apek dan Anda mendengar suara langkah kaki di lantai atas.")
    cetak_lambat("Ada tangga menuju lantai atas, pintu menuju dapur, dan tangga menuju basement.")
    
    pilihan = pilih([
        "Naik ke lantai atas",
        "Pergi ke dapur",
        "Turun ke basement"
    ])
    
    if pilihan == 1:
        return scene_lantai_atas()
    elif pilihan == 2:
        cetak_lambat("\nAnda berjalan ke dapur yang kotor.")
        cetak_lambat("Ada pintu belakang yang terbuka sedikit!")
        cetak_lambat("Anda mendengar suara mendekati...")
        
        sub_pilihan = pilih([
            "Keluar melalui pintu belakang",
            "Bersembunyi di lemari"
        ])
        
        if sub_pilihan == 1:
            cetak_lambat("\nAnda berlari keluar dan masuk ke dalam hutan...")
            return scene_hutan_escape()
        else:
            cetak_lambat("\nAnda bersembunyi di lemari...")
            cetak_lambat("Sesuatu membuka lemari itu...")
            ending_mengerikan()
            return False
    else:
        return scene_basement()

def scene_perbaiki_mobil():
    """Scene mencoba memperbaiki mobil"""
    cetak_lambat("\n--- MEMPERBAIKI MOBIL ---")
    cetak_lambat("\nAnda keluar dan membuka kap mesin.")
    cetak_lambat("Anda memeriksa mesin dengan senter ponsel...")
    cetak_lambat("Sepertinya ada masalah dengan aki.")
    cetak_lambat("\nTiba-tiba Anda mendengar suara ranting patah di belakang Anda...")
    
    pilihan = pilih([
        "Terus berusaha memperbaiki mobil",
        "Cepat masuk kembali ke mobil",
        "Berteriak meminta pertolongan"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda fokus pada mesin dan berhasil menghidupkannya!")
        cetak_lambat("Anda melompat ke dalam mobil dan melaju pergi...")
        cetak_lambat("Sesuatu mengejar Anda tapi mobil lebih cepat!")
        ending_selamat()
        return False
    elif pilihan == 2:
        cetak_lambat("\nAnda masuk ke mobil dan mengunci semua pintu.")
        cetak_lambat("Sesuatu mengintip dari jendela...")
        cetak_lambat("Anda tetap diam dan berharap itu akan pergi...")
        ending_pengecut()
        return False
    else:
        cetak_lambat("\nTeriakanmu bergema di hutan...")
        cetak_lambat("Tapi hanya mengundang perhatian yang tidak diinginkan...")
        ending_mengerikan()
        return False

def scene_tetap_di_mobil():
    """Scene tetap di dalam mobil"""
    cetak_lambat("\n--- TETAP DI MOBIL ---")
    cetak_lambat("\nAnda memutuskan untuk tetap di dalam mobil.")
    cetak_lambat("Anda mengunci semua pintu dan mematikan lampu.")
    cetak_lambat("Waktu berlalu sangat lambat...")
    cetak_lambat("\nSetelah beberapa jam, Anda mendengar suara aneh di sekitar mobil...")
    
    pilihan = pilih([
        "Tetap diam dan tunggu sampai pagi",
        "Coba hidupkan mesin lagi",
        "Keluar dan lari ke rumah tua"
    ])
    
    if pilihan == 1:
        ending_pengecut()
        return False
    elif pilihan == 2:
        cetak_lambat("\nAnda memutar kunci... Mesin menderu!")
        cetak_lambat("Keberuntungan berpihak pada Anda!")
        ending_selamat()
        return False
    else:
        cetak_lambat("\nDalam kepanikan, Anda keluar dan berlari ke rumah tua...")
        return scene_dalam_rumah()

def scene_awal():
    """Scene pembuka game"""
    cetak_lambat("\n--- PROLOG ---")
    cetak_lambat("\nMalam sudah larut. Anda menyetir sendirian melewati hutan yang gelap.")
    cetak_lambat("Tiba-tiba, mobil Anda batuk-batuk dan mati.")
    cetak_lambat("Anda berada di tengah hutan yang sunyi...")
    cetak_lambat("\nDi kejauhan, Anda melihat siluet sebuah rumah tua yang menyeramkan.")
    cetak_lambat("Tidak ada sinyal ponsel di sini.")
    
    time.sleep(2)
    
    cetak_lambat("\nApa yang akan Anda lakukan?")
    
    pilihan = pilih([
        "Keluar dan memperbaiki mobil",
        "Tetap di dalam mobil dan menunggu hingga pagi",
        "Pergi ke rumah tua dan mencari bantuan"
    ])
    
    if pilihan == 1:
        return scene_perbaiki_mobil()
    elif pilihan == 2:
        return scene_tetap_di_mobil()
    else:
        return scene_dalam_rumah()

def main():
    """Fungsi utama game"""
    cetak_judul()
    
    cetak_lambat("Selamat datang di game horor interaktif!")
    cetak_lambat("Setiap pilihan Anda akan menentukan nasib karakter...")
    cetak_lambat("Ada beberapa ending yang berbeda tergantung pilihan Anda.")
    
    input("\nTekan ENTER untuk memulai... ")
    
    # Mulai game
    scene_awal()
    
    # Tanya main lagi
    main_lagi = input("\nApakah Anda ingin bermain lagi? (y/n): ")
    if main_lagi.lower() == 'y':
        print("\n" * 3)
        main()
    else:
        cetak_lambat("\nTerima kasih telah bermain! Sampai jumpa...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame dihentikan. Terima kasih sudah bermain!")
        sys.exit(0)
