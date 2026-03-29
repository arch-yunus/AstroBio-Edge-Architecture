import numpy as np
import json
import os

class BiosignatureDetector:
    def __init__(self, confidence_threshold=0.6, db_path=None):
        self.confidence_threshold = confidence_threshold
        self.db_path = db_path or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "biosignatures_db.json")
        self.biosignatures_db = self.load_db()

    def load_db(self):
        """
        JSON tabanlı biyolojik imza veritabanını yükler.
        """
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("biosignatures", [])
        except Exception as e:
            print(f"[UYARI] Biyolojik imza veritabanı yüklenemedi: {e}")
            return []

    def analyze_spectrum(self, wavelengths, signal, peaks):
        """
        Tespit edilen tepe noktalarını bilinen biyolojik imzalarla karşılaştırır.
        """
        findings = {}
        total_hits = 0
        confidences = []

        if not peaks or not self.biosignatures_db:
            return {
                "is_positive": False,
                "confidence": 0.0,
                "findings": {}
            }

        for entry in self.biosignatures_db:
            name = entry["name"]
            expected_peaks = entry["peaks"]
            hits = 0
            
            # Dalga boyuna göre eşleştirme (nm bazında)
            for exp_peak in expected_peaks:
                for p_idx in peaks:
                    observed_nm = wavelengths[p_idx]
                    # +/- 10nm tolerans
                    if abs(observed_nm - exp_peak) < 10:
                        hits += 1
                        break
            
            if hits > 0:
                match_ratio = hits / len(expected_peaks)
                confidences.append(match_ratio * 0.9) # 0.9 baz güven oranı
                findings[name] = {
                    "type": entry["type"],
                    "match_ratio": f"%{match_ratio*100:.0f}",
                    "description": entry["description"]
                }
                total_hits += 1

        overall_confidence = np.mean(confidences) if confidences else 0.0
        
        return {
            "is_positive": overall_confidence > self.confidence_threshold,
            "confidence": float(overall_confidence),
            "findings": findings
        }
