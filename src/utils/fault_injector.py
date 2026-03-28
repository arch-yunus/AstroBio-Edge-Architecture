import numpy as np
import random

class FaultInjector:
    def __init__(self, radiation_level=0.01, sensor_noise_std=0.05):
        """
        radiation_level: Probability of a bit-flip per data processing cycle.
        sensor_noise_std: Standard deviation of additive Gaussian noise.
        """
        self.radiation_level = radiation_level
        self.sensor_noise_std = sensor_noise_std

    def inject_bit_flip(self, value):
        """
        Simulates a radiation-induced bit flip in a float/int value.
        """
        if random.random() < self.radiation_level:
            # Simple simulation: add a relatively large random spike
            return value * (1.0 + random.uniform(-0.5, 0.5))
        return value

    def corrupt_signal(self, signal):
        """
        Applies additive noise and potential bit-flips across a spectral signal.
        """
        noisy_signal = np.array(signal) + np.random.normal(0, self.sensor_noise_std, len(signal))
        
        # Randomly corrupt some indices to simulate bit flips
        for i in range(len(noisy_signal)):
            if random.random() < self.radiation_level * 0.1:
                noisy_signal[i] = self.inject_bit_flip(noisy_signal[i])
        
        return noisy_signal.tolist()

    def simulate_sensor_failure(self, probability=0.001):
        """
        Simulates total sensor blackout.
        """
        return random.random() < probability
