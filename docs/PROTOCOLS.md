# AstroBio-Mesh Protocol (AMP-v1)

## 1. Overview
AMP is a lightweight, fault-tolerant peer-to-peer protocol designed for extreme space environments (High latency, High radiation).

## 2. Node States
- **IDLE**: Scanning but not processing.
- **PROCESSING**: Analyzing local dataset.
- **ALARM**: Biosignature detected, broadcasting to mesh.
- **SYNC**: Synchronizing analytical weights or telemetry.

## 3. Message Format (Protobuf)
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

## 4. Retransmission Strategy
- **Exponential Backoff**: Up to 5 retries.
- **Carousel Routing**: Messages are passed to nearest neighbors first.

## 5. Planetary Protection
All nodes must broadcast a 'Sterility Status' every heartbeat to ensure Category IV compliance.
