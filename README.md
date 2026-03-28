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

## 🏗️ Sistem Mimarisi

Mimari üç ana katmana ayrılmıştır:

1.  **Sensör Soyutlama Katmanı (SAL)**: Farklı astrobiyoloji yüklerinden gelen verileri standartlaştırır.
2.  **Uç İşleme Motoru (EPE)**: RISC-V/ARM mimarilerinde çalışan yerelleştirilmiş ML modelleri ve sezgisel filtreler.
3.  **Mesh İletişim Protokolü (MCP)**: Düşük bant genişliğinde bile dağıtık modüller arasında veri bütünlüğünü ve senkronizasyonu sağlar.

> [!IMPORTANT]
> Bu sistem, **Gezegensel Koruma Kategori IV** için tasarlanmış olup, yüksek analitik hassasiyeti korurken sıfır çapraz kontaminasyon sağlar.

---

## 📂 Depo Yapısı

```tree
.
├── src/            # Çekirdek işleme mantığı ve uç sistemler
├── docs/           # Teknik şartnameler ve uyumluluk belgeleri
├── hardware/       # PCB tasarımları ve sensör şemaları
├── simulations/    # Testler için dijital ikiz ortamlar
├── models/         # Biyolojik imza tespiti için ML modelleri
├── CHANGELOG.md    # Versiyon takibi
└── LICENSE         # MIT Lisansı
```

---

## 🛠️ Teknik Yığın

- **Diller**: Rust (Güvenlik kritik), Python (Veri Bilimi), C++ (Gömülü Sürücüler)
- **Çerçeveler**: micro-ML, RTOS (FreeRTOS/Zephyr), Protocol Buffers
- **Donanım Hedefleri**: RISC-V (PolarFire SoC), ARM Cortex-M7
- **Standartlar**: CCSDS (İletişim), NASA-STD-8739.8 (Yazılım Güvencesi)

---

## 📡 Kurulum ve Kullanım

### Ön Koşullar
- Python 3.10+
- Rust Araç Zinciri
- Hedef donanım için çapraz derleyici (Cross-compiler)

### Yerel Simülasyon
```bash
# Depoyu klonlayın
git clone https://github.com/arch-yunus/AstroBio-Edge-Architecture.git

# Simülasyon ortamını hazırlayın
python simulations/setup_env.py
```

---

## 🤝 Katkıda Bulunma

Araştırmacıları, gezegen bilimcileri ve yazılım mühendislerini bekliyoruz. Lütfen yakında eklenecek olan `CONTRIBUTING.md` dosyasını inceleyin.

---

## ⚖️ Lisans

MIT Lisansı altında dağıtılmaktadır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

**İletişim**: [Yunus] - GitHub: [@arch-yunus](https://github.com/arch-yunus)
