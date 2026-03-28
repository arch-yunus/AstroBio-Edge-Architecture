class SpectralVisualizer:
    @staticmethod
    def plot_ascii(wavelengths, signal, peaks, title="Spectral Analysis"):
        """
        Generates a 1D ASCII plot for terminal-based visualization.
        """
        print(f"\n--- {title} ---")
        width = 60
        height = 10
        
        max_val = max(signal) if signal else 1
        
        for h in range(height, 0, -1):
            line = ""
            threshold = (h / height) * max_val
            for val in signal[::len(signal)//width]:
                if val >= threshold:
                    line += "#"
                else:
                    line += " "
            print(line)
        
        # Wavelength markers
        print("-" * width)
        print(f"{int(wavelengths[0])}nm" + " "*(width-10) + f"{int(wavelengths[-1])}nm")
        
        if peaks:
            print(f"Detected Peaks at Indices: {peaks}")

if __name__ == "__main__":
    # Test visualization
    import numpy as np
    w = np.linspace(400, 1000, 100)
    s = np.random.normal(0.1, 0.02, 100)
    s[40:50] += 0.5 # Add a peak
    SpectralVisualizer.plot_ascii(w, s, [45])
