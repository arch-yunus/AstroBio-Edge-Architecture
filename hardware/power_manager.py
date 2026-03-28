import random

class PowerManager:
    """
    Uç düğümün enerji tüketimini simüle eden modül.
    Uzay görevlerinde güç yönetimi en kritik sistemlerden biridir.
    """
    def __init__(self, battery_level=100.0):
        self.battery_level = battery_level
        self.energy_consumption_per_cycle = 2.5 # % bazında
        self.is_low_power_mode = False

    def consume_energy(self):
        """
        Her keşif döngüsünde enerji tüketir.
        """
        self.battery_level -= self.energy_consumption_per_cycle
        if self.battery_level < 20.0:
            self.is_low_power_mode = True
            self.energy_consumption_per_cycle = 1.0 # Enerji tasarrufu modu
        
        return self.battery_level

    def get_status(self):
        return {
            "battery": f"%{self.battery_level:.1f}",
            "mode": "DÜŞÜK GÜÇ" if self.is_low_power_mode else "NOMİNAL",
            "is_safe": self.battery_level > 5.0
        }
