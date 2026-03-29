import time

class FDIR:
    """
    Fault Detection, Isolation, and Recovery (Hata Algılama, İzole Etme ve Kurtarma).
    Uzay sistemlerinde otonomi için kritik öneme sahip bir mekanizmadır.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.fault_history = []
        self.recovery_count = 0

    def check_health(self, telemetry):
        """
        Telemetri verilerini analiz ederek sağlık kontrolü yapar.
        """
        status = "NOMİNAL"
        recommendations = []

        # 1. Batarya Kontrolü
        battery = float(telemetry.get("battery", "100").replace("%", ""))
        if battery < 10.0:
            status = "KRİTİK"
            recommendations.append("ACİL_GÜÇ_TASARRUFU")
        elif battery < 20.0:
            status = "UYARI"
            recommendations.append("DÜŞÜK_GÜÇ_MODU")

        # 2. Termal Kontrol
        temp = telemetry.get("temperature", 25.0)
        if temp > 60.0:
            status = "KRİTİK"
            recommendations.append("SİSTEM_SOĞUTMA_ZORUNLU")
        elif temp > 45.0:
            status = "UYARI"
            recommendations.append("PASİF_SOĞUTMA_AKTİF")

        # 3. Sinyal Kalitesi
        snr = telemetry.get("snr", 20.0)
        if snr < 5.0:
            status = "UYARI"
            recommendations.append("SENSÖR_RE-KALİBRASYON")

        if status != "NOMİNAL":
            self.fault_history.append({
                "timestamp": time.time(),
                "status": status,
                "issues": recommendations
            })

        return status, recommendations

    def execute_recovery(self, recommendations):
        """
        Önerilen kurtarma eylemlerini gerçekleştirir.
        """
        actions_taken = []
        for rec in recommendations:
            if rec == "SENSÖR_RE-KALİBRASYON":
                actions_taken.append("Sensör sıfırlandı ve gürültü filtresi güncellendi.")
            elif rec == "ACİL_GÜÇ_TASARRUFU":
                actions_taken.append("Tüm bilimsel cihazlar kapatıldı, sadece TT&C aktif.")
            elif rec == "SİSTEM_SOĞUTMA_ZORUNLU":
                actions_taken.append("İşlemci frekansı düşürüldü, radyatör kapakları açıldı.")
                
        if actions_taken:
            self.recovery_count += 1
            
        return actions_taken
