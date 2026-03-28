# Sistem Mimarisi: AstroBio-Edge

## 1. Giriş
Bu döküman, merkeziyetsiz astrobiyoloji görevleri için tasarlanan AstroBio-Edge sisteminin teknik mimarisini tanımlar.

## 2. Katmanlı Mimari

### 2.1 Sensör Soyutlama Katmanı (SAL)
SAL, çeşitli sensörler (Raman Spektrometreleri, Kütle Spektrometreleri vb.) için birleşik bir arayüz sağlar.
- **Hedef**: Donanım ve mantık arasındaki bağımlılığı en aza indirmek.
- **Uygulama**: Sanallaştırılmış cihaz sürücüleri.

### 2.2 Uç İşleme Motoru (EPE)
Sistemin "keşif" merkezidir.
- **Organik Tespit**: Spektral tepelerin sezgisel analizi.
- **Özellik Çıkarımı**: Verimli iletim için boyut küçültme.
- **Otonomi**: Düşük çözünürlüklü ipuçlarına dayanarak yüksek hassasiyetli taramaları tetikleme.

### 2.3 Mesh İletişim Protokolü (MCP)
Sürü halindeki birden fazla iniş aracı veya drone arasındaki eşler arası veri paylaşımını yönetir.
- **Hata Toleransı**: Bir düğüm arızalandığında dinamik yönlendirme.
- **Öncelik**: Hayati "Yaşam Bulundu" sinyalleri telemetride önceliklidir.

## 3. Veri Akışı
1. Ham Sensör Verisi -> SAL
2. Temizlenmiş Veri -> EPE
3. Tespit Olayı -> MCP (Sürüye Yayın)
4. Önceliklendirilmiş Telemetri -> Yer İstasyonu

## 4. Güvenlik ve Bütünlük
- **ECC**: Radyasyon kaynaklı bit değişimleri için Hata Düzeltme Kodları.
- **Bütünlük**: Değiştirilemez log tutma için tespit olaylarının kriptografik özetleri.
