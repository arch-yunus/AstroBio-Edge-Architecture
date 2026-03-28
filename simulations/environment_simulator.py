import numpy as np
import json

class PlanetSimulator:
    def __init__(self, planet_name="Mars"):
        self.planet_name = planet_name
        self.wavelengths = np.linspace(400, 1000, 600)  # 400nm to 1000nm

    def generate_spectrum(self, has_biosignature=False):
        """
        Generates a synthetic Raman-like spectrum.
        """
        # Base noise (geological background)
        spectrum = np.random.normal(0.05, 0.01, len(self.wavelengths))
        
        # Simulating baseline drift
        spectrum += np.sin(self.wavelengths / 200) * 0.05

        if has_biosignature:
            # Adding 'biological' peaks within the 400-1000nm range
            biosig_peaks = [
                (790, 0.4, 8),  # Simulated Amide-like shift
                (730, 0.3, 6),  # Simulated Amide-like shift
                (610, 0.2, 5),  # Simulated UV-Resonance marker
            ]
            for pos, intensity, width in biosig_peaks:
                # Map NM to indices
                idx = int((pos - 400) / (1000 - 400) * len(self.wavelengths))
                if 0 <= idx < len(self.wavelengths):
                    # Gaussian peak
                    peak = intensity * np.exp(-((np.arange(len(self.wavelengths)) - idx)**2) / (2 * width**2))
                    spectrum += peak

        return spectrum.tolist()

if __name__ == "__main__":
    sim = PlanetSimulator()
    data = sim.generate_spectrum(has_biosignature=True)
    print(f"Generated spectrum with {len(data)} points.")
