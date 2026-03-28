# 🌌 AstroBio-Edge-Architecture

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Görev: TUA AstroHackathon](https://img.shields.io/badge/G%C3%B6rev-TUA%20AstroHackathon-blue.svg)](https://tua.gov.tr)
[![Güvenlik: ESA-PSS-01](https://img.shields.io/badge/G%C3%BCvenlik-ESA--PSS--01-green.svg)](#)

**AstroBio-Edge-Architecture**, merkeziyetsiz astrobiyolojik veri işleme için tasarlanmış yeni nesil bir teknik ekosistemdir. Keşif noktasında uç bilişim (edge computing) kullanarak, ekstrem ortamlarda gerçek zamanlı biyolojik imza tespiti ve otonom yük yönetimi sağlar.

---

## 🚀 Genel Bakış

Geleneksel uzay görevleri, veri analizi için yüksek gecikmeli yer bağlantılarına dayanır. **AstroBio-Edge**, keşif esnasında kritik biyolojik sinyallerin telemetri darboğazlarından önce tanımlanmasını ve önceliklendirilmesini sağlayan "Sensörde Hesaplama" modelini uygular.

### Temel Sütunlar
- **Merkeziyetsiz Zeka**: Analitik iş yüklerini paylaşan eşler arası (P2P) uç düğümler (edge nodes).
- **Dinamik Biyolojik İmza Filtreleme**: Organik bileşik tanımlama için düşük gecikmeli algoritmalar.
- **ESA/NASA Uyumluluğu**: Gezegensel koruma ve radyasyon dayanıklılık protokollerine uygun.
- **Modüler Yük Entegrasyonu**: Spektroskopik, kimyasal ve mikroskobik sensörler için basitleştirilmiş arayüz.

---

## 🏗️ Sistem Mimarisi ve Teknik Derinlik

AstroBio-Edge sistemi, **Hata Toleranslı Dağıtık Hesaplama** prensipleri üzerine inşa edilmiştir.

### 1. Sensör Soyutlama Katmanı (SAL)
SAL, ham spektroskopik veriyi işlemek için bir tampon bölge görevi görür. Farklı üreticilerin sensörlerini (Raman, NIR, Mossbauer) tek bir veri formatına indirger.

### 2. Uç İşleme Motoru (EPE)
EPE, `src/utils/signal_processing.py` içerisinde tanımlanan algoritmaları kullanarak:
- **Baseline Correction**: Spektrumdaki gürültü tabanını otomatik olarak temizler.
- **Adaptive Peak Detection**: Dinamik eşik değerleri kullanarak biyolojik imzalara karşılık gelen spektral tepeleri yakalar.

### 3. Mesh İletişim Protokolü (AMP-v1)
AMP, `src/mesh_coordinator.py` tarafından yönetilir ve şu özellikleri sunar:
- **Quorum Sensing (Çoğunluk Algılama)**: Bir biyolojik imza tespit edildiğinde, sürüdeki diğer düğümlerden doğrulama istenir. Bu, bireysel sensör hatalarından kaynaklı yanlış pozitifleri (False Positive) engeller.
- **Carousel Routing**: Radyasyonun yoğun olduğu bölgelerde, mesajlar dinamik olarak en güvenli yoldan iletilir.

---

## 🛡️ Dayanıklılık ve Güvenlik (Resilience)

Uzay ortamı, donanım üzerinde bit değişimleri (bit-flips) ve sensör gürültüsü gibi fiziksel zorluklar yaratır.

- **Hata Enjeksiyonu (Fault Injection)**: `src/utils/fault_injector.py` modülü, sistemi radyasyon etkilerine karşı test etmek için kullanılır.
- **Hata Modları Analizi**: [FAILURE_MODES.md](docs/FAILURE_MODES.md) dosyasında detaylandırılan stratejilerle sistemin sürekliliği sağlanır.

---

## 📊 Görselleştirme ve Raporlama

Görev sonuçları iki seviyede izlenebilir:
1.  **Terminal Analizi**: `src/utils/visualizer.py` ile spektral verilerin ASCII tabanlı hızlı önizlemesi yapılır.
2.  **HTML Dashboard**: `src/utils/report_generator.py` ile tüm görev verileri profesyonel ve etkileşimli bir web paneline dönüştürülür.

---

## 📂 Depo Yapısı

```tree
.
├── src/            # Çekirdek işleme mantığı ve uç sistemler
│   ├── utils/      # Sinyal işleme, hata enjeksiyonu, raporlama
├── docs/           # Mimari, Protokoller ve Uyumluluk belgeleri
├── hardware/       # Sensör konfigürasyonları ve şemalar
├── simulations/    # Çok düğümlü görev simülasyonları
├── models/         # Biyolojik imza tanımlama modelleri
├── tests/          # Mantıksal doğrulama testleri
├── CHANGELOG.md    # Sürüm geçmişi
└── LICENSE         # MIT Lisansı
```

---

## 📡 Kullanım Kılavuzu

### 1. Kurulum
```bash
git clone https://github.com/arch-yunus/AstroBio-Edge-Architecture.git
pip install numpy  # Gerekli bağımlılık
```

### 2. Simülasyon Çalıştırma
Sürü halindeki düğümlerin koordinasyonunu simüle etmek için:
```bash
python simulations/multinode_sim.py
```

### 3. Rapor Üretme
Görev sonrası görsel dashboard oluşturmak için:
```bash
python src/utils/report_generator.py
```

---

## 📜 Gelecek Yol Haritası
- [ ] Gömülü Rust (no_std) implementasyonu.
- [ ] Gerçek zamanlı spektrometre donanım entegrasyonu.
- [ ] Derin öğrenme tabanlı biosignature sınıflandırıcı.

---

## 🤝 İletişim & Katkıda Bulunma

Gezegen bilimcileri ve uzay sistemleri mühendislerinin katkılarına açığız.

**Geliştirici**: [Yunus] - GitHub: [@arch-yunus](https://github.com/arch-yunus)
