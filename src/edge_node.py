import sys
import os
import time
import json

# Adding current dir to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.signal_processing import remove_background, detect_peaks, calculate_snr
from simulations.environment_simulator import PlanetSimulator
from models.biosignature_detector import BiosignatureDetector
from src.utils.fault_injector import FaultInjector
from models.biosignature_nn import BiosignatureNN
from hardware.power_manager import PowerManager

class EdgeNode:
    def __init__(self, node_id="Astro-Edge-01"):
        self.node_id = node_id
        self.simulator = PlanetSimulator()
        self.detector = BiosignatureDetector()
        self.nn_classifier = BiosignatureNN()
        self.power_manager = PowerManager()
        self.fault_injector = FaultInjector()
        self.logs = []

    def run_discovery_cycle(self):
        print(f"[{self.node_id}] Keşif döngüsü başlatılıyor...")
        
        # 0. Enerji Tüketimi
        current_battery = self.power_manager.consume_energy()
        
        # 1. Veri Edinimi (Simülasyondan)
        raw_data = self.simulator.generate_spectrum(has_biosignature=True)
        
        # 1.1 Hata Enjeksiyonu (Uzay gürültüsü ve Radyasyon simülasyonu)
        corrupted_data = self.fault_injector.corrupt_signal(raw_data)
        
        # 2. Ön işleme
        processed_data = remove_background(corrupted_data)
        
        # 3. Peak Detection
        peaks = detect_peaks(processed_data, threshold=0.1)
        snr = calculate_snr(processed_data, peaks)
        
        # 4. Biosignature Analysis
        results = self.detector.analyze_spectrum(self.simulator.wavelengths, processed_data, peaks)
        
        # 5. AI/ML Klasifikasyon (Derin Öğrenme Desteği)
        ai_confidence = self.nn_classifier.classify_organic(peaks)
        
        # 6. Sonuç İşleme (Hibrit Model)
        event = {
            "timestamp": time.time(),
            "node_id": self.node_id,
            "snr": snr,
            "is_positive": results["is_positive"],
            "confidence": (results["confidence"] + ai_confidence) / 2.0,
            "findings": results["findings"],
            "battery": f"%{current_battery:.1f}"
        }
        
        self.logs.append(event)
        
        if results["is_positive"]:
            print(f"[{self.node_id}] UYARI: BİYOLOJİK İMZA TESPİT EDİLDİ! Güven oranı: {results['confidence']:.2f}")
        else:
            print(f"[{self.node_id}] Önemli bir biyolojik imza bulunamadı. Bölge taraması tamamlandı.")
        
        return event

if __name__ == "__main__":
    node = EdgeNode()
    for _ in range(3):
        node.run_discovery_cycle()
        time.sleep(1)
