import unittest
import sys
import os

# Project root for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hardware.power_manager import PowerManager
from hardware.thermal_manager import ThermalManager
from src.utils.fdir import FDIR
from models.biosignature_detector import BiosignatureDetector

class TestAstroBioSystems(unittest.TestCase):
    def test_power_manager(self):
        pm = PowerManager(battery_level=100.0)
        pm.consume_energy()
        self.assertEqual(pm.battery_level, 97.5)
        self.assertEqual(pm.get_status()["mode"], "NOMİNAL")
        
        # Test low power mode
        pm.battery_level = 15.0
        pm.consume_energy()
        self.assertTrue(pm.is_low_power_mode)
        self.assertEqual(pm.get_status()["mode"], "DÜŞÜK GÜÇ")

    def test_thermal_manager(self):
        tm = ThermalManager(initial_temp=25.0)
        # Moderate load should increase temp slightly
        new_temp = tm.update_temperature(cpu_load=0.2, sun_exposure=True)
        self.assertGreater(new_temp, 25.0)
        
        # Overheating test
        tm.temperature = 55.0
        tm.update_temperature(cpu_load=0.9, sun_exposure=True)
        self.assertTrue(tm.is_overheating)
        self.assertTrue(tm.radiator_valve_open)

    def test_fdir_logic(self):
        fdir = FDIR("TEST-NODE")
        # Critical battery telemetry
        telemetry = {"battery": "%5.0", "temperature": 25.0, "snr": 15.0}
        status, recs = fdir.check_health(telemetry)
        self.assertEqual(status, "KRİTİK")
        self.assertIn("ACİL_GÜÇ_TASARRUFU", recs)
        
        # Recovery execution
        actions = fdir.execute_recovery(recs)
        self.assertTrue(len(actions) > 0)
        self.assertEqual(fdir.recovery_count, 1)

    def test_biosignature_detector_db(self):
        detector = BiosignatureDetector()
        # Mock wavelengths and simple peak
        wavelengths = [400, 430, 500, 600, 660, 1000]
        # Klorofil-A peaks are 430 and 660
        peaks = [1, 4] 
        signal = [0, 1, 0, 0, 1, 0]
        
        results = detector.analyze_spectrum(wavelengths, signal, peaks)
        self.assertTrue(results["is_positive"])
        self.assertIn("Klorofil-A", results["findings"])

if __name__ == "__main__":
    unittest.main()
