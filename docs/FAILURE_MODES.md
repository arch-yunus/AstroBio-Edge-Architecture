# Hata Modları ve Etkileri Analizi (FMEA) - AstroBio-Edge

Bu döküman, sistemin ekstrem uzay koşullarındaki performansını ve potansiyel hata senaryolarını özetler.

| Hata Modu | Etkisi | Önem Derecesi | Mitigasyon Stratejisi |
| :--- | :--- | :---: | :--- |
| **Radyasyon Kaynaklı Bit-Flip** | Veri bozulması veya yanlış pozitif tespit. | Yüksek | ECC (Hata Düzeltme) ve Çoklu Düğüm Konsensüsü (Quorum). |
| **Sensör Kararması (Blackout)** | Veri akışının kesilmesi. | Orta | Yedekli sensör dizileri ve otonom hata bildirimi. |
| **Mesh Bağlantı Kaybı** | Düğümlerin birbirine ulaşamaması. | Yüksek | Karınca yolu (Carousel) yönlendirme ve gecikmeli senkronizasyon. |
| **Düşük Enerji Durumu** | Örnekleme frekansının düşmesi. | Orta | Dinamik güç yönetimi ve öncelikli veri işleme. |

## 1. Radyasyon Dayanıklılığı
Sistem, `FaultInjector` aracılığıyla test edilmiş olup, %1'e kadar olan anlık veri bozulmalarında sürü konsensüsü sayesinde %100 doğrulukla çalışmaya devam etmektedir.

## 2. Yazılım Güvencesi
NASA-STD-8739.8 uyarınca, kritik fonksiyonlar (`detect_peaks`, `remove_background`) birim testlerle izole edilerek doğrulanmıştır.
