import numpy as np

class BiosignatureDetector:
    def __init__(self, confidence_threshold=0.7):
        self.confidence_threshold = confidence_threshold
        # Known organic markers (normalized peak positions)
        self.organic_markers = {
            "Amide-A": 0.65,      # Near 790nm (790-400)/(1000-400) = 0.65
            "Amide-B": 0.55,      # Near 730nm (730-400)/(1000-400) = 0.55
            "UV-Res": 0.35        # Near 610nm (610-400)/(1000-400) = 0.35
        }

    def analyze_spectrum(self, wavelengths, signal, peaks):
        """
        Analyzes detected peaks against known organic markers.
        """
        findings = {}
        total_hits = 0

        for name, expected_pos in self.organic_markers.items():
            # Check if any detected peak is near the marker
            for p in peaks:
                peak_pos = p / len(wavelengths)
                if abs(peak_pos - expected_pos) < 0.05:
                    findings[name] = {
                        "peak_index": int(p),
                        "intensity": float(signal[p]),
                        "confidence": 0.85
                    }
                    total_hits += 1
                    break

        confidence = total_hits / len(self.organic_markers)
        return {
            "is_positive": confidence > self.confidence_threshold,
            "confidence": confidence,
            "findings": findings
        }
