import sys
import os
import time

# Adding project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.edge_node import EdgeNode

class MeshCoordinator:
    def __init__(self, swarm_size=3):
        self.nodes = [EdgeNode(node_id=f"Astro-Edge-{i+1:02d}") for i in range(swarm_size)]
        self.global_registry = []
        self.adaptive_mode = False # Pozitif bulgu durumunda tüm sürüyü alarma geçirir
        self.alert_level = "NOMİNAL"

    def orchestrate_swarm(self, cycles=1):
        """
        Sürü operasyonlarını yönetir ve adaptif kararlar alır.
        """
        print(f"[Koordinatör] {len(self.nodes)} düğümlük sürü 'Egemenlik Modu'nda yönetiliyor...")
        
        for c in range(cycles):
            print(f"\n--- Görev Döngüsü {c+1} / {cycles} ---")
            cycle_results = []
            
            # 1. Döngüsel Keşif
            for node in self.nodes:
                # Eğer adaptif mod aktifse, her düğüm daha yüksek CPU yüküyle (hassasiyet) çalışır
                sun_exposure = (c % 2 == 0)
                event = node.run_discovery_cycle(sun_exposure=sun_exposure)
                cycle_results.append(event)
                self.global_registry.append(event)
            
            # 2. Konsensüs ve Adaptasyon Kararı
            self.check_consensus(cycle_results)
            
            # 3. Adaptif Davranış Kontrolü
            if any(r['is_positive'] for r in cycle_results):
                self.adaptive_mode = True
                self.alert_level = "KRİTİK_ODAKLANMA"
                print(f"[Koordinatör] ADAPTİF MOD AKTİF: Tüm düğümler yüksek çözünürlüklü taramaya geçiyor.")
            else:
                self.adaptive_mode = False
                self.alert_level = "NOMİNAL"

    def check_consensus(self, results):
        """
        Dinamik Quorum Sensing: Batarya ve güven oranına göre kararlılık analizi.
        """
        positives = [r for r in results if r['is_positive']]
        
        # Dinamik eşik: Eğer sürünün ortalama bataryası düşükse, eşik yükselir (enerji tasarrufu)
        avg_battery = sum(float(r['battery'].replace("%", "")) for r in results) / len(results)
        threshold = len(results) * (0.6 if avg_battery < 30.0 else 0.4)
        
        if len(positives) >= threshold:
            print(f"\n[Koordinatör] KORUM SAĞLANDI! (%{len(positives)/len(results)*100:.0f} düğüm hemfikir)")
            avg_conf = sum(r['confidence'] for r in positives) / len(positives)
            print(f"[Koordinatör] Sürü Onaylı Güven Seviyesi: {avg_conf:.2f}")
        elif len(positives) > 0:
            print(f"\n[Koordinatör] KISMİ TEMAS: {len(positives)} düğümde bulgu var. Konsensüs için yeterli değil.")
        else:
            print(f"\n[Koordinatör] Sürü Durumu: Nominal tarama devam ediyor.")

    def get_swarm_status(self):
        return {
            "node_count": len(self.nodes),
            "alert_level": self.alert_level,
            "adaptive_mode": self.adaptive_mode
        }

if __name__ == "__main__":
    coordinator = MeshCoordinator(swarm_size=4)
    coordinator.orchestrate_swarm(cycles=2)
