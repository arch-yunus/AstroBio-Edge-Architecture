# AstroBio-Edge: Görev Uyumluluğu ve Yazılım Güvencesi

Bu belge, NASA-STD-8739.8 ve ESA Gezegensel Koruma Kategori IV uyumluluğunu sağlamak için kullanılan protokolleri ve kontrol listelerini özetler.

## 1. NASA-STD-8739.8 (Yazılım Güvencesi)
- [x] **Modüler Mimari**: Sistemler SAL, EPE ve MCP katmanlarına ayrıştırılmıştır.
- [x] **Hata Toleransı**: `MeshCoordinator`, bireysel düğüm arızalarını yönetmek için çoğunluk algılama (quorum sensing) uygular.
- [ ] **Birim Test Kapsamı**: Sinyal işleme yardımcı araçları için > %80 kapsam hedeflenmektedir.
- [x] **Statik Analiz**: Tüm çekirdek mantık, güvenlik kritik Python/Rust standartlarına uygundur.

## 2. ESA-PSS-01 (Gezegensel Koruma)
- [x] **Sterilite Kalp Atışı**: Her telemetri paketi, düğümün biyolojik izolasyon durumunu doğrulamak için bir `SterilityHash` (SHA-256) içerir.
- [x] **Veri Bütünlüğü**: Telemetri sahteciliğini önlemek için "Yaşam Tespit Edildi" olaylarının kriptografik imzalanması.
- [x] **Dekontaminasyon**: Yazılım düzeyindeki kilitler, sterilite kontrolleri başarısız olursa sensör maruziyetini önler.

## 3. Veri Arşivleme (PDS4)
`DataLogger`, NASA'nın Gezegensel Veri Sistemi (PDS) arşiv formatlarıyla uyumlu olacak şekilde tasarlanmıştır:
- **XML/JSON Meta Verileri**: Sensör durumunu ve çevresel bağlamı yakalar.
- **CSV Telemetri**: Yer tabanlı yeniden analiz için yüksek çözünürlüklü spektral veriler.
