import random

class ThermalManager:
    """
    Uç düğümün sıcaklık durumunu ve soğutma sistemlerini simüle eder.
    Uzun süreli işlemci yükü ve güneş radyasyonu sıcaklığı artırır.
    """
    def __init__(self, initial_temp=25.0):
        self.temperature = initial_temp
        self.heater_active = False
        self.radiator_valve_open = False
        self.is_overheating = False

    def update_temperature(self, cpu_load=0.1, sun_exposure=True):
        """
        Sıcaklık modelini günceller.
        """
        # Radyasyon ve işlemci yüküne bağlı sıcaklık artışı
        ambient_heat = 0.5 if sun_exposure else -1.2 # Güneş altında ısınma, gölgede soğuma
        cpu_heat = cpu_load * 5.0 # İşlemci yüküne bağlı ısı
        
        self.temperature += ambient_heat + cpu_heat

        # Radyatör (Pasif/Aktif soğutma) etkisi
        if self.radiator_valve_open:
            self.temperature -= 2.0
        
        # Isıtıcı (Kışın donmayı engellemek için) etkisi
        if self.heater_active:
            self.temperature += 1.5

        # Rastgele gürültü (Sensör belirsizliği)
        self.temperature += random.uniform(-0.1, 0.1)

        # Sınır kontrolleri
        if self.temperature > 50.0:
            self.is_overheating = True
            self.radiator_valve_open = True # Acil soğutma
        else:
            self.is_overheating = False
            
        return self.temperature

    def set_control_action(self, action):
        """
        Termal kontrol eylemlerini uygular.
        """
        if action == "SOĞUT":
            self.radiator_valve_open = True
            self.heater_active = False
        elif action == "ISIT":
            self.radiator_valve_open = False
            self.heater_active = True
        elif action == "NOMİNAL":
            self.radiator_valve_open = False
            self.heater_active = False

    def get_status(self):
        return {
            "temperature": f"{self.temperature:.1f}C",
            "overheating": self.is_overheating,
            "radiator": "AÇIK" if self.radiator_valve_open else "KAPALI",
            "heater": "AÇIK" if self.heater_active else "KAPALI"
        }
