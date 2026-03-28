# 🌌 AstroBio-Edge-Architecture

![AstroBio-Edge Banner](assets/banner.png)

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Görev: TUA AstroHackathon](https://img.shields.io/badge/G%C3%B6rev-TUA%20AstroHackathon-blue.svg)](https://tua.gov.tr)
[![Güvenlik: ESA-PSS-01](https://img.shields.io/badge/G%C3%BCvenlik-ESA--PSS--01-green.svg)](#)

**AstroBio-Edge-Architecture**, merkeziyetsiz astrobiyolojik veri işleme için tasarlanmış yeni nesil bir teknik ekosistemdir. Keşif noktasında uç bilişim (edge computing) kullanarak, ekstrem ortamlarda gerçek zamanlı biyolojik imza tespiti ve otonom yük yönetimi sağlar.

---

## 🚀 Genel Bakış

Geleneksel uzay görevleri, veri analizi için yüksek gecikmeli yer bağlantılarına dayanır. **AstroBio-Edge**, keşif esnasında kritik biyolojik sinyallerin telemetri darboğazlarından önce tanımlanmasını ve önceliklendirilmesini sağlayan "Sensörde Hesaplama" modelini uygular.

### Temel Sütunlar
- **Merkeziyetsiz Zeka**: Analitik iş yüklerini paylaşan eşler arası (P2P) uç düğümler (edge nodes).
- **Yapay Zeka Destekli Analiz**: Derin öğrenme tabanlı biyolojik imza sınıflandırması.
- **Dinamik Enerji Yönetimi**: Uzun süreli görevler için akıllı güç tasarrufu algoritmaları.
- **ESA/NASA Uyumluluğu**: Gezegensel koruma protokollerine (Kategori IV) tam uyumluluk.

---

## 🏗️ Sistem Mimarisi ve Teknik Derinlik

AstroBio-Edge sistemi, **Hata Toleranslı Dağıtık Hesaplama** prensipleri üzerine inşa edilmiştir.

### 1. Sensör Soyutlama Katmanı (SAL)
SAL, ham spektroskopik veriyi işlemek için bir tampon bölge görevi görür. Farklı üreticilerin sensörlerini tek bir veri formatına indirger.

### 2. Uç İşleme Motoru (EPE)
EPE, spektral gürültü temizleme (Baseline Correction) ve adaptif tepe noktası tespiti (Adaptive Peak Detection) algoritmalarını koordine eder.

### 3. Yapay Zeka Katmanı (Models/AI)
`models/biosignature_nn.py` modülü, sinir ağı tabanlı bir sınıflandırıcı sunar. Yazılım, geleneksel sezgisel dedektör ile AI tabanlı sınıflandırıcıyı hibrit bir modelde birleştirerek güven oranını maksimize eder.

---

## ⚡ Donanım ve Performans Metrikleri

| Spesifikasyon | Değer | Açıklama |
| :--- | :--- | :--- |
| **CPU Hedefi** | ARM Cortex-M7 / RISC-V | Düşük güç tüketimli uç işlemciler. |
| **RAM İhtiyacı** | < 256 KB | micro-ML optimizasyonu ile minimize edilmiş bellek kullanımı. |
| **Tespit Süresi** | < 500 ms | Sinyal alımından karara kadar geçen süre. |
| **Enerji Tasarrufu** | LBO Modu | Batarya %20 altına düştüğünde tasarruf modu aktivasyonu. |

---

## 🛡️ Dayanıklılık ve Güvenlik (Resilience)

Uzay ortamı, donanım üzerinde bit değişimleri (bit-flips) ve sensör gürültüsü gibi fiziksel zorluklar yaratır.

- **Hata Enjeksiyonu**: `src/utils/fault_injector.py` modülü, sistemi radyasyon etkilerine karşı test eder.
- **Konsensüs**: Sürü (Swarm), çoğunluk algılama algoritmaları ile bireysel hata yapan düğümleri izole eder.

---

## 📊 Görselleştirme ve Raporlama

Görev sonuçları iki seviyede izlenebilir:
1.  **Terminal Analizi**: `src/utils/visualizer.py` ile ASCII tabanlı önizleme.
2.  **HTML Dashboard**: `src/utils/report_generator.py` ile etkileşimli görev paneli.

---

## 📂 Depo Yapısı

```tree
.
├── src/            # Çekirdek işleme mantığı ve uç sistemler
├── docs/           # Mimari ve Uyumluluk belgeleri
├── assets/         # Banner ve teknik çizimler
├── hardware/       # Güç yönetimi ve sensör konfigürasyonları
├── simulations/    # Çok düğümlü görev simülasyonları
├── models/         # Sezgisel ve AI tabanlı dedektör modelleri
├── tests/          # Mantıksal doğrulama testleri
└── LICENSE         # MIT Lisansı
```

---

## 📜 Gelecek Yol Haritası
- [ ] Gömülü Rust (no_std) implementasyonu.
- [ ] Derin öğrenme modellerinin donanım hızlandırıcı (NPU/DSP) optimizasyonu.
- [ ] Sürü bazlı otonom rota planlama.

---

## 🤝 Katkıda Bulunma

Gezegen bilimcileri ve uzay sistemleri mühendislerinin katkılarına açığız.

**Geliştirici**: [Yunus] - GitHub: [@arch-yunus](https://github.com/arch-yunus)
