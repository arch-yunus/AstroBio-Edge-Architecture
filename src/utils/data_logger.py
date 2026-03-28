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
            with open(self.csv_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "NodeID", "EventID", "Confidence", "SterilityHash", "Status"])

    def generate_sterility_hash(self, node_id):
        """
        Simulates an ESA-compliant sterility verification hash.
        """
        seed = f"{node_id}-{time.time()}"
        return hashlib.sha256(seed.encode()).hexdigest()[:12]

    def log_event(self, event):
        # 1. JSON Logging (Detailed)
        current_data = []
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r') as f:
                try:
                    current_data = json.load(f)
                except json.JSONDecodeError:
                    current_data = []
        
        current_data.append(event)
        with open(self.json_path, 'w') as f:
            json.dump(current_data, f, indent=2)

        # 2. CSV Logging (Compliance/Telemetry)
        with open(self.csv_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(event['timestamp'])),
                event['node_id'],
                hash(str(event['timestamp'])) % 10000,
                f"{event['confidence']:.4f}",
                self.generate_sterility_hash(event['node_id']),
                "BIO_POSITIVE" if event['is_positive'] else "NOMINAL"
            ])

        print(f"[Logger] Event recorded for {event['node_id']} in {self.json_path}")
