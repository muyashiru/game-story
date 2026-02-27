#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ASYLUM NIGHTMARE - Advanced Horror Text Adventure
Game horor kompleks dengan multiple paths, inventory system, dan sanity meter
"""

import time
import sys
import random
import webbrowser

AUTO_BUKA_GAMBAR = False
GAMBAR_SUDAH_DIBUKA = set()

UNSPLASH_SCENES = {
    "judul": "https://source.unsplash.com/1600x900/?horror,asylum,dark",
    "gedung": "https://source.unsplash.com/1600x900/?abandoned,hospital,night",
    "pintu": "https://source.unsplash.com/1600x900/?old,door,creepy",
    "koridor": "https://source.unsplash.com/1600x900/?dark,hallway,hospital",
    "monster": "https://source.unsplash.com/1600x900/?horror,shadow,creature",
    "skull": "https://source.unsplash.com/1600x900/?skull,dark,macabre",
    "escape": "https://source.unsplash.com/1600x900/?escape,night,forest",
    "ritual": "https://source.unsplash.com/1600x900/?ritual,candle,occult",
    "laboratorium": "https://source.unsplash.com/1600x900/?laboratory,abandoned,medical",
    "perpustakaan": "https://source.unsplash.com/1600x900/?old,library,dark",
    "kamar_mayat": "https://source.unsplash.com/1600x900/?morgue,hospital,cold",
    "ruang_rawat": "https://source.unsplash.com/1600x900/?hospital,ward,abandoned",
    "tangga_basement": "https://source.unsplash.com/1600x900/?basement,stairs,dark",
    "lobby": "https://source.unsplash.com/1600x900/?abandoned,lobby,building",
    "keamanan": "https://source.unsplash.com/1600x900/?security,monitor,room",
    "kantor": "https://source.unsplash.com/1600x900/?old,office,documents",
}

class Player:
    """Class untuk menyimpan status pemain"""
    def __init__(self):
        self.sanity = 100  # Kewarasan pemain
        self.inventory = []
        self.lokasi = "entrance"
        self.kunci_terkumpul = 0
        self.sudah_bertemu_monster = False
        self.tahu_rahasia = False
        self.memiliki_senjata = False
        
    def tambah_item(self, item):
        self.inventory.append(item)
        
    def hapus_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            
    def kurang_sanity(self, jumlah):
        self.sanity -= jumlah
        if self.sanity < 0:
            self.sanity = 0
            
    def cek_item(self, item):
        return item in self.inventory

player = Player()

def cetak_lambat(teks, delay=0.03):
    """Mencetak teks dengan efek ketikan"""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cetak_cepat(teks):
    """Cetak tanpa delay"""
    print(teks)

def cetak_merah(teks):
    """Cetak teks penting/bahaya"""
    cetak_lambat(f"\n⚠️  {teks}  ⚠️")

def tampilkan_status():
    """Menampilkan status pemain"""
    print("\n" + "="*50)
    print(f"🧠 Sanity: {player.sanity}% | 🎒 Item: {len(player.inventory)}/5")
    if player.inventory:
        print(f"📦 Inventory: {', '.join(player.inventory)}")
    print("="*50)

def tampilkan_gambar_unsplash(scene_key, judul_scene):
    """Menampilkan link gambar Unsplash untuk scene tertentu."""
    url = UNSPLASH_SCENES.get(scene_key, "https://source.unsplash.com/1600x900/?horror,dark")
    print("\n" + "=" * 70)
    print(f"🖼️  {judul_scene}")
    print(f"🔗 Unsplash: {url}")
    print("=" * 70)

    if AUTO_BUKA_GAMBAR and scene_key not in GAMBAR_SUDAH_DIBUKA:
        try:
            webbrowser.open(url, new=2)
            GAMBAR_SUDAH_DIBUKA.add(scene_key)
        except Exception:
            print("⚠️  Gagal membuka browser otomatis. Buka link secara manual.")

def tampilkan_ascii_judul():
    """Gambar judul game"""
    tampilkan_gambar_unsplash("judul", "THE BLACKWOOD PSYCHIATRIC HOSPITAL")
    time.sleep(1)

def tampilkan_ascii_gedung():
    """Gambar gedung rumah sakit"""
    tampilkan_gambar_unsplash("gedung", "BLACKWOOD ASYLUM - Abandoned Since 1963")
    time.sleep(1)

def tampilkan_ascii_pintu():
    """Gambar pintu masuk"""
    tampilkan_gambar_unsplash("pintu", "Pintu Masuk - Restricted Area")

def tampilkan_ascii_koridor():
    """Gambar koridor gelap"""
    tampilkan_gambar_unsplash("koridor", "Koridor Gelap - Lampu berkedip...")

def tampilkan_ascii_monster():
    """Gambar monster"""
    tampilkan_gambar_unsplash("monster", "SOMETHING IS WATCHING...")

def tampilkan_ascii_skull():
    """Gambar tengkorak untuk ending buruk"""
    tampilkan_gambar_unsplash("skull", "GAME OVER")

def tampilkan_ascii_escape():
    """Gambar pelarian"""
    tampilkan_gambar_unsplash("escape", "FREEDOM - EXIT")

def tampilkan_ascii_ritual():
    """Gambar ruang ritual"""
    tampilkan_gambar_unsplash("ritual", "Ruang Ritual - Dark energy emanates...")

def tampilkan_ascii_laboratorium():
    """Gambar laboratorium"""
    tampilkan_gambar_unsplash("laboratorium", "Laboratorium Eksperimen")

def tampilkan_ascii_perpustakaan():
    """Gambar perpustakaan"""
    tampilkan_gambar_unsplash("perpustakaan", "Perpustakaan Tua")

def tampilkan_ascii_kamar_mayat():
    """Gambar kamar mayat"""
    tampilkan_gambar_unsplash("kamar_mayat", "Kamar Mayat")

def tampilkan_ascii_ruang_rawat():
    """Gambar ruang rawat inap"""
    tampilkan_gambar_unsplash("ruang_rawat", "Ruang Rawat Inap")

def tampilkan_ascii_tangga_basement():
    """Gambar tangga ke basement"""
    tampilkan_gambar_unsplash("tangga_basement", "Tangga ke Basement")

def tampilkan_ascii_lobby():
    """Gambar lobby"""
    tampilkan_gambar_unsplash("lobby", "Lobby Lantai 1")

def tampilkan_ascii_keamanan():
    """Gambar ruang keamanan"""
    tampilkan_gambar_unsplash("keamanan", "Ruang Keamanan")

def tampilkan_ascii_kantor():
    """Gambar kantor administratif"""
    tampilkan_gambar_unsplash("kantor", "Kantor Administratif")

def cetak_judul():
    """Menampilkan judul game"""
    tampilkan_ascii_judul()
    time.sleep(1)

def pilih(pilihan_list, tampilkan_inventory=True):
    """Menampilkan pilihan dan mengembalikan input pemain"""
    if tampilkan_inventory and player.inventory:
        print(f"\n💼 Item yang Anda bawa: {', '.join(player.inventory)}")
    
    print("\n🔍 Pilihan Anda:")
    for i, pilihan in enumerate(pilihan_list, 1):
        print(f"  {i}. {pilihan}")
    
    while True:
        try:
            pilihan = int(input(f"\n➤ Pilih (1-{len(pilihan_list)}): "))
            if 1 <= pilihan <= len(pilihan_list):
                return pilihan
            else:
                print(f"❌ Pilih nomor antara 1 dan {len(pilihan_list)}!")
        except ValueError:
            print("❌ Masukkan nomor yang valid!")
        except KeyboardInterrupt:
            print("\n\n👋 Game dihentikan.")
            sys.exit(0)

# ==================== ENDINGS ====================

def ending_gila():
    """Ending - Kehilangan kewarasan"""
    tampilkan_ascii_skull()
    cetak_lambat("\n" + "="*70)
    cetak_lambat("🌀🌀🌀 ENDING: KEGILAAN 🌀🌀🌀")
    cetak_lambat("="*70)
    cetak_lambat("\nKewarasan Anda telah hilang sepenuhnya...")
    cetak_lambat("Anda mendengar suara-suara yang tidak ada...")
    cetak_lambat("Anda melihat bayangan-bayangan yang mengelilingi Anda...")
    time.sleep(1)
    cetak_lambat("\nStaf rumah sakit menemukan Anda berhari-hari kemudian,")
    cetak_lambat("tertawa terbahak-bahak di sudut ruangan yang gelap...")
    cetak_lambat("Kini Anda adalah pasien permanen di Blackwood Asylum.")
    cetak_lambat("\n💀 GAME OVER - Sanity: 0% 💀")
    cetak_lambat("="*70 + "\n")
    return False

def ending_terkutuk():
    """Ending - Terkutuk selamanya"""
    tampilkan_ascii_skull()
    cetak_lambat("\n" + "="*70)
    cetak_lambat("👻👻👻 ENDING: TERKUTUK 👻👻👻")
    cetak_lambat("="*70)
    cetak_lambat("\nAnda telah membangkitkan sesuatu yang seharusnya tetap tertidur...")
    cetak_lambat("Kutukan Dr. Blackwood kini melekat pada jiwa Anda.")
    time.sleep(1)
    cetak_lambat("\nAnda tidak pernah bisa meninggalkan rumah sakit ini.")
    cetak_lambat("Roh Anda bergabung dengan pasien-pasien lain yang terjebak...")
    cetak_lambat("Selamanya menghantui lorong-lorong gelap Blackwood Asylum.")
    cetak_lambat("\n💀 GAME OVER - Terkutuk Selamanya 💀")
    cetak_lambat("="*70 + "\n")
    return False

def ending_dimakan():
    """Ending - Dimakan oleh monster"""
    tampilkan_ascii_monster()
    cetak_lambat("\n" + "="*70)
    cetak_lambat("🩸🩸🩸 ENDING: MANGSA 🩸🩸🩸")
    cetak_lambat("="*70)
    cetak_lambat("\nKreatur itu terlalu cepat...")
    cetak_lambat("Terlalu kuat...")
    cetak_lambat("Terlalu lapar...")
    time.sleep(1)
    cetak_lambat("\nAnda menjadi salah satu dari ratusan korban")
    cetak_lambat("yang hilang di dalam Blackwood Asylum.")
    cetak_lambat("Tidak ada yang akan menemukan Anda.")
    cetak_lambat("\n💀 GAME OVER - Habis Dimakan 💀")
    cetak_lambat("="*70 + "\n")
    return False

def ending_selamat_biasa():
    """Ending - Selamat tapi trauma"""
    tampilkan_ascii_escape()
    cetak_lambat("\n" + "="*70)
    cetak_lambat("🏃🏃🏃 ENDING: PELARIAN 🏃🏃🏃")
    cetak_lambat("="*70)
    cetak_lambat("\nAnda berhasil keluar dari Blackwood Asylum hidup-hidup...")
    cetak_lambat("Tetapi pengalaman malam itu...")
    cetak_lambat("Akan menghantui Anda selamanya.")
    time.sleep(1)
    cetak_lambat("\nAnda tidak tidur nyenyak selama berbulan-bulan.")
    cetak_lambat("Setiap kegelapan mengingatkan Anda pada lorong-lorong itu.")
    cetak_lambat("Anda selamat... tapi dengan harga yang mahal.")
    cetak_lambat("\n✅ SELAMAT - Tapi Berbekas 🧠: {}/100".format(player.sanity))
    cetak_lambat("="*70 + "\n")
    return False

def ending_selamat_pahlawan():
    """Ending terbaik - Selamat dan mengakhiri kutukan"""
    tampilkan_ascii_escape()
    cetak_cepat("""
           ⭐        ⭐        ⭐
              YOU DID IT!
           ⭐        ⭐        ⭐
    """)
    cetak_lambat("\n" + "="*70)
    cetak_lambat("⭐⭐⭐ ENDING: SANG PEMBEBAS ⭐⭐⭐")
    cetak_lambat("="*70)
    cetak_lambat("\nAnda tidak hanya berhasil keluar hidup-hidup...")
    cetak_lambat("Tetapi juga mengakhiri kutukan yang mengikat Blackwood Asylum!")
    time.sleep(1)
    cetak_lambat("\nDengan memusnahkan sumber kutukan Dr. Blackwood,")
    cetak_lambat("Anda membebaskan ratusan jiwa yang tertahan di sini.")
    cetak_lambat("Roh-roh itu akhirnya bisa beristirahat dengan tenang.")
    time.sleep(1)
    cetak_lambat("\nAnda keluar sebagai pahlawan yang tidak dikenal...")
    cetak_lambat("Membawa rahasia yang tidak akan pernah Anda ceritakan.")
    cetak_lambat("Tapi Anda tahu... Anda telah melakukan hal yang benar.")
    cetak_lambat("\n🏆 ENDING TERBAIK - The True Hero 🏆")
    cetak_lambat(f"🧠 Sanity Tersisa: {player.sanity}%")
    cetak_lambat("="*70 + "\n")
    return False

def ending_jadi_monster():
    """Ending terburuk - Berubah jadi monster"""
    tampilkan_ascii_monster()
    cetak_lambat("\n" + "="*70)
    cetak_lambat("🐺🐺🐺 ENDING: TRANSFORMASI 🐺🐺🐺")
    cetak_lambat("="*70)
    cetak_lambat("\nAnda merasakan perubahan di dalam diri Anda...")
    cetak_lambat("Kutukan Dr. Blackwood telah menginfeksi jiwa Anda.")
    time.sleep(2)
    cetak_lambat("\nSecara perlahan, kemanusiaan Anda memudar...")
    cetak_lambat("Anda merasakan keinginan yang tidak wajar...")
    cetak_lambat("Rasa lapar yang aneh...")
    time.sleep(2)
    cetak_lambat("\nKini ANDA adalah monster yang menghantui Blackwood Asylum.")
    cetak_lambat("Menunggu korban berikutnya yang cukup bodoh untuk masuk...")
    cetak_lambat("\n💀 ENDING TERBURUK - You Are The Monster 💀")
    cetak_lambat("="*70 + "\n")
    return False

def ending_terjebak_loop():
    """Ending - Terjebak dalam time loop"""
    tampilkan_ascii_skull()
    cetak_lambat("\n" + "="*70)
    cetak_lambat("🔄🔄🔄 ENDING: INFINITE LOOP 🔄🔄🔄")
    cetak_lambat("="*70)
    cetak_lambat("\nAnda membuka mata...")
    cetak_lambat("Anda berdiri di depan gerbang Blackwood Asylum.")
    cetak_lambat("Seperti pertama kali Anda datang ke sini...")
    time.sleep(2)
    cetak_lambat("\nAnda mencoba mengingat... tapi semuanya kabur.")
    cetak_lambat("Anda merasa ini pernah terjadi sebelumnya...")
    cetak_lambat("Berulang kali...")
    cetak_lambat("Beratus-ratus kali...")
    time.sleep(2)
    cetak_lambat("\nAnda terjebak dalam lingkaran waktu yang tidak berujung.")
    cetak_lambat("Menjalani malam yang sama, berulang-ulang, untuk selamanya...")
    cetak_lambat("\n💀 GAME OVER - Eternal Damnation 💀")
    cetak_lambat("="*70 + "\n")
    return False

# ==================== SCENES ====================

def scene_ritual_room_final():
    """Scene final ritual room - kunci untuk ending terbaik"""
    tampilkan_ascii_ritual()
    cetak_lambat("\n━━━ RUANG RITUAL - THE HEART OF DARKNESS ━━━")
    cetak_lambat("\nAnda memasuki ruangan bundar besar dengan simbol-simbol aneh di dinding.")
    cetak_lambat("Di tengah ruangan ada altar dengan tengkorak manusia dan lilin-lilin hitam.")
    cetak_lambat("Anda merasakan energi gelap yang kuat di sini...")
    player.kurang_sanity(15)
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nInilah sumber kutukan Dr. Blackwood!")
    
    if player.cek_item("korek api") and player.cek_item("buku ritual"):
        cetak_lambat("\nAnda ingat ritual yang Anda baca di buku...")
        cetak_lambat("Untuk mengakhiri kutukan, Anda harus membakar altar ini!")
        
        pilihan = pilih([
            "Bakar altar dengan korek api dan baca counter-spell dari buku",
            "Hancurkan altar dengan tangan kosong",
            "Tinggalkan ruangan ini dan cari jalan keluar"
        ])
        
        if pilihan == 1:
            cetak_lambat("\nAnda menyalakan api dan mulai membaca mantra dari buku...")
            cetak_lambat("Api menjalar dengan cepat, membakar altar!")
            time.sleep(2)
            cetak_lambat("\nSuara teriakan memekakkan telinga terdengar!")
            cetak_lambat("Gedung mulai bergetar!")
            cetak_lambat("ANDA HARUS KELUAR SEKARANG!")
            time.sleep(1)
            
            if player.cek_item("peta rumah sakit"):
                cetak_lambat("\nAnda menggunakan peta untuk menemukan jalan keluar tercepat!")
                cetak_lambat("Anda berlari melewati lorong yang runtuh...")
                cetak_lambat("Cahaya pintu keluar terlihat!")
                cetak_lambat("ANDA BERHASIL KELUAR!")
                return ending_selamat_pahlawan()
            else:
                cetak_lambat("\nAnda berlari tanpa arah!")
                cetak_lambat("Langit-langit mulai runtuh...")
                cetak_lambat("Anda berlari sekuat tenaga...")
                
                if player.sanity >= 40:
                    cetak_lambat("Pikiran Anda cukup jernih untuk menemukan jalan keluar!")
                    return ending_selamat_pahlawan()
                else:
                    cetak_lambat("Kebingungan membuat Anda salah belok...")
                    cetak_lambat("Reruntuhan menimpa Anda...")
                    return ending_terkutuk()
        
        elif pilihan == 2:
            cetak_lambat("\nAnda mencoba menghancurkan altar!")
            cetak_lambat("Tapi saat Anda menyentuhnya...")
            cetak_lambat("ENERGI GELAP MENYERAP KE DALAM TUBUH ANDA!")
            return ending_jadi_monster()
        
        else:
            cetak_lambat("\nAnda meninggalkan ruangan...")
            cetak_lambat("Tapi kutukan masih aktif...")
            return scene_escape_final()
    
    else:
        cetak_lambat("\nAnda tidak memiliki alat yang tepat untuk menghancurkan kutukan ini.")
        
        pilihan = pilih([
            "Coba hancurkan altar dengan tangan kosong",
            "Cari jalan keluar dari gedung ini"
        ])
        
        if pilihan == 1:
            cetak_lambat("\nAnda menyentuh altar...")
            cetak_lambat("KESALAHAN FATAL!")
            return ending_jadi_monster()
        else:
            return scene_escape_final()

def scene_escape_final():
    """Scene pelarian akhir"""
    tampilkan_ascii_koridor()
    cetak_lambat("\n━━━ PELARIAN TERAKHIR ━━━")
    cetak_lambat("\nAnda harus keluar dari gedung ini SEKARANG!")
    cetak_lambat("Anda mendengar suara mengerikan semakin mendekat...")
    
    if player.cek_item("peta rumah sakit"):
        cetak_lambat("\nAnda membuka peta dan menemukan jalan keluar terdekat!")
        
        pilihan = pilih([
            "Lari ke pintu darurat di lantai 1",
            "Pecahkan jendela dan lompat",
            "Sembunyi dan tunggu sampai aman"
        ])
        
        if pilihan == 1:
            cetak_lambat("\nAnda berlari ke pintu darurat!")
            cetak_lambat("Pintu terbuka! Udara segar!")
            return ending_selamat_biasa()
        elif pilihan == 2:
            cetak_lambat("\nAnda memecahkan jendela dan melompat!")
            if player.sanity >= 30:
                cetak_lambat("Anda mendarat dengan aman dan berlari!")
                return ending_selamat_biasa()
            else:
                cetak_lambat("Anda jatuh dengan buruk...")
                cetak_lambat("Monster mengejar Anda...")
                return ending_dimakan()
        else:
            cetak_lambat("\nAnda bersembunyi di lemari...")
            cetak_lambat("KESALAHAN! Monster mencium bau ketakutan Anda!")
            return ending_dimakan()
    else:
        cetak_lambat("\nAnda tidak punya peta! Anda berlari tanpa arah!")
        
        if random.random() < 0.3:  # 30% chance berhasil
            cetak_lambat("\nDengan keberuntungan, Anda menemukan pintu keluar!")
            return ending_selamat_biasa()
        else:
            cetak_lambat("\nAnda tersesat di dalam labirin koridor...")
            cetak_lambat("Monster menemukan Anda...")
            return ending_dimakan()

def scene_laboratory():
    """Scene laboratorium"""
    tampilkan_ascii_laboratorium()
    cetak_lambat("\n━━━ LABORATORIUM EKSPERIMEN ━━━")
    cetak_lambat("\nAnda memasuki laboratorium yang berantakan.")
    cetak_lambat("Ada meja bedah dengan noda darah tua...")
    cetak_lambat("Alat-alat medis berkarat berserakan di mana-mana...")
    cetak_lambat("Di dinding tergantung foto-foto pasien dengan wajah menyeramkan.")
    player.kurang_sanity(10)
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nAnda melihat:")
    cetak_lambat("- Lemari dengan gembok berkarat")
    cetak_lambat("- Meja dengan dokumen-dokumen berserakan")
    cetak_lambat("- Pintu ke kamar mayat di ujung ruangan")
    
    pilihan = pilih([
        "Periksa lemari (perlu linggis)",
        "Baca dokumen di meja",
        "Masuk ke kamar mayat",
        "Kembali ke koridor"
    ])
    
    if pilihan == 1:
        if player.cek_item("linggis"):
            cetak_lambat("\nAnda menggunakan linggis untuk membuka lemari...")
            cetak_lambat("Di dalam ada korek api dan botol alkohol!")
            player.tambah_item("korek api")
            player.tambah_item("alkohol")
            cetak_merah("ITEM PENTING DIDAPAT: Korek Api & Alkohol!")
            time.sleep(1)
            return scene_laboratory()
        else:
            cetak_lambat("\nAnda butuh alat untuk membuka lemari ini.")
            return scene_laboratory()
    
    elif pilihan == 2:
        cetak_lambat("\nAnda membaca dokumen-dokumen eksperimen Dr. Blackwood...")
        cetak_lambat("'Hari ke-156: Subjek 42 menunjukkan tanda-tanda mutasi...'")
        cetak_lambat("'Hari ke-203: Ritual berhasil! Tapi subjek menjadi... sesuatu yang lain...'")
        cetak_lambat("'Hari ke-240: Saya telah membuat kesalahan yang mengerikan...'")
        player.tahu_rahasia = True
        player.kurang_sanity(8)
        time.sleep(2)
        cetak_merah("INFO: Anda tahu rahasia gelap Blackwood Asylum!")
        return scene_laboratory()
    
    elif pilihan == 3:
        return scene_morgue()
    
    else:
        return scene_second_floor_corridor()

def scene_morgue():
    """Scene kamar mayat"""
    tampilkan_ascii_kamar_mayat()
    cetak_lambat("\n━━━ KAMAR MAYAT ━━━")
    cetak_lambat("\nRuangan dingin dengan deretan laci logam di dinding...")
    cetak_lambat("Bau pembusukan sangat menyengat di sini.")
    cetak_lambat("Beberapa laci terbuka... dan kosong...")
    player.kurang_sanity(12)
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nAnda mendengar suara GORESAN dari dalam salah satu laci!")
    
    pilihan = pilih([
        "Buka laci yang berbunyi",
        "Periksa laci lain",
        "Keluar dari ruangan dengan cepat"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda perlahan membuka laci...")
        cetak_lambat("Di dalam ada... MAYAT YANG MASIH BERGERAK!")
        cetak_lambat("TANGAN-NYA MERAIH ANDA!")
        player.kurang_sanity(20)
        
        if player.sanity <= 0:
            return ending_gila()
        
        if player.cek_item("pisau"):
            cetak_lambat("\nAnda menggunakan pisau untuk mempertahankan diri!")
            cetak_lambat("Anda berhasil melepaskan diri dan menutup laci!")
            time.sleep(1)
            return scene_laboratory()
        else:
            cetak_lambat("\nAnda panik dan berlari keluar!")
            return scene_second_floor_corridor()
    
    elif pilihan == 2:
        cetak_lambat("\nAnda membuka laci lain...")
        cetak_lambat("Di dalam ada kunci berkarat dengan label 'RITUAL ROOM'!")
        player.tambah_item("kunci ruang ritual")
        player.kunci_terkumpul += 1
        cetak_merah("ITEM KUNCI DIDAPAT: Kunci Ruang Ritual!")
        time.sleep(1)
        return scene_morgue()
    
    else:
        cetak_lambat("\nAnda keluar dengan cepat dari kamar mayat...")
        return scene_laboratory()

def scene_library():
    """Scene perpustakaan"""
    tampilkan_ascii_perpustakaan()
    cetak_lambat("\n━━━ PERPUSTAKAAN TUA ━━━")
    cetak_lambat("\nRak-rak buku tinggi menjulang di ruangan besar ini.")
    cetak_lambat("Buku-buku medis dan jurnal-jurnal tua berdebu...")
    cetak_lambat("Ada tangga untuk mencapai rak tinggi.")
    player.kurang_sanity(5)
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nAnda melihat:")
    cetak_lambat("- Buku tebal berjudul 'Ritual Blackwood' di rak tinggi")
    cetak_lambat("- Meja baca dengan catatan-catatan")
    cetak_lambat("- Pintu tersembunyi di balik rak buku")
    
    pilihan = pilih([
        "Panjat tangga dan ambil buku ritual",
        "Baca catatan di meja",
        "Periksa pintu tersembunyi",
        "Kembali ke koridor"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda memanjat tangga tua yang berderit...")
        cetak_lambat("Tangga! HAMPIR PATAH!")
        
        if player.sanity >= 50:
            cetak_lambat("Dengan hati-hati, Anda berhasil mengambil buku!")
            player.tambah_item("buku ritual")
            cetak_merah("ITEM PENTING: Buku Ritual Blackwood!")
            cetak_lambat("\nBuku ini berisi cara untuk mengakhiri kutukan!")
            player.tahu_rahasia = True
            time.sleep(1)
            return scene_library()
        else:
            cetak_lambat("Tangan Anda gemetar... Anda jatuh!")
            player.kurang_sanity(10)
            cetak_lambat("Anda terluka tapi masih bisa berdiri...")
            return scene_library()
    
    elif pilihan == 2:
        cetak_lambat("\nAnda membaca catatan terakhir Dr. Blackwood:")
        cetak_lambat("'Jika ada yang membaca ini... jangan ulangi kesalahanku...'")
        cetak_lambat("'Mereka semua masih di sini... menunggu... lapar...'")
        cetak_lambat("'Satu-satunya cara adalah membakar sumber kutukan...'")
        cetak_lambat("'Di ruang ritual di lantai basement... tapi aku tidak bisa...'")
        player.kurang_sanity(7)
        time.sleep(2)
        return scene_library()
    
    elif pilihan == 3:
        cetak_lambat("\nAnda mendorong rak buku...")
        cetak_lambat("Ada tangga spiral turun ke bawah!")
        cetak_lambat("Sepertinya menuju ke basement...")
        
        pilihan2 = pilih([
            "Turun ke basement",
            "Tidak, terlalu berbahaya"
        ])
        
        if pilihan2 == 1:
            return scene_basement_entrance()
        else:
            return scene_library()
    
    else:
        return scene_second_floor_corridor()

def scene_basement_entrance():
    """Scene pintu masuk basement"""
    tampilkan_ascii_tangga_basement()
    cetak_lambat("\n━━━ TANGGA MENUJU BASEMENT ━━━")
    cetak_lambat("\nTangga spiral gelap menuju kegelapan di bawah...")
    cetak_lambat("Udara semakin dingin setiap langkah Anda turun...")
    cetak_lambat("Anda mendengar bisikan-bisikan samar...")
    player.kurang_sanity(8)
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nAnda sampai di dasar tangga.")
    cetak_lambat("Ada pintu besi berat dengan tulisan 'RESTRICTED AREA'")
    
    if player.cek_item("kunci ruang ritual"):
        cetak_lambat("\nAnda memiliki kunci untuk pintu ini!")
        
        pilihan = pilih([
            "Buka pintu dan masuk",
            "Kembali ke atas (mungkin belum siap)"
        ])
        
        if pilihan == 1:
            cetak_lambat("\nAnda membuka pintu besi...")
            cetak_lambat("DERAK... Pintu terbuka perlahan...")
            time.sleep(2)
            return scene_ritual_room_final()
        else:
            return scene_library()
    else:
        cetak_lambat("\nPintu terkunci rapat. Anda butuh kunci khusus.")
        cetak_lambat("Mungkin ada di kamar mayat atau tempat lain...")
        return scene_library()

def scene_patient_ward():
    """Scene ruang rawat pasien"""
    tampilkan_ascii_ruang_rawat()
    cetak_lambat("\n━━━ RUANG RAWAT INAP ━━━")
    cetak_lambat("\nDeretan tempat tidur berkarat dengan kasur compang-camping...")
    cetak_lambat("Beberapa tempat tidur masih ada bekas penggunaan...")
    cetak_lambat("Di dinding ada guratan-guratan dengan kuku...")
    player.kurang_sanity(7)
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nAnda mendengar suara... seseorang menangis?")
    
    pilihan = pilih([
        "Cari sumber suara tangisan",
        "Periksa tempat tidur satu per satu",
        "Keluar dari ruangan"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda mengikuti suara tangisan...")
        cetak_lambat("Menuju ke pojok ruangan...")
        cetak_lambat("Ada sosok membelakangi Anda, menangis...")
        
        pilihan2 = pilih([
            "Dekati sosok itu",
            "Panggil sosok itu",
            "Mundur perlahan"
        ])
        
        if pilihan2 == 1:
            cetak_lambat("\nAnda menepuk bahu sosok itu...")
            cetak_lambat("Dia berbalik...")
            tampilkan_ascii_monster()
            cetak_lambat("WAJAHNYA TIDAK ADA!")
            player.kurang_sanity(25)
            if player.sanity <= 0:
                return ending_gila()
            cetak_lambat("\nAnda berlari keluar dari ruangan!")
            return scene_second_floor_corridor()
        
        elif pilihan2 == 2:
            cetak_lambat("\n'Halo? Apa Anda butuh bantuan?'")
            cetak_lambat("Sosok itu berhenti menangis...")
            cetak_lambat("Perlahan berbalik...")
            tampilkan_ascii_monster()
            cetak_lambat("ITU BUKAN MANUSIA!")
            player.kurang_sanity(30)
            player.sudah_bertemu_monster = True
            if player.sanity <= 0:
                return ending_gila()
            
            if player.cek_item("senter"):
                cetak_lambat("\nAnda menyorotkan senter ke makhluk itu!")
                cetak_lambat("Makhluk itu menjerit dan mundur!")
                cetak_lambat("Anda punya kesempatan untuk lari!")
                return scene_second_floor_corridor()
            else:
                cetak_lambat("\nMakhluk itu mendekat...")
                cetak_lambat("Anda tidak punya senjata...")
                return ending_dimakan()
        
        else:
            cetak_lambat("\nAnda mundur perlahan...")
            cetak_lambat("Dan keluar dari ruangan dengan aman.")
            return scene_second_floor_corridor()
    
    elif pilihan == 2:
        cetak_lambat("\nAnda memeriksa tempat tidur satu per satu...")
        cetak_lambat("Di bawah salah satu tempat tidur, Anda menemukan pisau lipat!")
        player.tambah_item("pisau")
        player.memiliki_senjata = True
        cetak_merah("SENJATA DIDAPAT: Pisau Lipat!")
        time.sleep(1)
        return scene_patient_ward()
    
    else:
        return scene_second_floor_corridor()

def scene_second_floor_corridor():
    """Scene koridor lantai 2"""
    tampilkan_ascii_koridor()
    cetak_lambat("\n━━━ KORIDOR LANTAI 2 ━━━")
    cetak_lambat("\nKoridor panjang dengan cat yang mengelupas...")
    cetak_lambat("Lampu-lampu berkedip-kedip...")
    
    if player.sudah_bertemu_monster:
        cetak_lambat("Anda mendengar langkah kaki berat di kejauhan...")
        cetak_lambat("Makhluk itu masih mencari Anda...")
        player.kurang_sanity(5)
    
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    cetak_lambat("\nAnda bisa pergi ke:")
    
    pilihan_lokasi = [
        "Laboratorium Eksperimen",
        "Perpustakaan",
        "Ruang Rawat Inap",
        "Turun ke lantai 1"
    ]
    
    pilihan = pilih(pilihan_lokasi)
    
    if pilihan == 1:
        return scene_laboratory()
    elif pilihan == 2:
        return scene_library()
    elif pilihan == 3:
        return scene_patient_ward()
    else:
        return scene_first_floor_main()

def scene_security_room():
    """Scene ruang keamanan"""
    tampilkan_ascii_keamanan()
    cetak_lambat("\n━━━ RUANG KEAMANAN ━━━")
    cetak_lambat("\nRuang kecil dengan monitor CCTV yang sudah mati...")
    cetak_lambat("Ada meja dengan laci-laci...")
    player.kurang_sanity(3)
    tampilkan_status()
    
    cetak_lambat("\nAnda mencari di laci-laci...")
    cetak_lambat("Anda menemukan:")
    
    items_found = []
    if not player.cek_item("senter"):
        cetak_lambat("- Senter yang masih berfungsi!")
        player.tambah_item("senter")
        items_found.append("senter")
    
    if not player.cek_item("peta rumah sakit"):
        cetak_lambat("- Peta denah rumah sakit!")
        player.tambah_item("peta rumah sakit")
        items_found.append("peta")
    
    if items_found:
        cetak_merah(f"ITEM BERGUNA DIDAPAT: {', '.join(items_found)}!")
        time.sleep(1)
    else:
        cetak_lambat("Tidak ada yang berguna di sini.")
    
    return scene_first_floor_main()

def scene_office():
    """Scene kantor administratif"""
    tampilkan_ascii_kantor()
    cetak_lambat("\n━━━ KANTOR ADMINISTRATIF ━━━")
    cetak_lambat("\nMeja-meja kerja dengan dokumen berserakan...")
    cetak_lambat("Ada lemari arsip besar di pojok ruangan.")
    player.kurang_sanity(4)
    tampilkan_status()
    
    pilihan = pilih([
        "Periksa lemari arsip",
        "Baca dokumen di meja",
        "Kembali ke lobby"
    ])
    
    if pilihan == 1:
        cetak_lambat("\nAnda membuka lemari arsip...")
        cetak_lambat("File-file pasien dari tahun 1960an...")
        cetak_lambat("Semua dengan cap 'DECEASED' atau 'MISSING'...")
        
        if not player.cek_item("linggis"):
            cetak_lambat("\nDi balik lemari, Anda menemukan linggis!")
            player.tambah_item("linggis")
            cetak_merah("ALAT DIDAPAT: Linggis!")
            time.sleep(1)
        
        player.kurang_sanity(6)
        return scene_office()
    
    elif pilihan == 2:
        cetak_lambat("\nAnda membaca dokumen terakhir sebelum rumah sakit ditutup:")
        cetak_lambat("'Insiden Blackwood - 47 orang hilang dalam satu malam...'")
        cetak_lambat("'Tidak ada yang bisa menjelaskan apa yang terjadi...'")
        cetak_lambat("'Gedung ini harus ditutup dan disegel...'")
        player.kurang_sanity(8)
        time.sleep(2)
        return scene_office()
    
    else:
        return scene_first_floor_main()

def scene_first_floor_main():
    """Scene utama lantai 1"""
    tampilkan_ascii_lobby()
    cetak_lambat("\n━━━ LOBBY LANTAI 1 ━━━")
    cetak_lambat("\nLobby besar dengan meja resepsionis yang ditinggalkan...")
    
    if player.kunci_terkumpul >= 1 and player.tahu_rahasia:
        cetak_lambat("\nAnda sudah tahu apa yang harus dilakukan...")
        cetak_lambat("Saatnya mengakhiri kutukan ini atau kabur dari sini!")
        
        pilihan = pilih([
            "Cari jalan ke ruang ritual (ending heroik)",
            "Cari pintu keluar (ending biasa)",
            "Eksplorasi lebih dulu"
        ])
        
        if pilihan == 1:
            if player.cek_item("kunci ruang ritual"):
                cetak_lambat("\nAnda menuju ke perpustakaan untuk mencapai basement...")
                return scene_basement_entrance()
            else:
                cetak_lambat("\nAnda belum punya kunci ruang ritual...")
                cetak_lambat("Mungkin ada di kamar mayat...")
                return scene_first_floor_main()
        
        elif pilihan == 2:
            return scene_escape_final()
        
        else:
            pass  # lanjut ke pilihan eksplorasi normal
    
    tampilkan_status()
    
    if player.sanity <= 0:
        return ending_gila()
    
    pilihan_lokasi = [
        "Ruang Keamanan",
        "Kantor Administratif",
        "Naik ke lantai 2",
        "Coba cari pintu keluar"
    ]
    
    pilihan = pilih(pilihan_lokasi)
    
    if pilihan == 1:
        return scene_security_room()
    elif pilihan == 2:
        return scene_office()
    elif pilihan == 3:
        return scene_second_floor_corridor()
    else:
        cetak_lambat("\nAnda mencoba mencari pintu keluar...")
        cetak_lambat("Tapi semua pintu terkunci dari luar!")
        cetak_lambat("Anda terjebak di sini...")
        player.kurang_sanity(10)
        time.sleep(1)
        return scene_first_floor_main()

def scene_entrance():
    """Scene pertama - pintu masuk"""
    tampilkan_ascii_gedung()
    cetak_lambat("\n━━━ PINTU MASUK BLACKWOOD ASYLUM ━━━")
    cetak_lambat("\nAnda berdiri di depan pintu besar rumah sakit jiwa terbengkalai.")
    cetak_lambat("Gedung megah namun suram ini sudah ditinggalkan sejak tahun 1963.")
    cetak_lambat("Teman Anda yang bodoh menantang Anda untuk masuk...")
    cetak_lambat("Dan kini mereka sudah pergi, meninggalkan Anda sendirian...")
    time.sleep(2)
    
    cetak_lambat("\nAnda mendengar suara aneh dari dalam gedung...")
    cetak_lambat("Pintu besar sedikit terbuka...")
    
    pilihan = pilih([
        "Masuk ke dalam gedung (begin the nightmare)",
        "Tetap di luar dan tunggu teman Anda kembali",
        "Coba hubungi teman Anda dengan ponsel"
    ], tampilkan_inventory=False)
    
    if pilihan == 1:
        tampilkan_ascii_pintu()
        cetak_lambat("\nAnda mengumpulkan keberanian dan mendorong pintu...")
        cetak_lambat("KREEEK... Pintu terbuka dengan suara mengerikan.")
        cetak_lambat("Anda melangkah masuk ke dalam kegelapan...")
        time.sleep(2)
        cetak_merah("TIDAK ADA JALAN KEMBALI!")
        cetak_lambat("\nPintu tertutup dengan sendirinya di belakang Anda!")
        cetak_lambat("Terkunci rapat!")
        player.kurang_sanity(15)
        time.sleep(2)
        return scene_first_floor_main()
    
    elif pilihan == 2:
        cetak_lambat("\nAnda memutuskan untuk tetap di luar...")
        cetak_lambat("Waktu berlalu... 1 jam... 2 jam...")
        cetak_lambat("Teman Anda tidak kembali...")
        time.sleep(2)
        cetak_lambat("\nAnda mendengar teriakan dari dalam gedung!")
        cetak_lambat("ITU SUARA TEMAN ANDA!")
        
        pilihan2 = pilih([
            "Masuk untuk menyelamatkan teman Anda",
            "Lari dan cari bantuan"
        ], tampilkan_inventory=False)
        
        if pilihan2 == 1:
            cetak_lambat("\nAnda berlari masuk ke gedung!")
            cetak_lambat("Pintu menutup di belakang Anda!")
            player.kurang_sanity(20)
            return scene_first_floor_main()
        else:
            cetak_lambat("\nAnda berlari ke jalan raya terdekat...")
            cetak_lambat("Tapi tidak ada mobil yang lewat...")
            cetak_lambat("Tidak ada orang...")
            time.sleep(2)
            cetak_lambat("\nAnda menoleh ke belakang...")
            cetak_lambat("Gedung rumah sakit... menghilang?")
            cetak_lambat("Hanya hutan gelap yang tersisa...")
            time.sleep(2)
            cetak_lambat("\nAnda kembali ke lokasi gedung itu...")
            cetak_lambat("DAN ANDA SUDAH ADA DI DALAM!")
            return ending_terjebak_loop()
    
    else:
        cetak_lambat("\nAnda mengecek ponsel...")
        cetak_lambat("TIDAK ADA SINYAL.")
        cetak_lambat("Baterai tiba-tiba habis!")
        cetak_lambat("\nAnda mendengar tawa dari dalam gedung...")
        cetak_lambat("Tawa teman Anda... tapi terdengar... salah...")
        player.kurang_sanity(10)
        time.sleep(2)
        
        pilihan2 = pilih([
            "Masuk ke gedung",
            "Lari meninggalkan tempat ini"
        ], tampilkan_inventory=False)
        
        if pilihan2 == 1:
            cetak_lambat("\nAnda masuk ke gedung...")
            player.kurang_sanity(10)
            return scene_first_floor_main()
        else:
            cetak_lambat("\nAnda berlari menjauhi gedung...")
            cetak_lambat("Tapi kaki Anda terasa berat...")
            cetak_lambat("Anda tidak bisa... bergerak...")
            time.sleep(2)
            cetak_lambat("\nKetika Anda membuka mata...")
            cetak_lambat("Anda sudah ada di dalam lobby gedung!")
            cetak_merah("ANDA TIDAK BISA KABUR DARI TAKDIR!")
            player.kurang_sanity(25)
            return scene_first_floor_main()

def intro_story():
    """Cerita pembuka"""
    cetak_lambat("\n" + "="*70)
    cetak_lambat("                      THE STORY BEGINS")
    cetak_lambat("="*70)
    cetak_lambat("\nBlackwood Psychiatric Hospital...")
    time.sleep(1)
    cetak_lambat("\nDibangun tahun 1923 oleh Dr. Jonathan Blackwood,")
    cetak_lambat("rumah sakit jiwa terbesar di negara bagian ini.")
    time.sleep(1)
    cetak_lambat("\nTahun 1963, sesuatu yang mengerikan terjadi...")
    cetak_lambat("47 pasien dan staf menghilang dalam satu malam.")
    cetak_lambat("Tidak ada jejak, tidak ada petunjuk, tidak ada mayat.")
    time.sleep(1)
    cetak_lambat("\nGedung ditutup dan disegel.")
    cetak_lambat("Tapi cerita mengatakan...")
    cetak_lambat("Mereka semua masih di sana...")
    cetak_lambat("Menunggu...")
    time.sleep(2)
    cetak_lambat("\nDan malam ini, Anda akan menemukan kebenarannya...")
    time.sleep(2)
    input("\n[Tekan ENTER untuk memulai nightmare...] ")

def main():
    """Fungsi utama game"""
    global player, AUTO_BUKA_GAMBAR, GAMBAR_SUDAH_DIBUKA
    
    cetak_judul()
    
    cetak_lambat("⚠️  PERINGATAN  ⚠️")
    cetak_lambat("Game ini berisi konten horor yang intens.")
    cetak_lambat("Anda akan menghadapi pilihan-pilihan sulit.")
    cetak_lambat("Hanya sedikit yang bisa selamat...")
    cetak_lambat("\nPilihan Anda menentukan nasib Anda.")
    cetak_lambat("Ada 7 ending berbeda yang bisa Anda capai.")
    
    mulai = input("\nApakah Anda siap? (y/n): ")
    if mulai.lower() != 'y':
        cetak_lambat("\nKeputusan yang bijak...")
        cetak_lambat("Beberapa pintu lebih baik tetap ditutup.")
        return

    mode_gambar = input("\nBuka gambar Unsplash otomatis di browser? (y/n, default n): ").strip().lower()
    AUTO_BUKA_GAMBAR = mode_gambar == 'y'
    GAMBAR_SUDAH_DIBUKA = set()
    if AUTO_BUKA_GAMBAR:
        cetak_lambat("Mode gambar aktif: browser akan membuka gambar saat scene pertama kali muncul.")
    else:
        cetak_lambat("Mode gambar manual: link Unsplash akan ditampilkan di terminal.")
    
    print("\n" * 2)
    intro_story()
    print("\n" * 2)
    
    # Reset player untuk game baru
    player = Player()
    
    # Mulai game dari entrance
    scene_entrance()
    
    # Tanya main lagi
    print("\n" + "="*70)
    main_lagi = input("\nApakah Anda ingin mencoba lagi? (y/n): ")
    if main_lagi.lower() == 'y':
        print("\n" * 3)
        main()
    else:
        cetak_lambat("\nTerima kasih telah bermain ASYLUM NIGHTMARE!")
        cetak_lambat("Semoga malam Anda tidak dipenuhi mimpi buruk...")
        cetak_lambat("\n👻 Created with fear and code 👻\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Game dihentikan paksa!")
        print("Tapi ingat... Anda tidak bisa kabur dari Blackwood Asylum...")
        print("Mereka akan tetap menunggu Anda... 👻\n")
        sys.exit(0)
