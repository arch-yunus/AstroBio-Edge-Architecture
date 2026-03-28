import numpy as np

def remove_background(signal, window_size=50):
    """
    Simulates baseline correction (background subtraction) for spectral data.
    """
    baseline = np.convolve(signal, np.ones(window_size)/window_size, mode='same')
    return signal - baseline

def detect_peaks(signal, threshold=0.1, min_dist=10):
    """
    Very simple peak detection heuristic for noisy spectral data.
    Returns indices of detected peaks.
    """
    peaks = []
    for i in range(min_dist, len(signal) - min_dist):
        if signal[i] > threshold and signal[i] == np.max(signal[i-min_dist:i+min_dist]):
            peaks.append(i)
    return peaks

def calculate_snr(signal, peaks):
    """
    Calculates Signal-to-Noise Ratio for the strongest detected peak.
    """
    if not peaks:
        return 0.0
    signal_power = np.max(signal[peaks])
    noise_power = np.std(signal)
    return signal_power / noise_power if noise_power > 0 else 0.0
