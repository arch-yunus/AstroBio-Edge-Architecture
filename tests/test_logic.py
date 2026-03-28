import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.signal_processing import detect_peaks, remove_background
import numpy as np

class TestAstroBioLogic(unittest.TestCase):
    def test_peak_detection(self):
        # Basit bir sinyal ve tepe noktası oluştur
        signal = np.zeros(100)
        signal[50] = 1.0
        peaks = detect_peaks(signal, threshold=0.5)
        self.assertIn(50, peaks)

    def test_background_removal(self):
        # Sabit bir gürültü ekle
        signal = np.ones(100) * 0.5
        # Tepe noktası ekle
        signal[50] = 1.0
        processed = remove_background(signal, window_size=10)
        # Background removal sonrası tepe noktası hala belirgin olmalı
        self.assertTrue(processed[50] > 0.4)

if __name__ == '__main__':
    unittest.main()
