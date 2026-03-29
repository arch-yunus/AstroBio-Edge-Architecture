import numpy as np
import random

class FaultInjector:
    def __init__(self, radiation_level=0.01, sensor_noise_std=0.05):
        """
        radiation_level: Her veri işleme döngüsünde bir bit-flip olasılığı.
        sensor_noise_std: Katkısal Gauss gürültüsünün standart sapması.
        """
        self.radiation_level = radiation_level
        self.sensor_noise_std = sensor_noise_std
        self.solar_storm_active = False

    def update_solar_storm_status(self, is_active=False):
        """
        Sistem genelinde güneş fırtınası durumunu aktif/deaktif eder.
        """
        self.solar_storm_active = is_active
        if is_active:
            print("[FAULT_INJECTOR] DİKKAT: Güneş Patlaması (Solar Flare) aktif! Radyasyon seviyeleri kritik.")

    def inject_bit_flip(self, value):
        """
        Float/int değerinde radyasyon kaynaklı bit-flip simülasyonu.
        Güneş fırtınası sırasında olasılık 10 kat artar.
        """
        prob = self.radiation_level * (10 if self.solar_storm_active else 1)
        if random.random() < prob:
            # Rastgele bir sapma veya değer bozulması
            return value * (1.0 + random.uniform(-0.8, 0.8))
        return value

    def corrupt_signal(self, signal):
        """
        Spektral sinyale gürültü ve bit-flip uygular.
        """
        # Güneş fırtınası varsa baz gürültü artar
        effective_noise = self.sensor_noise_std * (3.0 if self.solar_storm_active else 1.0)
        noisy_signal = np.array(signal) + np.random.normal(0, effective_noise, len(signal))
        
        # Tekil veri noktalarında bozulma
        corruption_prob = self.radiation_level * (0.5 if self.solar_storm_active else 0.1)
        for i in range(len(noisy_signal)):
            if random.random() < corruption_prob:
                noisy_signal[i] = self.inject_bit_flip(noisy_signal[i])
        
        return noisy_signal.tolist()

    def simulate_sensor_failure(self, probability=0.001):
        """
        Sensör kararmasını simüle eder.
        """
        effective_prob = probability * (10 if self.solar_storm_active else 1)
        return random.random() < effective_prob
