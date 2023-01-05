# icovid

### Nama dan NPM anggota:
- Graciella Regina                   - 2006463282
- Gregorius Bhisma                   - 2006473970
- Hanif Ibrahim Syuaib               - 2006482003
- Izzan Nufail Arvin                 - 2006462922
- Muhammad Kenshin Himura Mahmuddin  - 2006473844
- Najwa Kariza Anjelia               - 2006463452
- Steven Novaryo                     - 2006473951

### Link herokuapp:
- [Heroku Dashboard](https://dashboard.heroku.com/apps/icovid-id)
- [Heroku App](https://icovid-id.herokuapp.com/)

### Cerita aplikasi:
Website kami bernama iCovid. Terinspirasi dari iMaba BEM Fasilkom UI, harapan dari website ini adalah dapat menjadi kanal informasi mengenai Covid-19 bagi masyarakat Indonesia. Pengguna juga dapat saling berbagi wawasan melalui forum yang disediakan oleh website ini. 

### Manfaat aplikasi:
Website kelompok kami memberikan informasi mengenai Covid-19 dalam bentuk artikel-artikel atau post, menceritakan pengalaman melalui forum, serta update data Covid-19 secara realtime.

### Daftar modul:

```
Authentication    → Registration and login
Home/About        → Halaman utama website yang menampilkan About iCovid, Cuplikan artikel dan Update Covid-19, serta tampilan testimoni
Utilities         → Form khusus admin ( base model, etc )
Article Post      → Halaman di mana pengguna bisa mencari berita tentang Covid-19
Profile Account   → Profile User Biasa 
Forum             → Forum tempat pengguna bisa reply satu sama lain mengenai suatu topik
Update Covid-19   → Scraping 
```

### Pembagian

```
Authentication    → Steven Novaryo
Home/About        → Graciella Regina
Utilities         → Hanif Ibrahim Syuaib
Article Post      → Izzan Nufail Arvin
Profile Account   → Najwa Kariza A
Forum             → Gregorius Bhisma
Update Covid-19   → Muhammad Kenshin Himura Mahmuddin
```

### Persona

|  | Pasien Covid-19|Masyarakat Umum |
|--|-------------- | ---------------| 
| Goals | Menemukan referensi bacaan mengenai Covid-19 | Mendapatkan update harian dan artikel mengenai Covid-19 di Indonesia|   
| Motivation | Pasien bersemangat untuk lekas sembuh| Masyarakat mengharapkan website yang mudah digunakan untuk semua kalangan |Masyarakat mengharapkan wadah untuk saling bertukar informasi dengan mudah |
|  | Pasien bersemangat untuk lekas sembuh| Masyarakat mengharapkan website yang mudah digunakan untuk semua kalangan |Masyarakat mengharapkan wadah untuk saling bertukar informasi dengan mudah |

**Admin**     : Bisa mengakses utility untuk melihat log serta menginput berita-berita yang ditampilkan pada Article Post
**Registered User** : Bisa mengakses semua fitur pada website iCovid namun tidak bisa mengakses utility dan hanya bertindak sebagai pembaca pada Article Post. User juga bisa me-reply thread pada forum, mengisi feedback pada HomePage
**Unregistered User** : Hanya bisa melihat halaman pada website namun tidak bisa mereply thread pada forum dan mengisi formulir yang ada
