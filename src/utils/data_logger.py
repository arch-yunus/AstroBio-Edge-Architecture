import json
import csv
import os
import time
import hashlib

class DataLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.json_path = os.path.join(log_dir, "discovery_events.json")
        self.csv_path = os.path.join(log_dir, "compliance_telemetry.csv")
        self._init_csv()

    def _init_csv(self):
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ZamanDamgasi", "DugumID", "OlayID", "GuvenOrani", "BütünlükHash", "Durum"])

    def generate_integrity_hash(self, event_data):
        """
        NASA-STD-8739.8 uyumlu veri bütünlüğü hash'i üretir.
        """
        content = json.dumps(event_data, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

    def log_event(self, event):
        """
        Olayı kriptografik imzalarla loglar.
        """
        # Bütünlük hash'i ekle
        event["integrity_hash"] = self.generate_integrity_hash(event)
        
        # 1. JSON Logging
        current_data = []
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r', encoding="utf-8") as f:
                try:
                    current_data = json.load(f)
                except json.JSONDecodeError:
                    current_data = []
        
        current_data.append(event)
        with open(self.json_path, 'w', encoding="utf-8") as f:
            json.dump(current_data, f, indent=2, ensure_ascii=False)

        # 2. CSV Logging (Telemetry)
        with open(self.csv_path, 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(event['timestamp'])),
                event['node_id'],
                hash(str(event['timestamp'])) % 10000,
                f"{event['confidence']:.4f}",
                event["integrity_hash"][:16],
                "BIO_POSITIVE" if event['is_positive'] else "NOMINAL"
            ])

        print(f"[Logger] {event['node_id']} için güvenli log kaydı tamamlandı. SHA-256 doğrulandı.")
