# 🏥 ASYLUM NIGHTMARE - Advanced Horror Game

Game horor interaktif berbasis teks yang kompleks dengan sistem inventory, sanity meter, dan multiple branching paths.

## 📖 Deskripsi

**"Asylum Nightmare: The Blackwood Psychiatric Hospital"** adalah game petualangan horor berbasis teks yang jauh lebih kompleks dari game biasa. Anda terjebak di rumah sakit jiwa terbengkalai dengan sejarah kelam. Setiap keputusan mempengaruhi sanity (kewarasan) Anda, dan hanya dengan strategi yang tepat Anda bisa mencapai ending terbaik.

## 🎮 Fitur Advanced

### Sistem Gameplay
- **Sanity System**: Kewarasan Anda berkurang seiring pengalaman mengerikan
- **Inventory Management**: Kumpulkan dan gunakan item strategis (maksimal 5 item)
- **Multiple Branching Paths**: Lebih dari 15 scene berbeda dengan pilihan kompleks
- **Item Dependencies**: Beberapa aksi memerlukan item khusus
- **Hidden Secrets**: Temukan rahasia gelap Blackwood Asylum
- **Monster Encounters**: Hadapi makhluk supernatural yang berbahaya

### 7 Ending Berbeda
1. 🌀 **KEGILAAN** - Sanity mencapai 0%, kehilangan akal sehat
2. 👻 **TERKUTUK** - Terjebak selamanya di asylum
3. 🩸 **MANGSA** - Dimakan oleh monster
4. 🏃 **PELARIAN** - Selamat tapi trauma (ending standar)
5. ⭐ **SANG PEMBEBAS** - Ending terbaik! Selamat DAN mengakhiri kutukan
6. 🐺 **TRANSFORMASI** - Berubah menjadi monster
7. 🔄 **INFINITE LOOP** - Terjebak dalam lingkaran waktu

## 🗺️ Lokasi yang Bisa Dijelajahi

### Lantai 1
- **Lobby** - Pusat navigasi
- **Ruang Keamanan** - Temukan senter dan peta
- **Kantor Administratif** - Temukan linggis dan dokumen rahasia

### Lantai 2
- **Laboratorium Eksperimen** - Tempat eksperimen Dr. Blackwood
- **Perpustakaan** - Kunci untuk ending terbaik ada di sini
- **Ruang Rawat Inap** - Tempat pasien... atau monster?
- **Kamar Mayat** - Temukan kunci penting

### Basement
- **Ruang Ritual** - Sumber kutukan dan kunci ending heroik

## 🎒 Item Penting

| Item | Fungsi | Lokasi |
|------|--------|---------|
| 🔦 Senter | Mengusir makhluk gelap | Ruang Keamanan |
| 🗺️ Peta | Navigasi dan escape lebih mudah | Ruang Keamanan |
| 🔧 Linggis | Membuka lemari terkunci | Kantor Admin |
| 🔪 Pisau | Pertahanan diri | Ruang Rawat Inap |
| 🔥 Korek Api | Untuk ritual akhir | Laboratorium |
| 📖 Buku Ritual | Cara mengakhiri kutukan | Perpustakaan |
| 🔑 Kunci Ritual | Akses ke ruang ritual | Kamar Mayat |
| 🍾 Alkohol | Item tambahan | Laboratorium |

## 🎯 Cara Mencapai Ending Terbaik (SPOILER!)

<details>
<summary>Klik untuk melihat walkthrough ending terbaik</summary>

### Path ke "SANG PEMBEBAS" Ending:

1. **Masuk gedung** dari pintu depan
2. **Lantai 1**: Kunjungi Ruang Keamanan → ambil **Senter** dan **Peta**
3. **Lantai 1**: Kunjungi Kantor Admin → ambil **Linggis**
4. **Naik ke Lantai 2** → Pergi ke **Laboratorium**
5. **Laboratorium**: Gunakan linggis untuk buka lemari → ambil **Korek Api**
6. **Laboratorium**: Masuk ke **Kamar Mayat**
7. **Kamar Mayat**: Periksa laci lain → ambil **Kunci Ruang Ritual**
8. **Kembali ke Lantai 2** → Pergi ke **Perpustakaan**
9. **Perpustakaan**: Panjat tangga (butuh sanity >50%) → ambil **Buku Ritual**
10. **Perpustakaan**: Buka pintu tersembunyi → Turun ke **Basement**
11. **Basement**: Gunakan kunci → Masuk **Ruang Ritual**
12. **Ruang Ritual**: Pilih "Bakar altar dengan korek api dan baca counter-spell"
13. **Escape**: Gunakan peta untuk keluar → **VICTORY!**

**Tips Penting:**
- Jangan biarkan sanity < 40% untuk ending terbaik
- Hindari encounter monster jika tidak punya senter
- Ambil semua item penting sebelum ke basement
- Baca semua dokumen untuk memahami cerita

</details>

## 💀 Tips Survival

### Manajemen Sanity
- **KRITIS**: Jika sanity = 0%, instant game over (Ending: Kegilaan)
- **Hindari**: Jangan pilih opsi yang obviously berbahaya
- **Senter**: Sangat membantu mengusir monster (-0% sanity loss)
- **Dokumen**: Membaca rahasia mengurangi sanity, tapi perlu untuk ending terbaik

### Strategi Inventory
- Prioritaskan: Senter, Peta, Korek Api, Buku Ritual, Kunci Ritual
- Jangan buang waktu mengumpulkan item yang tidak penting
- Pisau berguna tapi tidak wajib untuk ending terbaik

### Eksplorasi
- **Ruang Keamanan** → WAJIB dikunjungi pertama
- **Perpustakaan** → Kunci untuk ending heroik
- **Kamar Mayat** → Tempat kunci penting
- **Ruang Rawat Inap** → HATI-HATI! Monster sering muncul di sini

## 🎮 Cara Bermain

```bash
python asylum_nightmare.py
```

1. Baca cerita dengan saksama
2. Pilih opsi dengan mengetik nomor (1, 2, 3, dst)
3. Perhatikan status Sanity dan Inventory Anda
4. Kumpulkan item strategis
5. Temukan rahasia dan capai ending terbaik!

## 📊 Difficulty Level

**⭐⭐⭐⭐⭐ VERY HARD**

- Multiple death scenarios
- Sanity management krusial
- Butuh planning yang matang
- Item dependencies kompleks
- Monster encounters berbahaya
- Hanya ~15% pemain mencapai ending terbaik pada percobaan pertama

## 🎯 Achievement Unlockable

- 🏃 **Survivor** - Keluar hidup-hidup (ending 4)
- ⭐ **Hero** - Capai ending terbaik (ending 5)
- 👻 **Collector** - Kumpulkan semua 8 item dalam satu playthrough
- 🧠 **Sane Mind** - Selesaikan game dengan sanity >60%
- 📚 **Loremaster** - Baca semua dokumen rahasia
- 💀 **True Horror** - Temukan semua 7 ending

## ⚠️ Content Warning

Game ini berisi:
- Tema horor psikologis
- Deskripsi kekerasan
- Suasana mencekam dan disturbing
- Tema rumah sakit jiwa dan eksperimen manusia

**Tidak direkomendasikan untuk:**
- Usia di bawah 17 tahun
- Orang dengan kondisi kecemasan
- Dimainkan sendirian di malam hari (just kidding... or am I? 👻)

## 🎭 Lore & Background Story

### Dr. Jonathan Blackwood
Dokter brilian yang terobsesi dengan penyembuhan penyakit mental melalui metode "tidak konvensional". Eksperimennya dengan ritual okultisme berakhir dengan bencana tahun 1963.

### The Incident of 1963
Dalam satu malam, 47 orang (32 pasien dan 15 staf) menghilang tanpa jejak. Investigasi tidak menemukan apa-apa. Gedung ditutup dan disegel, tapi penduduk lokal masih mendengar suara-suara aneh dari dalam.

### The Curse
Dr. Blackwood tidak mati... dia berubah. Bersama pasien-pasiennya, mereka terjebak di dunia antara hidup dan mati, menunggu korban baru untuk bergabung dengan mereka untuk selamanya...

## 🔧 Technical Details

- **Language**: Python 3.6+
- **Dependencies**: Standard library only (sys, time, random)
- **Platform**: Cross-platform (Windows, Linux, macOS)
- **Lines of Code**: 800+ lines
- **Playtime**: 20-45 menit (tergantung eksplorasi)

## 📝 Perbedaan dengan Horror Game v1

| Fitur | Horror Game v1 | Asylum Nightmare |
|-------|----------------|------------------|
| Complexity | Simple | Advanced |
| Total Scenes | 6-8 scenes | 15+ scenes |
| Endings | 4 endings | 7 endings |
| Systems | Basic choice | Sanity + Inventory |
| Difficulty | Easy | Very Hard |
| Playtime | 5-10 min | 20-45 min |
| Items | None | 8 collectible items |
| Monster | None | Multiple encounters |

## 🎬 Developer Notes

Game ini dirancang untuk memberikan pengalaman horor yang lebih mendalam dengan:
- **Replayability tinggi**: 7 ending mendorong multiple playthroughs
- **Strategic thinking**: Tidak bisa sembarangan pilih, harus mikir
- **Risk vs Reward**: Item bagus sering di tempat berbahaya
- **Atmosfer**: Pacing dan deskripsi dibuat untuk build tension
- **Fair but hard**: Semua ending bisa dicapai, tapi butuh skill

---

## 👻 Final Words

*"Beberapa tempat tidak seharusnya dikunjungi..."*  
*"Beberapa pintu tidak seharusnya dibuka..."*  
*"Beberapa rahasia tidak seharusnya diketahui..."*  

*"Tapi Anda sudah di sini sekarang..."*  
*"Dan Blackwood Asylum tidak akan membiarkan Anda pergi..."*

**Selamat bermain dan semoga beruntung! Anda akan membutuhkannya... 🏥👻**

---

*Created with 💀 by a horror enthusiast*  
*Version 1.0 - February 2026*
