import time
import os
import sys

# Adding project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.mesh_coordinator import MeshCoordinator
from src.base_station import BaseStation
from src.utils.report_generator import generate_final_report

def run_astro_mission(swarm_size=4, cycles=3):
    """
    Tüm AstroBio-Edge-Architecture projesini orkestre eden ana dosya.
    Simülasyon, veri işleme, FDIR ve raporlama süreçlerini birleştirir.
    """
    print("\n" + "*"*80)
    print("      ASTROBIO-EDGE MİSYONU BAŞLATILIYOR (EVRENSEL - UNIVERSAL CLASS)")
    print("*"*80 + "\n")
    
    # 1. Kontrol Merkezi ve Sürü Koordinatörünü Hazırla
    base_station = BaseStation()
    coordinator = MeshCoordinator(swarm_size=swarm_size)
    
    print(f"[Mission] {swarm_size} düğümlük sürü ve Görev Kontrol Merkezi aktif.")
    
    # 2. Görev Döngülerini Başlat
    for cycle in range(cycles):
        print(f"\n" + "-"*60)
        print(f"      GÖREV DÖNGÜSÜ {cycle+1} / {cycles}")
        print("-"*60 + "\n")
        
        # Sürü koordinatörü düğümleri çalıştırır
        for node in coordinator.nodes:
            # Rastgele gün ışığı simülasyonu (Isınma/Soğuma için)
            sun_exposure = (cycle % 2 == 0)
            
            # Düğüm keşif döngüsünü çalıştırır
            event = node.run_discovery_cycle(sun_exposure=sun_exposure)
            
            # Veriyi kontrol merkezine (BaseStation) ilet
            base_station.receive_telemetry(node.node_id, event)
            
            # Görselleştirme için kısa bekleme (Simülasyon akışını izlemek için)
            time.sleep(0.3)
            
        # Görev Kontrol İstasyonunda durumu güncelle
        base_station.display_dashboard()
        
    # 3. Misyon Sonu Raporu Oluştur
    print("\n" + "="*80)
    print("      GÖREV SONU ANALİZİ VE RAPORLAMA")
    print("="*80 + "\n")
    
    mission_summary = base_station.generate_mission_report()
    
    # Mevcut rapor üreticisi ile PDF/HTML benzeri log oluştur (varsayılan araç)
    generate_final_report(mission_summary)
    
    print("\n\n" + "*"*80)
    print("      ASTROBIO-EDGE MİSYONU BAŞARIYLA TAMAMLANDI.")
    print("*"*80 + "\n")

if __name__ == "__main__":
    # Misyon parametrelerini ayarla
    size = 3
    steps = 4
    
    # Eğer terminalden argüman gelirse kullan (İsteğe bağlı)
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    if len(sys.argv) > 2:
        steps = int(sys.argv[2])
        
    run_astro_mission(swarm_size=size, cycles=steps)
