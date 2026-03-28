# AstroBio-Mesh Protokolü (AMP-v1)

## 1. Genel Bakış
AMP, ekstrem uzay ortamları (Yüksek gecikme, Yüksek radyasyon) için tasarlanmış hafif ve hata toleranslı bir eşler arası protokoldür.

## 2. Düğüm Durumları
- **IDLE**: Tarama yapıyor ancak veri işlemiyor.
- **PROCESSING**: Yerel veri setini analiz ediyor.
- **ALARM**: Biyolojik imza tespit edildi, ağa yayın yapılıyor.
- **SYNC**: Analitik ağırlıkları veya telemetriyi senkronize ediyor.

## 3. Mesaj Formatı (Protobuf)
```protobuf
message EdgeDiscovery {
  string node_id = 1;
  double timestamp = 2;
  bool is_positive = 3;
  float confidence = 4;
  map<string, Finding> findings = 5;
  bytes raw_spectral_summary = 6;
}
```

## 4. Yeniden İletim Stratejisi
- **Üstel Geri Çekilme (Exponential Backoff)**: En fazla 5 deneme.
- **Karınca Yolu Yönlendirme**: Mesajlar önce en yakın komşulara iletilir.

## 5. Gezegensel Koruma
Kategori IV uyumluluğunu sağlamak için tüm düğümler her kalp atışında (heartbeat) bir 'Sterilite Durumu' yayınlamalıdır.
