import sys
import os
import time

# Adding project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.mesh_coordinator import MeshCoordinator
from src.utils.data_logger import DataLogger

def run_mission():
    print("BAŞLATILIYOR: AstroBio-Edge Çoklu Düğüm Görev Simülasyonu")
    print("-------------------------------------------------------")
    
    logger = DataLogger()
    coordinator = MeshCoordinator(swarm_size=3)
    
    # Simulate a 2-cycle scan mission
    coordinator.orchestrate_swarm(cycles=2)
    
    # Sonuçları kaydet
    print("\n[Simülatör] Görev logları sonlandırılıyor...")
    for event in coordinator.global_registry:
        logger.log_event(event)
        
    print("\n[Simülatör] Görev Simülasyonu Tamamlandı. Sonuçlar için logs/ dizinini kontrol edin.")

if __name__ == "__main__":
    run_mission()
