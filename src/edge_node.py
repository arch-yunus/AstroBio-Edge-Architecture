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
from hardware.thermal_manager import ThermalManager
from src.utils.fdir import FDIR

class EdgeNode:
    def __init__(self, node_id="Astro-Edge-01"):
        self.node_id = node_id
        self.simulator = PlanetSimulator()
        self.detector = BiosignatureDetector()
        self.nn_classifier = BiosignatureNN()
        self.power_manager = PowerManager()
        self.thermal_manager = ThermalManager()
        self.fdir = FDIR(node_id)
        self.fault_injector = FaultInjector()
        self.logs = []

    def run_discovery_cycle(self, sun_exposure=True):
        print(f"[{self.node_id}] Keşif döngüsü başlatılıyor...")
        
        # 1. Donanım Durum Güncellemesi (Güç & Termal)
        current_battery = self.power_manager.consume_energy()
        current_temp = self.thermal_manager.update_temperature(cpu_load=0.4, sun_exposure=sun_exposure)
        
        # 2. Sağlık Kontrolü (FDIR)
        telemetry = {
            "battery": f"%{current_battery:.1f}",
            "temperature": current_temp,
            "snr": 15.0 # Varsayılan baz SNR
        }
        health_status, recommendations = self.fdir.check_health(telemetry)
        
        if health_status != "NOMİNAL":
            print(f"[{self.node_id}] FDIR UYARISI: Durum {health_status}. Öneriler: {recommendations}")
            actions = self.fdir.execute_recovery(recommendations)
            for action in actions:
                print(f"[{self.node_id}] KURTARMA: {action}")

        # 3. Veri Edinimi (Simülasyondan)
        raw_data = self.simulator.generate_spectrum(has_biosignature=True)
        
        # 3.1 Hata Enjeksiyonu (Uzay gürültüsü ve Radyasyon simülasyonu)
        corrupted_data = self.fault_injector.corrupt_signal(raw_data)
        
        # 4. Ön işleme ve Analiz
        processed_data = remove_background(corrupted_data)
        peaks = detect_peaks(processed_data, threshold=0.1)
        snr = calculate_snr(processed_data, peaks)
        
        # 5. Biosignature Analysis (Hibrit: Kural Tabanlı + AI)
        results = self.detector.analyze_spectrum(self.simulator.wavelengths, processed_data, peaks)
        ai_confidence = self.nn_classifier.classify_organic(peaks)
        
        # 6. Sonuç İşleme
        combined_confidence = (results["confidence"] + ai_confidence) / 2.0
        
        event = {
            "timestamp": time.time(),
            "node_id": self.node_id,
            "health": health_status,
            "temperature": f"{current_temp:.1f}C",
            "battery": f"%{current_battery:.1f}",
            "snr": float(snr),
            "is_positive": bool(results["is_positive"] and combined_confidence > 0.5),
            "confidence": float(combined_confidence),
            "findings": results["findings"]
        }
        
        self.logs.append(event)
        
        if event["is_positive"]:
            print(f"[{self.node_id}] !!! KRİTİK TESPİT !!! Güven: {combined_confidence:.2f}")
            for name, info in results["findings"].items():
                print(f"   -> {name} ({info['type']}): {info['match_ratio']} eşleşme")
        else:
            print(f"[{self.node_id}] Bölge taraması tamamlandı, biyosinyal bulunamadı.")
        
        return event

if __name__ == "__main__":
    node = EdgeNode()
    for i in range(5):
        node.run_discovery_cycle(sun_exposure=(i < 3))
        time.sleep(0.5)
